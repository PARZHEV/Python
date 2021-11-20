#!/usr/bin/env python
# coding: utf-8

# In[10]:


# 6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с 
# интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
# При записи передавать из командной строки значение суммы продаж. 
# Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, 
# включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
import csv
import numpy as np

def Bulka_price(): 
   with open("bakery.csv", 'a', encoding='utf-8') as r_file:
          r_file.write(f"{input()}"+"\n")
        
   with open("bakery.csv", 'r', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        for row in file_reader:
            if count == 0:
                a = [f'{".".join(row)}']
            else:
                a = a + [f'{".".join(row)}']
            count += 1
        a = list(np.float_(a))
        return sum(a)



# In[11]:


Bulka_price()


# In[9]:


a


# In[ ]:


def Bulka_price_list(): 
   with open("bakery.csv", 'a', encoding='utf-8') as r_file2:
          r_file2.write(f"{input()}"+"\n")
        
   with open("bakery.csv", 'r', encoding='utf-8') as r_file2:
        file_reader2 = csv.reader(r_file2, delimiter = ",")
        count = 0
        for row in file_reader:
            if count == 0:
                b = [f'{".".join(row)}']
            else:
                b = b + [f'{".".join(row)}']
            count += 1
            b = list(np.float_(b))
            return b


# In[ ]:


Bulka_price_list()


# In[ ]:


with open("bakery.csv", 'a', encoding='utf-8') as r_file:
          r_file.write(f"{input()}"+"\n")
        
with open("bakery.csv", 'r', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        for row in file_reader:
            if count == 0:
                a = [f'{".".join(row)}']
            else:
                a = a + [f'{".".join(row)}']
            count += 1
        a


# In[32]:


a1 = [1,2]

len(a1)
if len(a1) ==0:
    print(a1)
elif len(a1) ==1:
    print(a1[0]) #вывести с цифры до конца
elif len(a1) ==2:
    print(a1[1:]) #вывести с цифры первой до второй


# In[17]:


with open("bakery.csv", 'r', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        for row in file_reader:
            if count == 0:
                a = [f'{".".join(row)}']
            else:
                a = a + [f'{".".join(row)}']
            count += 1
a


# In[ ]:


import csv
import numpy as np

with open("bakery.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    count = 0
    for row in file_reader:
        if count == 0:
            a = f'{".".join(row)}'
            a = [a]
        else:
            a = a + [f'{".".join(row)}']
        count += 1


a = list(np.float_(a))
sum(a)


# In[ ]:




