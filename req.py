# данный модуль надо предварительно установить через pip
import requests
from html.parser import HTMLParser
# import datetime

tvdata = []
# глобальная переменная для нахождения нужных данных в полученном HTML файле
k = 0
week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница',
        'Суббота', 'Воскресенье']

# Парсим HTML, вытягивая оттуда только необходимые данные


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global k
        if ((attrs == [('class', 'tv_channel_program')]) and (tag == 'ul')):
            k = 1
        if ((tag == 'li') and (k == 1)):
            # ((attrs == [('class','tv_channel_program')]) and (tag == 'ul'))
            k = 2

    def handle_endtag(self, tag):
        global k
        if ((tag == 'li') and (k == 2)):
            k = 1
        if (tag == 'ul'):
            if (k == 1):
                tvdata.append('day')
            k = 0

    def handle_data(self, data):
        # print("Data     :", data)
        global k
        if (k == 2):
            tvdata.append(data)

# вывод в консоль тв программы


# def prog_out(tvdays):
#     for day in tvdays:
#         print(week[tvdays.index(day)], ':', '\n')
#         for el in day:
#             print(el, ':', day[el])
#         print('\n')

# данные полученные после парсинга, преобразуем в список словарей,
# где словарь - тв программа на день, пары (время: название программы)


def tv_prog(address):
    r = requests.get(address)
    html = r.text
    parser = MyHTMLParser()
    parser.feed(html)
    # print(tvdata)
    tvdays = []
    buf = {}

    time = '00:00'
    prog = 'something'
    for el in tvdata:
        if (el == 'day'):
            tvdays.append(buf)
            buf = {}
        else:
            if (el[2] == ':'):
                # time = datetime.datetime.strptime(el,'%H:%M')
                time = el
            else:
                prog = el
                buf[time] = prog
    # print(tvdays)
    # pro_gout(tvdays)
    return tvdays

# tv_prog('https://tv.i.ua/inter/')
