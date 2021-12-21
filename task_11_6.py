#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


# In[77]:


class CountError(Exception):

    def __init__(self,  number, message="введите число"):
      
        self.number = number
        self.message = message
        # переопределяется конструктор встроенного класса `Exception()`
        super().__init__(self.message)

try:
    number = int(input())
except:
    raise CountError(number)


# In[ ]:




