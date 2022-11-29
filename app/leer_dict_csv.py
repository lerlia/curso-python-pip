import csv 
import matplotlib.pyplot as plt

#El nombre de la función debe ser igual al nombre del módulo para que permita leer el csv.
def leer_dict_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    data = []
    print("*****" * 9)
    print("*Country/Territory" + ":__________" + "2022 Population*")
    print("*****" * 9)
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      del country_dict["Rank"]
      del country_dict["CCA3"]
      del country_dict["Capital"]
      del country_dict["Continent"]
      del country_dict["Area (km²)"]
      del country_dict["Density (per km²)"]
      del country_dict["Growth Rate"]
      del country_dict["World Population Percentage"]
      data.append(country_dict)

      labels = country_dict.keys()
      values = country_dict.values()

      fix, ax = plt.subplots()
      ax.bar(labels, values)
      plt.savefig("country.png")
      plt.close()
      
      #labels = country_dict["Country/Territory"] + ":_____________" + country_dict["2022 Population"]
      #print(data)
      print(labels, values)
    return data
     
if __name__ == "__main__":
  data = leer_dict_csv("data.csv")
  #print(data[10])
  #print(data[0])

  
 