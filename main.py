import requests

# Код к первому заданию

def filtering_by_geo ():
    # Отфильстровать список по гео
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    filtered_geo_logs = []
    for visit in geo_logs:
        place = list(visit.values())
        if "Россия" in place[0]:
            filtered_geo_logs.append(visit)
    return filtered_geo_logs

def searching_uniq():
    # Поиск уникальных значений
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    uniq = []
    for user, list_id in ids.items():
        for id in list_id:
            if id not in uniq:
                uniq.append(id)
    return uniq

def main_channel():
    # Канал с максимальным объемом
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    buffer = 0
    main_sourse = None
    for sourse, traffic in stats.items():
        if buffer < int(traffic):
            buffer = int(traffic)
            main_sourse = sourse
    return main_sourse


# Код ко второму заданию

def create_folder():
    url = 'https://cloud-api.yandex.net'
    token =           #!!!!!!!!!!!!!!!!!!  Введите токен с Яндекса !!!!!!!!!!!!!!!!
    folder_name = 'my_folder'
    create_folder_url = url + '/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    params = {'path': folder_name}
    return requests.put(f'{create_folder_url}?path={folder_name}', headers=headers)


if __name__ == '__main__':
    # task 1
    print(filtering_by_geo())
    print(searching_uniq())
    print(main_channel())

    # task 2
    create_folder()


