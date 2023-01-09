import requests
from datetime import datetime

paragraphs = []
reversed_paragraphs = []
url = 'https://baconipsum.com/api?type=meat-and-filler'
word = 'Pancetta'
counter = 0
min_paragraphs_num = 5


def get_paragraphs():
    global paragraphs
    number_of_paragraphs = input('Enter number of paragraphs:')
    if int(number_of_paragraphs) >= min_paragraphs_num:
        response = requests.get(url+'&paras='+number_of_paragraphs)
        paragraphs = response.json()
    else:
        print('Type number >= 5')
        get_paragraphs()


def reverse_paragraphs():
    global paragraphs
    global reversed_paragraphs
    reversed_paragraphs = paragraphs[::-1]


def calculete_paragraphs_with_word():
    global counter
    for paragraph in paragraphs:
        if paragraph.find(word) != -1:
            counter += 1


def reversed_paragraphs_to_str():
    str = ''
    for paragraph in reversed_paragraphs:
        str += paragraph+'\n'
    return str


def save_to_file():
    global counter
    global reversed_paragraphs
    name = 'Maksym Bielozorov'
    current_datetime = datetime.now()
    current_date = current_datetime.strftime('%d.%m.%Y')
    try:
        file = open('results.txt', 'w')
        file.write(name+'\n')
        file.write(f'Date: {current_date}\n')
        file.write(f'Number of paragraphs includes "Pancetta": {counter}\n')
        file.write(f'Reversed paragraphs:\n{reversed_paragraphs_to_str()}\n')
        file.close()
    except:
        print('Something wrong')


def main():
    get_paragraphs()
    reverse_paragraphs()
    calculete_paragraphs_with_word()
    save_to_file()


main()
