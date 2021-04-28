import random

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

    grundvärden = ["Smidighet, Styrka, Intelligens, Karisma"] #De fyra värden jag hittills angivit som riktiga finns här

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

random.seed()

#def sla_sexsidig_tarning_tioggr():
#
#    i = 0
#    while i < 10:
#        print(random.randint(1, 6))
#        i += 1

def t6_function():

    print(random.randint(1, 6))

def t20_function():

    print(random.randint(1, 20))

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
        else:
            print(felmeddelande2)

startfunktion()