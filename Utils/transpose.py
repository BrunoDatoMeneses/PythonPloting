from csv import reader, writer
import os

def transposeFiles():


    for root, dirs, files in os.walk("Files"):
        for filename in files:
            print(filename)
            with open("Files/"+filename) as f, open("TFiles/T_"+filename, 'w') as fw:
                writer(fw, delimiter=';').writerows(zip(*reader(f, delimiter=';')))

def rename():

    for file in os.listdir("Files"):
        print(file)
        print(file[12:])
        os.rename(file, file[12:])



