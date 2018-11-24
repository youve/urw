#! /usr/bin/python
# -*- coding: utf-8 -*-

##############################
# Module: URW
# Date: 2012-07-16
# Version: 0.3
'''
Randomly generates a character for the game Unreal World
'''
##############################
# Log:
# 2012-07-17 added favourite weapon
# 2012-07-16 added region to settle in and an occupation (the main item this character will
#            produce for trading with NPCs (rain's ironworking and weaving mods are assumed)
#            monk is like hermit (doesn't trade) but additionally focuses heavily on rituals
# 2012-05-19 updated for version 3.14
# 2007-12-26 first version
##############################

import random
import readline

##############################
#Global Variables
##############################

culture = ["0) Kaumolainen", "1)Driikiläinen", "2) Kiesseläinen", "3) Reemiläinen", "4) Sartolainen", "5) Islander", "6) Koivulainen", "7) Kuikka-tribe", "8) Owl-tribe", "9) Seal-tribe"]

region = ["Kaumo", "Driik", "Kiesse", "Reemi", "Sarto", "Island Territory", "Koivula", "Kuikka", "Owl-tribe", "Seal-tribe", "Njerpez", "Starting region", "First island found", "First cave found", "First peninsula found"]

sex = ["Male", "Female"]

playmode = ['Custom', 'Custom - easy', 'Custom - too easy']

picture = ["Picture 1", "Picture 2", "Picture 3", "Picture 4", "Picture 5", "Picture 6"]

season = ["1) Spring", "2) Summer", "3) Autumn", "4) Winter"]

scenario = ["1) The village", "2) Runaway slave", "3) Unfortunate hunting trip", "4) Lonely settler", "5) Hurt, helpless, and afraid", "6) Traps and trapping", "7) I want to be a fisherman", "8) Abandoned trap-fence", "9) Abandoned camp", "10) Agriculture"]

course = ["2) Living in the Wild", "3) Advanced adventures"]

job = ["Farmer", "Cook", "Fisherman", "Carpenter", "Hideworker", "Tailor", "Smith", "Hermit", "Monk", "Weaver"]

weapon = ['dagger', 'sword', 'club', 'axe', 'flail', 'spear']

skills = ['agriculture', 'building', 'cookery', 'herblore', 'fishing', 'hideworking', 'ritual', 'timbercraft', 'physician', 'trapping', 'tracking', 'survival', 'weatherlore', 'carpentry', 'skiing', 'stealth', 'climbing', 'swimming', 'bow', 'dagger', 'sword', 'club', 'axe', 'spear']

def again():
        yes = input("Again? y/n ")
        if yes == "y":
                print("\n\n\n")
                mainloop()

def naming(c, s):
        if s == 'Female':
                if c[0] in ['7', '8', '9']:
                        namelist = ['Aila', 'Aili', 'Alie', 'Ailitza', 'Beerit', 'Laila', 'Maaret', 'Maarit', 'Ouna', 'Ravdna', 'Ulla']
                elif c[0] in ['0','2','3']:
                        namelist = ['Aino', 'Anja', 'Anna', 'Annikki', 'Anu', 'Arhippa', 'Arho', 'Aune', 'Asta', 'Elina', 'Heli', 'Hellu', 'Helna', 'Helka', 'Heta', 'Hetta', 'Hetti', 'Hintriikka', 'Ieva', 'Ilpotar', 'Kati', 'Katja', 'Katuska', 'Kyllikki', 'Leena', 'Liena', 'Liina', 'Maija', 'Marja', 'Marjatta', 'Marjukka', 'Marketta', 'Matju', 'Mauru', 'Mielikki', 'Mielus', 'Nastasja', 'Niina', 'Outi', 'Raisa', 'Rauni', 'Salme', 'Senja', 'Senni', 'Talvikki', 'Tellervo', 'Terho', 'Tuulikki', 'Ulla', 'Varpuli', 'Veera', 'Veeruska', 'Vellamo']
                else:
                        namelist = ['Alina', 'Alli', 'Alma', 'Anna', 'Annikki', 'Asta', 'Aune', 'Auni', 'Eeva', 'Eivor', 'Ella', 'Elli', 'Elenora', 'Elina', 'Elsa', 'Elsi', 'Emma', 'Heta', 'Hetta', 'Hetti', 'Helena', 'Heli', 'Helvi', 'Helviiki', 'Henna', 'Henni', 'Hilta', 'Hiltu', 'Iisa', 'Inka', 'Inkeri', 'Kaarina', 'Kaija', 'Kerttu', 'Kyllikki', 'Liina', 'Liinu', 'Liisa', 'Liisi', 'Liisu', 'Linta', 'Lissa', 'Lissu', 'Lyyli', 'Lyylia', 'Lyylikki', 'Maija', 'Mari', 'Nelli', 'Noora', 'Priska', 'Rauni', 'Riika', 'Riikku', 'Terhi', 'Terhikki', 'Tuire', 'Venla']
        else:
                if c[0] in ['7','8','9']:
                        namelist = ['Ahtia', 'Aimo', 'Antti', 'Arijoutsi', 'Aslak', 'Jonne', 'Joukamoinen', 'Joukonen', 'Jouna', 'Jouni', 'Jussa', 'Jussi', 'Lauri', 'Laurukainen', 'Lemminkäinen', 'Lemmitty', 'Lemmäs', 'Niila', 'Nilla', 'Nils', 'Peivas', 'Wimme']
                elif c[0] in ['0','2','3']:
                        namelist = ['Aarne', 'Aaro', 'Ahti', 'Ahto', 'Ahvo', 'Aimo', 'Aippo', 'Alvi', 'Anania', 'Antti', 'Antero', 'Ano', 'Arpia', 'Asko', 'Eero', 'Eikka', 'Erkki', 'Hannu', 'Harle', 'Harlu', 'Heikki', 'Heino', 'Herppa', 'Hirvo', 'Hyväneuvo', 'Ieri', 'Ierikka', 'Ikitiera', 'Iku', 'Ilari', 'Ilkka', 'Ilmari', 'Ilpo', 'Isto', 'Jeremia', 'Jerkko', 'Joukahainen', 'Joukavainen', 'Jouko', 'Jousia', 'Juha', 'Juhani', 'Jukka', 'Jurkka', 'Jussi', 'Jyri', 'Kaipia', 'Kalerva', 'Kalervo', 'Kaleva', 'Kalevi', 'Kalle', 'Kauko', 'Kimmo', 'Kolja', 'Kolkka', 'Konsta', 'Korjus', 'Kuisma', 'Kuopia', 'Laes', 'Leemes', 'Lemetti', 'Martti', 'Matti', 'Mielitty', 'Mikko', 'Miku', 'Neko', 'Nestor', 'Nikke', 'Niko', 'Niilo', 'Nousia', 'Nyri', 'Nyyrikki', 'Ohvana', 'Ohto', 'Oleksi', 'Olesa', 'Olli', 'Osmo', 'Pekka', 'Peko', 'Pellervo', 'Pertteli', 'Pertti', 'Petru', 'Puavo', 'Päiviö', 'Rautia', 'Reko', 'Rikori', 'Ruuri', 'Ruurikki', 'Sami', 'Sampsa', 'Seppo', 'Sämpsä', 'Tapio', 'Tauno', 'Teppo', 'Tepu', 'Teuri', 'Tiera', 'Timo', 'Tommi', 'Tornia', 'Tuomas', 'Untamo', 'Unto', 'Vetka', 'Vilja', 'Väinämö', 'Väinö', 'Väiski', 'Yrjö', 'Yrkki']
                else:
                        namelist = ['Aake', 'Aarne', 'Aarno', 'Aaro', 'Ahti', 'Akseli', 'Aleksi', 'Ano', 'Anselmi', 'Anskar', 'Anssi', 'Ari', 'Arkko', 'Antton', 'Armas', 'Eerik', 'Eerikki', 'Eero', 'Erkki', 'Esko', 'Hakon', 'Hannu', 'Hannus', 'Harri', 'Harttu', 'Heino', 'Hemmo', 'Henrik', 'Iiro', 'Ilkka', 'Jaakko', 'Jani', 'Janne', 'Jere', 'Kalle', 'Kaumieli', 'Kaulempi', 'Kauppo', 'Kari', 'Keiho', 'Ketteli', 'Knuutti', 'Klavus', 'Kurtti', 'Kustaa', 'Kustavi', 'Kyösti', 'Laaku', 'Lalli', 'Lasse', 'Lassi', 'Lauri', 'Mauno', 'Maunu', 'Mielo', 'Mikko', 'Nousia', 'Ohto', 'Ohtoi', 'Olaus', 'Olavi', 'Olli', 'Oskari', 'Paavo', 'Panu', 'Pasi', 'Pentti', 'Petrus', 'Pieti', 'Pietu', 'Pohto', 'Pertti', 'Perttuli', 'Pärttyli', 'Ragwald', 'Reko', 'Saku', 'Santeri', 'Santtu', 'Simo', 'Soini', 'Stig', 'Teppo', 'Timo', 'Tord', 'Torkel', 'Tuukka', 'Turkka', 'Turo', 'Uolevi', 'Uoti', 'Urmas', 'Utria', 'Vesa', 'Vilhelmi', 'Vilho', 'Ville', 'Vorna', 'Väinämö', 'Väinö', 'Väiski', 'Wilhelm']
        print(random.choice(namelist))

def mainloop():
        print('\n\n')
        print(random.choice(playmode))
        charculture = random.choice(culture)
        charsex = random.choice(sex)
        naming(charculture, charsex)
        print(charculture)
        print(charsex)
        print(random.choice(picture))
        print(random.choice(season))
        print(random.choice(scenario))
        print(random.choice(course))
        settle = random.choice(region)
        occupation = random.choice(job)
        weapons = random.choice(weapon)
        print('Settle in: ' + settle)
        print('Occupation: ' + occupation)
        print('Favourite weapon: ' + weapons)
        random.shuffle(skills)
        skillpreferences = ''
        for skill in skills:
            skillpreferences = skillpreferences + skill + " "
        print(skillpreferences)
        again()

mainloop()
