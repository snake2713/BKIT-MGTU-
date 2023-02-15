from abc import ABC
from abc import abstractmethod


class Figure(ABC):
    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def square(self): #с помощью self можно обращаться внутри класса к функциональности текущего объекта
        """
      Виртуальный метод для вычисления площади фигуры.
        """
        pass