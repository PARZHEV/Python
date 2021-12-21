#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, 
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию 
# и не завершиться с ошибкой.


# In[1]:


class ZeroError():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def check(self):
        try:
            c = self.a / self.b
        except ZeroDivisionError:
            c = 0
        print(c)
    
mc = ZeroError(1,0)
mc.check()


# In[ ]:




