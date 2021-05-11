import random

random.seed()

list = [0]

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

    print("Du slog en sexa, omslag!")
    första = (random.randint(1, 6))
    andra = (random.randint(1, 6))

    if första == 6:
        print("a " + str(första))
        en_del_av_obT6()

    else:
        list.append(första)
        print(str(första))

    if andra == 6:
        print("b " + str(andra))
        en_del_av_obT6()
        
    else: 
        list.append(andra)
        print(str(andra))
        
    if första != 6 and andra != 6:
    
        numbers_sum = sum(list)
        print(str(numbers_sum) + " är din totala summa")

def obT6_function():

    ursprunglig = (random.randint(6, 6))

    if ursprunglig == 6:
        en_del_av_obT6()

    else:
        print("Du slog en " + str(ursprunglig) + "a")

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

obT6_function()