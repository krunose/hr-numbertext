# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0$ nul
1 een
2 twee
3 drie
4 vier
5 vyf
6 ses
7 sewe
8 agt
9 nege

10 tien
11 elf
12 twaalf
13 dertien
14 veertien
17 sewentien
19 negentien
1(\d) $1|tien

20 twintig
30 dertig
40 veertig
70 sewentig
80 tagtig
90 negentig
(\d)0 $1tig
(\d)(\d) $2-en-$(\10)

# function a
a:0* " "	# eenhonderd
a:0*1?\d -en-	# eenhonderd-en-een
a:0*\d0 -en-	# eenhonderd-en-twintig
a:\d+ " "	# eenhonderd een-en-twintig

# function b
b:0*1?\d	# negentienduisend
b:0*\d0		# twintigduisend
b:\d+ " "	# een-en-twintig duisend

^1(\d\d) honderd$(a:\1)$1
(\d)(\d\d) $1honderd$(a:\2)$2

^1(\d{3}) duisend$(a:\1)$1
(\d{1,3})(\d{3}) $1$(b:\1)duisend$(a:\2)$2

(\d{1,3})(\d{6}) $1$(b:\1)miljoen$(a:\2)$2
(\d{1,3})(\d{9}) $1$(b:\1)miljard$(a:\2)$2
(\d{1,3})(\d{12}) $1$(b:\1)biljoen$(a:\2)$2
(\d{1,3})(\d{15}) $1$(b:\1)biljard$(a:\2)$2
(\d{1,3})(\d{18}) $1$(b:\1)triljoen$(a:\2)$2
(\d{1,3})(\d{21}) $1$(b:\1)triljard$(a:\2)$2

# negative number

[-−](\d+) min |$1

# decimals

([-−]?\d+)[.,] $1| komma
([-−]?\d+[.,]\d*)(\d) $1| |$2

# currencies

# unit/subunit

u:([^,]*),([^,]*),([^,]*)	\1
s:([^,]*),([^,]*),([^,]*)	\2
p:([^,]*),([^,]*),([^,]*)	\3

CHF:(.)	$(\1: Zwitserse franc, centime, centimes)
CNY:(.)	$(\1: renminbi yuan, fen, fen)
EUR:(.)	$(\1: euro, cent, cent)
GBP:(.)	$(\1: pond sterling, penny, pence)
JPY:(.)	$(\1: yen, sen, sen)
USD:(.)	$(\1: Amerikaanse dollar, sent, sent)
ZAR:(.)	$(\1: rand, sent, sent)

"(JPY [-−]?\d+)[.,](\d\d)0" $1
"(JPY [-−]?\d+[.,]\d\d)(\d)" $1 $2 rin

"([A-Z]{3}) ([-−]?0)([.,]00?)?" nul $(\1:u)
"([A-Z]{3}) ([-−]?\d+)([.,]00?)?" $2 $(\1:u)

"(CNY [-−]?\d+)[.,](\d)0?" $1 $2 jiao
"(CNY [-−]?\d+[.,]\d)(\d)" $1 $2 fen

"(([A-Z]{3}) [-−]?\d+)[.,](01)" $1 een $(\2:s)
"(([A-Z]{3}) [-−]?\d+)[.,](\d)" $1 $(\30) $(\2:p)
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1 $3 $(\2:p)

"""
from __future__ import unicode_literals
