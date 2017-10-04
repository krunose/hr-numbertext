# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 zero
1 um
2 dois
3 três
4 quatro
5 cinco
6 seis
7 sete
8 oito
9 nove
10 dez
11 onze
12 doze
13 treze
14 quatorze
15 quinze
16 dezasseis
17 dezassete
18 dezoito
19 dezanove
20 vinte
30 trinta
40 quarenta
50 cinquenta
60 sessenta
70 setenta
80 oitenta
90 noventa
(\d)(\d) $(\10) e $2
100 cem
1(\d\d) cento e $1
200 duzentos
300 trezentos
500 quinhentos
(\d)(00) $1centos
(\d)(\d\d) $(\100) e $2

:0+
:0*\d{1,2}(\d{6}){0,} e		# mil e um, mil e dez
:0*\d00(\d{6}){0,} e		# mil e quinhentos
:0*\d{1,2}000(\d{6}){0,} e	# um milhão e onze mil
:0*\d{1}00000(\d{6}){0,} e	# um milhão e cem mil

1(\d\d\d) mil $(:\1) $1
(\d{1,3})(\d\d\d) $1 mil $(:\2) $2
1(\d{6}) um milhão $(:\1) $1
(\d{1,6})(\d{6}) $1 milhões $(:\2) $2
1(\d{12}) um bilião $(:\1) $1
(\d{1,6})(\d{12}) $1 biliões $(:\2) $2
1(\d{18}) um trilião $(:\1) $1
(\d{1,6})(\d{18}) $1 triliões $(:\2) $2
1(\d{24}) um quatrilião $(:\1) $1
(\d{1,6})(\d{24}) $1 quatriliões $(:\2) $2

# negative number

[-−](\d\d*) menos |$1

# decimals

([-−]?\d+)[.] $1| ponto
([-−]?\d+)[,] $1| vírgula
([-−]?\d+[.,])([^0]\d) $1| |$2
"([-−]?\d+[.,])(\d)(\d)(\d)" |$1 |$2| |$3| |$4
([-−]?\d+[.,]\d*)(\d) $1| |$2

# currency (monedas)

# unit/subunit singular/plural

us:([^,]*),([^,]*),([^,]*),([^,]*) \1
up:([^,]*),([^,]*),([^,]*),([^,]*) \2
ss:([^,]*),([^,]*),([^,]*),([^,]*) \3
sp:([^,]*),([^,]*),([^,]*),([^,]*) \4

AOA:(\D+) $(\1: kwanza, kwanzas, cêntimo, cêntimos)
ARG:(\D+) $(\1: peso argentino, pesos argentinos, centavo, centavos)
BOB:(\D+) $(\1: boliviano, bolivianos, centavo, centavos)
BRL:(\D+) $(\1: real, réis, centavo, centavos)
CHF:(\D+) $(\1: franco suíço, francos suíços, cêntimo, cêntimos)
CNY:(\D+) $(\1: yuan renminbi, yuan renminbi, fen, fen)
CVE:(\D+) $(\1: escudos cabo-verdianos, escudos cabo-verdianos, centavo, centavos)
EUR:(\D+) $(\1: euro, euros, cent, cents)
GBP:(\D+) $(\1: libra esterlina, libras esterlinas, penny, pence)
JPY:(\D+) $(\1: iene, ienes, sen, sen)
MOP:(\D+) $(\1: pataca, patacas, avo, avos)
MXN:(\D+) $(\1: peso mexicano, pesos mexicanos, centavo, centavos)
MZM:(\D+) $(\1: metical, meticais, centavo, centavos)
STD:(\D+) $(\1: dobra, dobras, cêntimo, cêntimos)
USD:(\D+) $(\1: dólar americano, dólares americanos, cêntimo, cêntimos)
XOF:(\D+) $(\1: franco CFA, francos CFA, cêntimo, cêntimos)

# masculine to feminine conversion of "un" after millions,
# if "as?$" matches currency name

f:(.*il[hi])(.*),(.*) \1$(f:\2,\3)	# don't modify millions
f:(.*um)([^a].*,|,)(.*as?) $(f:\1a\2\3)	# um libra -> uma libra
f:(.*d)oi(s.*),(.*as?) $(f:\1ua\2,\3)	# dois libra -> duas libra
f:(.*ent)o(s.*),(.*as?) $(f:\1a\2,\3)	# duzentos libra -> duzentas libra
f:(.*),(.*) \1 \2

"([A-Z]{3}) ([-−]?1)([.,]00?)?" $(f:|$2,$(\1:us))
"([A-Z]{3}) ([-−]?\d+0{6,})([.,]00?)?" $2 de $(\1:up)
"([A-Z]{3}) ([-−]?\d+)([.,]00?)?" $(f:|$2,$(\1:up))

"(CNY [-−]?\d+)[.,]10?" $1 $2 jiao
"(CNY [-−]?\d+)[.,](\d)0?" $1 $2 jiao
"(CNY [-−]?\d+[.,]\d)1" $1 $2 fen
"(CNY [-−]?\d+[.,]\d)(\d)" $1 $2 fen

"(([A-Z]{3}) [-−]?\d+)[.,](01)" $1 e |$(1) $(\2:ss)
"(([A-Z]{3}) [-−]?\d+)[.,](\d)" $1 e |$(\30) $(\2:sp)
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1 e |$3 $(\2:sp)

"""
from __future__ import unicode_literals
