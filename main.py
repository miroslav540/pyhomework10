class Fabric:

    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type: str):
        types = {"dog": Dog, "bird": Bird, "fish": Fish}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fabric = Fabric()
    animal_from_fabric = fabric.make_animal('Bird', 'Соловей', 3, 5, 'соловейки', 'тру-ля-ля')
    print(animal_from_fabric)


print('--------------------------TASK 3----------------------------------')

'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.'''


class Sum:

    def __init__(self, drob1: str, drob2:str):
        self.drob1 = drob1
        self.drob2 = drob2

    def translate_str_to_digit(self, str_drob: str):
        data_chislit = int(str_drob.split('/')[0])
        data_znamenat = int(str_drob.split('/')[1])
        return data_chislit, data_znamenat

    def data_sum(self, data1, data2):
        a_ch = self.translate_str_to_digit(data1)[0]
        a_zn = self.translate_str_to_digit(data1)[1]
        b_ch = self.translate_str_to_digit(data2)[0]
        b_zn = self.translate_str_to_digit(data2)[1]
        ch = a_ch * b_zn + b_ch * a_zn
        zn = b_zn * a_zn
        res = (ch, zn)
        return res

    def __str__(self):
        return f'{self.drob1} + {self.drob2} =  {self.data_sum(self.drob1, self.drob2)[0]}/{self.data_sum(self.drob1, self.drob2)[1]}'

class Multy:

    def __init__(self, drob1: str, drob2:str):
        self.drob1 = drob1
        self.drob2 = drob2

    def translate_str_to_digit(self, str_drob: str):
        data_chislit = int(str_drob.split('/')[0])
        data_znamenat = int(str_drob.split('/')[1])
        return data_chislit, data_znamenat

    def data_mult(self, data1, data2):
        a_ch = self.translate_str_to_digit(data1)[0]
        a_zn = self.translate_str_to_digit(data1)[1]
        b_ch = self.translate_str_to_digit(data2)[0]
        b_zn = self.translate_str_to_digit(data2)[1]
        res = (a_ch * b_ch, a_zn * b_zn)
        return res

    def __str__(self):
        return f'{self.drob1} * {self.drob2} =  {self.data_mult(self.drob1, self.drob2)[0]}/{self.data_mult(self.drob1, self.drob2)[1]}'



a = '3/5'
b = '4/5'

sum1 = Sum(a, b)
mult1 = Multy(a,b)
print(sum1)