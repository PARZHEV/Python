#!/usr/bin/env python
# coding: utf-8

# In[82]:


# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...


# @type_logger
# def calc_cube(x):
#    return x ** 3

# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; 
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? 
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(function_to_decorate):
    def fun(arg1): 
        print (arg1, ':', type(arg1))
        function_to_decorate(arg1)
    return fun
 
@type_logger
def calc_cube(x):
    return x ** 3
 
a = calc_cube(5)


# In[ ]:




