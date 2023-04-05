'''  Угадай число
Компьютер сам загадывает и отгадывает '''

import numpy as np


def random_predict(number: int=1) -> int:
    """ Угадываем число методом половинного деления (см. readme.md)

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Число попыток (начальное значение)
    count = 0
    # Границы рассматриваемого целочисленного отрезка (первоначальные)
    a, b = 1, 101
    
    while True:
        count += 1  # Включается счетчик числа попыток
        predict_number = (a+b) // 2  # Предполагаемое число как целочисленная середина отрезка
        
        if predict_number == number:
            break   #  В этом случае загаданное число найдено :)
        
        elif predict_number < number:
            a = predict_number  # Уменьшаем отрезок вдвое сдвинув к середине нижний конец отрезка
            
        else:
            b = predict_number  # Уменьшаем отрезок вдвое сдвинув к середине верхний конец отрезка
    
    return count


def score_game(random_predict) -> int:
    """ Определение среднего количества попыток угадывания из 1_000 подходов

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    
    # Список, где будут храниться числа попыток, потребовавшихся для угадывания
    # каждого загаданного случайного числа
    count_ls = []
    
    # Массив, где будут храниться загадываемые случайные числа
    random_array = np.random.randint(1, 101, size=(1_000))
    
    # Заполняется список 
    for number in random_array:
        count_ls.append(random_predict(number)) 
    
    # Определяется среднее значение количества попыток   
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score
    

if __name__ == '__main__':
    score_game(random_predict) 
    
 