# autonumbertext

`Autonumbertext` je jednostavna skripta za korištenje iz naredbenoga retka u PHP-u* kojoj je zadaća olakšati održavanje pravila za pretvaranje brojeva iz brojevnoga zapisa u slovni zapis.

Datoteka [hr.soros](https://github.com/krunose/hr-numbertext) sadrži dijelove koji je potrebno napisati samo jednom, ne ponavljaju se: pravila za brojeve do sto; ali postoje i dijelovi koji se ponavljaju: brojevi milijun i bilijun imaju istu strukturu, odnosno svi brojevi na -ijun imaju ista pravila te je samo potrebno mijenjati broj nulā s obzirom na to o kojem se broju radi (milijun: šest nula; bilijun: dvanaest nula).

Ta pravilnost omogućuje automatiziranje izrade pravila prema preddefiniranome predlošku. Zadaća je skripte `autonumbertext` olakšati održavanje pravila jer se izmjene za sve brojeve na -ijun mogu napraviti samo na jednom mjestu, u predlošku, a skripta će izmjenu pretvoriti u pravilo za sve brojeve od milijun do tridecilijun.

Prednost je predložaka i u tome što se je ih je jednostavno pripremiti za druge jezike u kojima su brojevi slični kao u hrvatskome. Potrebno je samo urediti predložak i skripta će iz njega generirati pravila za taj jezik.

**&ast;** iako PHP nije optimalno rješenje za ovakav zadatak, jedini je programski jezik u kojem sam to znao napisati dovoljno brzo i onako kako sam zamislio.

---

- v. [pravila za hrvatski](https://github.com/krunose/hr-numbertext/blob/master/README.md)
- v. stranice projekta [NUMBERTEXT.org](http://numbertext.org/)

## Što još treba napraviti

- dokumentirati kako koristiti skriptu
- dokumentirati što skripta i kako radi (to će pomoći s korištenjem skripte onima koji ne mogu čitati izvorni kod skripte)
- dokumentirati strukturu predložaka
- dokumentirati potencijal skripte i predložaka za izradi pravila za slične/srodne jezike (srpski, bosanski, crnogorski)

## Sadržaj repozitorija

- *`autonumbertext.php`* – skripta pisana u PHP-u za raspisivanje pravila na temelju predložaka
- *`numbers.txt`* – nazivi/imena brojeva od tisuću do tridecilijarde; iz ove datoteke `autonumbertext.php` izvlači nazive brojeva
- *`header.txt`* – dijelovi pravila koji se ne ponavljaju; jednoznamenkasti i dvoznamenkasti brojevi
- *`femininum.txt`* – predložak za brojeve ž. r. od tisuću (uključujući tisuću) nadalje (milijarda, bilijarda, trilijarda ...)
- *`masculinum.txt`* – predložak za brojeve m. r. (brojevi na -ijun) od milijun (uključujući milijun) nadalje (milijun, bilijun, trilijun ...)
- *`footer.txt`* – pravila koja slijede nakon pravila za cijele brojeve. Ono što slijedi, ali se ne ponavlja. Dijelove koji bi se mogli ponavljati u pravilima za cijene, treba izdvojiti u poseban predložak i prilagoditi skriptu `autonumbertext`
- *`autonumbertext.md`* – dokumentacija (u izradi)

---
Repozitorij skripte: https://github.com/krunose/hr-numbertext/autonumbertext
