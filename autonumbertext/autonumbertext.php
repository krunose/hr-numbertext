<?php


/*

Generiranje pravila za NUMBERTEXT.org iz predložaka

--------------------------------------------------------------

Kruno, kruno.se (na gmx.com), 2017.

Inačica:			0.1.2 (2017-09-06)	→		ispravljeni nepravilni deklinacijski obrasci (milijardu > milijarda)
					0.1.1 (2017-07-21)	→		dodan primjer upotrebe

--------------------------------------------------------------

Sintaksa ukratko (GNU/Linux):

	php autonumbertext.php <langCode>

primjer: php autonumbertext.php hr


Za dokumentaciju v. 'autonumbertext.md'.


*/




// skripta prima samo jedan argument (oznaku jezika)
if($argc < 2 || $argc > 2) {

	// izlaz ako pridruženo više ili manje od jednoga argumenta
	exit("\nSkripta prima samo jedan dodatni argument i to je oznaka jezika (recimo: hr).\n\nIzgleda da ste unijeli premalo argumenata (nedostaje oznaka jezika) ili ste ih unijeli previše. Za više informacija pogledajte datoteku autonumbertext.md.\n\n");

// ako je dodijeljen jedan argument (oznaka jezika), definiraj varijable
} else {

	$langCode = $argv[1];	// oznaka jezika (recimo: hr)
	$outputFile = $argv[1] . ".soros";	// datoteka u koju se spremaju generirana pravila
	$genFolder = $argv[1] . "-rules";	// mapa u kojoj će biti generirana pravila
	$zeros = 0;	// inicijalno postavljanje varijable za definiranje broja nula u brojevima od tisuću nadalje

}




// datoteke potrebne za rad skripte
$filesNeeded = array(

	"numbers.txt",	// nazivi brojeva od od tisuću nadalje (u nominativu jednine)
	"header.txt",	// sve potrebno do broja tisuću (autor pravila, jedinice, desetice, stotice ...)
	"femininum.txt",	// predložak za brojeve ž.r. (tisuća, milijarda, bilijarda ...)
	"masculinum.txt",	// predložak za brojeve m.r. (milijun, bilijun, trilijun ...)
	"footer.txt"	// sve nakon cijelih brojeva (decimalni brojevi, ispisivanje brojeva u cijene i sl.)

);





// postavljanje varijable za prikupljanje naziva datoteka koje nedostaju (ako nedostaju)
$missingFiles = "";

// provjera postoje li u mapi u kojoj se nalazi 'autonumbertext.php' i sve ostale pomoćne datoteke
foreach($filesNeeded as $neededFile) {

	if(file_exists($neededFile)) {

		continue;

	} else {

		// prikupljanje datoteka koje nedostaju u varijablu radi prijave greške korisniku
		$missingFiles .= "\t" . $neededFile . "\n";

	}

}

// ako skripta ne nalazi sve potrebne datoteke ...
if($missingFiles != "") {

	// ... prekini izvršavanje uz obavijest
	exit("\nIzgleda da mapa u kojoj se nalazi skripta 'autonumbertext.php' ne sadržava sve potrebne datoteke. Nedostaju datoteke\n\n" . $missingFiles . "\nZa više informacija vidi datoteku autonumbertext.md.\n\n");

}




// sadržaj mape u kojoj se nalazi skripta autonumbertext.php
$scanDir = scandir(".");

// provjera postoji li već mapa u koju će se spremati generirana pravila
if(!in_array($genFolder, $scanDir)) {

	// ako datoteka ne postoji, generira se
	mkdir($genFolder, 0777, true);

}




// skripta ne briše prethodno generirana pravila, već vrši preimenovanje starih datoteka i u mapu sprema novu datoteku <langCode>.soros (hr.soros)
if(file_exists($genFolder . "/" . $argv[1] . ".soros")) {

	rename($genFolder . "/" . $argv[1] . ".soros", $genFolder . "/" . time() . "-" . $argv[1] . ".soros");

}




// funkcija za spremanje sadržaja u željenu datoteku
function writeLine($line, $folder, $file) {

	$writeHandle = fopen($folder . "/" . $file, "a+");
		fwrite($writeHandle, $line);
			fclose($writeHandle);

}





// zamjena oznaka u predlošcima
function replacePlaceholders($line, $name, $num, $genFolder, $outputFile) {


	// uspoređuje se sa 'tisuć' jer je 'u' već skinuto radi dodavanja gramatičkih nastavaka
	if($name != "tisuć") {

		$gram = "ostalo";

	} else {

		$gram = "tisuću";

	}


	// nastavci brojeva ženskoga roda (tisuću, milijarda, bilijarda...)
	$numberGram = array(

		"tisuću" => array(

			"u",
			"e",
			"e",
			"a",
			"a",
			"a",
			"a",
			"a",
			"a",
			"a",
			"a",
			"e",
			"e",
			"e",
			"e",
			"e",
			"e",
			"a",
			"a",
			"a",
			"e",
			"a",
			"e",
			"a",
			"e",
			"a",
			"e"

		),

		"ostalo" => array(

			"a",
			"e",
			"e",
			"i",
			"i",
			"i",
			"a",
			"a",
			"a",
			"a",
			"a",
			"e",
			"e",
			"e",
			"e",
			"e",
			"e",
			"i",
			"i",
			"a",
			"e",
			"a",
			"e",
			"a",
			"a",
			"a",
			"e"

		)

	);



	$line = str_replace("-digit-", $num, $line);
	$line = str_replace("-name-", $name, $line);
	$line = str_replace("-digit2-", ($num + 2), $line);

	if(preg_match("/-gram(\d{1,2})-/", $line, $matches)) {

		$line = str_replace("-gram" . $matches[1] . "-", $numberGram[$gram][$matches[1]], $line);

	}

		// zapiši redak u odgovarajuću datoteku nakon što se izvrši zamjena
		writeLine($line, $genFolder, $outputFile);

}




// čitanje datoteka readak po redak
function readUserFile($file, $typeOpen, $callback, $argOne, $argTwo, $argThree, $argFour) {

	$openHandle = fopen($file, $typeOpen);

	if($openHandle) {

		while(($line = fgets($openHandle)) !== false) {

			// zovi odgovarajuću funkciju s obzirom na to koja se datoteka čita
			call_user_func($callback, $line, $argOne, $argTwo, $argThree, $argFour);

		}
	}
	fclose($openHandle);

}




// zapisivanje datoteke 'header.txt' u datoteku <langCode>.soros (recimo: hr.soros)
readUserFile($filesNeeded[1], "r", "writeLine", $genFolder, $outputFile, null, null);




// učitavanje naziva brojeva od tisuću nadalje (tisuća, milijun, milijarda ...)
$numbers = file($filesNeeded[0]);

// preskoči prazne retke ako ih ima u datoteci 'numbers.txt'
array_filter($numbers);




	// svaki broj iz datoteke 'numbers.txt' ispiši prema odgovarajućem predlošku
	foreach($numbers as $numberKey => $numberName) {

		// ispisivanje ime broja u komentarima (recimo: # tisuća)
		$wholeNumberName = $numberName;

		$numberName = trim($numberName);

		$zeros = $zeros + 3;

		// ako je riječ o prvom broju iz datoteke 'numbers.txt' ili o parnom retku iz datoteke, riječ o brojevima ženskoga roda ([0]: tisuća, ([1] milijun), [2] milijarda)
		if($numberKey == 0 || $numberKey % 2 == 0) {

			// uzmi samo osnovu, nastavci su već dodani u predlošku 'femininum.txt'
			$numberName = substr($numberName, 0, -1);

			// zapiši komentar s imenom broja (recimo: # tisuća)
			writeLine("\n\n# " . $wholeNumberName . "\n", $genFolder, $outputFile);

			// čitaj odgovarajući predložak redak po redak i ispisuj prema predlošku
			readUserFile($filesNeeded[2], "r", "replacePlaceholders", $numberName, $zeros, $genFolder, $outputFile);

		// dodavanje novoga retka iza svakoga broja (vizualno formatiranje)
		writeLine("\n", $genFolder, $outputFile);

		// ponovi sve iz prethodnoga, ali za brojeve muškoga roda (milijun, bilijun ...)
		} else {

			writeLine("\n\n# " . $wholeNumberName . "\n", $genFolder, $outputFile);

			readUserFile($filesNeeded[3], "r", "replacePlaceholders", $numberName, $zeros, $genFolder, $outputFile);

			writeLine("\n", $genFolder, $outputFile);

		}

	}



	// add footer to rules
	readUserFile($filesNeeded[4], "r", "writeLine", $genFolder, $outputFile, null, null);




?>