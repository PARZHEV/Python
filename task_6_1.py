#!/usr/bin/env python
# coding: utf-8

# In[158]:


# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей 
# вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]

# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.


import re


with open('nginx_logs.txt') as ip:
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        log = ip.read()
        ip_list1 = re.findall(regexp, log)


with open('nginx_logs.txt') as get:
        regexp2 = r'G\w+[T]'
        log2 = get.read()
        get_list2 = re.findall(regexp2, log)


with open('nginx_logs.txt') as path:
        regexp3 = r'/\w+/\w+_\d{1}'
        log3 = path.read()
        path_list3 = re.findall(regexp3, log)

results = list(zip(ips_list, ips_list2, ips_list3 ))
results


# In[ ]:




