# autonumbertext

`Autonumbertext` je jednostavna skripta pisana u PHP-u kojoj je zadaća olakšati održavanje pravila za pretvaranje brojeva iz zapisa brojkama u slovni zapis. Brojeve je moguće definirati relativno jednostavnim pravilima koja se ponavljaju i zadaća je ove skripte bila automatizirati ispisivanje tih pravila za brojeve do tridecilijarde.

Iako PHP nije optimalno rješenje za ovakav zadatak, jedini je jezik koji sam poznavao dovoljno za izvršenje ovakvoga zadatka.

Pravilnost uzorka omogućuje ispisivanje pravila prema predlošku i olakšava održavanje pravila.

Skripta se može iskoristiti i za druge jezike, potrebno je samo urediti odgovarajuće predloške tako da odgovaraju stanju u jeziku za koji se pravila pišu.

---

- v. [pravila za hrvatski](https://github.com/krunose/hr-numbertext/blob/master/README.md)
- v. stranice projekta [NUMBERTEXT.org](http://numbertext.org/)

## Što još treba napraviti

- dokumentirati kako koristiti skriptu
- dokumentirati što skripta radi i kako radi
- dokumentirati strukturu predložaka

## Sadržaj repozitorija

- `autonumbertext.php` – skripta pisana u PHP-u za raspisivanje pravila na temelju predložaka
- `number-formats.php` – php-skripta za generiranje valjanih oblika brojeva (v. početni komentar u samoj skripti)
- `numbers.txt` – nazivi/imena brojeva od tisuću do tridecilijarde; iz ove datoteke `autonumbertext.php` izvlači nazive brojeva
- `header.txt` – dijelovi pravila koji se ne ponavljaju; jednoznamenkasti i dvoznamenkasti brojevi
- `femininum.txt` – predložak za brojeve ž. r. od tisuću (uključujući tisuću) nadalje (milijarda, bilijarda, trilijarda ...)
- `masculinum.txt` – predložak za brojeve m. r. (brojevi na -ijun) od milijun (uključujući milijun) nadalje (milijun, bilijun, trilijun ...)
- `footer.txt` – pravila koja slijede nakon pravila za cijele brojeve. Ono što slijedi, ali se ne ponavlja. Dijelove koji bi se mogli ponavljati u pravilima za cijene, treba izdvojiti u poseban predložak i prilagoditi skriptu `autonumbertext`
- `autonumbertext.md` – dokumentacija (u izradi)

---
Repozitorij skripte: https://github.com/krunose/hr-numbertext/autonumbertext
