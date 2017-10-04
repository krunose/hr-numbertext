# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 nulla
1 egy
2$ kettő
2 két
3 három
4 négy
5 öt
6 hat
7 hét
8 nyolc
9 kilenc
10 tíz
1(\d) tizen$1
20 húsz
2(\d) huszon$1
3(\d) harminc$1
4(\d) negyven$1
5(\d) ötven$1
6(\d) hatvan$1
7(\d) hetven$1
8(\d) nyolcvan$1
9(\d) kilencven$1
1(\d\d) száz$1
(\d)(\d\d) $1száz$2
1(\d{3}) ezer$1

# separator function
:0*	# kétezer
:\d* -	# kétezer-egy

(\d{1,3})(\d{3}) $1ezer$(:\2)$2
(\d{1,3})(\d{6}) $1millió$(:\2)$2
(\d{1,3})(\d{9}) $1milliárd$(:\2)$2
(\d{1,3})(\d{12}) $1billió$(:\2)$2
(\d{1,3})(\d{15}) $1billiárd$(:\2)$2
(\d{1,3})(\d{18}) $1trillió$(:\2)$2
(\d{1,3})(\d{21}) $1trilliárd$(:\2)$2

# negative numbers

[-−](\d+) mínusz |$1

# decimals

"([-−]?\d+)[.,](\d)" |$1| egész |$2 tized
"([-−]?\d+)[.,](\d\d)" |$1| egész |$2 század
"([-−]?\d+)[.,](\d{3})" |$1| egész |$2 ezred
"([-−]?\d+)[.,](\d)(\d)(\d)(\d)" |$1| egész |$2| |$3| |$4| |$5|
"([-−]?\d+[.,]\d+)(\d)" $1 |$2|

# currency

# unit/subunit

u:([^,]*),([^,]*)	\1
s:([^,]*),([^,]*)	\2

AUD:(.)	$(\1: ausztrál dollár, cent)
BGN:(.)	$(\1: bolgár leva, sztotinka)
BRL:(.)	$(\1: brazil real, centavo)
CAD:(.)	$(\1: kanadai dollár, cent)
CHF:(.)	$(\1: svájci frank, rappen)
CNY:(.)	$(\1: kínai jüan, fen)
CZK:(.)	$(\1: cseh korona, haléř)
DKK:(.)	$(\1: dán korona, øre)
EEK:(.)	$(\1: észt korona, sent)
EUR:(.)	$(\1: euró, cent)
GBP:(.)	$(\1: font sterling, penny)
HKD:(.)	$(\1: hongkongi dollár, cent)
HRK:(.)	$(\1: horvát kuna, lipa)
HUF:(.)	$(\1: forint, fillér)
ISK:(.)	$(\1: izlandi korona, eyrir)
JPY:(.)	$(\1: japán jen, szen)
KRW:(.)	$(\1: dél-koreai von, cson)
LTL:(.)	$(\1: litván litas, centas)
LVL:(.)	$(\1: lett lat, santīm)
MXN:(.)	$(\1: mexikói peso, centavo)
NOK:(.)	$(\1: norvég korona, øre)
NZD:(.)	$(\1: új-zélandi dollár, cent)
PLN:(.)	$(\1: lengyel złoty, grosz)
RON:(.)	$(\1: román lej, bani)
RSD:(.)	$(\1: szerb dinár, para)
RUB:(.)	$(\1: orosz rubel, kopejka)
SEK:(.)	$(\1: svéd korona, öre)
SGD:(.)	$(\1: szingapúri dollár, cent)
TRY:(.)	$(\1: török líra, kuruş)
UAH:(.)	$(\1: ukrán hrivnya, kopijka)
USD:(.)	$(\1: USA-dollár, cent)
ZAR:(.)	$(\1: dél-afrikai rand, cent)

"(JPY [-−]?\d+)[.,](\d\d)0" $1
"(JPY [-−]?\d+[.,]\d\d)(\d)" $1 $2 rin

"([A-Z]{3}) ([-−]?\d+)([.,]00?)?" $2 $(\1:u)

"(CNY [-−]?\d+)[.,](\d)0?" $1 $2 jiao
"(CNY [-−]?\d+[.,]\d)(\d)" $1 $2 fen

"(([A-Z]{3}) [-−]?\d+)[.,](\d)" $1 $(\30) $(\2:s)
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1 $3 $(\2:s)

# ordinal numbers

"ord 1" első
"ord 2" második
"ord ([-−]?\d+)" $(ord:|$1)

ord:(.*)nulla	\1nulladik
ord:(.*)egy	\1egyedik
ord:(.*)kettő	\1kettedik
ord:(.*)három	\1harmadik
ord:(.*)négy	\1negyedik
ord:(.*)öt	\1ötödik
ord:(.*)hat	\1hatodik
ord:(.*)hét	\1hetedik
ord:(.*)nyolc	\1nyolcadik
ord:(.*)kilenc	\1kilencedik
ord:(.*)tíz	\1tizedik
ord:(.*)húsz	\1huszadik
ord:(.*)harminc	\1harmincadik
ord:(.*)(negy|öt|het|kilenc)ven	\1\2venedik
ord:(.*)(hat|nyolc)van	\1\2vanadik
ord:(.*)száz	\1századik
ord:(.*)ezer	\1ezredik
ord:(.*)illió	\1illiomodik
ord:(.*)illiárd	\1illiárdodik

help Functions: ord \(ordinal numbers\)\nExtra language modules: hu_HU_2 \(formal numerals\)
"""
from __future__ import unicode_literals
