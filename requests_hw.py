import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_de():
    with open('DE') as file_path_DE:
        to_lang = 'de'
        text = []
        for t in file_path_DE:
            text.append(t)
        params = {'key': API_KEY, 'text': text, 'lang': '{}-ru'.format(to_lang)}

        response = requests.get(URL, params=params)
        json_ = response.json()

    with open('DE_RU', 'w', encoding='utf-8') as fw:
        fw.write(''.join(json_['text']))

def translate_es():
    with open('ES') as file_path_ES:
        to_lang = 'es'
        text = []
        for t in file_path_ES:
            text.append(t)
        params = {'key': API_KEY, 'text': text, 'lang': '{}-ru'.format(to_lang)}
        response = requests.get(URL, params=params)
        json_ = response.json()

    with open('ES_RU', 'w', encoding='utf-8') as fw:
        fw.write(''.join(json_['text']))

def translate_fr():
    with open('FR') as file_path_FR:
        to_lang = 'es'
        text = []
        for t in file_path_FR:
            text.append(t)
        params = {'key': API_KEY, 'text': text, 'lang': '{}-ru'.format(to_lang)}
        response = requests.get(URL, params=params)
        json_ = response.json()

    with open('FR_RU', 'w', encoding='utf-8') as fw:
        fw.write(''.join(json_['text']))
    #return ''.join(json_['text'])

translate_de()
translate_es()
translate_fr()
#print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'en'))
#print(translate_de())


#requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))

