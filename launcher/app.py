from pathlib import Path
from tkinter import BOTH, END, LEFT, RIGHT, Button, Entry, Frame, Label, Listbox, StringVar, Tk, Toplevel, ttk

from launcher.module_runtime import ModuleRuntime
from launcher.services import JsonStore, LoaderCatalog, MinecraftCatalog, ModrinthClient

BASE = Path.home() / ".modular_mc_launcher"
INSTALLS_STORE = JsonStore(BASE / "installations.json")
SETTINGS_STORE = JsonStore(BASE / "settings.json")


def run():
    root = Tk()
    root.title("Modular Minecraft Launcher")
    root.geometry("1160x760")
    root.configure(bg="#10151d")

    settings = SETTINGS_STORE.load({"installations_path": str(BASE / "instances")})
    installs = INSTALLS_STORE.load([])
    runtime = ModuleRuntime(Path(__file__).parent / "modules")

    left = Frame(root, bg="#161c27")
    left.pack(side=LEFT, fill=BOTH, expand=True)
    right = Frame(root, bg="#0f131a", width=360)
    right.pack(side=RIGHT, fill=BOTH)

    Label(left, text="Установки", bg="#161c27", fg="#e9f0ff", font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=10, pady=10)
    installs_box = Listbox(left, bg="#0f131a", fg="#d9e7ff")
    installs_box.pack(fill=BOTH, expand=True, padx=10, pady=10)

    for i in installs:
        installs_box.insert(END, f"{i['name']} :: {i['minecraft_version']} [{i['loader']['name']} {i['loader']['version']}]")

    toolbar = Frame(left, bg="#161c27")
    toolbar.pack(fill="x", padx=10, pady=(0, 10))

    version_type = StringVar(value="release")
    loader = StringVar(value="vanilla")
    loader_version = StringVar(value="none")

    ttk.Combobox(toolbar, textvariable=version_type, values=["release", "snapshot", "old_beta", "old_alpha"], width=12).pack(side=LEFT, padx=4)
    loader_box = ttk.Combobox(toolbar, textvariable=loader, values=list(LoaderCatalog.builtin().keys()), width=10)
    loader_box.pack(side=LEFT, padx=4)
    loader_version_box = ttk.Combobox(toolbar, textvariable=loader_version, width=12)
    loader_version_box.pack(side=LEFT, padx=4)

    def refresh_loader_versions(*_):
        values = LoaderCatalog.builtin().get(loader.get(), ["none"])
        loader_version_box["values"] = values
        loader_version.set(values[0])

    loader_box.bind("<<ComboboxSelected>>", refresh_loader_versions)
    refresh_loader_versions()

    def create_installation():
        versions = MinecraftCatalog.fetch_versions()
        candidates = [v for v in versions if v["type"] == version_type.get()]
        if not candidates:
            return
        version = candidates[0]["id"]
        item = {
            "name": f"{version}-{loader.get()}",
            "minecraft_version": version,
            "version_type": version_type.get(),
            "loader": {"name": loader.get(), "version": loader_version.get()},
            "game_dir": str(Path(settings["installations_path"]) / f"{version}-{loader.get()}"),
        }
        installs.append(item)
        INSTALLS_STORE.save(installs)
        installs_box.insert(END, f"{item['name']} :: {item['minecraft_version']} [{item['loader']['name']} {item['loader']['version']}]")

    Button(toolbar, text="Создать установку", command=create_installation).pack(side=LEFT, padx=6)

    Label(right, text="Модули", bg="#0f131a", fg="#e9f0ff", font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=10, pady=(10, 4))
    modules_container = Frame(right, bg="#0f131a")
    modules_container.pack(fill=BOTH, expand=True)

    for manifest in runtime.list_manifests():
        runtime.render_module_preview(modules_container, manifest)

    search_row = Frame(right, bg="#0f131a")
    search_row.pack(fill="x", padx=10, pady=10)
    query = Entry(search_row)
    query.pack(side=LEFT, fill="x", expand=True)

    results = Listbox(right, bg="#111826", fg="#d9e7ff", height=10)
    results.pack(fill="x", padx=10, pady=(0, 10))

    def find_mods(project_type: str):
        results.delete(0, END)
        for hit in ModrinthClient.search(query.get(), project_type=project_type):
            results.insert(END, f"{hit['title']} ({hit['downloads']} загрузок)")

    btns = Frame(right, bg="#0f131a")
    btns.pack(fill="x", padx=10, pady=(0, 12))
    Button(btns, text="Моды", command=lambda: find_mods("mod")).pack(side=LEFT, padx=3)
    Button(btns, text="Ресурс-паки", command=lambda: find_mods("resourcepack")).pack(side=LEFT, padx=3)
    Button(btns, text="Шейдеры", command=lambda: find_mods("shader")).pack(side=LEFT, padx=3)

    def open_module_editor():
        win = Toplevel(root)
        win.title("Редактор модулей")
        win.geometry("720x500")
        Label(win, text="JSON манифест модуля", font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=12, pady=8)
        text = Entry(win)
        text.pack(fill="x", padx=12)
        Label(win, text="Поддержка расширений: интерфейс, цвета, окна, анимации, обработчики.").pack(anchor="w", padx=12, pady=6)
        Label(win, text="Публикация в Google Cloud: настройте bucket и OAuth в settings.json.").pack(anchor="w", padx=12)

    Button(right, text="Открыть редактор модулей", command=open_module_editor).pack(fill="x", padx=10, pady=(0, 12))

    root.mainloop()
