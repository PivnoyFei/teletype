import random
from datetime import timedelta

from django.conf import settings
from ski_resort import messages, talk_services


def context(game, question, start_text):
    return {
        "start": game.finish,
        "day": game.day,
        "name": game.name,
        "question": question,
        "statistics": talk_services.statistics(game),
        "start_text": start_text,
    }


def profit_newbie(game):
    return game.newbie * settings.INCOME_NEWBIE


def profit_professional(game):
    return game.professional * settings.INCOME_PROFESSIONAL


def all_lift_places(game):
    return (
        game.lift * settings.LIFT[1] + game.kupe_lift * settings.KUPE_LIFT[1]
    )


def hotel_places(game):
    return game.hotel * settings.HOTEL[1]


def restauran_places(game):
    return game.restauran * settings.RESTAURAN[1]


def total_people(game):
    return game.newbie + game.professional


def track_newbie_places(game):
    return (
        game.low_track * settings.LOW_TRACK[2]
        + game.middle_track * settings.MIDDLE_TRACK[2]
    )


def track_professional_places(game):
    return (
        game.middle_track * settings.MIDDLE_TRACK[2]
        + game.high_track * settings.HIGH_TRACK[2]
    )


def get_trail_maintenance(game):
    return (
        game.low_track * settings.LOW_TRACK[1]
        + game.middle_track * settings.MIDDLE_TRACK[1]
        + game.high_track * settings.HIGH_TRACK[1]
    )


def got_lift_seat(game):
    if all_lift_places(game) < total_people(game):
        return True
    return False


def got_hotel_seat(game):
    if hotel_places(game) < total_people(game):
        return True
    return False


def got_restauran_seat(game):
    if restauran_places(game) < total_people(game):
        return True
    return False


def got_professional_track_seat(game):
    if track_professional_places(game) < game.professional:
        return True
    return False


def got_newbie_track_seat(game):
    if track_newbie_places(game) < game.newbie:
        return True
    return False


def get_arrived_left_people(game):
    game.left_newbie = random.randint(3, 9)
    game.arrived_newbie = random.randint(7, 13)
    game.left_professional = random.randint(1, 3)
    game.arrived_professional = random.randint(2, 6)
    popularity = game.popularity

    comments = {
        60: (random.randint(1, 3), random.randint(1, 2), 1),
        70: (random.randint(1, 3), random.randint(1, 3), 0),
        85: (random.randint(1, 3), random.randint(2, 5), 0),
        95: (random.randint(2, 5), random.randint(2, 7), 0)
    }

    if popularity < 20:
        game.left_newbie += 1
        game.arrived_newbie -= 1
        game.arrived_professional -= 1

    if popularity < 30:
        game.left_newbie += 1
        game.arrived_newbie -= 1
        game.left_professional += 1
        game.arrived_professional -= 1

    for i in comments:
        if popularity > i:
            if comments[i][2]:
                game.left_newbie -= 1
                game.left_professional -= 1
            game.arrived_newbie += comments[i][0]
            game.arrived_professional += comments[i][1]

    return game


def people(game):
    count = 0
    if got_hotel_seat(game):
        game.hotel_in_demand = True
        count += total_people(game) - hotel_places(game)

    if got_restauran_seat(game):
        game.restauran_in_demand = True
        count += (total_people(game) - restauran_places(game))

    if got_lift_seat(game):
        game.lift_in_demand = True
        count += (total_people(game) - all_lift_places(game))

    if got_newbie_track_seat(game):
        game.low_track_in_demand = True
        count_newbie = (game.newbie - track_newbie_places(game))
        game.popularity -= count_newbie
        game.newbie -= count_newbie
        game.left_newbie += count_newbie

    if got_professional_track_seat(game):
        game.high_track_in_demand = True
        count_newbie = (game.professional - track_professional_places(game))
        game.popularity -= count_newbie * 2
        game.professional -= count_newbie
        game.left_professional += count_newbie

    if count > 0:
        game.newbie -= int(count / 2)
        game.professional -= int(count / 2)
        game.popularity -= int(count * 1.5)
        game.left_newbie += int(count / 2)
        game.left_professional += int(count / 2)
    if game.left_newbie > game.newbie:
        game.left_newbie = game.newbie
    if game.left_professional > game.professional:
        game.left_professional = game.professional
    if game.newbie < 0:
        game.newbie = 0
    if game.professional < 0:
        game.professional = 0
    return game


def new_day(game):
    game.day += 1
    game.data_today += timedelta(days=1)
    game.building = 0
    game.count_building = 0
    game.hotel_in_demand = False
    game.restauran_in_demand = False
    game.low_track_in_demand = False
    game.high_track_in_demand = False
    game.lift_in_demand = False

    game.cr_newbie = profit_newbie(game)
    game.cr_professional = profit_professional(game)
    game.cr += game.cr_newbie + game.cr_professional
    get_arrived_left_people(game)

    if game.day == 1:
        game.left_professional = 0

    people(game)

    game.old_professional = game.professional
    game.old_newbie = game.newbie

    game.newbie += game.arrived_newbie - game.left_newbie
    game.professional += game.arrived_professional - game.left_professional

    game.cr_track = get_trail_maintenance(game)
    game.cr -= game.cr_track
    game.cr -= game.advertising

    for _ in range(int(game.advertising / 10000)):
        game.popularity += random.randint(3, 5)
    game.popularity -= random.randint(5, 10)
    if game.popularity > 100:
        game.popularity = 100

    n_day = random.randint(0, 2)
    if n_day == 2:
        game.cr -= 1000
    elif n_day == 3:
        game.popularity += random.randint(2, 4)

    if game.popularity < 0:
        game.finish = False
        game.save()
        return ("Начать сначала",), messages.the_end[0].format(user=game.user)
    if game.cr < 0:
        game.finish = False
        game.save()
        return ("Начать сначала",), messages.the_end[1].format(user=game.user)
    if not game.finish and game.day > 20 and game.cr < 1000000:
        return ("Начать сначала",), messages.the_end[2]
    if not game.finish and game.cr > 1000000:
        if game.popularity > 60:
            game.popularity -= 40
        elif 60 > game.popularity > 40:
            game.popularity -= 20
        game.finish = True
        # services.user_level(game.user, 100)
        game.save()
        return (
            ("Продолжить", "Начать сначала"),
            messages.end_or[0].format(user=game.user)
        )
    if game.cr > 10000000:
        # services.user_level(game.user, 10)
        game.save()
        return ("Начать сначала",), messages.end_or[1]
    game.save()
    return ("Продолжить",), messages.talk_break[n_day]
