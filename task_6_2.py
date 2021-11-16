#!/usr/bin/env python
# coding: utf-8

# In[28]:


# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.

import re


with open('nginx_logs.txt') as ip:
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        log = ip.read()
        ip_list = re.findall(regexp, log)

from collections import Counter
counter = Counter(ip_list)

max_val = max(counter.values())

def get_key(counter, value):
    for k, v in counter.items():
        if v == value:
            return k

print(get_key(counter, max_val))

