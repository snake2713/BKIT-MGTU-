from operator import itemgetter


class Book:
    """Книга"""

    def __init__(self, id, price, name, shop_id):
        self.id = id
        self.price = price
        self.name = name
        self.shop_id = shop_id

class Shop:
    """Книжный магазин"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class BookShop:
    """ 'Книги магазина' для реализации связи многие-ко-многим """
    def __init__(self, shop_id, book_id):
        self.shop_id = shop_id
        self.book_id = book_id


Shops = [
    Shop(1, 'Книжный лабиринт'),
    Shop(2, 'Читай-город'),
    Shop(3, 'Антикварная лавка'),
    Shop(4, 'Достоевский'),
    Shop(5, 'Аллегория')
]

Books = [
    Book(1, 100, 'Анжелика', 1),
    Book(2, 339, 'Левша', 2),
    Book(3, 254, 'Повесть временных лет', 2),
    Book(4, 468, 'Курс Python', 3),
    Book(5, 179, 'Анна Каренина', 3),
    Book(6, 700, 'Всадник без головы', 4),
    Book(7, 660, 'Евгений Онегин', 5)
]

Books_Shops = [
    BookShop(1, 1),
    BookShop(2, 2),
    BookShop(2, 3),
    BookShop(3, 4),
    BookShop(3, 5),
    BookShop(4, 6),
    BookShop(5, 7)
]


def main():
    one_to_many = [(b.name, b.price, s.name)
                   for s in Shops
                   for b in Books
                   if b.shop_id == s.id]

    many_to_many_temp = [(s.name, bs.shop_id, bs.book_id)
                         for s in Shops
                         for bs in Books_Shops
                         if s.id == bs.shop_id]

    many_to_many = [(name, b.name)
                    for name, shop_id, book_id in many_to_many_temp
                    for b in Books if b.id == book_id]

    print('Задание В1')
    res_1 = []
    for i in Shops:
        book = list(filter(lambda a: a[2] == i.name, one_to_many))
        if i.name[0] == 'А':
            s_name = [x for x, _, _ in book]
            res_1.append((i.name, s_name))
    print(res_1)

    print('Задание В2')
    res_unsorted = []
    for s in Shops:
        s_book = list(filter(lambda i: i[2] == s.name, one_to_many))
        if len(s_book) > 0:
            prices = [price for _, price, _ in s_book]
            prices_min = min(prices)
            res_unsorted.append((s.name, prices_min))
    res_2 = sorted(res_unsorted, key=itemgetter(1))
    print(res_2)

    print('Задание В3')
    res_13 = {}
    # Перебираем все отделы
    many_to_many.sort(key=lambda i: i[1])
    print(many_to_many)

if __name__ == '__main__':
    main()