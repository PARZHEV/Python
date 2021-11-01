#!/usr/bin/env python
# coding: utf-8

# In[50]:


# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")

def num_translate(num):
    list_translate = {'zero': 'ноль', 'one':'один', 'two':'два', 'three':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь', 'eight':'восемь', 'nine':'девять', 'ten':'десять'}
    return list_translate[num]

num_translate('zero')

