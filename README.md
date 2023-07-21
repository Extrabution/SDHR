# SDHR


## Развёртывание
- Шаг 1:
    Скопировать репозиторий
    `!git clone https://github.com/Extrabution/SDHR.git`
- Шаг 2:
    Сбилдить Docker контейнеры при помощи bash скрипта
    `!./build_services.sh`
- Шаг 3:
    Запустить контейнеры при помощи скрипта
    `!./start_services.sh`
## API
API можно увидеть в SwaggerUI по маршруту `/docs/`
- Маршрут api/control-history принимает query q в формате
    date_startDdate_end
    Где:
    date_start: %Y-%m-%dT%H:%M:%S
    date_end: %Y-%m-%dT%H:%M:%S
    
