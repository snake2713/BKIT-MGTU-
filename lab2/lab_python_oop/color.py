class FigureColor:
    """
    Класс «Цвет фигуры», он содержит свойство для описания цвета геометрической фигуры
    """
    def __init__(self): #init нужен для инициализации экземпляров класса после их создания 
        self._color = None #после инициализации имеет значение None

    @property #нужен для определения методов класса, которые действуют как атрибуты
    #также property позволяет превращать атрибуты класса в свойства или управляемые атрибуты
    def colorproperty(self):
        """
        Геттер
        """
        return self._color

    @colorproperty.setter
    def colorproperty(self, value):
        """
        Сеттер
        """
        self._color = value