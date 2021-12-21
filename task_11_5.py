#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу 
# в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).


# In[7]:


import re


stockdata = []
data = {}

class Stock:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers
    
    @classmethod
    def save_data(cls, name, numbers):
        
        data['name'] = name
        data['number'] = numbers
        return stockdata.append(data) 
           

        

    
a = Stock.save_data('Printer',124)
print(stockdata)

