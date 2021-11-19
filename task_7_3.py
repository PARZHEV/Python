#!/usr/bin/env python
# coding: utf-8

# In[133]:


# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). 
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках 
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, 
# например, во фреймворке django.


import os
from collections import defaultdict
from os.path import relpath
from shutil import copyfile, copy, copy2
import django

dir_path = os.path.join('my_project')
django_files = {}
for dir_path, dirs, files in os.walk(dir_path):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        rel_path = relpath(os.path.join(dir_path, file))
        if ext not in django_files:
            django_files[ext] = []
        django_files[ext].append(rel_path)

path_to_authapp = os.path.join('my_project', 'templates', 'authapp')
path_to_mainapp = os.path.join('my_project', 'templates', 'mainapp')
for i in django_files['html']:
    if i.find('authapp', 1) >0:
        path_from = os.path.join(i)
        copy(path_from, path_to_authapp)
    else:
        path_from = os.path.join(i)
        copy(path_from, path_to_mainapp)


# In[ ]:




