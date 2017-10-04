# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 zéro
1 un
2 deux
3 trois
4 quatre
5 cinq
6 six
7 sept
8 huit
9 neuf
10 dix
11 onze
12 douze
13 treize
14 quatorze
15 quinze
16 seize
20 vingt
30 trente
40 quarante
50 cinquante
60 soixante
70 septante
80 huitante
90 nonante
(\d)1 $(\10) et un
(\d)(\d) $(\10)-$2
1(\d\d) cent $1
(\d)00$ $1 cents
(\d)(\d\d) $1 cent $2
1100 onze cents
11(\d\d) onze cent $1
1(\d{3}) mille $1
(\d{1,3})(\d{3}) $1 mille $2
1(\d{6}) un million $1
(\d{1,3})(\d{6}) $1| millions $2
1(\d{9}) un milliard $1
(\d{1,3})(\d{9}) $1| milliards $2
1(\d{12}) un billion $1
(\d{1,3})(\d{12}) $1| billions $2
1(\d{15}) un billiard $1
(\d{1,3})(\d{15}) $1| billiards $2
1(\d{18}) un trillion $1
(\d{1,3})(\d{18}) $1| trillions $2
1(\d{21}) un trilliard $1
(\d{1,3})(\d{21}) $1| trilliards $2
1(\d{24}) un quadrillion $1
(\d{1,3})(\d{24}) $1| quadrillions $2

# negative number

[-−](\d+) moins |$1

# decimals

"([-−]?\d+)[.,]" "$1| point"
"([-−]?\d+[.,]0*)(\d+)" $1 |$2

# currency

# unit/subunit singular/plural

us:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \1
up:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \2
ud:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \3
ss:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \4
sp:([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*) \5

# masculine/feminine

mf:.*un(e?) \1

BIF:(\D+) $(\1: franc burundais, francs burundais, de francs burundais, centime, centimes, un)
CAD:(\D+) $(\1: dollar canadien, dollars canadiens, de dollars canadiens, cent, cents, un)
CDF:(\D+) $(\1: franc congolais, francs congolais, de francs congolais, centime, centimes, un)
CHF:(\D+) $(\1: franc suisse, francs suisses, de francs suisses, centime, centimes, un)
DJF:(\D+) $(\1: franc de Djibouti, francs de Djibouti, de francs de Djibouti, centime, centimes, un)
DZD:(\D+) $(\1: dinar algérien, dinars algériens, de dinars algériens, centime, centimes, un)
EUR:(\D+) $(\1: euro, euros, d’euros, centime, centimes, un)
GBP:(\D+) $(\1: livre sterling, livres sterling, de livres sterling, penny, pennies, une)
GNF:(\D+) $(\1: franc guinéen, francs guinéens, de francs guinéens,,, un)
HTF:(\D+) $(\1: gourde, gourde, de gourde, centime, centimes, une)
KMF:(\D+) $(\1: franc des Comores, francs des Comores, de francs des Comores, centime, centimes, un)
LBP:(\D+) $(\1: livre libanaise, livres libanaises, de livres libanaises,,, une)
MAD:(\D+) $(\1: dirham marocain, dirhams marocains, de dirhams marocains, centime, centimes, un)
MGA:(\D+) $(\1: ariary, ariarys, d’ariarys, iraimbilanja, iraimbilanja, un)
MRO:(\D+) $(\1: ouguiya, ouguiya, d’ouguiya, khoum, khoums, un)
MUR:(\D+) $(\1: roupie mauricienne, roupies mauriciennes, de roupies mauriciennes, cent, cents, une)
RWF:(\D+) $(\1: franc rwandais, francs rwandais, de francs rwandais, centime, centimes, un)
SCR:(\D+) $(\1: roupie seychelloise, roupies seychelloises, de roupies seychelloise, cent, cents, une)
TND:(\D+) $(\1: dinar tunisien, dinars tunisiens, de dinars tunisiens, millime, millimes, un)
USD:(\D+) $(\1: dollar américain, dollars américains, de dollars américains, cent, cents, un)
VUV:(\D+) $(\1: vatu, vatus, de vatus,,, un)
X[AO]F:(\D+) $(\1: franc CFA, francs CFA, de francs CFA, centime, centimes, un)
XPF:(\D+) $(\1: franc Pacifique, francs Pacifique, de francs Pacifique, centime, centimes, un)

"(GNF|LBP|VUV) ([-−]?[01](.0+)?)" $2 $(\1:us)
"(GNF|LBP|VUV) ([-−]?\d+0{6,})" $2 $(\1:ud)
"(GNF|LBP|VUV) ([-−]?\d+[.,]\d+)" $2 $(\1:up)

"([A-Z]{3}) ([-−]?1)([.,]00?)?" $2$(\1:mf) $(\1:us)              # un/une
"([A-Z]{3}) ([-−]?\d*[02-9]1)([.,]00?)?" $2$(\1:mf) $(\1:up)     # cent un/une mais pas cent onze
"([A-Z]{3}) ([-−]?[0])([.,]00?)?" $2 $(\1:us)
"([A-Z]{3}) ([-−]?\d+0{6,})([.,]00?)?" $2 $(\1:ud)
"([A-Z]{3}) ([-−]?\d+)([.,]00?)?" $2 $(\1:up)

"((MGA|MRO) [-−]?\d+)[.,]0" $1
"((MGA|MRO) [-−]?\d+)[.,]2" $1 et |$(1) $(\2:ss)
"((MGA|MRO) [-−]?\d+)[.,]4" $1 et |$(2) $(\2:sp)
"((MGA|MRO) [-−]?\d+)[.,]6" $1 et |$(3) $(\2:sp)
"((MGA|MRO) [-−]?\d+)[.,]8" $1 et |$(4) $(\2:sp)

"((TND) [-−]?\d+)[.,](001)" $1 et |$(1) $(\2:ss)
"((TND) [-−]?\d+)[.,](\d)" $1 et |$(\300) $(\2:sp)
"((TND) [-−]?\d+)[.,](\d\d)" $1 et |$(\30) $(\2:sp)
"((TND) [-−]?\d+)[.,](\d\d\d)" $1 et |$3 $(\2:sp)

"(([A-Z]{3}) [-−]?\d+)[.,](01)" $1 et |$(1) $(\2:ss)
"(([A-Z]{3}) [-−]?\d+)[.,](\d)" $1 et |$(\30) $(\2:sp)
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1 et |$3 $(\2:sp)


# ordinal numbers

"ordf 1" première
"ordm? 1" premier

"ord[fm]? ([-−]?\d+)" $(ord:|$1)

ord:(.*)e \1ième	# quatre etc.
ord:(.*)f \1vième	# neuf
ord:(.*q) \1uième	# cinq
"ord:(.*[^ ]) *" \1ième		# others

help Functions: ord (ordinal numbers)\nordf (feminine ordinal numbers)\nordm (masculine ordinal numbers)
"""
from __future__ import unicode_literals
