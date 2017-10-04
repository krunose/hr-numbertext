# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 nulis
1 vienas
2 du
3 trys
4 keturi
5 penki
6 šeši
7 septyni
8 aštuoni
9 devyni
10 dešimt
11 vienuolika
12 dvylika
13 trylika
14 keturiolika
15 penkiolika
16 šešiolika
17 septyniolika
18 aštuoniolika
19 devyniolika

2(\d) dvidešimt $1
3(\d) trisdešimt $1
([4-9])(\d) $1|asdešimt $2

1(\d\d) šimtas $1
(\d)(\d\d) $1 šimtai $2

1(\d{3}) tūkstantis $1
(\d?1\d|\d?\d?0)(\d{3}) $1 tukstančių $2
(\d?\d1)(\d{3}) $1 tūkstantis $2
(\d{1,3})(\d{3}) $1 tūkstančiai $2

(\d?1\d|\d?\d?0)(\d{6}) $1 milijonų $2
(\d?\d?1)(\d{6}) $1 milijonas $2
(\d{1,3})(\d{6}) $1 milijonai $2

(\d?1\d|\d?\d?0)(\d{9}) $1 milijardų $2
(\d?\d?1)(\d{9}) $1 milijardas $2
(\d{1,3})(\d{9}) $1 milijardai $2

(\d?1\d|\d?\d?0)(\d{12}) $1 trilijonų $2
(\d?\d?1)(\d{12}) $1 trilijonas $2
(\d{1,3})(\d{12}) $1 trilijonai $2

(\d?1\d|\d?\d?0)(\d{15}) $1 kvadrilijonų $2
(\d?\d?1)(\d{15}) $1 kvadrilijonas $2
(\d{1,3})(\d{15}) $1 kvadrilijonai $2

(\d?1\d|\d?\d?0)(\d{18}) $1 kvintilijonų $2
(\d?\d?1)(\d{18}) $1 kvintilijonas $2
(\d{1,3})(\d{18}) $1 kvintilijonai $2

# negative numbers

[-−](\d+) minus |$1

# decimals

# decimals
([-−]?\d+)[.,] $1| taškas
([-−]?\d+[.,]\d*)(\d) $1| |$2

# currency

# unit/subunit

us:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \1
up:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \2
ug:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \3
ss:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \4
sp:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \5
sg:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \6

LTL:(\D+) $(\1: litas, litų, litai, centas, centų, centai)
EUR:(\D+) $(\1: euras, eurų, eurai, centas, centų, centai)

"([A-Z]{3}) ([-−]?\d*(1\d|0))([.,]00?)?" $2| $(\1:up)
"([A-Z]{3}) ([-−]?\d*1)([.,]00?)?" $2| $(\1:us)
"([A-Z]{3}) ([-−]?\d+)([.,]00?)?" $2| $(\1:ug)

"(([A-Z]{3}) [-−]?\d+)[.,](01)" $1 |$(1) $(\2:ss)
"((LTL|EUR) [-−]?\d+)[.,](1\d|\d0)" $1 $3| $(\2:sp)
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1 |$3 $(\2:sg)

"""
from __future__ import unicode_literals
