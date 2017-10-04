# numbertext-hr-test-0.9.5-based

Sadržaj se ove mape može koristiti kao dodatak LibreOfficeovu Calcu radi testiranja i provjere pravila. Za sada je u okviru funkcije NUMBERTEXT() dostupno

- ispisivanje slovima prirodnih brojeva do tridecilijarde
- ispisivanje slovima rednih brojeva do devetsto devedeset devet milijuna devetsto devedeset devet tisuća devetsko devedeset devet(i)
  - redni su brojevi do devedeset devet tisuća devetsto devedeset devet(i) napisani dobro
  - redne brojeve iza toga broja treba doraditi (broj će se ispisati, ali u ponekom su slučaju moguća (manja) odstupanja od uobičajenoga zapisivanja rednih brojeva u hrvatskome jeziku 

a potrebno je još napraviti

- ispisivanje valuta (funkcija MONEYTEXT())
- decimalne brojeve (funkcija NUMBERTEXT())

## Temeljeno na dodatku numbertext-0.9.5.oxt

Dodatak je iz ovoga repozitorija namijenjen isključivo testiranju pravila radi prijava grešaka i slično. Dodatak još nije dostupan u službenim repozitorijima ili izvornom kodu LibreOfficea. Izvorna inačica dodatka (`numbertext-0.9.5.oxt`) ne sadržava pravila za hrvatski jezik. Taj je dodatak uzet kao osnova za dodavanje pravila za hrvatski jezik.


## Korištenje dodatka

Sadržaj je ove mape potrebno preuzeti s GitHuba kao ZIP-datoteku i nakon preuzimanja preimenovati je iz `numbertext-hr-test-0.9.5-based.zip` u `numbertext-hr-test-0.9.5-based.oxt`, otvoriti LibreOffice Calc te kroz izbornik **Alati** → **Upravljanje dodacima** instalirati preuzetu OXT-datoteku.

Pravila se mogu testirati tako da u ćeliju A1 upišete broj, a u koju drugu ćeliju formulu `=NUMBERTEXT(A1)`. Ako ne koristite hrvatske lokalne postavke za LibreOffice, formulu je potrebno upisati u obliku `=NUMBERTEXT(A1;"hr_HR")`.

## Uređivanje pravila

Pravila su za hrvatski jezik dostupna na https://github.com/krunose/hr-numbertext i na toj se poveznici može naći više o projektu.

---

https://github.com/krunose/hr-numbertext/numbertext-hr-test-0.9.5-based/

---

Zadnja izmjena 2017-10-04
