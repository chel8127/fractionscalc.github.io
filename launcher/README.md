# Modular Minecraft Launcher (Python)

Прототип реального лаунчера с модульной архитектурой:

- создание установок и выбор типов версий (`release`, `snapshot`, `old_beta`, `old_alpha`);
- выбор загрузчика и версии загрузчика;
- настройки и хранилище конфигураций в `~/.modular_mc_launcher`;
- поиск модов/ресурспаков/шейдеров через Modrinth API;
- загрузка пользовательских модулей интерфейса из `launcher/modules/*/module.json`;
- отдельное окно редактора модулей (базовый MVP).

## Запуск

```bash
python -m launcher.main
```

## Развитие

Для полноценной загрузки клиента Minecraft нужно добавить:

1. авторизацию Microsoft/Xbox;
2. скачивание ассетов и библиотек по version json;
3. запуск Java-процесса с classpath;
4. интеграцию Fabric/Forge API для автоинсталла загрузчиков;
5. публикацию модулей в Google Cloud Storage (GCS SDK + OAuth).
