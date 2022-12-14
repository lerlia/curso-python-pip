import utils
import read_csv
import chart
import pandas as pd

def run():
    '''
    data = list(filter(lambda item : item["Continent"] == "South America", data))
    countries = list(map(lambda x: x["Country/Territory"], data))
    percentages = list(map(lambda x: x["World Population Percentage"], data))
    '''
    
    df = pd.read_csv("data.csv")
    df = df[df["Continent"] == "Africa"]

    countries = df["Country/Territory"]
    percentages = df["World Population Percentage"]
    chart.generate_pie_chart(countries, percentages)
    
    data = read_csv.read_csv("data.csv")
    country = input("Ingrese un país: ")
    print(country)

    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        chart.generate_bar_chart(country["Country/Territory"], labels, values)

if __name__ == "__main__":
    run()


