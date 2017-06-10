# autonumbertext

`Autonumbertext` je jednostavna skripta kojoj je zadaća olakšati održavanje pravila za pretvaranje brojeva iz brojevnoga zapisa u slovni zapis.

Datoteka [hr.soros](https://github.com/krunose/hr-numbertext) sadrži dijelove koji je potrebno napisati samo jednom, ne ponavljaju se: pravila za brojeve do sto; ali postoje i dijelovi koji se ponavljaju: brojevi milijun i bilijun imaju istu strukturu, odnosno svi brojevi na -ijun imaju ista pravila te je samo potrebno mijenjati broj nulā s obzirom na to o kojem se broju radi (milijun: šest nula; bilijun: dvanaest nula).

Ta pravilnost omogućuje automatiziranje izrade pravila prema preddefiniranome predlošku. Zadaća je skripte `autonumbertext` olakšati održavanje pravila jer se izmjene za sve brojeve na -ijun mogu napraviti samo na jednom mjestu, u predlošku, a skripta će izmjenu pretvoriti u pravilo za sve brojeve od milijun do tridecilijun.

Prednost je predložaka i u tome što se je ih je jednostavno pripremiti za druge jezike u kojima su brojevi slični kao u hrvatskome. Potrebno je samo urediti predložak i skripta će iz njega generirati pravila za taj jezik.

---

- v. [pravila za hrvatski](https://github.com/krunose/hr-numbertext/blob/master/README.md)
- v. stranice projekta [NUMBERTEXT.org](http://numbertext.org/)

## Što još treba napraviti

- dokumentirati princip rada skripte (to će pomoći s korištenjem skripte onima koji ne mogu čitati izvorni kod skripte)
- dokumentirati potencijal skripte i predložaka za izradi pravila za slične/srodne jezike (srpski, bosanski, crnogorski)

---
Repozitorij skripte: https://github.com/krunose/hr-numbertext/autonumbertext
