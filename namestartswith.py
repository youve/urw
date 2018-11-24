#! /usr/bin/python3
# -*- coding: utf-8 -*-

import re,readline,random

names = {'e': {'m': ['Aarne', 'Aaro', 'Ahti', 'Ahto', 'Ahvo', 'Aimo', 'Aippo', 'Alvi', 'Anania', 'Antti', 'Antero', 'Ano', 'Arpia', 'Asko', 'Eero', 'Eikka', 'Erkki', 'Hannu', 'Harle', 'Harlu', 'Heikki', 'Heino', 'Herppa', 'Hirvo', 'Hyväneuvo', 'Ieri', 'Ierikka', 'Ikitiera', 'Iku', 'Ilari', 'Ilkka', 'Ilmari', 'Ilpo', 'Isto', 'Jeremia', 'Jerkko', 'Joukahainen', 'Joukavainen', 'Jouko', 'Jousia', 'Juha', 'Juhani', 'Jukka', 'Jurkka', 'Jussi', 'Jyri', 'Kaipia', 'Kalerva', 'Kalervo', 'Kaleva', 'Kalevi', 'Kalle', 'Kauko', 'Kimmo', 'Kolja', 'Kolkka', 'Konsta', 'Korjus', 'Kuisma', 'Kuopia', 'Laes', 'Leemes', 'Lemetti', 'Martti', 'Matti', 'Mielitty', 'Mikko', 'Miku', 'Neko', 'Nestor', 'Nikke', 'Niko', 'Niilo', 'Nousia', 'Nyri', 'Nyyrikki', 'Ohvana', 'Ohto', 'Oleksi', 'Olesa', 'Olli', 'Osmo', 'Pekka', 'Peko', 'Pellervo', 'Pertteli', 'Pertti', 'Petru', 'Puavo', 'Päiviö', 'Rautia', 'Reko', 'Rikori', 'Ruuri', 'Ruurikki', 'Sami', 'Sampsa', 'Seppo', 'Sämpsä', 'Tapio', 'Tauno', 'Teppo', 'Tepu', 'Teuri', 'Tiera', 'Timo', 'Tommi', 'Tornia', 'Tuomas', 'Untamo', 'Unto', 'Vetka', 'Vilja', 'Väinämö', 'Väinö', 'Väiski', 'Yrjö', 'Yrkki'], 'f': ['Aino', 'Anja', 'Anna', 'Annikki', 'Anu', 'Arhippa', 'Arho', 'Aune', 'Asta', 'Elina', 'Heli', 'Hellu', 'Helna', 'Helka', 'Heta', 'Hetta', 'Hetti', 'Hintriikka', 'Ieva', 'Ilpotar', 'Kati', 'Katja', 'Katuska', 'Kyllikki', 'Leena', 'Liena', 'Liina', 'Maija', 'Marja', 'Marjatta', 'Marjukka', 'Marketta', 'Matju', 'Mauru', 'Mielikki', 'Mielus', 'Nastasja', 'Niina', 'Outi', 'Raisa', 'Rauni', 'Salme', 'Senja', 'Senni', 'Talvikki', 'Tellervo', 'Terho', 'Tuulikki', 'Ulla', 'Varpuli', 'Veera', 'Veeruska', 'Vellamo']}, 'w': {'m': ['Aake', 'Aarne', 'Aarno', 'Aaro', 'Ahti', 'Akseli', 'Aleksi', 'Ano', 'Anselmi', 'Anskar', 'Anssi', 'Ari', 'Arkko', 'Antton', 'Armas', 'Eerik', 'Eerikki', 'Eero', 'Erkki', 'Esko', 'Hakon', 'Hannu', 'Hannus', 'Harri', 'Harttu', 'Heino', 'Hemmo', 'Henrik', 'Iiro', 'Ilkka', 'Jaakko', 'Jani', 'Janne', 'Jere', 'Kalle', 'Kaumieli', 'Kaulempi', 'Kauppo', 'Kari', 'Keiho', 'Ketteli', 'Knuutti', 'Klavus', 'Kurtti', 'Kustaa', 'Kustavi', 'Kyösti', 'Laaku', 'Lalli', 'Lasse', 'Lassi', 'Lauri', 'Mauno', 'Maunu', 'Mielo', 'Mikko', 'Nousia', 'Ohto', 'Ohtoi', 'Olaus', 'Olavi', 'Olli', 'Oskari', 'Paavo', 'Panu', 'Pasi', 'Pentti', 'Petrus', 'Pieti', 'Pietu', 'Pohto', 'Pertti', 'Perttuli', 'Pärttyli', 'Ragwald', 'Reko', 'Saku', 'Santeri', 'Santtu', 'Simo', 'Soini', 'Stig', 'Teppo', 'Timo', 'Tord', 'Torkel', 'Tuukka', 'Turkka', 'Turo', 'Uolevi', 'Uoti', 'Urmas', 'Utria', 'Vesa', 'Vilhelmi', 'Vilho', 'Ville', 'Vorna', 'Väinämö', 'Väinö', 'Väiski', 'Wilhelm'], 'f': ['Alina', 'Alli', 'Alma', 'Anna', 'Annikki', 'Asta', 'Aune', 'Auni', 'Eeva', 'Eivor', 'Ella', 'Elli', 'Elenora', 'Elina', 'Elsa', 'Elsi', 'Emma', 'Heta', 'Hetta', 'Hetti', 'Helena', 'Heli', 'Helvi', 'Helviiki', 'Henna', 'Henni', 'Hilta', 'Hiltu', 'Iisa', 'Inka', 'Inkeri', 'Kaarina', 'Kaija', 'Kerttu', 'Kyllikki', 'Liina', 'Liinu', 'Liisa', 'Liisi', 'Liisu', 'Linta', 'Lissa', 'Lissu', 'Lyyli', 'Lyylia', 'Lyylikki', 'Maija', 'Mari', 'Nelli', 'Noora', 'Priska', 'Rauni', 'Riika', 'Riikku', 'Terhi', 'Terhikki', 'Tuire', 'Venla']}, 'n': {'m': ['Ahtia', 'Aimo', 'Antti', 'Arijoutsi', 'Aslak', 'Jonne', 'Joukamoinen', 'Joukonen', 'Jouna', 'Jouni', 'Jussa', 'Jussi', 'Lauri', 'Laurukainen', 'Lemminkäinen', 'Lemmitty', 'Lemmäs', 'Niila', 'Nilla', 'Nils', 'Peivas', 'Wimme'], 'f': ['Aila', 'Aili', 'Alie', 'Ailitza', 'Beerit', 'Laila', 'Maaret', 'Maarit', 'Ouna', 'Ravdna', 'Ulla']}}


def searchdict(string,dict):
	matches = []
	for region in dict:
		for gender in dict[region]:
			for item in dict[region][gender]:
				if re.search(string,item):
					matches.extend([(item + ' (' + region + ' ' + gender + ')')])
	if len(matches) > 0:
		print(random.choice(matches))
	else:
		print('Nothing!')

def again():
        yes = input("Again? y/n ")
        if yes == "y":
                print("\n\n\n")
                mainloop()

def mainloop():
	letter = input('Give me a letter: ').upper()
	searchdict(letter,names)
	again()

mainloop()

#789 north, 023 east, 1456 west
# names['e']['m']