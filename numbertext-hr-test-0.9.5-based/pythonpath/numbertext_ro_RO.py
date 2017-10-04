# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 zero
1 unu
2$ doi
2 două
3 trei
4 patru
5 cinci
6$ șase
6 șai
7 șapte
8 opt
9 nouă
10 zece
11 unsprezece
12 doisprezece
14 paisprezece
1(\d) $1sprezece
(\d)0 $1zeci
(\d)(\d) $(\10) și $2
1(\d\d) o sută $1
(\d)(\d\d) $1 sute $2
1(\d{3}) o mie $1
(1?\d)(\d{3}) $1 mii $2
(\d{1,3})(\d{3}) $1 de mii $2

1(\d{6}) un milion $1
(1?\d)(\d{6}) $1 milioane $2
(\d{1,3})(\d{6}) $1 de milioane $2
1(\d{9}) un miliard $1
(1?\d)(\d{9}) $1 miliarde $2
(\d{1,3})(\d{9}) $1 de miliarde $2
1(\d{12}) un trilion $1
(1?\d)(\d{12}) $1 trilioane $2
(\d{1,3})(\d{12}) $1 de trilioane $2
1(\d{15}) un cvadrilion $1
(1?\d)(\d{15}) $1 cvadrilioane $2
(\d{1,3})(\d{15}) $1 de cvadrilioane $2
1(\d{18}) un cvintilion $1
(1?\d)(\d{18}) $1 cvintilioane $2
(\d{1,3})(\d{18}) $1 de cvintilioane $2
1(\d{21}) un sextilion $1
(1?\d)(\d{21}) $1 sextilioane $2
(\d{1,3})(\d{21}) $1 de sextilioane $2
1(\d{24}) un septilion $1
(1?\d)(\d{24}) $1 septilioane $2
(\d{1,3})(\d{24}) $1 de septilioane $2

# negative number

[-−](\d+) minus |$1

# decimals

"([-−]?\d+)[.,]" $1| virgulă
"([-−]?\d+[.,])([^0]\d)" $1| |$2
"([-−]?\d+[.,])(\d)(\d)(\d)" $1| |$2 |$3 |$4
"([-−]?\d+[.,]\d*)(\d)" $1| |$2

# currency

# feminine/masculine correction for 1 and 2

f:(.*)unu \1 o
f:(.*do)i "\1uă "
m:(.*un)u \1
.:(.*) \1

# unit/subunit, singular/plural, feminine/masculine unit, feminine/masculine subunit

us(.).:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) $(\1:\6) \2
up(.).:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) $(\1:\6) \3
ss.(.):([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) $(\1:\6) \4
sp.(.):([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) $(\1:\6) \5

# "mm" means masculine unit and masculine subunit

CHF:(.+),(.+) $(\1mm: franc elvețian, franci elvețieni, cent, cenți, \2)
CNY:(.+),(.+) $(\1mm: yuan renminbi, yuani renminbi, fen, fen, \2)
EUR:(.+),(.+) $(\1mm: euro, euro, cent, cenți, \2)
GBP:(.+),(.+) $(\1fm: liră sterlină, lire sterline, penny, pence, \2)
JPY:(.+),(.+) $(\1mm: yen, yeni, sen, sen, \2)
RON:(.+),(.+) $(\1mm: leu românesc, lei românești, ban, bani, \2)
USD:(.+),(.+) $(\1mm: dolar american, dolari americani, cent, cenți, \2)

"([A-Z]{3}) ([-−]?1)([.,]00?)?" $(\1:us,|$2)
"([A-Z]{3}) ([-−]?\d+)([.,]00?)?" $(\1:up,|$2)

"(CNY [-−]?\d+)[.,]10?" $1| un jiao
"(CNY [-−]?\d+)[.,](\d)0?" $1| $2| jiao
"(CNY [-−]?\d+[.,]\d)1" $1| $2| fen
"(CNY [-−]?\d+[.,]\d)(\d)" $1| $2| fen

"(([A-Z]{3}) [-−]?\d+)[.,](01)" $1| $(\2:ss,$(1))
"(([A-Z]{3}) [-−]?\d+)[.,](\d)" $1| $(\2:sp,$(\30))
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1| $(\2:sp,$3)

"""
from __future__ import unicode_literals
