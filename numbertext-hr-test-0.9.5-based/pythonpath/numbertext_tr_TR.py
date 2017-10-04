# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 sıfır
1 bir
2 iki
3 üç
4 dört
5 beş
6 altı
7 yedi
8 sekiz
9 dokuz
10 on
1(\d) on $1
20 yirmi
2(\d) yirmi $1
30 otuz
3(\d) otuz $1
40 kırk
4(\d) kırk $1
50 elli
5(\d) elli $1
60 altmış
6(\d) altmış $1
70 yetmiş
7(\d) yetmiş $1
80 seksen
8(\d) seksen $1
90 doksan
9(\d) doksan $1

(1)(\d\d)  yüz $2		# yüz ..
([2-9])(\d\d) $1 yüz $2		# üç yüz ...
(1)(\d\d\d)  bin $2		# bin
(\d{1,2})([1-9]\d\d) $1 bin $2	# on bin iki yüz
(\d{1,3})(\d{3}) $1 bin $2	# yüz bin iki yüz
(\d{1,3})(\d{6}) $1 milyon $2
(\d{1,3})(\d{9}) $1 milyar $2
(\d{1,3})(\d{12}) $1 trilyon $2
(\d{1,3})(\d{15}) $1 katrilyon $2
(\d{1,3})(\d{18}) $1 kentilyon $2
(\d{1,3})(\d{21}) $1 sekstilyon $2
(\d{1,3})(\d{24}) $1 septilyon $2

# negative number

[-−](\d+) negatif |$1

# decimals

([-−]?\d+)[.,] $1| virgül
"([-−]?\d+[.,]0*)(\d+)" $1 |$2
([-−]?\d+[.,]\d*)(\d) $1| |$2

# currency

# unit/subunit singular/plural

us:([^,]*),([^,]*),([^,]*),([^,]*) \1
up:([^,]*),([^,]*),([^,]*),([^,]*) \2
ss:([^,]*),([^,]*),([^,]*),([^,]*) \3
sp:([^,]*),([^,]*),([^,]*),([^,]*) \4

AUD:(\D+) $(\1: Avustralya doları, Avustralya doları, sent, sent)
BGN:(\D+) $(\1: Bulgar levası, Bulgar levası, stotinka, stotinki)
BWP:(\D+) $(\1: Botswana pulası, Botswana pulası, thebe, thebe)
CAD:(\D+) $(\1: Kanada doları, Canadian dollars, sent, sent)
CHF:(\D+) $(\1: İsviçre frangı, İsviçre frangı, santim, santim)
CNY:(\D+) $(\1: Çin yuanı, Çin yuanı, fen, fen)
CZK:(\D+) $(\1: Çek korunası, Çek korunası, heller, heller)
EEK:(\D+) $(\1: Estonya kronu, Estonya kronu,	sent, sent)
EUR:(\D+) $(\1: euro, euro, sent, sent)
GBP:(\D+) $(\1: sterlin, sterlin, peni, peni)
GHS:(\D+) $(\1: Gana sedisi, Gana sedisi, peseva, peseva)
GMD:(\D+) $(\1: Gambiya dalası, Gambiya dalası, butut, butut)
HKD:(\D+) $(\1: Hong Kong doları, Hong Kong doları, sent, sent)
HRK:(\D+) $(\1: Hırvatistan kunası, Hırvatistan kunası, lipa, lipa)
HUF:(\D+) $(\1: Macar forinti, Macar forinti, filler, filler)
INR:(\D+) $(\1: Hindistan rupisi, Hindistan rupisi, paise, paise)
JMD:(\D+) $(\1: Jamaika doları, Jamaika doları, sent, sent)
JPY:(\D+) $(\1: Japon yeni, Japon yeni, sen, sen)
KES:(\D+) $(\1: Kenya şilini, Kenya şilini, sent, sent)
LRD:(\D+) $(\1: Liberya doları, Liberya doları, sent, sent)
LSL:(\D+) $(\1: Lesotho loti, maloti, sente, lisente)
LTL:(\D+) $(\1: Litvanya litası, Litvanya litası, centas, centai)
LVL:(\D+) $(\1: Letonya latı, Letonya latı, santims, santimi)
MGA:(\D+) $(\1: ariary, ariaries, iraimbilanja, iraimbilanja)
MUR:(\D+) $(\1: Mauritius rupisi, Mauritius rupisi, sent, sent)
MXN:(\D+) $(\1: Meksika pezosu, Meksika pezosu, sentavo, sentavo)
MWK:(\D+) $(\1: Malawian kwacha, Malawian kwacha, tambala, tambala)
NAD:(\D+) $(\1: Namibya doları, Namibya doları, sent, sent)
NGN:(\D+) $(\1: Nijerya nairası, Nijerya nairası, kobo, kobo)
NZD:(\D+) $(\1: Yeni Zelanda doları, Yeni Zelanda doları, sent, sent)
PGK:(\D+) $(\1: Papua Yeni Gine kinası, Papua Yeni Gine kinası, toea, toea)
PHP:(\D+) $(\1: Filipinler pezosu, Filipinler pezosu, sentavo, sentavo)
PKR:(\D+) $(\1: Pakistan rupisi, Pakistan rupisi, paisa, paisa)
PLN:(\D+) $(\1: Polonya zlotisi, Polonya zlotisi, grosz, groszy)
RON:(\D+) $(\1: Romen leyi, Romen leyi, ban, ban)
RSD:(\D+) $(\1: Sırbistan dinarı, Sırbistan dinarı, para, para)
RUB:(\D+) $(\1: Rus rublesi, Rus rublesi, kopek, kopek)
RWF:(\D+) $(\1: Ruanda frangı, Ruanda frangı, santim, santim)
SDG:(\D+) $(\1: Sudan poundu, Sudan poundu, piastre, piastres)
SGD:(\D+) $(\1: Singapur doları, Singapur doları, sent, sent)
SLL:(\D+) $(\1: Sierra Leone leonu, Sierra Leone leonu, sent, sent)
SZL:(\D+) $(\1: lilangeni, emalangeni, cent, cents)
THB:(\D+) $(\1: Tayland bahtı, Tayland bahtı, satang, satang)
TRY:(\D+) $(\1: Türk lirası, Türk lirası, kuruş, kuruş)
TTD:(\D+) $(\1: Trinidad ve Tobago doları, Trinidad ve Tobago doları, sent, sent)
TZS:(\D+) $(\1: Tanzanya şilini, Tanzanya şilini, sent, sent)
UAH:(\D+) $(\1: Ukrayna hryvnyası, Ukrayna hryvnyası, kopiyka, kopiyka)
UGX:(\D+) $(\1: Uganda şilini, Uganda şilini, sent, sent)
USD:(\D+) $(\1: ABD doları, ABD doları, sent, sent)
X[AO]F:(\D+) $(\1: CFA franc, CFA francs, centime, centimes)
ZAR:(\D+) $(\1: Güney Afrika randı, Güney Afrika randı, sent, sent)
ZMK:(\D+) $(\1: Zambiya kıvaçası, Zambiya Kıvaçası, ngwee, ngwee)
ZWD:(\D+) $(\1: Zimbabve doları, Zimbabve doları, sent, sent)

"(JPY [-−]?\d+)[.,](\d\d)0" $1
"(JPY [-−]?\d+[.,]\d\d)(\d)" $1 $2 rin

# removing spaces from number names before currencies

"space:([^ ]+) +([^ ].*)" \1$(space:\2)
space:(.*) \1

"([A-Z]{3}) ([-−]?1)([.,]00?)?" $2 $(\1:us)
"([A-Z]{3}) ([-−]?\d+)([.,]00?)?" $(space:|$2) $(\1:up)

"(CNY [-−]?\d+)[.,](\d)0?" $1 $2 jiao
"(CNY [-−]?\d+[.,]\d)(\d)" $1 $2 fen

"((MGA|MRO) [-−]?\d+)[.,]0" $1
"((MGA|MRO) [-−]?\d+)[.,]2" $1 |$(1) $(\2:ss)
"((MGA|MRO) [-−]?\d+)[.,]4" $1 |$(2) $(\2:sp)
"((MGA|MRO) [-−]?\d+)[.,]6" $1 |$(3) $(\2:sp)
"((MGA|MRO) [-−]?\d+)[.,]8" $1 |$(4) $(\2:sp)

"(([A-Z]{3}) [-−]?\d+)[.,](01)" $1 |$(1) $(\2:ss)
"(([A-Z]{3}) [-−]?\d+)[.,](\d)" $1 |$(\30) $(\2:sp)
"(([A-Z]{3}) [-−]?\d+)[.,](\d\d)" $1 $(space:|$3) $(\2:sp)

"""
from __future__ import unicode_literals
