<?php

/*

==============================================================
Generiranje valjanih oblika brojeva
==============================================================

--------------------------------------------------------------

Copyright (c) Krunoslav Šebetić <kruno.se@gmx.com> 2017.


		0.2.1 (2017-08-25)	→		dorađeni komentari
		0.2 (2017-07-21)		→		inicijalna inačica

--------------------------------------------------------------

Sintaksa ukratko (GNU/Linux):

	php number-formats.php

--------------------------------------------------------------

==== Kratak opis i objašnjenje ====

Skripta 'number-formats.php' definira prihvatljive oblike brojeva. Rezultat je datoteka 'number-formats.txt'. Sadržaj datoteke treba ručno unijeti (kopirati) u datoteku 'header.txt' odmah ispod retka '__numbertext__', odnosno zamijeniti ono što se na tome mjestu već nalazi.

	=> Za rad je ove skripte da se u istoj mapi sa skriptom nalazi i datoteka 'numbers.txt' <=

Nakon toga treba pokrenuti skriptu 'autonumbertext.php'. Za više informacija v. 'autonumbertext.md'.

Općenite se informacije o projektu nalaze u datoteci ../README.md.

----------------------------

LibreOfficeov dodatak numbertext pretvara zapis brojeva znamenkama u zapis riječima. Nakon instalacije dodatka sa

	https://extensions.libreoffice.org/extensions/numbertext-1

iz Calca se u ćeliju može unijeti formula '=numbertext(5)' što će rezultirati riječju 'pet'.

	=> Za sada se ova pravila ne nalaze u spomenutom dodatku i ova značajka još nije dostupna u Calcu <=

Dalje, veliki se brojevi mogu zapisivati u različitim oblicima pa tako milijun može biti zapisan kao 1000000, 1 000 000, 1.000.000 i još 1,000.000. Stvar se dodatno komplicira ako se u obzir uzmu i decimalni brojevi.

Pravopisi često sugeriraju jedno, dopuštaju drugo, a čini se da svaka struka ima svoj način zapisivanja velikih brojeva. Navedena su četiri zapisa najčešća, a numbertext brojem tumači samo 1000000. Ova skripta daje pravila za pretvaranje svih ostalih zapisa u taj: 1 000 000 → 1000000; 1,000.000 → 1000000...

Tako redak

	(\d{1,3}).(\d{3}) $(\1\2)

znači da brojeve od 1000 do 999999 iz oblika 1 000 i 1.000 računalu vraćaju kao 1000. Oznaka \1 vraća ono što je u prvoj zagradi (jedna, dvije, ili tri znamenke) iza kojih slijedi točka, a iza nje još (bilo koje) tri znamenke: (\d{1,3}).(\d{3}) [10.000] → $(\1\2) [(10)(000)] → 10000.

Navedeni se oblici možda mogu napisati i sažetije, ali ovjde se išlo na preciznost nauštrb ekonomičnosti. Svaki redak odgovara jednom unosu u datoteci 'numbers.txt' u obliku sa razmacima, u obliku sa točkama i u obliku sa zarezima i točkama (27 unosa iz datoteke 'numbers.txt' puta tri oblika broja jednako je osamdeset i jednom retku iz datoteke 'number-formats.txt').

	==> Valja imati na umu da lokalizacijska datoteka za hrvatski u LibreOfficeu prihvaća kao razdjelnik tisućica samo točku (1.000; 1.000.000) i decimalni zarez (1.000.000,23), odnosno oblik 1000000,23. Možda su svi ostali oblici iz ovih pravila suvišni. <== 

--------------------------------------------------------------

==== Za napraviti ====

	- dodati pravila za decimalne brojeve
	- dodati komentare u skriptu radi lakšega čitanja
	- dodati nove oblike cijelih brojeva (ako se u kojoj struci koristi još koji oblik)
	- automatski dodati sadržaj datoteke 'number-formats.txt' na odgovarajuće mjesto u datoteku 'hr-rules/hr.soros' (automatsko pokretanje ove skripte kroz 'autonumbertext.php' i zapisivanje razultata izravno u 'hr.soros')
	- optimizirati skriputa radi sažimanja zapisa u datoteci 'number-formats.txt' (isti rezultat u manjem broju redaka)
	- temeljito testirati pravila


*/

if(file_exists("numbers.txt")) {

	unlink("number-formats.txt");

	$numOfNumbers = file("numbers.txt");

	array_filter($numOfNumbers);

	$numOfNumbers = count($numOfNumbers);

	$splitters = array(

		"[\.]",
		"[\,]",
		"[\s]"

	);


	// $digits množi $c sa 3, $c mora počinjati sa 2 tako da razultat bude 6 jer brojevi s manje od tri znamenke nemaju razdjelnike ($c = 1; $digits = $c * 3; $digits = 3 > 100 ==> a sto nema razdjelnika)
	$c = 2;

	while($c <= $numOfNumbers) {
	
		$digits = ($c * 3);

		$getNumber = str_repeat("1", $digits); // simulacija broja s odgovarajućim brojem znamenki, e.g. 1111111

		$number = str_split($getNumber, 3);

		$numSplitter = "";	// 1,111.111
		$numDot = "";			// 1.111.111
		$numSpace = "";		// 1 111 111

		$count = count($number);

		if($count % 2 != 0) {

			$splitter = $splitters[0];

		} else {

			$splitter = $splitters[1];

		}


		for($i = (count($number) - 1); $i >= 0; $i--) {

			switch($splitter) {

				case $splitters[0]:
					$splitter = $splitters[1];
						break;

				case $splitters[1]:
					$splitter = $splitters[0];
						break;
			}



			if($i != (count($number) - 1)) {

				if($i != 0) {

					$numSplitter .= '(\d{3})' . $splitter;			// dynamic splitter (dots and commas): 1,223.332
					$numDot .= '(\d{3})' . $splitters[0];			// dot as splitter:							1.223.332
					$numSpace .= '(\d{3})' . $splitters[2];		// space as splitter:						1 223 332

				} else {

					$numSplitter .= '(\d{3})';
					$numDot .= '(\d{3})';
					$numSpace .= '(\d{3})';

				}

			} else {

				$numSplitter .= '(\d{1,3})' . $splitter;
				$numDot .= '(\d{1,3})' . $splitters[0];
				$numSpace .= '(\d{1,3})' . $splitters[2];

			}

		}

		$lastPart = ' $(';

		for($j = 1; $j <= $count; $j++) {

			$lastPart .= "\\" . $j;

		}

		$lastPart = $lastPart . ")";

		// spremanje svih zapisa u jednu varijablu (1 000 000; 1,000.000; 1.000.000) kako se fwrite() ne bi moralo pozivati više od jednom.
		$writeThis = $numSplitter . $lastPart . "\n" . $numSpace . $lastPart . "\n" . $numDot . $lastPart . "\n";

		$handle = fopen("number-formats.txt", "a+");
			fwrite($handle, $writeThis);
				fclose($handle);

		$c++;

	}

} else {

	exit("Sorry, can't find file 'numbers.txt'. See documentation and check if all needed files are available.\n");

}

?>