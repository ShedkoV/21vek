# Разработка сервиса

## Рабочее окружение
Для начала разработки необходимо настроить рабочее окружение. Нам понадобятся следующие системные зависимости:
- [python](https://www.python.org/downloads/) версии >= 3.9.9

### Установить poetry
В проекте используется poetry версии 1.5.1

Настройка окружения:
1. Настроить репозиторий
    ```shell script
    git clone https://github.com/ShedkoV/21vek.git
    cd 21vek
    ```
2. Установить зависимости. Зависимости установятся в виртуальное окружение.
    ```shell script
    poetry install -E lint
   
## Локальный запуск сервиса
export PYTHONPATH="$PWD/src"
Из корневой директории запустить скрипт `start.sh`

Запуск линтера:
```shell script
flake8 --config=setup.cfg src
```

Запуск mypy
```shell script
mypy --config-file setup.cfg
```

Развернуть сервис:
```powershell
docker compose -f src/tools/docker-compose.yaml up -d
```