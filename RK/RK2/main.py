from unittest import TestCase, main
from RK1 import * 

class order_test(TestCase):
    def test_1(self):
        expected_result_for_C1 = [('Антикварная лавка', ['Курс Python', 'Анна Каренина']),
                                  ('Аллегория', ['Евгений Онегин'])]
        res_C1 = []
        for i in Shops:
            book = list(filter(lambda a: a[2] == i.name, one_to_many))
            if i.name[0] == 'А':
                s_name = [x for x, _, _ in book]
                res_C1.append((i.name, s_name))
        self.assertEqual(res_C1, expected_result_for_C1)

    def test_2(self):
        expected_result_for_C2 = [('Книжный лабиринт', 100),
                                  ('Антикварная лавка', 179),
                                  ('Читай-город', 254),
                                  ('Аллегория', 660),
                                  ('Достоевский', 700)]
        res_unsorted_C2 = []
        for s in Shops:
            s_book = list(filter(lambda i: i[2] == s.name, one_to_many))
            if len(s_book) > 0:
                prices = [price for _, price, _ in s_book]
                prices_min = min(prices)
                res_unsorted_C2.append((s.name, prices_min))
        res_C2 = sorted(res_unsorted_C2, key=itemgetter(1))
        self.assertEqual(res_C2, expected_result_for_C2)

    def test_3(self):
        expected_result_for_C3 = [('Книжный лабиринт', 'Анжелика'),
                                  ('Антикварная лавка', 'Анна Каренина'),
                                  ('Достоевский', 'Всадник без головы'),
                                  ('Аллегория', 'Евгений Онегин'),
                                  ('Антикварная лавка', 'Курс Python'),
                                  ('Читай-город', 'Левша'),
                                  ('Читай-город', 'Повесть временных лет')]

        # Перебираем все отделы
        many_to_many.sort(key=lambda i: i[1])
        self.assertEqual(many_to_many, expected_result_for_C3)


if __name__ == '__main__':
    main()