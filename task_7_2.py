#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html


# In[25]:


import os
dir_name = 'my_project'
if not os.path.exists(dir_name):
   os.mkdir(dir_name)

cur_dir = os.getcwd()

dir_path = os.path.join('my_project', 'settings')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)

directory_folder = cur_dir+'\\'+dir_path+'\\__init__.py'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")

directory_folder = cur_dir+'\\'+dir_path+'\\dev.py'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")

directory_folder = cur_dir+'\\'+dir_path+'\\prod.py'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")

dir_path = os.path.join('my_project', 'mainapp')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)

directory_folder = cur_dir+'\\'+dir_path+'\\__init__.py'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")
    
directory_folder = cur_dir+'\\'+dir_path+'\\models.py'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")
    
directory_folder = cur_dir+'\\'+dir_path+'\\views.py'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")

dir_path = os.path.join('my_project', 'mainapp', 'templates')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)

dir_path = os.path.join('my_project', 'mainapp', 'templates', 'mainapp')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)

directory_folder = cur_dir+'\\'+dir_path+'\\base.html'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")

directory_folder = cur_dir+'\\'+dir_path+'\\index.html'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")


dir_path = os.path.join('my_project', 'authapp')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)

directory_folder = cur_dir+'\\'+dir_path+'\\__init__.py'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")
    
directory_folder = cur_dir+'\\'+dir_path+'\\models.py'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")
    
directory_folder = cur_dir+'\\'+dir_path+'\\views.py'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")

dir_path = os.path.join('my_project', 'authapp', 'templates')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)

dir_path = os.path.join('my_project', 'authapp', 'templates', 'authapp')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)

directory_folder = cur_dir+'\\'+dir_path+'\\base.html'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")

directory_folder = cur_dir+'\\'+dir_path+'\\index.html'
with open(directory_folder, 'w') as file: 
    file.write("этот текст создан автоматически")



# In[ ]:




