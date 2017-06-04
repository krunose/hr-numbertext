# hr-numbertext

Repozitorij **hr-numbertext** sadrži pravila za pretvaranje brojevnoga zapisa u slovni zapis, odnosno pravila zapisuju brojeve slovima onako kako bi se ti brojevi izgovarali na hrvatskome jeziku.

Za potrebe pretvaranja brojeva u riječi razvijen je jednostavan jezik Soros, koji je pak temeljen na programskom jeziku `regex`, što je pokrata od engleskoga izraza *regular expression* (hr. *pravilni izrazi*).

## NUMBERTEXT.org

Projekt se održava na internetskoj adresi [NUMBERTEXT.org](http://numbertext.org/) i nastao je iz potrebe generaliziranja funkcije `BAHTTEXT` iz Microsoftova Excela kako bi ova značajka bila dostupna i u LibreOfficeu, uredskome paketu otvorenoga koda.

Na istoj se adresi nalazi i specifikacija jezika Soros koja objašnjava kako pisati pravila: [izravna poveznica na specifikaciju](http://numbertext.org/numbertext.pdf).

## Testiranje i integriranje pravila

Postoji i [integrirano razvojno ogruženje](http://numbertext.org/Soros.html) (engl. *integrated development enviroment*; skraćeno: IDE) koje omogućuje pisanje i provjeravanje pravila.

Značajka je u LibreOffice integrirana pomoću dodatka [`numbertext-0.9.5.oxt`](https://extensions.libreoffice.org/extensions/numbertext-1).

## Što još treba napraviti

Pravila bi za hrvatski jezik trebala opisati pretvaranje cijelih brojeva, decimalnih brojeva te cijena. Trenutno su opisani samo cijeli brojevi i pravila za hrvatski jezik nisu uključena u projekt NUMBERTEXT.org i nisu dostupan u LibreOfficeu. Prije uključivanja bi pravila trebalo obraditi decimalne brojeve, ispisivanje cijena te dobro testirati pravila.

Pojedinačni zadaci prema važnosti i predviđenom redoslijedu izvršavanja:

- ujednačiti različite zapise brojeva (razmak kao razdjelnik tisućica, točka kao razdjelnik tisućica...) u oblik broja koji jezik Soros može interpretirati (redak 21. u datoteci `hr.soros`)
- napisati pravila za pretvorbu decimalnih brojeva
- napisati pravila za pretvaranje cijena
- sažeti pravila: pisana su tako da se izbjegnu pogreške, ali broj je pravila moguće smanjiti pisanjem efikasnijih pravilnih izraza (engl. *regular expression*)
- temeljito testirati pravila
- uključiti pravila u dodatak `numbertext`

---

Pravila za hrvatski su dostupna na adresi https://github.com/krunose/hr-numbertext

---

Zadnja izmjena pravila 2017-05-31