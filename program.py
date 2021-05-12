import random

random.seed()

list = [0]
list_obT6 = [0]
list_T6 = [0]
list_T20 = [0]

def smidighet_function():

    f = open("stats.txt", "rt") #öppnar filen och läser ifrån den

    smidighet = "Smidighet:" #Bestämmer strängen som ska sökas efter

    for line in f:

        if smidighet in line: # Checkar om den hittar str och isf printar linjen med str i.

            print(line[11:13]) # ser till så koden bara printar en viss del av line

    f.close()

def styrka_function():

    f = open("stats.txt", "rt")

    styrka = "Styrka:"

    for line in f:

        if styrka in line:

            print(line[8:10])

    f.close()

def intelligens_function():

    f = open("stats.txt", "rt")

    intelligens = "Intelligens:"

    for line in f:

        if intelligens in line:

            print(line[13:15])

    f.close()

def karisma_function():

    f = open("stats.txt", "rt")

    karisma = "Karisma:"

    for line in f:

        if karisma in line:

            print(line[9:11])

    f.close()

def egenskapskoll_function():
    
    egenskap = input("Vilket värde vill du ha reda på?") #Frågar användaren efter vilket värde de vill ta reda på

    felmeddelande1 = "Du har inte angivit en korrekt egenskap." #Felmeddelande som visas om man anger en felaktig egenskap

    grundvärden = ["1"] #Det jag gjorde fel fungerar när jag gör såhär så då gör vi såhär

    for raw_input in grundvärden: #Denna for loop körs för att först se om Karisma, Styrka, Intelligens, eller Smidighet är angivna, för att sedan köra en av föregående funktioner
        if egenskap == "Karisma":
            karisma_function()
        elif egenskap == "Styrka":
            styrka_function()
        elif egenskap == "Intelligens": #Jag använder if else och else if satser då jag inte har så många värden att gå igenom innan jag kommer hitta till rätt plats i loopen
            intelligens_function()
        elif egenskap == "Smidighet":
            smidighet_function()
        else:
            print(felmeddelande1) #Om ditt angivna värde inte matchar något av de värdena som är angivna så visas ett felmeddelande

def sla_sexsidig_tarning_tioggr():

    i = 0
    while i < 10:
        print(random.randint(1, 6))
        i += 1

def t6_function():

    print(random.randint(1, 6)) #Slår en tärning som ger mig ett värde mellan 1 och 6

def t20_function():

    print(random.randint(1, 20)) #Slår en tärning som ger mig ett värde mellan 1 och 20

def smyga_function():

    f = open("stats.txt", "rt")

    text = "Du slog: "

    smidighet = "Smidighet:"

    for line in f:

        if smidighet in line:

            dex = int(line[11:13])
            
            val = int(random.randint(1, 20))

            if val == 1:
                print(text + str(val) + " , perfekt!")
            
            elif val <= dex:
                print(text + str(val) + ", du lyckades!")

            elif val == 20:
                print(text + str(val) + ", fummel!")

            elif val > dex:
                print(text + str(val) + ", du misslyckades!")

            else:
                print("vad är problemet")

    f.close()

def getskill_function():

    angivet = input("Vilken egenskap vill du se?")

    thisdict = {
    "Smyga": "13",
    "Fäktas": "17",
    "Dyrka lås": "16"
    }

    print(thisdict[angivet])

def en_del_av_obT6():

    första = (random.randint(1, 6))
    andra = (random.randint(1, 6))

    if första == 6 and andra == 6: #Om BÅDA är sexor, high roller liksom, då ska funktionen köras två gånger
        print("a " + str(första))
        print("b " + str(första))
        en_del_av_obT6()
        en_del_av_obT6()

    elif första == 6: #Om FÖRSTA är en sexa så körs den en gång
        print("Sexa!")
        en_del_av_obT6()
    
    else: #Annars appendar man till listan o kör vidare med slag 2
        list.append(första)
        print(str(första))

    if andra == 6: #SLAG TVÅ DAMER OCH HERRAR (Herrar eftersom bara Björn läser).
        print("Sexa!") #Nu är alltså det ANDRA slaget en sexa. Samma visa som förra gången more or less
        en_del_av_obT6()
        
    else: #Lite lose att inte slå en sexa så då bara appendar man, o visan är över för denna gång om ingen sexa slagits
        list.append(andra)
        print(str(andra))

def obT6_function():

    ursprunglig = (random.randint(6, 6)) #Står just nu så att det första slaget ALLTID är en sexa för att testa så att hela funktionen kommer fungera

    if ursprunglig == 6:
        print("Du slog en sexa!")
        en_del_av_obT6()
        numbers_sum = sum(list)
        print(str(numbers_sum) + " är din totala summa") #Denna körs när hela obt6 grejen innan körts, och printar ut den sammanlagda summan

    else:
        print("Du slog en " + str(ursprunglig) + "a") #Riktigt lose att inte ens slå EN sexa på första slaget

def startfunktion():
    
    angivet = input("Vad vill du göra?")

    felmeddelande2 = "Du har inte angivit en korrekt handling."

    alternativ = ["1"]

    for raw_input in alternativ:
        if angivet == "Se egenskaper":
            egenskapskoll_function()
        elif angivet == "Slå sexsidig tärning":
            t6_function()
        elif angivet == "Slå tjugosidig tärning":
            t20_function()
        elif angivet == "obT6":
            obT6_function()
        elif angivet == "Smyga":
            smyga_function()
        elif angivet == "Getskill":
            getskill_function()
        else:
            print(felmeddelande2) #Ungefär samma funktion som tidigare, som kör en av de andra funktionerna jag skapat. Det fungerar och det finns struktur. Jag nöjd.

#startfunktion() #Kör startfunktion som sedan kör en annan funktion.

obT6_function() #Kört endast denna nu för att testa min obT6 funktion