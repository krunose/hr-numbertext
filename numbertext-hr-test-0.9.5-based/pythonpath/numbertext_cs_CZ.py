# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 nula
^1$ jedno
1 jeden
^2$ dvě
2 dva
3 tři
4 čtyři
5 pět
6 šest
7 sedm
8 osm
9 devět
10 deset
11 jedenáct
14 čtrnáct
15 patnáct
19 devatenáct
1(\d) $1náct
([234])(\d) $1cet $2
5(\d) padesát $1
6(\d) šedesát $1
9(\d) devadesát $1
(\d)(\d) $1desát $2
1(\d\d) sto $1
2(\d\d) dvě stě $1
([34])(\d\d) $1 sta $2
(\d)(\d\d) $1 set $2
1(\d\d\d) tisíc $1
([234])(\d\d\d) $1 tisíce $2
(\d{1,3})(\d\d\d) $1 tisíce $2
1(\d{6}) milion $1
([234])(\d{6}) $1 miliony $2
(\d{1,3})(\d{6}) $1 milionů $2
1(\d{9}) miliarda $1
([234])(\d{9}) $1 miliardy $2
(\d{1,3})(\d{9}) $1 miliard $2
1(\d{12}) bilion $1
([234])(\d{12}) $1 biliony $2
(\d{1,3})(\d{12}) $1 bilionů $2
1(\d{15}) biliarda $1
([234])(\d{15}) $1 biliardy $2
(\d{1,3})(\d{15}) $1 biliard $2
1(\d{18}) trilion $1
([234])(\d{18}) $1 triliony $2
(\d{1,3})(\d{18}) $1 trilionů $2
1(\d{21}) triliarda $1
([234])(\d{21}) $1 triliardy $2
(\d{1,3})(\d{21}) $1 triliard $2
1(\d{24}) kvadrilion $1
([234])(\d{24}) $1 kvadriliony $2
(\d{1,3})(\d{24}) $1 kvadrilionů $2

# negative number

[-−](\d+) minus |$1

# decimals

([-−]?\d+)[.,] $1| čárka
([-−]?\d+[.,])([^0]\d) $1| |$2
([-−]?\d+[.,])(\d)(\d)(\d) $1| |$2 |$3 |$4
([-−]?\d+[.,]\d*)(\d) $1| |$2

# currency

# unit/subunit singular/plural

us:([^,]*),([^,]*),([^,]*),([^,]*) \1
up:([^,]*),([^,]*),([^,]*),([^,]*) \2
ss:([^,]*),([^,]*),([^,]*),([^,]*) \3
sp:([^,]*),([^,]*),([^,]*),([^,]*) \4

CHF:(\D+) $(\1: švýcarský frank, švýcarských franků, centim, centimů)
CNY:(\D+) $(\1: juan renminbi, juan renminbi, fen, fen)
CZK:(\D+) $(\1: koruna česká, korun českých, haléř, haléřů)
EUR:(\D+) $(\1: euro, euro, cent, centů)
GBP:(\D+) $(\1: libra šterlinků, libra šterlinků, penny, pence)
JPY:(\D+) $(\1: jen, jenů, sen, sen)
USD:(\D+) $(\1: americký dolar, amerických dolarů, cent, centů)

"([A-Z]{3}) ([-−]?1)([.,]00?)?" $2 $(\1:us)
"([A-Z]{3}) ([-−]?\d+)([.,]00?)?" $2 $(\1:up)

"(CNY [-−]?\d+)[.,]10?" $1 $2 jiao
"(CNY [-−]?\d+)[.,](\d)0?" $1 $2 jiao
"(CNY [-−]?\d+[.,]\d)1" $1 $2 fen
"(CNY [-−]?\d+[.,]\d)(\d)" $1 $2 fen

"(([A-Z]{3}) [-−]?\d+)[.,](01)" $1 $(1) $(\2:ss)
"(([A-Z]{3}) [-−]?\d+)[.,](\d)" $1 $(\30) $(\2:sp)
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1 $3 $(\2:sp)
"""
from __future__ import unicode_literals
