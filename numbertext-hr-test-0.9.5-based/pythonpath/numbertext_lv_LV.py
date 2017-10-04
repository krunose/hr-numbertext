# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 nulle
1 viens
2 divi
3 trīs
4 četri
5 pieci
6 seši
7 sepiņi
8 astoņi
9 deviņi
10 desmit
11 vienpadsmit
12 divpadsmit
13 trīspadsmit
14 četrpadsmit
15 piecpadsmit
16 sešpadsmit
17 septiņpadsmit
18 astoņpadsmit
19 deniņpadsmit
([2])(\d) divdesmit $2
([23456789])(\d) $1|desmit $2
1(\d\d) simts $1
(\d)(\d\d) $1 simti $2
1(\d{3}) viens tūkstotis $1
(\d{1,3})(\d{3}) $1 tūkstoši $2
1(\d{6}) viens miljons $1
(\d{1,3})(\d{6}) $1 miljoni $2
1(\d{9}) viens miljards $1
(\d{1,3})(\d{9}) $1 miljardi $2
1(\d{12}) viens triljons $1
(\d{1,3})(\d{12}) $1 triljoni $2
1(\d{15}) viens kvadriljons $1
(\d{1,3})(\d{15}) $1 kvadriljoni $2
1(\d{18}) viens kvintiljons $1
(\d{1,3})(\d{18}) $1 kvintiljoni $2
1(\d{21}) viens sekstiljons $1
(\d{1,3})(\d{21}) $1 sekstiljoni $2
1(\d{24}) viens septiljons $1
(\d{1,3})(\d{24}) $1 septiljoni $2

# negative numbers

[-−](\d+) mīnus |$1

# decimals


([-−]?\d+)[.,] $1| komats
([-−]?\d+[.,]\d*)(\d) $1| |$2


# female conversion
f:(.*)viens viena
f:(.*)i \1as
f:(.*) \1

# currency

# unit/subunit

us:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \1
up:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \2
ug:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \3
ss:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \4
sp:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \5
sg:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \6

LVL:(\D+) $(\1: lats, lati,latu, santīms, santīmi, santīmu)
EUR:(\D+) $(\1: eiro, eiro, eiro, cents, centi, centu)
RUB:(\D+) $(\1: rublis, rubļi, rubļu, kapeika, kapeikas, kapeiku)
USD:(\D+) $(\1: ASV dolārs, ASV dolāri, ASV dolāru, cents, centi, centu)


"([A-Z]{3}) ([-−]?1)([.,]00?)?" $2| $(\1:us)
"([A-Z]{3}) ([-−]?\d*[02-9]1)([.,]00?)?" $2| $(\1:us)
"([A-Z]{3}) ([-−]?[23456789])([.,]00?)?" $2| $(\1:up)
"([A-Z]{3}) ([-−]?\d*[02-9][23456789])([.,]00?)?" $2| $(\1:up)
"([A-Z]{3}) ([-−]?\d+)([.,]00?)?" $2| $(\1:ug)

"((RUB) [-−]?\d+)[.,]([02-9])1" $1 $(\30) |$(f:$(1)) $(\2:ss)
"((RUB) [-−]?\d+)[.,]([02-9][23456789])" $1 $(f:$3)  $(\2:sp)

"(([A-Z]{3}) [-−]?\d+)[.,](01)" $1 |$(1) $(\2:ss)
"(([A-Z]{3}) [-−]?\d+)[.,]([02-9])1" $1 $(\30) |$(1)  $(\2:ss)

"(([A-Z]{3}) [-−]?\d+)[.,]([02-9][23456789])" $1 |$3 $(\2:sp)

"(([A-Z]{3}) [-−]?\d+)[.,](\d)" $1 |$(\30) $(\2:sg)
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1 |$3 $(\2:sg)

"""
from __future__ import unicode_literals