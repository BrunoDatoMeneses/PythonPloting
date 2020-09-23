import csv

with open('fichier.csv') as csvfile:
    csv_reader  = csv.DictReader(csvfile, delimiter=';', )
    for row in csv_reader :
        print(row["Davide1"])
        #print(', '.join(row))

