import random

articles = {
    'Что такое Zero waste' : 'https://telegra.ph/CHto-takoe-Zero-waste-05-08',
    'Коды переработки пластмасс' : 'https://telegra.ph/Kody-pererabotki-plastmass-05-08',
    'Куда сдать отходы на переработку' : 'https://telegra.ph/Kuda-sdat-othody-na-pererabotku-05-12',
    'Сортировка отходов дома' : 'https://telegra.ph/Sortirovka-othodov-doma-05-12',
    'Как беречь лесные ресурсы' : 'https://telegra.ph/Kak-berech-lesnye-resursy-05-13',
    'Что такое Tetra Pak' : 'https://telegra.ph/CHto-takoe-Tetra-Pak-05-13',
    'Коды переработки других материалов' : 'https://telegra.ph/Kody-pererabotki-drugih-materialov-05-08',
    'Куда сдавать старые вещи' : 'https://telegra.ph/Kuda-sdavat-starye-veshchi-05-14',
    'Различные коды на упаковке' : 'https://telegra.ph/Drugie-kody-na-upakovke-05-08'
}

def get_list_of_articles():
    string = ''
    for title, ref in articles.items():
        string += '<a href="' + ref + '">' + title + '</a>\n\n'
    return string

def get_random_article():
    it = random.randint(0, len(articles) - 1)
    string = '<a href="' + list(articles.values())[it] + '">' + list(articles.keys())[it] + '</a>'
    return string