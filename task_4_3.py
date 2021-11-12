#!/usr/bin/env python
# coding: utf-8

# In[14]:


# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, 
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. 
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

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
        root = doc.getElementsByTagName("ValCurs")[0]
        date = "Date - {date}".format(date=root.getAttribute('Date'))
        return myDict[inputCur2], date
               


# In[15]:


currency_rates('USD')


# In[ ]:




