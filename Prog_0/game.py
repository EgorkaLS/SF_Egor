
from unicodedata import name
import numpy as np


def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток до отгадывания числа
    """

    count = 0   #начальная инициализация счётчика попыток 
    lo_pred = 1 # нижняя граница диапазона загадываемых чисел
    hi_pred=101 # верхняя граница диапазона загадываемых чисел (можно увеличить для расширения диапазона здесь и 47 стр.)
    predict_number = np.random.randint(lo_pred, hi_pred) # предполагаемое число

    while True:
        count += 1
        if predict_number > number: 
            hi_pred = predict_number # Снижаем верхнюю границу при неудачной попытке
            predict_number = np.random.randint(lo_pred, predict_number)  
        if predict_number < number:
            lo_pred = predict_number  # завышаем нижнюю границу при неудачной попытке
            predict_number = np.random.randint(predict_number, hi_pred)  
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

#print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Алгоритм угадывает число в среднем за: {score} попыток')
    return (score)

# RUN
if name == "mine":
    score_game(random_predict)