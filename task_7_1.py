#!/usr/bin/env python
# coding: utf-8

# In[11]:


# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); 
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; 
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

dir_name = 'my_project'
if not os.path.exists(dir_name):
   os.mkdir(dir_name)

dir_path = os.path.join('my_project', 'settings')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)

dir_path = os.path.join('my_project', 'mainapp')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)

dir_path = os.path.join('my_project', 'adminapp')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)

dir_path = os.path.join('my_project', 'authapp')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)


# In[12]:





# In[13]:





# In[ ]:




