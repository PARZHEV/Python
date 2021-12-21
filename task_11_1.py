#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и 
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, 
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.


# In[1]:


import re

class Date:
    def __init__(self, date):
        self.date = date
      
    
    @classmethod
    def d_m_y(cls, date):
    
        sp = re.findall(r'\d+', date)
        d = int(sp[0])
        m = int(sp[1])
        y = int(sp[2])
        return d, m, y
    
    @staticmethod
    def check(m, y):
        if 1 <= m <= 12:
            print('Все хорошо по месяцу')
        else:
            print('Месяц должен быть от 1 до 12')
        if 1900 <= y:
            print('Все хорошо по году')
        else:
            print('Год должен быть от 1900 и выше')
        

    
a = Date.d_m_y('12-12-1022')
print(a)
print(Date.check(a[1],a[2]))


# In[ ]:




