# NUMBERTEXT

Repozitorij **hr-numbertext** sadrži pravila za pretvaranje brojevnoga zapisa u slovni zapis, odnosno pravila zapisuju brojeve slovima onako kako bi se ti brojevi izgovarali na hrvatskome jeziku.

Za potrebe pretvaranja brojeva u riječi razvijen je jednostavan jezik Soros, koji je pak temeljen na programskom jeziku `regex`, što je pokrata od engleskoga izraza *regular expression*.

Projekt se održava na internetskoj adresi [NUMBERTEXT.org](http://numbertext.org/) i nastao je iz potrebe generaliziranja funkcije `BAHTTEXT` iz Microsoftova Excela kako bi ova značajka bila dostupna i u LibreOfficeu, uredskome paketu otvorenoga koda.

Značajka je u LibreOffice integrirana pomoću dodatka [`numbertext-0.9.5.oxt`](https://extensions.libreoffice.org/extensions/numbertext-1).

Pravila bi za hrvatski jezik trebala opisati pretvaranje cijelih brojeva, decimalnih brojeva te cijena. Trenutno su opisani samo cijeli brojevi i pravila za hrvatski jezik nisu uključena u projekt NUMBERTEXT.org i nisu dostupan u LibreOfficeu. Prije uključivanja bi pravila trebalo obraditi decimalne brojeve i cijene.

## Što još treba napraviti

- ujednačiti različite zapise brojeva (razmak kao razdjelnik tisućica, točka kao razdjelnik tisućica...) u oblik broja koji jezik Soros može interpretirati
- napisati pravila za pretvorbu decimalnih brojeva
- napisati pravila za pretvaranje cijena
- sažeti pravila: za sada su pravila pisana opširno radi izbjegavanja pogrešaka, ali pravila je moguće napisati i sažetije
- temeljito testirati pravila
- uključiti pravila u dodatak `numbertext`

---

Pravila za hrvatski su dostupna na adresi https://github.com/krunose/hr-numbertext

---

Zadnja izmjena pravila 2017-05-31