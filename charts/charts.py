import matplotlib.pyplot as plt

def generate_pie_charts():
    labels = ["Primer Trimestre", "Segundo Trimestre", "Tercer Trimestre"]
    values = [345, 234, 989]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()

