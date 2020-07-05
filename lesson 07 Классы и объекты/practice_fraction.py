class Fraction():
    """Класс для работы с дробями в виде "числитель/знаменатель". Поддерживает различные методы для
    работы с ним, включая перегрузку операторов"""

    def __init__(self, a = 0, b = 1):
        self.a = a
        self.b = b

    def __str__(self):
        return '{}/{}'.format(self.a, self.b)

    def convert_to_fraction(self, number):
        """Возвращает тип fracnion из другого типа"""
        if isinstance(number, Fraction):
            self.a, self.b = number.a, number.b
        else:
            self.a, self.b = number, 1

    def reduction_to_the_common_base(self, frac1, frac2):
        """Приведение двуъ дробей к общему основанию"""
        if frac1.b != frac2.b: # Приводим к общему основанию
            frac1.a *= frac2.b
            frac1.b *= frac2.b
            frac2.a *= frac1.b
            frac2.b *= frac1.b
        return frac1, frac2

    def __add__(self, other):
        """Сложение с другой дробью или числом"""
        frac1 = Fraction()
        frac1.a, frac1.b = self.a, self.b # Мы не хотим побочных эффектов при вычислениях
        frac2 = Fraction()
        frac2.convert_to_fraction(other)
        # self, other = reduction_to_the_common_base(self, other)
        if frac1.b != frac2.b: # Приводим к общему основанию
            frac1.a, frac1.b, frac2.a, frac2.b = frac1.a * frac2.b, frac1.b * frac2.b, frac2.a * frac1.b, frac2.b * frac1.b
        # непосредственно сложение дробей
        result = Fraction()
        result.a = frac1.a + frac2.a
        result.b = frac1.b
        return result

    def __sub__(self, other):
        """Вычитание из одной дроби другой, включая простое число"""
        frac1 = Fraction()
        frac1.a, frac1.b = self.a, self.b # Мы не хотим побочных эффектов при вычислениях
        frac2 = Fraction()
        frac2.convert_to_fraction(other)
        if frac1.b != frac2.b: # Приводим к общему основанию
            frac1.a, frac1.b, frac2.a, frac2.b = frac1.a * frac2.b, frac1.b * frac2.b, frac2.a * frac1.b, frac2.b * frac1.b
        # непосредственно сложение дробей
        result = Fraction()
        result.a = frac1.a - frac2.a
        result.b = frac1.b
        return result
    
    def __mul__(self, other):
        """Умножение одной дроби на другую, включая простое число"""
        frac1 = Fraction()
        frac1.a, frac1.b = self.a, self.b # Мы не хотим побочных эффектов при вычислениях
        frac2 = Fraction()
        frac2.convert_to_fraction(other)
        # непосредственно умножение дробей
        result = Fraction()
        result.a = frac1.a * frac2.a
        result.b = frac1.b * frac2.b
        return result
  
    def __int__(self):
        """Приведение к простому целому числу"""
        return int(self.a / self.b)

    def __float__(self):
        """Приведение к числу с плавающей точкой"""
        return float(self.a / self.b)

class OperationsOnFraction(Fraction):
    
    def getint(self):
        """Возвращает целую часть дроби"""
        return int(self)

    def getfloat(self):
        """Возвращает представление дроби в виде числа с плавающей точкой"""
        return float(self)

num_a = Fraction(3, 2)
print('num_a =', num_a)
num_b = Fraction(4, 3)
print('num_b =', num_b)
print('num_a + num_b =', num_a + num_b)
print('num_a + 3 = ', num_a + 3)
print('num_a - num_b =', num_a - num_b)
print('num_a + 3 = ', num_a - 4)
print('num_a * num_b =', num_a * num_b)
print('num_a * 3 = ', num_a * 4)
print('int(num_a) = ', int(num_a))
print('float(num_a) = ', float(num_a))

num_c = OperationsOnFraction(5, 4)
print('num_c =', num_c)
print('num_c.getint = {}'.format(num_c.getint()))
print('num_c.getfloat =', num_c.getfloat())
