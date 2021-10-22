#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
#    Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
#    К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#    * Решить задачу под пунктом b, не создавая новый список.


# In[1]:


# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X)
results1 = []
for i in range(1000):
      if(i % 2 != 0):
        results1.append(int(i**3))      
print(results1)


# In[4]:


#    Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
p = []
for i in results1:
    str_i = str(i)
    lst_str = list(str_i)
    lst_num = map(int, lst_str)
    s = sum(lst_num)
    if(s % 7 == 0):
        p.append(int(i))
print(p)


# In[8]:


sum = 0
for i in p:
    sum += i
print(sum)


# In[7]:


#    К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
results2 = []
for i in range(1000):
      if(i % 2 != 0):
        results2.append(int(i**3+17))      
k = []
for i in results2:
    str_i = str(i)
    lst_str = list(str_i)
    lst_num = map(int, lst_str)
    s = sum(lst_num)
    if(s % 7 == 0):
        k.append(int(i))
print(k)


# In[9]:


sum = 0
for i in k:
    sum += i
print(sum)


# In[ ]:




