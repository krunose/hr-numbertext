# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 null
1$ eins
1 ein
2 zwei
3 drei
4 vier
5 fünf
6 sechs
7 sieben
8 acht
9 neun
10 zehn
11 elf
12 zwölf
16 sechzehn
17 siebzehn
1(\d) $1zehn
20 zwanzig
2(\d) $1undzwanzig
30 dreißig
3(\d) $1unddreißig
60 sechzig
6(\d) $1undsechzig
70 siebzig
7(\d) $1undsiebzig
(\d)0 $1zig
(\d)(\d) $2und$1zig
#1(\d\d) hundert$1
(\d)(\d\d) $1hundert$2
#1(\d{3}) tausend$1
(\d{1,3})(\d{3}) $1tausend$2
1(\d{6}) eine Million $1
(\d{1,3})(\d{6}) $1 Millionen $2
1(\d{9}) eine Milliarde $1
(\d{1,3})(\d{9}) $1 Milliarden $2
1(\d{12}) eine Billion $1
(\d{1,3})(\d{12}) $1 Billionen $2
1(\d{15}) eine Billiarde $1
(\d{1,3})(\d{15}) $1 Billiarden $2
1(\d{18}) eine Trillion $1
(\d{1,3})(\d{18}) $1 Trillionen $2
1(\d{21}) eine Trilliarde $1
(\d{1,3})(\d{21}) $1 Trilliarden $2

# negative number

[-−](\d+) minus |$1

# decimals

"([-−]?\d+)[.,]" $1| Komma
"([-−]?\d+[.,]\d*)(\d)" $1| |$2

# currency

# unit/subunit singular/plural

us:([^,]*),([^,]*),([^,]*),([^,]*) \1
up:([^,]*),([^,]*),([^,]*),([^,]*) \2
ss:([^,]*),([^,]*),([^,]*),([^,]*) \3
sp:([^,]*),([^,]*),([^,]*),([^,]*) \4

CHF:(\D+) $(\1: Schweizer Franken, Schweizer Franken, Rappen, Rappen)
CNY:(\D+) $(\1: Yuan, Yuan, Fen, Fen)
EUR:(\D+) $(\1: Euro, Euro, Cent, Cent)
GBP:(\D+) $(\1: Pfund Sterling, Pfund Sterling, Penny, Pence)
USD:(\D+) $(\1: US-Dollar, US-Dollar, Cent, Cents)

"JPY ([-−]?\d+([.,]\d+)?)" $1 Yen

"([A-Z]{3}) ([-−]?1)([.,]00?)?" $2 $(\1:us)
"([A-Z]{3}) ([-−]?\d+)([.,]00?)?" $2 $(\1:up)

"(CNY [-−]?\d+)[.,]10?" $1 $2 Jiao
"(CNY [-−]?\d+)[.,](\d)0?" $1 $2 Jiao
"(CNY [-−]?\d+[.,]\d)1" $1 $2 Fen
"(CNY [-−]?\d+[.,]\d)(\d)" $1 $2 Fen

"(([A-Z]{3}) [-−]?\d+)[.,](01)" $1 und $(1) $(\2:ss)
"(([A-Z]{3}) [-−]?\d+)[.,](\d)" $1 und $(\30) $(\2:sp)
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1 und $3 $(\2:sp)

# ordinal numbers

"ord ([-−]?[024569])" $1te
"ord ([-−]?\d*0[24569])" $1te
"ord ([-−]?\d*1\d)" $1te
"ord ([-−]?\d+)" $(ord:$1)

ord:(.*)eins	\1erste
ord:(.*)drei	\1dritte
ord:(.*)sieben	\1siebte
ord:(.*)acht	\1achte
"ord:(.*)eine Milli(on|ard)e?"	\1einmilli\2ste
"ord:(.*)eine Billi(on|ard)e?"	\1einbilli\2ste
"ord:(.*)eine Trilli(on|ard)e?"	\1eintrilli\2ste
"ord:(.*) Milli(on|ard)en"	\1milli\2ste
"ord:(.*) Billi(on|ard)en"	\1billi\2ste
"ord:(.*) Trilli(on|ard)en"	\1trilli\2ste
"(ord:.*) "	$1
ord:(.*)	\1ste

help Functions: ord \(ordinal numbers\)
"""
from __future__ import unicode_literals
