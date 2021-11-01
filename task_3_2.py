#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. 
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(num):
    list_translate = {'zero': 'ноль', 'one':'один', 'two':'два', 'three':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь', 'eight':'восемь', 'nine':'девять', 'ten':'десять'}
    return list_translate[num]


# In[8]:


num_translate_adv('zero')


# In[ ]:




