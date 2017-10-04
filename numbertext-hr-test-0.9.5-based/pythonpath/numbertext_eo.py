# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 nulo
1 unu
2 du
3 tri
4 kvar
5 kvin
6 ses
7 sep
8 ok
9 naŭ
1(\d) dek $1
(\d)(\d) $1dek $2
1(\d\d) cent $1
(\d)(\d\d) $1cent $2
1(\d{3}) mil $1
(\d{1,3})(\d{3}) $1 mil $2
1(\d{6}) unu miliono $1
(\d{1,3})(\d{6}) $1 milionoj $2
1(\d{9}) unu miliardo $1
(\d{1,3})(\d{9}) $1 miliardoj $2
1(\d{12}) unu duiliono $1
(\d{1,3})(\d{12}) $1 duilionoj $2
1(\d{15}) unu duiliardo $1
(\d{1,3})(\d{15}) $1 duiliardoj $2
1(\d{18}) unu triiliono $1
(\d{1,3})(\d{18}) $1 triilionoj $2
1(\d{21}) unu triiliardo $1
(\d{1,3})(\d{21}) $1 triiliardoj $2

# negative number

[-−](\d+) negativa |$1

# decimals

"([-−]?\d+)[.,]" "$1| komo"
"([-−]?\d+[.,]\d*)(\d)" $1| |$2

# currency

# unit/subunit singular/plural

us:([^,]*),([^,]*),([^,]*),([^,]*) \1
up:([^,]*),([^,]*),([^,]*),([^,]*) \2
ss:([^,]*),([^,]*),([^,]*),([^,]*) \3
sp:([^,]*),([^,]*),([^,]*),([^,]*) \4

CHF:(\D+) $(\1: svisa franko, svisaj frankoj, centimo, centimoj)
CNY:(\D+) $(\1: ĉina juano, ĉinaj juanoj, fen-o, fen-oj)
EUR:(\D+) $(\1: eŭro, eŭroj, cendo, cendoj)
GBP:(\D+) $(\1: sterlinga pundo, sterlingaj pundoj, penco, pencoj)
JPY:(\D+) $(\1: japana eno, japanaj enoj, seno, senoj)
USD:(\D+) $(\1: usona dolaro, usonaj dolaroj, cendo, cendoj)

"([A-Z]{3}) ([-−]?1)" $2 $(\1:us)
"([A-Z]{3}) ([-−]?\d+)" $2 $(\1:up)

"(([A-Z]{3}) [-−]?\d+)[.,](01)" $1 |$(1) $(\2:ss)
"(([A-Z]{3}) [-−]?\d+)[.,](\d)" $1 |$(\30) $(\2:sp)
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1 |$3 $(\2:sp)

"""
from __future__ import unicode_literals
