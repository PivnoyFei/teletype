from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from users.models import CustomUser


def get_datetime():
    return datetime.today() + relativedelta(years=1000)


class Ski(models.Model):
    """Связвнв с моделью юзер через one-to-one"""
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(
        "Лыжный курорт", default="Лыжный курорт", max_length=100)

    cr = models.IntegerField("Деньги", default=100000)
    hotel = models.IntegerField("Отель", default=1)
    hotel_in_demand = models.BooleanField(
        "Отель востребован", default=False)

    restauran = models.IntegerField("Ресторан", default=1)
    restauran_in_demand = models.BooleanField(
        "Ресторан востребован", default=False)

    low_track = models.IntegerField("Маленькая горка", default=1)
    low_track_in_demand = models.BooleanField(
        "Маленькая горка востребована", default=False)

    middle_track = models.IntegerField("Средняя горка", default=0)

    high_track = models.IntegerField("Большая горка", default=0)
    high_track_in_demand = models.BooleanField(
        "Большая горка востребована", default=False)

    lift = models.IntegerField("Подьемник", default=1)
    kupe_lift = models.IntegerField("Кабиночный подьемник", default=0)
    lift_in_demand = models.BooleanField(
        "Подьемники востребованы", default=False)

    advertising = models.IntegerField("Расходы на рекламу", default=0)
    popularity = models.IntegerField("Популярность курорта", default=50)

    day = models.IntegerField("День", default=0)
    data_today = models.DateField("Сегодняшний день", default=get_datetime())

    newbie = models.IntegerField("Новичек", default=20)
    professional = models.IntegerField("Профессионал", default=0)
    old_newbie = models.IntegerField("Новичков было", default=0)
    old_professional = models.IntegerField("Профессионалов было", default=0)
    left_newbie = models.IntegerField("Уехало новичков", default=0)
    left_professional = models.IntegerField("Уехало Профессионалов", default=0)
    arrived_newbie = models.IntegerField("Приехало новичков", default=0)
    arrived_professional = models.IntegerField(
        "Приехало Профессионалов", default=0)

    cr_newbie = models.IntegerField("деньги от новичков", default=0)
    cr_professional = models.IntegerField(
        "деньги от профессионалов", default=0)
    cr_building = models.IntegerField("Содержание построек", default=0)
    cr_track = models.IntegerField("Содержание трасс", default=10000)

    count_building = models.IntegerField("Построек за день", default=0)
    finish = models.BooleanField("Конец игры", default=False)
