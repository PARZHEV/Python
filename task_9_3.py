#!/usr/bin/env python
# coding: utf-8

# In[34]:


# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, 
# {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии 
# (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, 
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
   


    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income

    


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
       

    def get_full_name(self):
        self.full_name = f'{self.name} {self.surname}'
        return self.full_name

    def get_total_income(self):
        self.total_income = self.income['wage']+self.income['bonus']
        return self.total_income



r = Position('Ivanov','Ivan', 'Cleark', {"wage": 10000, "bonus": 1000} )

print(r.get_full_name())
print(r.get_total_income())


# In[ ]:




