#!/usr/bin/env python
# coding: utf-8

# In[106]:


# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. 
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, 
# разделитель между значениями — запятая. 
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. 
# Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, 
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». 
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

import csv
with open("users2.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    count = 0
    for row in file_reader:
        if count == 0:
            a = f'{" ".join(row)}'
            a = [a]
        else:
            a = a + [f'{" ".join(row)}']
        count += 1

with open("hobby2.csv", encoding='utf-8') as r_file2:
    file_reader2 = csv.reader(r_file2, delimiter = ",")
    count = 0
    for row in file_reader2:
        if count == 0:
            b = f'{" ".join(row)}'
            b = [b]
        else:
            b = b + [f'{" ".join(row)}']
        count += 1
uniq = a
fifa = b
uniq_and_fifa = dict(zip(uniq, fifa))
uniq_and_fifa

    


# In[112]:


d2 = uniq_and_fifa
with open('out.txt','w', encoding='utf-8') as out:
    for key,val in d2.items():
        out.write('{}:{}\n'.format(key,val))


# In[113]:


file_1 = open('out.txt', 'r', encoding='utf-8')
content = file_1.read()
print(content)


# In[ ]:




