from functions import *

print('Это программа для работы с текстом\nЕе фунцкционал будет доробатываться')
user_text = input('Введите текст, с которым хотите работать\n')

function_choise = input('Введите "1", если хотите узнать статистику по этому тексту\n')

if function_choise == '1':
    print(stat_func(user_text))





