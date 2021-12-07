#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: 
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. 
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.


# In[17]:


from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_method_1(self):
        pass


class MyClass():

    
    def my_method_1(self, V, H):
        self.V = V
        self.H = H
        self.resultsV = self.V/6.5 + 0.5
        self.resultsH = 2*self.H + 0.3
        self.result = self.resultsV + self.resultsH
        
    @property
    def my_method(self):
        return f" {self.result}"

mc = MyClass()
mc.my_method_1(1,2)
print(mc.V)
print(mc.H)

print(mc.my_method)


# In[ ]:




