import re

mytext = "name@rokot.ru 19289 Rokot Hermta 1 hello 19817 marat@gmail.com"

"""
\d = any Digits [0-9]
\D = any non Gigits
\w = (A-Z, a-z)
\W = any, кроме букфф
\s = пробелы
\S = any но не space
\. = точка
+ = неважно что будет дальше
(?!) = исключение
"""

textlookfor = r"\d\d\d"
textlookfor2 = r"[0-9][0-9]"
textlookfor3 = r"\wok\w+\.\w\w"


allresults = re.findall(textlookfor, mytext)
allresults2 = re.findall(textlookfor2, mytext)

allresults3 = re.findall(textlookfor3, mytext)


print(allresults)
print(allresults2)
print(allresults3)
