from pyowm import OWM
from pyowm.utils.config import get_default_config # Узнать текущую погоду в любом городе

language = get_default_config()
language['language'] = 'ru'
owm = OWM('23232775d430e5fe2ac9a9c2cbdb8410', language)

manager = owm.weather_manager()


def seven_days(latt, lonn):
    one_call = manager.one_call(lat=latt, lon=lonn)
    today = 0
    for i in range(7):
        day = one_call.forecast_daily[today]
        if i == 0:
            print(f'Сегодня будет {day.detailed_status}, температура воздуха днём {day.temperature("celsius").get("day")}')
        elif i == 1:
            print(f'Через {i} день {day.detailed_status}, температура воздуха днём {day.temperature("celsius").get("day")}')
        elif i <= 4:
            print(f'Через {i} дня будет {day.detailed_status}, температура воздуха днём {day.temperature("celsius").get("day")}')
        else:
            print(f'Через {i} дней будет {day.detailed_status}, температура воздуха днём {day.temperature("celsius").get("day")}')
        today += 1

seven_days(57.029, 24.052)
