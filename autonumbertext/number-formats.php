<?php

/*

==============================================================
Generiranje valjanih oblika cijelih brojeva
==============================================================

--------------------------------------------------------------

Copyright (c) Krunoslav Šebetić <kruno.se@gmx.com> 2017.

version: 0.1 (2017-07-21)

--------------------------------------------------------------

Sintaksa ukratko (GNU/Linux):

	php number-formats.php

--------------------------------------------------------------

==== Kratak opis i objašnjenje ====

Skripta 'number-formats.php' definira prihvatljive oblike brojeva za dodatak numbertext. Rezultat je izvođenja datoteka 'number-formats.txt'. Sadržaj datoteke treba unijeti (kopirati) u datoteku header.txt odmah ispod retka '__numbertext__', odnosno zamijeniti ono što se na tome mjestu već nalazi.

	=> Za rad je ove skripte nužna datoteka 'numbers.txt' <=

Nakon toga treba pokrenuti skriptu 'autonumbertext.php'. Za više informacija v. 'autonumbertext.md'.

Općenite se informacije o projektu nalaze u datoteci 'README.md'.

----------------------------

LibreOfficeov dodatak numbertext pretvara brojeve, zapisane znamenkama, u brojeve zapisane riječima. Nakon instalacije dodatka sa

	https://extensions.libreoffice.org/extensions/numbertext-1

iz Calca se u ćeliju može unijeti formula '=numbertext(5)' što će vratiti rezultat 'pet'.

Nevolja je u tome što se veliki brojevi mogu zapisivati u različitim oblicima pa tako miliju može biti zapisan kao 1000000; zatim 1 000 000; 1.000.000; još i 1,000.000.

Pravopisi često sugeriraju jedno, a čini se da svaka struka ima svoj način zapisivanja velikih brojeva neovisno o tome što u pravopisu stoji. Navedena su četiri zapisa najčešća, a izgleda da numbertext barata samo prvim načinom zapisivanja. Ova skripta pretvara sve ostale zapise u taj prvi zapis: 1 000 000 → 1000000; 1,000.000 → 1000000...

Tako redak

	(\d{1,3}).(\d{3}) $(\1\2)

znači da brojeve od 1000 do 999999 iz oblika 1 000/1.000 vrate u obliku 1000. Oznaka \1 vraća ono što je u prvoj zagradi: jedna, dvije, ili tri znamenke iz kojih slijedi točka, a iza nje još tri (bilo koje) znamenke: (\d{1,3}).(\d{3}) [10.000] → $(\1\2) [(10)(000)] → 10000.

Navedeni se oblici možda mogu napisati i sažetije, ali ovjde se išlo na preciznost nauštrb ekonomičnosti. Svaki redak odgovara jednom unosu u datoteci 'numbers.txt' u obliku sa razmacima, u obliku sa točkama i u obliku sa zarezima i točkama (27 unosa iz datoteke 'numbers.txt' puta tri oblika broja jednako je osamdeset i jednom retku iz datoteke 'number-formats.txt'). 

--------------------------------------------------------------

==== Za napraviti ====

	- dodati komentare u skriptu radi lakšega čitanja
	- dodati nove oblike cijelih brojeva (ako se u kojoj struci koristi još koji oblik)
	- automatski dodati sadržaj datoteke 'number-formats.txt' na odgovarajuće mjesto u datoteku 'hr-rules/hr.soros'
	- sažeti zapis sadržaja datoteke 'number-formats.txt'
	- temeljito testirati pravila za hrvatski jezik

--------------------------------------------------------------

==== Izmjene ====

2017-07-21	→	inicijalna inačica

--------------------------------------------------------------

*/

if(file_exists("numbers.txt")) {

	unlink("number-formats.txt");

	$numOfNumbers = file("numbers.txt");

	array_filter($numOfNumbers);

	$numOfNumbers = count($numOfNumbers);


	// $digits is multiplying $c with 3, need to start with 2 so we don't print numbers with 3 digits as those don't have separators
	$c = 2;

	while($c <= $numOfNumbers) {
	
		$digits = ($c * 3);

		$getNumber = str_repeat("1", $digits); // simulate real number, e.g. 1111111

		$number = str_split($getNumber, 3);

		$numSplitter = "";	// 1,111.111
		$numDot = "";			// 1.111.111
		$numSpace = "";		// 1 111 111

		$count = count($number);

		if($count % 2 != 0) {

			$splitter = ".";

		} else {

			$splitter = ",";

		}


		for($i = (count($number) - 1); $i >= 0; $i--) {

				switch($splitter) {

					case ".":
						$splitter = ",";
							break;

					case ",":
						$splitter = ".";
							break;
				}



			if($i != (count($number) - 1)) {

				if($i != 0) {

					$numSplitter .= '(\d{3})' . $splitter;
					$numDot .= '(\d{3}).';
					$numSpace .= '(\d{3})\s';

				} else {

					$numSplitter .= '(\d{3})';
					$numDot .= '(\d{3})';
					$numSpace .= '(\d{3})';

				}

			} else {

				$numSplitter .= '(\d{1,3})' . $splitter;
				$numDot .= '(\d{1,3}).';
				$numSpace .= '(\d{1,3})\s';

			}

		}

		$lastPart = ' $(';

		for($j = 1; $j <= $count; $j++) {

			$lastPart .= "\\" . $j;

		}

		$lastPart = $lastPart . ")";

		// get all formats in one line: 1 000 000; 1,000.000; 1.000.000
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