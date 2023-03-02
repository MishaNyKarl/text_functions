def stat_func(text):
    """Функция для вывода статистики текста пользователя"""

    list_of_words = {}
    number_of_proposal = text.count('.') + text.count('?') + text.count('!')        #Подсчет предложений реализован через подсчет количества точек и знаков восклицательности

    list_of_text = cleaning(text) #Очистка текста

    number_of_words = 0 #Количество слов в тексте
    for word in list_of_text:
        number_of_words += 1
        if len(word) > 2:
            col = text.count(word)
            list_of_words[word] = col
    list_of_words_changible = list_of_words

    max_value = max(list_of_words_changible.values())       #Нахождение самых популярных слов в тексте и добавление их в словарь
    final_dict = {k: v for k, v in list_of_words_changible.items() if v == max_value}

    return f'Текст состоит из %s слов\n' %number_of_words + 'Количество предложений: ' + str(number_of_proposal) + '\nСамое популярное слово и его повторения: ' + str(final_dict)


def cleaning(text):
    """Функция используется для удаления знаков препинания и преобразования строки в массив list_of_text"""
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.replace('»', '')
    text = text.replace('«', '')
    text = text.replace(';', '')
    list_of_text = text.split(' ')

    return list_of_text