from selenium import webdriver
from datetime import timedelta
from datetime import datetime
import os
import sys
from selenium.webdriver.chrome.options import Options
import pickle

months = {
    '1': 'jan',
    '2': 'feb',
    '3': 'mar',
    '4': 'apr',
    '5': 'may',
    '6': 'jun',
    '7': 'jul',
    '8': 'aug',
    '9': 'sep',
    '10': 'oct',
    '11': 'nov',
    '12': 'dec',
    1: 'jan',
    2: 'feb',
    3: 'mar',
    4: 'apr',
    5: 'may',
    6: 'jun',
    7: 'jul',
    8: 'aug',
    9: 'sep',
    10: 'oct',
    11: 'nov',
    12: 'dec'
}

def genReadings():
    opts = Options()
    opts.add_argument('--headless')
    get = lambda n: c.find_element_by_css_selector(f'#center-col > p:nth-child({n})').text
    c = webdriver.Chrome(options = opts)
    t = datetime.today()
    d = 6 - t.weekday()
    t += timedelta(d)
    m, d, y = t.month, t.day, t.year
    c.get(f'https://suscopts.org/readings/{y}/{months[m]}/{d}/')
    readings = {
        'Vespers Gospel': get(9) + get(10),
        'Matins Gospel': get(14) + get(15),
        'Pauline Epistle': get(19),
        'Catholic Epistle': get(21),
        'Acts': get(23),
        'Synxarium': get(25),
        'Gospel': get(27) + get(28),
    }
    with open('readings.pickle', 'wb') as file: file.write(pickle.dumps(readings))

def getReadings():
    with open('readings.pickle', 'rb') as file: readings =  pickle.loads(file.read())
    r = {}
    for key, value in readings.items():
        r[key] = value.replace('\n', '<br />')
    return r