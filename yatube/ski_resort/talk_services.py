import random

from django.conf import settings
from django.utils import dateformat
from ski_resort import messages, services


def statistics(game):
    return messages.statistics.format(
        popularity=game.popularity,
        cr=game.cr,
        hotel_places=services.hotel_places(game),
        restauran_places=services.restauran_places(game),
        all_lift_places=services.all_lift_places(game),
        total_people=services.total_people(game),
        newbie=game.newbie,
        professional=game.professional,
        track_newbie_places=services.track_newbie_places(game),
        track_professional_places=services.track_professional_places(game)
    )


def talk(game, text, values):
    if values == 'Поговорить с бухгалтером':
        return text.format(
            income=(
                services.profit_newbie(game)
                + services.profit_professional(game)
            ),
            cr_track=game.cr_track,
            advertising=game.advertising,
            cr_building=game.cr_building,
            balance=(
                game.cr
                + services.profit_newbie(game)
                + services.profit_professional(game)
                - game.cr_building
                - game.cr_track
                - game.advertising
            )
        )
    if values == 'Поговорить с экономистом':
        return text.format(
            total_people=services.total_people(game),
            newbie=game.newbie,
            professional=game.professional,
            hotel=int(
                services.total_people(game)
                * 100 / services.hotel_places(game)
            ),
            restauran_places=services.restauran_places(game),
            all_lift_places=services.all_lift_places(game),
            track_newbie_places=services.track_newbie_places(game),
            track_professional_places=(
                services.track_professional_places(game))
        )
    if values == 'Поговорить с менеджером по рекламе':
        return text.format(
            popularity=game.popularity,
            advertising=game.advertising
        )
    return text


def talk_building(game, index):
    if game.count_building == 2:
        return messages.stop_building[0]
    game_index = (
        game.hotel_in_demand,
        game.restauran_in_demand,
        game.low_track_in_demand,
        game.low_track_in_demand or game.high_track_in_demand,
        game.high_track_in_demand,
        game.lift_in_demand,
        game.lift_in_demand,
    )
    if game.cr - settings.SERVICE_LIST[index][0] > 0:
        game.cr -= settings.SERVICE_LIST[index][0]
        if index == 0:
            game.hotel += 1
        elif index == 1:
            game.restauran += 1
        elif index == 2:
            game.low_track += 1
        elif index == 3:
            game.middle_track += 1
        elif index == 4:
            game.high_track += 1
        elif index == 5:
            game.lift += 1
        elif index == 6:
            game.kupe_lift += 1
        game.count_building += 1
        if game_index[index]:
            game.popularity += random.randint(3, 5)
        game.popularity += random.randint(2, 5)
        game.save()
        return messages.talk_building[index]
    else:
        return messages.stop_building[1]


def days(game):
    message = messages.days_end if game.finish else messages.days
    left_days = game.day if game.finish else 20 - game.day
    return message.format(
        data_today=game.data_today.strftime("%d"),
        month=dateformat.format(game.data_today, settings.DATE_FORMAT),
        years=game.data_today.strftime("%Y"),
        day=game.day,
        left_days=left_days,
        old_newbie=game.old_newbie,
        left_newbie=game.left_newbie,
        arrived_newbie=game.arrived_newbie,
        newbie=game.newbie,
        old_professional=game.old_professional,
        left_professional=game.left_professional,
        arrived_professional=game.arrived_professional,
        professional=game.professional,
        cr_newbie=game.cr_newbie,
        cr_professional=game.cr_professional,
        cr_track=game.cr_track,
        advertising=game.advertising,
        cr=game.cr,
    )
