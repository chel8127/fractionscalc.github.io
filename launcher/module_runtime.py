import importlib
import json
from pathlib import Path
from tkinter import Frame, Label
from typing import Dict, List

from launcher.models import ModuleManifest


class ModuleRuntime:
    def __init__(self, modules_dir: Path):
        self.modules_dir = modules_dir
        self.modules_dir.mkdir(parents=True, exist_ok=True)

    def list_manifests(self) -> List[ModuleManifest]:
        manifests: List[ModuleManifest] = []
        for file in self.modules_dir.glob("*/module.json"):
            payload = json.loads(file.read_text(encoding="utf-8"))
            manifests.append(ModuleManifest(**payload))
        return manifests

    def render_module_preview(self, parent: Frame, manifest: ModuleManifest):
        bg = manifest.style.get("background", "#202531")
        fg = manifest.style.get("foreground", "#e8edf8")
        frame = Frame(parent, bg=bg, bd=2, relief="ridge")
        Label(frame, text=manifest.title, bg=bg, fg=fg, font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=8, pady=(8, 2))
        Label(frame, text=manifest.description or manifest.entrypoint, bg=bg, fg=fg).pack(anchor="w", padx=8, pady=(0, 8))
        frame.pack(fill="x", padx=6, pady=6)

    def execute(self, manifest: ModuleManifest, context: Dict):
        module_name, fn_name = manifest.entrypoint.split(":", 1)
        module = importlib.import_module(module_name)
        fn = getattr(module, fn_name)
        fn(context)
