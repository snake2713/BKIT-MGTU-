import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число

    try: #пробуем преобразовать строку в число
        coef = float(coef_str)
    except ValueError: #в функцию передан аргумент с неподдерживаемым значением.
        print('Введено некорректное число.')
        coef = get_coef(index, 'Введите коэффициент снова:')
    return coef


def get_D(a, b, c):
    return b * b - 4 * a * c

def get_roots(a, b, c):
    result = [] 
     # Рассматриваем случаи, когда b или c уравнения равны 0:
    if c == 0:
        result.append(0)
        Dc = - b / a #решаем простое уравнение типа x^2 - bx 
        if Dc > 0:
            root1 = math.sqrt(Dc)
            root2 = - math.sqrt(Dc)
            result.append(root1) #добавляем корень в конец списка результатов
            result.append(root2) #аналогично
        return result

    elif b == 0:
        Db = - c / a #решаем простое уравнение типа x^4 = c
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
            D2 = - b / (2 * a)
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
            D3 = (- b - math.sqrt(D1)) / (2 * a)
            if D3 == 0:
                result.append(0)
            if D3 > 0:
                root1 = - math.sqrt(D3)
                root2 = math.sqrt(D3)
                result.append(root1)
                result.append(root2)
            D4 = (- b + math.sqrt(D1)) / (2 * a)
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
        a = get_coef(1, 'Введите коэффициент А снова:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots) #возвращаем количество символов в строке(те корней)
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


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()