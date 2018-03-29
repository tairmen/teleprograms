import requests
from html.parser import HTMLParser


tvdata = []
week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница',
        'Суббота', 'Воскресенье']

# Парсим HTML, вытягивая оттуда только необходимые данные


class MyHTMLParser(HTMLParser):

    # глобальная переменная для нахождения нужных данных в полученном HTML
    # файле

    k = 0

    def handle_starttag(self, tag, attrs):
        if ((attrs == [('class', 'tv_channel_program')]) and (tag == 'ul')):
            self.k = 1
        if ((tag == 'li') and (self.k == 1)):
            self.k = 2

    def handle_endtag(self, tag):
        if ((tag == 'li') and (self.k == 2)):
            self.k = 1
        if (tag == 'ul'):
            if (self.k == 1):
                tvdata.append('day')
            self.k = 0

    def handle_data(self, data):
        # print("Data     :", data)
        if (self.k == 2):
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
    try:
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
                    time = el
                else:
                    prog = el
                    buf[time] = prog
        # print(tvdays)
        # pro_gout(tvdays)
        return tvdays
    except BaseException:
        return 'Error'

# tv_prog('https://tv.i.ua/trk-ukraina/')
