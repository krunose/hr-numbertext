# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 nolla
1 yksi
2 kaksi
3 kolme
4 neljä
5 viisi
6 kuusi
7 seitsemän
8 kahdeksan
9 yhdeksän
10 kymmenen
1(\d) $1toista
(\d)(\d) $1kymmentä$2
1(\d\d) sata$1
(\d)(\d\d) $1sataa$2
1(\d{3}) tuhat$1
(\d)(\d{3}) $1tuhatta$2
(\d{2,3})(\d{3}) $1tuhatta $2
1(\d{6}) miljoona $1
(\d{1,3})(\d{6}) $1 miljoonaa $2
1(\d{9}) miljardi $1
(\d{1,3})(\d{9}) $1 miljardia $2
1(\d{12}) biljoona $1
(\d{1,3})(\d{12}) $1 biljoonaa $2
1(\d{15}) tuhat biljoona $1
(\d{1,3})(\d{15}) $1 tuhat biljoonaa $2
1(\d{18}) triljoona $1
(\d{1,3})(\d{18}) $1 triljoonaa $2
1(\d{21}) tuhat triljoona $1
(\d{1,3})(\d{21}) $1 tuhat triljoonaa $2
1(\d{24}) kvadriljoona $1
(\d{1,3})(\d{24}) $1 kvadriljoonaa $2

# negative numbers

[-−](\d+) miinus |$1

# decimals

([-−]?\d+)[.,]([01])	|$1| ja |$2 kymmenesosa
([-−]?\d+)[.,](\d)	|$1| ja |$2 kymmenesosaa
([-−]?\d+)[.,]0([01])	|$1| ja |$2 sadasosa
([-−]?\d+)[.,](\d\d)	|$1| ja |$2 sadasosaa
([-−]?\d+)[.,]00([01])	|$1| ja |$2 tuhannesosa
([-−]?\d+)[.,](\d\d\d)	|$1| ja |$2 tuhannesosaa
"([-−]?\d+)[.,](\d)(\d)(\d)(\d)" |$1| ja |$2| |$3| |$4| |$5|
"([-−]?\d+[.,]\d+)(\d)" $1 |$2|

# currency

# unit/subunit singular/singular partitive

us:([^,]*),([^,]*),([^,]*),([^,]*) \1
up:([^,]*),([^,]*),([^,]*),([^,]*) \2
ss:([^,]*),([^,]*),([^,]*),([^,]*) \3
sp:([^,]*),([^,]*),([^,]*),([^,]*) \4

AUD:(\D+) $(\1: Australian dollari, Australian dollaria, sentti, senttiä)
CAD:(\D+) $(\1: Kanadan dollari, Kanadan dollaria, sentti, senttiä)
CHF:(\D+) $(\1: Sveitsin frangi, Sveitsin frangia, rappeni, rappenia)
CNY:(\D+) $(\1: juan renminbi, juan renminbia, feni, feniä)
CYP:(\D+) $(\1: Kyproksen punta, Kyproksen puntaa, sentti, senttiä)
CZK:(\D+) $(\1: Tšekin kruunu, Tšekin kruunua, haléři, haléřia)
DKK:(\D+) $(\1: Tanskan kruunu, Tanskan kruunua, äyri, äyriä)
EEK:(\D+) $(\1: Viron kruunu, Viron kruunua, sentti, senttiä)
EUR:(\D+) $(\1: euro, euroa, sentti, senttiä)
GBP:(\D+) $(\1: Englannin punta, Englannin puntaa, penni, pennia)
HKD:(\D+) $(\1: Hongkongin dollari, Hongkongin dollaria, sentti, senttiä)
HRK:(\D+) $(\1: Kroatian kuna, Kroatian kunaa, lipa, lipaa)
HUF:(\D+) $(\1: Unkarin forintti, Unkarin forinttia, filléri, fillériä)
IDR:(\D+) $(\1: Indonesian rupia, Indonesian rupiaa, seni, seniä)
ISK:(\D+) $(\1: Islannin kruunu, Islannin kruunua, äyri, äyriä)
JPY:(\D+) $(\1: Japanin jeni, Japanin jenia, seni, seniä)
KRW:(\D+) $(\1: Etelä-Korean won, Etelä-Korean won, chon, chonia)
LTL:(\D+) $(\1: Liettuan lita, Liettuan litiä, centasi, centasia)
LVL:(\D+) $(\1: Latvian lati, Latvian latia, santiimi, santiimia)
MYR:(\D+) $(\1: Malesian ringgit, Malesian ringgit, sentti, senttiä)
NZD:(\D+) $(\1: Uuden-Seelannin dollari, Uuden-Seelannin dollaria, sentti, senttiä)
NOK:(\D+) $(\1: Norjan kruunu, Norjan kruunua, äyri, äyriä)
PHP:(\D+) $(\1: Filippiinien peso, Filippiinien peso, centavo, centavoa)
PLN:(\D+) $(\1: Puolan złoty, Puolan złotya, groszy, groszya)
RON:(\D+) $(\1: Romanian leu, Romanian leu, bani, bania)
RUB:(\D+) $(\1: Venäjän rupla, Venäjän ruplaa, kopeekka, kopeekkaa)
SEK:(\D+) $(\1: Ruotsin kruunu, Norjan kruunua, äyri, äyriä)
SGD:(\D+) $(\1: Singaporen dollari, Singaporen dollaria, sentti, senttiä)
THB:(\D+) $(\1: Thaimaan baht, Thaimaan bahtia, satang, satangia)
TRY:(\D+) $(\1: Turkin liira, Turkin liiraa, kuruşi, kuruşia)
USD:(\D+) $(\1: USA:n dollari, USA:n dollaria, sentti, senttiä)

"(JPY [-−]?\d+)[.,](\d\d)0" $1
"(JPY [-−]?\d+[.,]\d\d)1" $1 $2 rini
"(JPY [-−]?\d+[.,]\d\d)(\d)" $1 $2 riniä

"([A-Z]{3}) ([-−]?1)([.,]00?)?" $2 $(\1:us)
"([A-Z]{3}) ([-−]?\d+)([.,]00?)?" $2 $(\1:up)

# chiao?
"(CNY [-−]?\d+)[.,]10?" $1 $2 chiao
"(CNY [-−]?\d+)[.,](\d)0?" $1 $2 chiaota
"(CNY [-−]?\d+[.,]\d)1" $1 $2 feni
"(CNY [-−]?\d+[.,]\d)(\d)" $1 $2 feniä

"(([A-Z]{3}) [-−]?\d+)[.,](01)" $1 $(1) $(\2:ss)
"(([A-Z]{3}) [-−]?\d+)[.,](\d)" $1 $(\30) $(\2:sp)
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1 $3 $(\2:sp)
"""
from __future__ import unicode_literals
