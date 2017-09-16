# hr-numbertext

Repozitorij **hr-numbertext** sadrži pravila za zapisivanje brojeva riječima na hrvatskome jeziku.

Pravila se (datoteka `hr.soros`) ne mogu koristiti sama po sebi, već ih je potrebno uključiti u LibreOfficeov dodatak [`numbertext-0.9.5.oxt`](https://extensions.libreoffice.org/extensions/numbertext-1) čime će se iz Calca moći koristiti funkcije NUMBERTEXT() i MONEYTEXT().

## NUMBERTEXT.org

Projekt se održava na internetskoj adresi [NUMBERTEXT.org](http://numbertext.org/) i nastao je iz potrebe generaliziranja funkcije `BAHTTEXT` iz Microsoftova Excela kako bi ova značajka bila dostupna i u LibreOfficeu.

Na istoj se adresi nalazi i specifikacija jezika Soros kojim se pišu pravila: [izravna poveznica na specifikaciju](http://numbertext.org/numbertext.pdf).

## Testiranje i integriranje pravila

Postoji i [integrirano razvojno ogruženje](http://numbertext.org/Soros.html) (engl. *integrated development enviroment*; skraćeno: IDE) koje omogućuje pisanje i provjeravanje pravila.

## Što još treba napraviti

Pravila bi za hrvatski jezik trebala opisati pretvaranje cijelih brojeva, decimalnih brojeva, rednih brojeva te cijena (pozitivni i negativni brojevi). Trenutačno su opisani samo cijeli brojevi i pravila se za hrvatski još ne mogu koristiti u LibreOfficeu.

Pojedinačni zadaci prema važnosti i predviđenom redoslijedu izvršavanja:

- napisati pravila za pretvorbu decimalnih brojeva
- napisati pravila za pretvaranje cijena
- sažeti pravila: pisana su tako da se izbjegnu pogreške, ali broj je pravila moguće smanjiti pisanjem efikasnijih pravilnih izraza (engl. *regular expression*)
- temeljito testirati pravila
- uključiti pravila u dodatak `numbertext`

Napravljeno

- ujednačiti različite zapise brojeva
- napisati pravila za cijele brojeve

---

Pravila za hrvatski su dostupna na adresi https://github.com/krunose/hr-numbertext

---

Zadnja izmjena pravila 2017-09-16