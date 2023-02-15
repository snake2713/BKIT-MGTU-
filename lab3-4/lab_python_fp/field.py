# Необходимо реализовать генератор field. Генератор field последовательно выдает значения ключей словаря. 
def field(items, *args):
    #items - список словарей
    # *args - неограниченное количество аргументов
    assert len(args) > 0 #проверяем на истинность 
               
           # Реализация генератора
                
    if len(args) > 1:
        for el in items:
            dct = {}
            for keys, val in el.items():
                for arg in args:
                    if keys == arg: #ключ = значение 
                        dct[keys] = val #записываем для вывода в список 
            yield dct #возвращаем функцию с ее локальными переменными
    else:
        for el in items:
            for keys in el:
                for arg in args:
                    if keys == arg:
                        yield el[keys]


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    print(list(field(goods, 'title')))
    #field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
    print(list(field(goods, 'title', 'price')))
    #field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха'}