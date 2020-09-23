from csv import reader, writer
import os

def transposeFiles():


    for root, dirs, files in os.walk("Files"):
        for filename in files:
            print(filename)
            with open("XP/"+filename) as f, open("TFiles/T_"+filename, 'w') as fw:
                writer(fw, delimiter=';').writerows(zip(*reader(f, delimiter=';')))

