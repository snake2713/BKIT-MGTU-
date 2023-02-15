import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    '''
    Проверяем можно ли преобразовать строку в число и если 
    нельзя, то вводим коэффицент вновь.
    '''
    try:
        coef = float(coef_str)
        # print(string_int)
    except ValueError:
        # Handle the exception
        print('Введено некорректное число.')
        coef = get_coef(index, 'Введите коэффициент снова:')
    return coef


def get_D(a, b, c):
    return b * b - 4 * a * c

def get_D2(a, b, c):
    return (- b + c) / (2 * a)

def get_roots(a, b, c):
    result = []  # Cписок корней
    '''
    Рассмотрим случаи, когда один из коэффициентов
    b или c равен 0 отдельно, так как их можно 
    вычислить проще.
    '''
    if c == 0:
        result.append(0)
        Dc = - b / a
        if Dc > 0:
            root1 = math.sqrt(Dc)
            root2 = - math.sqrt(Dc)
            result.append(root1)
            result.append(root2)
        return result

    elif b == 0:
        Db = - c / a
        if Db > 0:
            root1 = math.sqrt(math.sqrt(Db))
            root2 = - math.sqrt(math.sqrt(Db))
            result.append(root1)
            result.append(root2)
        if Db == 0:
            result.append(0)
        return result

    else:
        D1 = get_D(a, b, c)
        if D1 < 0:
            return result
        elif D1 == 0:
            D2 = get_D2(a, b, 0)
            if D2 < 0:
                return result
            # Если D2 = 0, то b = 0, а такой случай мы разобрали
            else:
                root1 = - math.sqrt(D2)
                root2 = math.sqrt(D2)
                result.append(root1)
                result.append(root2)
            return result
        else:
            D3 = (a, b, -math.sqrt(D1))
            if D3 == 0:
                result.append(0)
            if D3 > 0:
                root1 = - math.sqrt(D3)
                root2 = math.sqrt(D3)
                result.append(root1)
                result.append(root2)
            D4 = (a, b, math.sqrt(D1))
            if D4 == 0:
                result.append(0)
            if D4 > 0:
                root3 = - math.sqrt(D4)
                root4 = math.sqrt(D4)
                result.append(root3)
                result.append(root4)
            return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    while a == 0:
        a = get_coef(1, 'Коэффицент A не может быть равен 0. Введите коэффициент А снова:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))