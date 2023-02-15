#сортировка по возрастанию 
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
#Без использованием lambda-функции.
    result = sorted(data, key=abs, reverse=True)
    #sorted(массив,key=функция ключа,reverse=False)
    print(result)
#С использованием lambda-функции.
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    #Lambda аргументы: выражение
    print(result_with_lambda)