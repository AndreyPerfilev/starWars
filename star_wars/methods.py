import  requests

all_characters_from_films=[]
list_with_name_characters=[]
url = "https://swapi.dev/api/people/4/"
get_result= requests.get(url)
get_json= get_result.json()
print(get_json)
films=get_json.get('films')
print("ФИЛЬМЫ С ДАРТ ВЕЙДЕРОМ ",films)

"""Добавляем актеров фильма по карточке  в список и сортируем ,без копий"""
def append_characters_in_list(url_film):
    get_film=requests.get(url_film)
    json_film=get_film.json()
    get_characters = json_film.get("characters")
    for i in get_characters:
        if i not in all_characters_from_films:
            all_characters_from_films.append(i)
    print("Актеры ФИЛЬМА " + url_film +"добавлены")


"""Получаем имя персонажа из карточки и добавляем в список"""
def get_name_from_actor(url_actors):
    get_actors=requests.get(url_actors)
    json_actors=get_actors.json()
    name_characters=json_actors.get("name")
    list_with_name_characters.append(name_characters)


"""Циклом перебираем фильмы с дарт вейдером и к каждому применяем метод добавления актеров"""
for i in films:
    append_characters_in_list(i)
print("Список всех карточек персонажей", all_characters_from_films)

"""Циклом перебираем карточки актеров и применяем к ним метод добавления имени персонажа в список """
for i in all_characters_from_films:
    get_name_from_actor(i)
print("Список всеx имен персонажей", list_with_name_characters)
"""циклом записываем имена из спискав документ"""
fw=open('name.txt','a',encoding='utf-8')
for i in list_with_name_characters:
    fw.write(i+'\n')
fw.close()








