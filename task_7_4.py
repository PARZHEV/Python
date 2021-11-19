#!/usr/bin/env python
# coding: utf-8

# In[304]:


# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — 
# верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), 
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

# Так и не понял как сделать подсчет файликов и распределния их в словарь (честно сидел больше суток)
#  ниже мои потуги и попытки сделать эту задачу

import os
from collections import defaultdict
from os.path import relpath
from shutil import copyfile, copy, copy2
import django

dir_path = os.path.join('my_project')
django_files = {}
for root, dirs, files in os.walk(dir_path):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        rel_path = relpath(os.path.join(dir_path, file))
        if ext not in django_files:
            django_files[ext] = []
        django_files[ext].append(rel_path)
        
        

for ext, files in sorted(django_files.items(),
                        key=lambda x: len(x[1]), reverse=True):
                    print(f'{ext}: {len(files)}')


# In[302]:


dir_path = os.path.join('my_project')
django_files = {}
for root, dirs, files in os.walk(dir_path):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        rel_path = relpath(os.path.join(dir_path, file))
        if ext not in django_files:
            django_files[ext] = []
        django_files[ext].append(rel_path)
        
        

for ext, files in sorted(django_files.items(),
                        key=lambda x: len(x[1]), reverse=True):
                    print(f'{ext}: {len(files)}')


# In[301]:


import os

import django

dir_path = os.path.join('PARZHEV')
django_files = defaultdict(list)
for root, dirs, files in os.walk(dir_path):
       for file in files:
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            rel_path = relpath(os.path.join(root, file), dir_path)
            django_files[ext].append(rel_path)
django_files


# In[298]:


import os

import django
cur_dir = os.getcwd()
django_files = defaultdict(list)
root_dir = os.path.join('PARZHEV')
for root, dirs, files in os.walk(root_dir):
       for file in files:
            rel_path = relpath(os.path.join(file), root_dir)
            if os.stat(os.path.join(root_dir, rel_path)).st_size <40:
                django_files[2].append(rel_path)
            else:
                if os.stat(os.path.join(root_dir, rel_path)).st_size <40:
                    django_files[20].append(rel_path)
django_files 


# In[282]:


django_files 


# In[149]:


dir_path = os.path.join('my_project')
django_files = {}
for dir_path, dirs, files in os.walk(dir_path):
    for file in files:
        
        rel_path = relpath(os.path.join(dir_path, file))
        
        ext = 1
        
        if ext > os.stat(rel_path).st_size:
            django_files[ext] = []
        django_files[ext].append(rel_path)
        
        
        

for ext, files in sorted(django_files.items(),
                        key=lambda x: len(x[1]), reverse=True):
                    print(f'{ext}: {len(files)}')


# In[292]:


cur_dir


# In[9]:


for ext, files in sorted(django_files.items(),
                        key=lambda x: len(x[1]), reverse=True):
   print(f'{ext}: {len(files)}')


# In[15]:





# In[90]:



pathname = os.path.join('my_project')
os.stat(pathname).st_size


# In[330]:


import os

import django

root_dir = os.path.join('Python GB homework')
for root, dirs, files in os.walk(root_dir):
    django_files = {}
for root, dirs, files in os.walk(root_dir):
       for file in files:
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            rel_path = relpath(os.path.join(root, file), root_dir)
            if os.stat(os.path.join(root_dir, rel_path)).st_size < 10:
                    django_files[2].append(rel_path)
            else:
                os.stat(os.path.join(root_dir, rel_path)).st_size < 10
                django_files[2].append(rel_path)
django_files


# In[322]:


for file in files:
            rel_path = relpath(os.path.join(file), root_dir)
            


# In[ ]:




