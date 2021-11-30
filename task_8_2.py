#!/usr/bin/env python
# coding: utf-8

# In[67]:


# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) 
# для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, 
#                                 <response_size>), например:

# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')


import re

figure2_list6
with open('nginx_logs.txt') as ip:
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        log = ip.read()
        ip_list1 = re.findall(regexp, log)
        
with open('nginx_logs.txt') as date:
        regexp2 = r'\d+/\w+/\d+\:\d+\:\d+\:\d+......'
        log2 = date.read()
        date_list2 = re.findall(regexp2, log)      
        
        
with open('nginx_logs.txt') as get:
        regexp3 = r'G\w+[T]'
        log3 = get.read()
        get_list3 = re.findall(regexp3, log)


with open('nginx_logs.txt') as path:
        regexp4 = r'/\w+/\w+_\d{1}'
        log4 = path.read()
        path_list4 = re.findall(regexp4, log)

with open('nginx_logs.txt') as figure:
        regexp5 = r'\s\d+\s'
        log5 = figure.read()
        figure_list5 = re.findall(regexp5, log)
        
with open('nginx_logs.txt') as figure2:
        regexp6 = r'\s\d\s'
        log6 = figure2.read()
        figure2_list6 = re.findall(regexp6, log)
 

results = list(zip(ip_list1, date_list2, get_list3, path_list4, figure_list5, figure2_list6))
results

