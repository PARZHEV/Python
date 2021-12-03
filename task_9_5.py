#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


# In[20]:


class Stationery:
    
    title = 'Name'
        
    def draw(self):
         print("Запуск отрисовки")

class Pen(Stationery):
    
    
    def draw(self):
        print('Запуск отрисовки Ручкой')

class Pencil(Stationery):
        
    def draw(self):
        print("Запуск отрисовки карандашом")
        
class Stationery(Stationery):
        
    def Handle(self):
        print("Запуск отрисовки маркером")
        
        
s = Stationery()
s.draw()
c = Pen()
c.draw()

