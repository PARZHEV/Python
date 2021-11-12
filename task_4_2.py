#!/usr/bin/env python
# coding: utf-8

# In[121]:


# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) 
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно 
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в 
# обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? 
# Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными 
# величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента 
# передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком 
# регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
from xml.dom import minidom

# Ежедневные курсы валют ЦБ РФ
url = "http://www.cbr.ru/scripts/XML_daily.asp"

# Чтение URL
webFile = urllib.request.urlopen(url)
data = webFile.read()

# Имя файла
UrlSplit = url.split("/")[-1]
ExtSplit = UrlSplit.split(".")[1]
FileName = UrlSplit.replace(ExtSplit, "xml")

# Парисинг xml
doc = minidom.parse(FileName)
# Парисинг xml
currency = doc.getElementsByTagName("Valute")

charcode = []
for rate in currency:
    name = rate.getElementsByTagName("CharCode")[0]
    value = rate.getElementsByTagName("Value")[0]
    str = "{0}".format(name.firstChild.data, value.firstChild.data)
    charcode.append(str)

Value = []
for rate in currency:
    value = rate.getElementsByTagName("Value")[0]
    str = "{0}".format(value.firstChild.data)
    str = float(str.replace(',','.'))
    Value.append(str)
Value

myDict = {charcode[i]: Value[i] for i in range(0, len(charcode), 1)} 

       
def currency_rates(inputCur2):
        return myDict[inputCur2]
       


# In[122]:


currency_rates('USD')


# In[123]:


currency_rates("EUR")


# In[ ]:





# In[ ]:




