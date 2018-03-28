import xml.etree.ElementTree as ET
import req

# находим все телепередачи в заданном часовом диапазоне


def find_all(progs, st, et):
    tmp = {}
    for el in progs:
        if ((el > st) and (el < et)):
            tmp[el] = progs[el]
    return tmp

# получаем сериалы из списка телепередач


def get_ser(progs):
    tmp = {}
    for el in progs:
        if ((progs[el][0:6] == 'Сериал') or (progs[el][0:3] == 'Т/с')):
            tmp[el] = progs[el]
    return tmp

# из входного XML файла получаем результат


def get_xml():
    tree = ET.parse('tv.xml')
    root = tree.getroot()
    # day = input('введите день: ')
    # print('введите промежуток времеми: ')
    # tm = input()
    day = 'Среда'
    for i in range(7):
        if (req.week[i] == day):
            di = i
    # print(di)
    startime = '00:00'
    endtime = '24:00'
    res = []
    for child in root:
        url = child.get('href')
        # urls.append(url)
        # req.prog_out(req.tv_prog(url))
        # allprogs.append(req.tv_prog(url))
        # print('-------------------------------------------------\n')
        # print('канал ',child.get('name'), '\n')
        buf = req.tv_prog(url)[di]
        tmp = find_all(buf, startime, endtime)
        buf = get_ser(tmp)
        for el in buf:
            res.append({'channel': child.get('name'),
                        'time': el, 'text': buf[el]})
        # req.prog_out([buf])
        # print('-------------------------------------------------\n')
        req.tvdata = []
    return res

# записуем результат в XML файл


def make_xml():
    top = ET.Element('serials')
    buf = get_xml()
    for el in buf:
        tag = ET.SubElement(
            top, 'c', {
                'time': el['time'], 'channel': el['channel']})
        tag.text = el['text']
        tagn = ET.SubElement(top, 'br')
        tagn.text = '\n'
    # print(ET.tostring(top, encoding='unicode'))
    tree = ET.ElementTree(top)
    tree.write('serials.xml', encoding='utf=8')


make_xml()
