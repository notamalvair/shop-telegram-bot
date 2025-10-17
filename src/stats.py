import datetime
import order as ordr
import user as usr
from random import randint
from settings import Settings

settings = Settings()

def get_text_stats(data, title, ylabel):
    """Generate text-based statistics instead of graphs"""
    if not data:
        return f"{title}\n\nНет данных для отображения."
    
    stats_text = f"{title}\n\n"
    stats_text += f"{ylabel}:\n"
    stats_text += "=" * 30 + "\n"
    
    for date, value in data.items():
        stats_text += f"{date}: {value}\n"
    
    total = sum(data.values())
    avg = total / len(data) if data else 0
    stats_text += "=" * 30 + "\n"
    stats_text += f"Всего: {total}\n"
    stats_text += f"Среднее: {avg:.1f}\n"
    
    return stats_text


def get_random_data():
    return {f"{randint(1, 30):02}.{randint(1, 12):02}.{randint(2010, 2030)}": randint(5, 100) for _ in range(randint(2, 30))}


def get_random_stats():
    return get_text_stats(get_random_data(), "Название", "Ось Y")


class RegistrationCharts:
    def __init__(self):
        self.user_list = usr.get_user_list()

    def get_stats(self, data, title):
        return get_text_stats(data, title, "Количество регистраций")

    def all_time(self):
        return self.get_stats({f"{date.day:02}.{date.month:02}.{date.year}": [user.get_register_date().date() for user in self.user_list].count(date) for date in dict.fromkeys([user.get_register_date().date() for user in self.user_list])}, "Регистрации за все время")

    def last_x_days(self, days):
        return self.get_stats({f"{(datetime.date.today() - datetime.timedelta(days=i)).day:02}.{(datetime.date.today() - datetime.timedelta(days=i)).month:02}": len(list(filter(lambda user: user.get_register_date().date() == datetime.date.today() - datetime.timedelta(days=i), self.user_list))) for i in range(30, -1, -1)}, f"Регистрации за последние {days} дней")

    def last_x_hours(self, hours):
        return self.get_stats({f"{(datetime.datetime.today() - datetime.timedelta(hours=i)).hour:02}:00": len(list(filter(lambda user: user.get_register_date().hour == (datetime.datetime.now() - datetime.timedelta(hours=i)).hour and user.get_register_date() > datetime.datetime.now() - datetime.timedelta(hours=hours), self.user_list))) for i in range(hours, -1, -1)}, f"Регистрации за последние {hours} часов.")


class OrderCharts:
    def __init__(self):
        self.order_list = ordr.get_order_list()

    def get_stats(self, data, title):
        return get_text_stats(data, title, "Количество заказов")

    def all_time(self):
        return self.get_stats({f"{date.day:02}.{date.month:02}.{date.year}": [order.get_date().date() for order in self.order_list].count(date) for date in dict.fromkeys([order.get_date().date() for order in self.order_list])}, "Заказы за все время")

    def last_x_days(self, days):
        return self.get_stats({f"{(datetime.date.today() - datetime.timedelta(days=i)).day:02}.{(datetime.date.today() - datetime.timedelta(days=i)).month:02}": len(list(filter(lambda order: order.get_date().date() == datetime.date.today() - datetime.timedelta(days=i), self.order_list))) for i in range(days, -1, -1)}, f"Заказы за последние {days} дней")

    def last_x_hours(self, hours):
        return self.get_stats({f"{(datetime.datetime.today() - datetime.timedelta(hours=i)).hour:02}:00": len(list(filter(lambda order: order.get_date() > datetime.datetime.now() - datetime.timedelta(hours=hours) and order.get_date().hour == (datetime.datetime.today() - datetime.timedelta(hours=i)).hour, self.order_list))) for i in range(hours, -1, -1)}, "Заказы за сегодня" if hours == (datetime.datetime.now().hour + 1) else f"Заказы за последние {hours} часов.")
