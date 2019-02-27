import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(file_to_open, new_file, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    # params = {
    #    'key': API_KEY,
    #    'text': text,
    #    'lang': 'ru-{}'.format(to_lang),
    #}

    with open(file_to_open) as file_path:
        text = file_path.read()
        params = {'key': API_KEY, 'text': text, 'lang': '{}-{}'.format(from_lang, to_lang)}
        response = requests.get(URL, params=params)
        json_ = response.json()

    with open(new_file, 'w', encoding='utf-8') as fw:
        fw.write(''.join(json_['text']))

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'en'))
translate_it('DE', 'DE_RU', 'de')

