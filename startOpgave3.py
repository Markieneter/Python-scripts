# Iteratie opdracht
# Start script voor opgave over sikkelcel
# (c) Martijn van der Bruggen, 2007-2010
# Updates:
# November 2010, code bijgewerkt met instructies voor de opdracht
# Hogeschool van Arnhem en Nijmegen

# Sequenties voor respectievelijk sikkelcel- en normale cellen
# Bekend is dat het gen coderend voor hemoglobine bij sikkelcel aandoening een andere nucleotide heeft
# De sequentie voor de sikkelcel en een "normale bloedcel" zijn hier onder gegeven
sikkel_seq = 'GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'
normaal_seq ='GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'

# In het bestand enzymen. txt staan kandidaat restrictie enzymen
# Opdracht schrijf een programma dat al deze enzymen doorloopt een suggestie
# geeft welk restrictie enzym welk knipt in de ene sequentie en niet in de andere sequentie
# Hiermee kunnen we diagnostisch enzym voorstellen om vast te stellen of een persoon
# drager is van het sikkelcel allel
bestand = open ("enzymen.txt")


# Aanwijzingen voor het schrijven van je programma
# -------------------------------------------------------------
# Het lezen van een regel kan met bestand.readline()
# Lees door totdat je een lege regel aantreft
# Een regel bestaat uit twee stukken enzym en knipsequentie. Bijvoorbeeld: DdeI C^TGAG
# Het opsplitsen van een regel in twee stukken op de spatie kan middels: enzym, seq = regel.split()
# Door bovenstaande split verkrijg je twee variabelen enzym en seq, respectievelijk de naam van het enzym en de sequentie waar deze in knipt
# Verwijderen het dakje uit de seq met seq.replace("^","")
# --------------------------------------------------------------------

# Auteur: © Mark
# Datum: 42
# Functie: 42

# Hier begint de functie en word het bestand gelezen
def main():
    regel = bestand.readline()

# Een loop waarbij het bestand gesplits wordt.
    for regel in bestand:
        enzym, seq = regel.split()
        seq = seq.replace("^","")
        # Hier wordt de sequentie in een lijst gezet.
        list_seq = []
        list_seq.append(seq)
        #hier word de lijst in een loop gedaan en gekeken of het in de sequencie zit.
        for x in list_seq:
            print(x)
            if x in sikkel_seq:
                print("Deze enzym zit in de sikkel sequence")
            else:
                print("Deze enzym zit niet in de sikkel sequence")
            if x in  normaal_seq:
                print("Deze enzym zit in de normaal sequence")
            else:
                print("Deze enzym zit niet in de normaal sequence")
# hier eindigt de functie
main()
     
         




