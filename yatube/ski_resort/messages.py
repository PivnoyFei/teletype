game_description = {
    'Лыжный курорт': (
        '\n    Правительство нашей планеты хочет открыть филиал нашей суперуспешной сети горнолыжных курортов '
        'на планете Боннасис системы Процион. Мы запланировали открытие курорта на <Date>, но, к сожалению, '
        'местный управляющий оставляет желать лучшего. Вас, <user>, как прославленного торговца, мы просим дать '
        'ему наглядный урок управления курортом. Если вы сможете не более чем за 20 дней увеличить начальный '
        'капитал до некоторой суммы, то вы получите вознаграждение в размере 10.000 cr. Все детали вы узнаете на месте.',
        'из Космические Рейнджеры 2 Доминаторы',
        '\n    Квест включает в себя управление горнолыжным курортом, тратя деньги на строительство различных объектов и рекламу. '
        '\nИгрок должен заработать 1.000.000 кредитов в течение 20 "дней" внутри мини-игры, '
        'соблазняя все больше и больше гостей тратить свои деньги. Популярность должна поддерживаться, '
        'чтобы курорт не стал несостоятельным и не был закрыт. '
        '\nПосле получения требуемого 1.000.000 cr. игрок имеет возможность продолжить игру без ограничения по времени'),
}

start_game = ('Начать сначала', 'Продолжить')

start_text = (
    '\n    В космопорте вас встретил гаалец, исполнявший обязанности генерального менеджера '
    'лыжного курорта: теперь, пока генеральным менеджером будете вы, он станет вашим '
    'заместителем. По дороге в горы он объяснил, что к текущему моменту построен один '
    'подъемник, одна трасса для новичков, одна гостиница и ресторан. Оставшиеся после этого'
    'на счету капитал равняется 100.000 cr, а ваша цель - набрать 1.000.000 cr.'
    '\n'
    '\n    Место, куда вы приехали, оказалось довольно живописным. Небольшая гостиница и '
    'ресторанчик, к которым почти вплотную спускаются горные склоны. Приглядевшись получше, '
    'вы заметили небольшой кресельный подъемник и пологую трассу. Рядом с гостиницей '
    'располагался небольшой домик, предназначенный для администрации и персонала. Здесь и '
    'был ваш офис - как раз рядом со спальней.'
    '\n'
    '\n- Сегодня строить уже ничего нельзя, но вы можете поговорить со специалистами или '
    'просто отдохнуть, -сказал гаалец.'
)

question_one = (
    'Поговорить со специалистом',
    'Всё идет отлично! Отдохнуть остаток дня'
)

question = (
    'Поговорить со специалистом',
    'Построить что-нибудь',
    'Всё идет отлично! Отдохнуть остаток дня'
)

question_2 = (
    '\nС кем вы хотите поговорить?',
    '\nЧто будем строить?'
)

ask_advisers_start = (
    'Поговорить с заместителем',
    'Поговорить с менеджером по строительству',
    'Поговорить с бухгалтером',
    'Поговорить с экономистом',
    'Поговорить с менеджером по рекламе',
    'На сегодня хватит! Отдохнуть остаток дня'
)

ask_advisers = (
    'Поговорить с заместителем',
    'Поговорить с менеджером по строительству',
    'Поговорить с бухгалтером',
    'Поговорить с экономистом',
    'Поговорить с менеджером по рекламе',
    'Построить что-нибудь',
    'На сегодня хватит! Отдохнуть остаток дня'
)

ask_advertising_manager_start = (
    'Тратить на рекламу 0 cr в день',
    'Тратить на рекламу 10.000 cr в день',
    'Тратить на рекламу 20.000 cr в день',
    'Тратить на рекламу 30.000 cr в день',
    'Тратить на рекламу 40.000 cr в день',
    'Тратить на рекламу 50.000 cr в день',
    'Проконсультироваться с кем-нибудь еще',
    'На сегодня хватит! Отдохнуть остаток дня'
)

ask_advertising_manager = (
    'Тратить на рекламу 0 cr в день',
    'Тратить на рекламу 10.000 cr в день',
    'Тратить на рекламу 20.000 cr в день',
    'Тратить на рекламу 30.000 cr в день',
    'Тратить на рекламу 40.000 cr в день',
    'Тратить на рекламу 50.000 cr в день',
    'Проконсультироваться с кем-нибудь еще',
    'Построить что-нибудь',
    'На сегодня хватит! Отдохнуть остаток дня'
)

new_day = (
    "На сегодня хватит! Отдохнуть остаток дня",
    "Всё идет отлично! Отдохнуть остаток дня"
)

question_building = (
    'Гостиница - 110.000 cr',
    'Ресторан - 80.000 cr',
    'Трасса для новичков - 30.000 cr',
    'Обычная трасса - 45.000 cr',
    'Трасса для профессионалов - 60.000 cr',
    'Подъемник кресельный - 80.000 cr',
    'Подъемник кабиночный - 110.000 cr',
    'Ничего не строить',
    'На сегодня хватит! Отдохнуть остаток дня',
)

stop_building = (
    "Вы не можете строить больше двух сооружений в день",
    "Недостаточно средств"
)

days = (
    '\nСегодня {data_today} {month} {years}, {day}-й день вашего руководства курортом. Осталось дней: {left_days}.'
    '\nВы сидите в своем офисе. Перед вами на столе лежит отчет за прошедшие сутки:'
    '\n'
    '\nНовички - было: {old_newbie}, уехало: {left_newbie}, приехало: {arrived_newbie}, сейчас: {newbie}.'
    '\nПрофессионалы - было: {old_professional}, уехало: {left_professional}, приехало: {arrived_professional}, сейчас: {professional}.'
    '\n'
    '\nПолучено денег'
    '\nот новичков: {cr_newbie} cr'
    '\nот профессионалов: {cr_professional} cr'
    '\nПотрачено денег'
    '\nна содержание трасс: {cr_track} cr'
    '\nна рекламу: {advertising} cr'
    '\nДенег на счету: {cr} cr'
)

days_end = (
    '\nСегодня {data_today} {month} {years}, {left_days}-й день вашего руководства курортом.'
    '\nВы сидите в своем офисе. Перед вами на столе лежит отчет за прошедшие сутки:'
    '\n'
    '\nНовички - было: {old_newbie}, уехало: {left_newbie}, приехало: {arrived_newbie}, сейчас {newbie}.'
    '\nПрофессионалы - было: {old_professional}, уехало: {left_professional}, приехало: {arrived_professional}, сейчас {professional}.'
    '\n'
    '\nПолучено денег'
    '\nот новичков: {cr_newbie} cr'
    '\nот профессионалов: {cr_professional} cr'
    '\nПотрачено денег'
    '\nна содержание трасс: {cr_track} cr'
    '\nна рекламу: {advertising} cr'
    '\nДенег на счету: {cr} cr'
)

statistics = (
    '\nПопулярность      {popularity} %'
    '\nДенег на счету:    {cr} cr'
    '\nГостиниц:              {hotel_places} мест'
    '\nРесторанов:          {restauran_places} мест'
    '\nПодъемники:        {all_lift_places} мест'
    '\n-----------------------------------'
    '\nВСЕГО ПОСЕТИТЕЛЕЙ: {total_people}'
    '\nНовичков:                     {newbie}'
    '\nПрофессионалов:         {professional}'
    '\n-----------------------------------'
    '\nТРАССЫ ОБСЛУЖИВАЮТ:'
    '\nНовичков:                      {track_newbie_places}'
    '\nПрофессионалов:          {track_professional_places}'
)

talk = (
    '\n    Выш заместитель с удовольствием поделился с вами свои опытом.\n'
    '\n - Гостиницы нужны, чтобы вы смогли поселить больше народу, а значит получать больше денег. В одной'
    'гостинице может жить 60 туристов. Каждый ресторан удовлетворяет потребность 45 туристов в еде. '
    'Кресельный подъемник способен поднять на гору 30 лыжников, а кабиночный - 50. Каждая трасса вмещает '
    'до 20 клиентов. Трассы для новичков и для профессионалов обслуживают по 20 новичков и профи соответственно, '
    'а обычной трассой пользуются по 10 лыжников из каждой категории.'
    '\n'
    '\n    Теперь о деньгах. На содержание трасс в день тратится по 10.000 cr за каждую легкую трассу, '
    'по 15.000 cr за обычную и по 20.000 cr за тяжелую. Каждый новичок платит вам 2.000 cr в день, '
    'а профессионал - 6.000 cr. Затраты на рекламу вы определяете самостоятельно.',
    '\n    Малок - менеджер по строительству - быстро доложил обстановку:'
    '\n'
    '\n- В день можно возводить до двух сооружений. Такую скорость постройки обеспечивает блоковая технология, '
    'позволяющая компоновать объекты из уже готовых частей. Мы можем строить следующие сооружения:'
    '\n    1) Гостиница - стоит 110.000 cr, вмещает 60 персон.'
    '\n    2) Ресторан - стоит 80.000 cr, питает 45 персон.'
    '\n    3) Трасса для новичков - стоит 30.000 cr, обслуживает 20 новичков'
    '\n    4) Трасса для профессионалов - стоит 60.000 cr, обслуживает 20 профессионалов'
    '\n    5) Обычная трасса - стоит 45.000 cr, обслуживает 10 новичков и 10 профессионалов'
    '\n    6) Подъемник кресельный - стоит 80.000 cr, вмещает 30 персон.'
    '\n    7) Подъемник кабиночный - стоит 110.000 cr, вмещает 50 персон.',
    '\n    Фэянин-бухгалтер подготовил вам баланс на завтра'
    '\n-----------------------------------------------------------------'
    '\nТуристы:                     {income} cr.'
    '\nСодержание трасс:   {cr_track} cr.'
    '\nРеклама:                     {advertising} cr.'
    '\nСтроительство:          {cr_building} cr.'
    '\n-----------------------------------------------------------------'
    '\nБаланс:                       {balance} cr',
    '\n    Экономистом был необъятных размеров человек, который быстро и по делу доложил обстановку:'
    '\n'
    '\n- В настоящее время на базе отдыхает туристов: {total_people} '
    '(новичков: {newbie}; профессионалов: {professional}).'
    '\nГостиницы заполнены на {hotel} %.'
    '\nРестораны обслуживают {restauran_places} персон.'
    '\nПодъёмников достаточно для {all_lift_places} клиентов.'
    '\nТрассы вмещают {track_newbie_places} новичков и {track_professional_places} профессионалов.',
    '\n    Рекламой курорта занимался веселый молодой человек. Его доклад звучал так:'
    '\n'
    '\n- Популярность курорта в настоящее время равна {popularity}%. От популярности зависит приток клиентов;'
    '\nкроме того, если популярность упадет до 0, курорт могут закрыть!'
    '\n'
    '\n    Строительство любого объекта увеличивает популярность '
    'на 2-5%, а если этот объект востребован - то на 5-10%. '
    'Каждый недовольный новичок, уехавший с курорта, уменьшает '
    'популярность на 1%, а профессионал - на 2%. Недовольны '
    'клиенты бывают нехваткой ресторанов, подъемников или трасс '
    'нужной сложности. Однако имейте в виду, что не все '
    'уехавшие клиенты бывают недовольны.'
    '\n'
    '\n    Кроме того, популярность курорта падает на 5-10% в день '
    'сама по себе. Поэтому курорту необходима реклама. '
    'Каждые потраченные 10.000 cr в день увеличивают популярность '
    'курорта на 3-5%. К сожалению, законы планеты Боннасис '
    'запрещают тратить на рекламу более 50.000 cr в день.'
    '\n'
    '\n    Текущие расходы на рекламу равны {advertising} cr в день.'
)

talk_building = (
    '\n    Вы позвали малока и сообщили ему о своем решении построить гостиницу. Малок обещал построить'
    ' ее к вечеру. Вы выглянули в окно и заметили, как на площадку выехало несколько машин. Рабочие'
    ' стали быстро разгружать блоки и монтировать здание. Через несколько часов гостиница была готова,'
    ' и к ней подъехали несколько машин с новыми туристами.',
    '\n    Вы приказали менеджеру по строительству срочно возвести ресторан. Через несколько минут вы'
    ' выглянули в окно и заметили, как на площадку въехало несколько машин. Рабочие стали быстро'
    ' разгружать блоки и монтировать здание, а еще через несколько часов ресторан был готов, и в него'
    ' зашли первые посетители, довольно причмокивая языком.',
    '\n    Вы сказали малоку, что вам нужна новая трасса для новичков. Малок отдал распоряжение, и вскоре'
    ' на горные склоны выехало несколько трассоукладчиков. Через несколько часов от вершины подъемника'
    'до самого низа тянулась великолепная пологая трасса.',
    '\n    Вы позвали малоку, что вам нужна новая обычная трасса. Малок отдал распоряжение, и вскоре'
    ' на горные склоны выехало несколько трассоукладчиков. Через несколько часов от вершины подъемника'
    ' до самого низа тянулась великолепная трасса с небольшим количеством поворотов.',
    ' Вы позвали малоку, что вам нужна новая трасса для профессионалов. Малок отдал распоряжение, и вскоре'
    ' на горные склоны выехало несколько трассоукладчиков. Через несколько часов от вершины подъемника'
    'до самого низа тянулась великолепная извилистая трасса.',
    '\n    Вы позвали марлока и сказали, что вам необходимо срочно построить кресельный подъемник.'
    ' Марлок сказал, что все будет сделано. Вскоре на площадку въехало несколько машин. Рабочие'
    ' стали быстро разгружать детали и монтировать из них подъемник. Через несколько часов'
    ' он был готов, и к нему тут же потянулись все новые и новые туристы. Их отношение к вам'
    ' немного улучшилось',
    '\n    Вы позвали малока и сказали, что вам необходимо срочно построить кабиночный подъемник.'
    ' Малок сказал, что все будет готово через несколько часов. Вы выглянули в окно и заметили,'
    ' как на площадку въехали машины. Рабочие стали быстро разгружать детали и монтировать из них'
    ' подъемник. Через несколько часов он был готов, и к нему тут же потянулись все новые и новые туристы.'
)

talk_break = (
    '\n    Весь остаток дня вы смотрели, как туристы съезжают на лыжах с горы.'
    ' Все-таки вы делаете большое, полезное дело! Ободренные этой нехитрой'
    ' мыслью, вы легли спать, а наутро отправились в офис с желанием превратить '
    ' свой курорт в лучшее место во Вселенной!',
    '    А почему бы вам, собственно, не воспользоваться услугами собственного'
    ' курорта? Выбрав самую легкую трассу, вы надели лыжи и поднялись на вершину'
    ' горы. Однако, с горы на лыжах ехать - это вам не звездолетом управлять!'
    ' На первом же повороте вы вылетели с трассы и проделали остаток пути вниз'
    ' по склону на собственной спине. Это отбило у вас охоту к экстремальным '
    ' развлечениям до самого вечера.'
    '\n'
    '\n    На следующее утро вы отправились в офис с ломотой во всем теле.'
    ' И что, интересно, заставляет туристов приехать к вам на курорт, да еще и '
    ' платить за это бешеные деньги?',
    '\n    Сегодня вы решили сыграть в карты с собственным заместителем, и после нескольких часов'
    ' проиграли ему 1.000 cr. Да не зря говорят - с гаальцами и пеленгами в карты лучше не играть!'
    ' Делать нечего - пришлось выписать заместителю премию на указанную сумму. Не будете же вы'
    ' платить ему из собственного кармана?!'
    '\n'
    '\n    Понятно, что утром, когда вы вернулись в свой офис, настроение у нас было препаршивейшее.',
    ' Вы культурно провели остаток дня в местном баре, '
    'благо для вас там все бесплатно. Лишь поздно вечером'
    ' вы добрели до постели и заснули как убитый. Проснувшись утром с легким похмельем, вы привели себя'
    ' в порядок и отправились в офис, чтобы ознакомиться с текущим положением дел.',
    '\n    Не успели вы спуститься в бар для заслуженного отдыха, '
    'как вас перехватил какой то пленг, оказавшийся'
    ' местным журналистом. Весь вечер вам пришлось давать ему '
    'интервью и поить его пивом за счет отеля. но зато'
    ' пленг, по всей видимости, оказался доволен вами и написал '
    'хорошую статью, так как, вернувшись утром в офис,'
    ' вы узнали, что популярность курорта немного возросла.',
    '\n    Вы отправились к себе в спальню и весь день остаток '
    'дня смотрели стереовизор. Ну надо же - в секторе'
    ' Перец поднялись цены на малокские табуретки! Эх, какие '
    'деньги можно было бы сделать, если бы вы не застряли'
    ' на этой чертовой планетке!'
    '\n    В расстроенных чувствах вы легли спать. Впрочем, '
    'утром вы уже сидели за своим рабочем столом и утешали'
    ' себя тем, что 10000 cr, обещанные правительством планеты Моква, - тоже неплохая сумма.',
    '\n    Вы весь день лазили по планетной компьютерной сети. '
    'Надо же, а на соседнем курорте с профессионалов'
    ' дерут по 7 тысяч в день! Правда и популярность тамошнего '
    'курорта значительно ниже чем у вас. Жаль, что вы'
    ' не имеете право менять жестко установленные планетой Моква цены на путевки...'
    '\n'
    '\n    Утром наспех позавтракав, вы пошли в свой офис разбираться с делами вашего курорта.',
    '\n    Сегодня вы неожиданно для себя разговорились '
    'с менеджером по строительству. И что же - оказалось что'
    ' в молодости малок тоже был рейнджером! Но однажды ему дали задание построить малокский форпост на'
    ' незаселенной планете, и это ему так понравилось, что он переквалифицировался в строители.'
    '\n'
    '\n    Вы весь день обменивались воспоминаниями с рейнджерской жизнью '
    'и остались вполне довольны друг другом,'
    '\nУтром вы взялись за управление курортом с новыми силами',
    '\n    Вы попросили своего заместителя прокатить вас по окрестностям на своем аэрокаре. Надо отметить,'
    ' что с высоты птичьего полета ваш курорт выглядит еще красивее, чем в низу. Ну разве можно не любить'
    ' такое славное местечко?!'
    '\n'
    '\n    Благодаря этим хорошим впечатлениям, вы наутро принялись за работу с удвоенной энергией!'
)

the_end = (
    'Популярность курорта упала до нуля! Ваш заместитель не упустил своего шанса, сразу же отправил на планету Моква'
    'рапорт о непопулярности курорта. Ответ пришел незамедлительно - рейнджер {user} уволен!'
    '\nВы провалили вашу миссию',
    'Вы растратили все деньги! Ваш заместитель не упустил своего шанса, сразу же отправил на планету Моква'
    'рапорт о разорении курорта. Ответ пришел незамедлительно - рейнджер {user} уволен!'
    '\nВы провалили вашу миссию.',
    'Время вышло! Вы провалили вашу миссию.'
)

end_or = (
    '\n    Проверив содержимое счета курорта, вы к своей неописуемой '
    'радости обнаружили, что на нем больше 1.000.000 cr!'
    '\nВаша миссия выполнена! Вы показали менеджерам планеты Боннасис, '
    'как надо работать. Уже отправляясь в космопорт,'
    '\nвы встретились со своим заместителем.'
    '\n'
    '\n-Руководство планеты Моква восхищено вашим профессионализмом, '
    '{user}, и хочет предложить вам продление контракта.'
    '\nВашей задачей будет заработать 10.000.000 cr, но уже без всяких '
    'ограничений по времени. Если вы сможете выполнить'
    '\nэто задание, то вдобавок к сумме в 10.000 cr мы выплатим вам '
    'неплохую премию прямо здесь. Разумеется, вы в любой'
    '\nмомент сможете отказаться от этого дополнительного задания. Ну как, согласны?',
    '\n    Проверив содержимое счета курорта, вы к своей неописуемой '
    'радости обнаружили, что на нем больше 10.000.000 cr!'
    '\nВаша миссия выполнена! Вы показали менеджерам планеты Боннасис, '
    'как надо работать. Заместитель торжественно выдал вам'
    '\nпремию в 10.000 cr. Ваш счет теперь равен 10.000 cr! '
    'И надо еще слетать на планету Моква за своим гонораром в 10000 cr.'
    '\n'
    '\n    В общем, вы неплохо заработали на этой планетке, '
    'надо отметить! "Может быть, стоит переквалифицироваться в управляющие?"'
    '\n-думали вы, возвращаясь в космопорт.'
)
