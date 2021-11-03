import time
import sys

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]

required = ("\n Gebruik alleen A, B, C of D \n")


def begin():
    print("Er breekt oorlog uit in Syrie, wat ga je doen?")
    print("A | Je blijft in het land.")
    print("B | Je bent dood omdat je huis gebombardeerd werd.")
    print("C | Je gaat uit het land vluchten.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_mening()
    if choice in answer_B:
        option_niks()
    if choice in answer_C:
        option_verzet()
    else:
        print(required)
        begin()


def option_mening():
    print("Je blijft in het land, wat ga je doen?")
    print("A | Je overleeft en wacht to de oorlog over is.")
    print("B | Je gaat dood een bombardement.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_vluchten()
    if choice in answer_B:
        print("Je bent overleden.")
        sys.exit()
    else:
        print(required)
        option_mening()


def option_vluchten():
    print("Je hebt gekozen om te overleven en te wachten to de oorlog over is, hoe gaat je dat doen?.")
    print("A | Je begint een boederij ver weg van de oorlog.")
    print("B | Je leeft in armoede.")
    print("C | Je vlucht weg.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_paspoortlibanon()
    if choice in answer_B:
        option_paspoortcyprus()
    if choice in answer_C:
        option_paspoortturkije()
    else:
        print(required)
        option_vluchten()


def option_paspoortlibanon():
    print("Om ver weg te komen heb je een auto nodig, Heb je een auto?")
    print("A | Ja")
    print("B | Nee")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_paspoortmeelibanon()
    if choice in answer_B:
        print("Je hebt geen auto, De oorlog komt dichter en dichter bij, na een 2 dagen is de oorlog bij, je wordt doodgeschoten.")
        sys.exit()
    else:
        print(required)
        option_paspoortlibanon()


def option_paspoortmeelibanon():
    print("Je hebt je auto bij je en je bent ver weg van de oorlog gekomen. Je begint je eigen boerderij.")
    time.sleep(1)
    print("Na 2 jaar lang geen last te hebben van de oorlog, word je opgepakt door de terroristen. Je moet 5 jaar de gevangenis in.")
    time.sleep(10)
    print("Je bent uit de gevangenis gekomen, en je gaat naar nederland om daar te gaan werken en een nieuw leven te beginnen.")
    print("Je moet een beroep kiezen voor je toekomst in Nederland.")
    print("A | Tandarts")
    print("B | Supermarkt Manager")
    print("C | Bouwvakker")
    print("D | Software Developer")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Gefeliciteerd! Je bent tandarts geworden.")
        time.sleep(1)
        print("Je gaat wonen in een gigantisch huis en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_B:
        print("Gefeliciteerd! Je bent supermarkt manager geworden.")
        time.sleep(1)
        print("Je gaat wonen in een flat en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_C:
        print("Gefeliciteerd! Je bent bouwvakker geworden.")
        time.sleep(1)
        print("Je komt te overlijden door een bedrijfsongeval.")
        sys.exit()
    if choice in answer_D:
        print("Gefeliciteerd! Je bent software developer geworden.")
        time.sleep(1)
        print("Je gaat wonen in een mooie villa en je leeft lang en gelukkig.")
        sys.exit()
    else:
        print(required)
        option_paspoortmeelibanon()


def option_niks():
    print("Je ziet dat mensen in je omgeving in het land blijven, Wat ga jij doen?")
    print("A | Je gaat dood voordat je weet wat je gaat doen.")
    print("B | Je blijft in het land.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Je gaat dood voordat weet wat je gaat doen")
        sys.exit()
    if choice in answer_B:
        option_vluchten()
    else:
        print(required)
        option_niks()


def option_verzet():
    print("Je hebt besloten om te blijven in het land. De terroristen willen je dood hebben, wat doe je?")
    print("A | Je geeft je over.")
    print("B | Je blijft in het land.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Je hebt er voor gekozen om jezelf over te geven aan de terrosisten. De terroisten heeft je gevangen genomen en gemarteld. Je bent overleden.")
        sys.exit()
    if choice in answer_B:
        option_vluchten()
    else:
        print(required)
        option_verzet()


def option_paspoortcyprus():
    print("Om in het land te blijven heb je een auto nodig zodat je ver van de oorlog kan komen maar wel nog in het land blijft, heb je een auto?")
    print("A | Ja")
    print("B | Nee")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_paspoortmeecyprus()
    if choice in answer_B:
        print("Je hebt geen auto, de terroristen vermoorden je.")
        sys.exit()
    else:
        print(required)
        option_paspoortcyprus()


def option_paspoortmeecyprus():
    print("Je moet ver weg van de oorlog rijden.")
    print("Kies A of B")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_veilignederland()
    if choice in answer_B:
        print("Je auto gaat onderweg kapot, je bent in de middel of no where. Je hebt geen eten en water. Je gaat dood.")
        sys.exit()
    else:
        print(required)
        option_paspoortmeecyprus()


def option_veilignederland():
    print("Je bent veilig aangekomen in een andere stad van het land.")
    time.sleep(1)
    print("Je bent veilig aangekomen in de stad, nu is het tijd om een beroep te kiezen.")
    print("A | Tandarts")
    print("B | Supermarkt Manager")
    print("C | Bouwvakker")
    print("D | Software Developer")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Gefeliciteerd! Je bent tandarts geworden.")
        time.sleep(1)
        print("Je gaat wonen in een gigantisch huis en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_B:
        print("Gefeliciteerd! Je bent supermarkt manager geworden.")
        time.sleep(1)
        print("Je gaat wonen in een flat en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_C:
        print("Gefeliciteerd! Je bent bouwvakker geworden.")
        time.sleep(1)
        print("Je komt te overlijden door een bedrijfsongeval.")
        sys.exit()
    if choice in answer_D:
        print("Gefeliciteerd! Je bent software developer geworden.")
        time.sleep(1)
        print("Je gaat wonen in een mooie villa en je leeft lang en gelukkig.")
        sys.exit()
    else:
        print(required)
        option_veilignederland()


def option_paspoortturkije():
    print("om te blijven in het land heb een auto nodig. Heb je die?")
    print("A | Ja")
    print("B | Nee")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_paspoortmeeturkije()
    if choice in answer_B:
        print("Je hebt geen auto. Je wordt vermoord door de terroristen.")
        sys.exit()
    else:
        print(required)
        option_paspoortturkije()


def option_paspoortmeeturkije():
    print("Je bent nu al 2 jaar in het land maar je wil iets anders, je gaat naar Nederland..")
    time.sleep(1)
    print("Je bent veilig aangekomen in Nederland. Je krijgt een verblijfsvergunning, nu is het tijd om een beroep te kiezen.")
    print("A | Tandarts")
    print("B | Supermarkt Manager")
    print("C | Bouwvakker")
    print("D | Software Developer")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Gefeliciteerd! Je bent tandarts geworden.")
        time.sleep(1)
        print("Je gaat wonen in een gigantisch huis en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_B:
        print("Gefeliciteerd! Je bent supermarkt manager geworden.")
        time.sleep(1)
        print("Je gaat wonen in een flat en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_C:
        print("Gefeliciteerd! Je bent bouwvakker geworden.")
        time.sleep(1)
        print("Je komt te overlijden door een bedrijfsongeval.")
        sys.exit()
    if choice in answer_D:
        print("Gefeliciteerd! Je bent software developer geworden.")
        time.sleep(1)
        print("Je gaat wonen in een mooie villa en je leeft lang en gelukkig.")
        sys.exit()
    else:
        print(required)
        option_paspoortturkije()


begin()