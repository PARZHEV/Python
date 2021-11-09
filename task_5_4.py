#!/usr/bin/env python
# coding: utf-8

# In[112]:


# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# ```

# Подсказка: использовать возможности python, изученные на уроке.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
def new_fun():
    x=[]
    for i in range(len(src)):
        x1  =  src[i]
        x2  =  src[i+1]
        if x1 < x2:
            x.append(x2)
print(x)


# In[83]:


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
def next_figure():
    for i in range(len(src)):
        x1  =  src[i]
        x2  =  src[i+1]
        if x1 < x2:
            yield x2
next_figure2 = next_figure()


# In[85]:


next(next_figure2)

