import csv 

#El nombre de la función debe ser igual al nombre del módulo para que permita leer el csv.
def leer_csv(path):
  with open(path, 'r') as archivocsv:
    reader = csv.reader(archivocsv, delimiter=",")
    for row in reader:
      print("**********************" * 5)
      print(row)

if __name__ == "__main__":
  leer_csv("./app/data.csv")