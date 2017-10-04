# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 nič
1 ena
2$ dve
2 dva
3 tri
4 štiri
5 pet
6 šest
7 sedem
8 osem
9 devet
10 deset
11 enajst
1(\d) $1najst
20 dvajset
2(\d) $1indvajset
(\d)0 $1deset
(\d)(\d) $2in$1deset
1(\d\d) sto $1
2(\d\d) dvesto $1
(\d)(\d\d) $1sto $2
1(\d\d\d) tisoč $1
(\d{1,3})(\d\d\d) $1 tisoč $2
1(\d{6}) milijon $1
([234])(\d{6}) $1 milijona $2
(\d{1,3})(\d{6}) $1 milijonov $2
1(\d{9}) milijarda $1
([234])(\d{9}) $1| milijardi $2
(\d{1,3})(\d{9}) $1 milijardov $2
1(\d{12}) bilijon $1
([234])(\d{12}) $1 bilijona $2
(\d{1,3})(\d{12}) $1 bilijonov $2
1(\d{15}) tisoč bilijonov $1
(\d{1,3})(\d{15}) $1 tisoč bilijonov $2
1(\d{18}) trilijon $1
([234])(\d{18}) $1 trilijona $2
(\d{1,3})(\d{18}) $1 trilijonov $2
1(\d{21}) tisoč trilijonov $1
(\d{1,3})(\d{21}) $1 tisoč trilijonov $2
1(\d{24}) kvadrilijon $1
([234])(\d{24}) $1 kvadrilijona $2
(\d{1,3})(\d{24}) $1 kvadrilijonov $2

# negative number

[-−] minus
[-−](\d+) minus |$1

# decimals

"([-−]?\d+)[.,]" $1| vejica
"([-−]?\d+[.,])([^0]\d)" $1| |$2
"([-−]?\d+[.,])(\d)(\d)(\d)" $1| |$2 |$3 |$4
"([-−]?\d+[.,]\d*)(\d)" $1| |$2

# currency

# unit/subunit affixation

u1:([^,]*)(,[^,]*){9} \1
u2:([^,]*,){1}([^,]*)(,[^,]*){8} \2
u3:([^,]*,){2}([^,]*)(,[^,]*){7} \2
u4:([^,]*,){3}([^,]*)(,[^,]*){6} \2
u5:([^,]*,){4}([^,]*)(,[^,]*){5} \2
s1:([^,]*,){5}([^,]*)(,[^,]*){4} \2
s2:([^,]*,){6}([^,]*)(,[^,]*){3} \2
s3:([^,]*,){7}([^,]*)(,[^,]*){2} \2
s4:([^,]*,){8}([^,]*)(,[^,]*){1} \2
s5:([^,]*,){9}([^,]*) \2

CHF:(.+) $(\1: švicarski frank, švicarska franka, švicarski franki, švicarske franke, švicarskih frankov, centim, centima, centimi, centime, centimov)
EUR:(.+) $(\1: evro, evra, evri, evre, evrov, cent, centa, centi, cente, centov)
GBP:(.+) $(\1: funt šterling, funta šterlinga, funti šterlingi, funte šterlinge, funtov šterlingov, peni, penija, peniji, penije, penijev)
JPY:(.+) $(\1: japonski jen, japonska jena, japonski jeni, japonske jene, japonskih jenov, sen, sena, seni, sene, senov)
USD:(.+) $(\1: ameriški dolar, ameriška dolarja, ameriški dolarji, ameriške dolarje, ameriških dolarjev, cent, centa, centi, cente, centov)

"([A-Z]{3}) ([-−]?)1([.,]00?)?" $2 en $(\1:u1)
"([A-Z]{3}) ([-−]?\d*01)([.,]00?)?" $2 $(\1:u1)
"([A-Z]{3}) ([-−]?(2|\d*02))([.,]00?)?" $2 $(\1:u2)
"([A-Z]{3}) ([-−]?(3|\d*03))([.,]00?)?" $2 $(\1:u3)
"([A-Z]{3}) ([-−]?(4|\d*04))([.,]00?)?" $2 $(\1:u4)
"([A-Z]{3}) ([-−]?\d+)([.,]00?)?" $2 $(\1:u5)

"(([A-Z]{3}) [-−]?\d+)[.,](01)" $1 en $(\2:s1)
"(([A-Z]{3}) [-−]?\d+)[.,](02)" $1 $3 $(\2:s2)
"(([A-Z]{3}) [-−]?\d+)[.,](03)" $1 $3 $(\2:s3)
"(([A-Z]{3}) [-−]?\d+)[.,](04)" $1 $3 $(\2:s4)
"(([A-Z]{3}) [-−]?\d+)[.,](\d)" $1 $(\30) $(\2:s5)
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1 $3 $(\2:s5)

"""
from __future__ import unicode_literals
