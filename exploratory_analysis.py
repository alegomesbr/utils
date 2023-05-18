import pandas as pd
import seaborn as sns
#import matplotlib.pyplot as plt

pessoas = ["pessoa1", "pessoa2", "pessoa3", "pessoa4", "pessoa5", "pessoa6", "pessoa7", "pessoa8", "pessoa9"]
idades = [15, 20, 33, 47, 51, 51, 63, 70, 83]

mydf = pd.DataFrame({'Pessoas': pessoas, 'Idade': idades})

def exploratory_metrics():
    # media
    print("Média: {}".format(mydf["Idade"].mean()))
    # mediana
    print("Mediana: {}".format(mydf["Idade"].median()))
    # moda
    print("Moda: {}".format(mydf["Idade"].mode()))
    # percentil
    print("Percentil: {}".format(mydf['Idade'].quantile(q=0.7)))
    # quartil (Q1 = 0.25, Q2 = 0.5, Q3 = 0.75)
    print("Quartil: {}".format(mydf['Idade'].quantile(q=0.25)))
    
    # Medidas de Dispersão: amplitude, variância, desvio padrão
    # amplitude
    print("Amplitude: {}".format(mydf["Idade"].max() - mydf["Idade"].min()))
    # variância
    print("Variância: {}".format(mydf["Idade"].var()))
    # desvio padrão
    print("Desvio Padrão: {}".format(mydf["Idade"].std()))


def plot_histogram():
    #sns.distplot(mydf["Idade"])
    sns.distplot(mydf["Idade"], bins=2)
    plt.show()

def plot_scatter():
    # diagrama de dispersao
    sns.scatterplot(x="Idade", y="Pessoas", data=mydf)
    plt.show()

def plot_boxplot():
    #sns.boxplot(x=mydf["Idade"], orient="h")
    sns.boxplot(x=mydf["Idade"], orient="v")
    plt.show()

def plot_lineplot():
    # line plot
    x = [1, 2, 3, 4, 5, 5, 6, 7, 8]
    y = [1, 1.5, 2.1, 1.7, 3.2, 2.9, 4.3, 5.2, 8]
    
    mydf2 = pd.DataFrame({'X': x, 'Y': y})
    
    sns.set_style("darkgrid")
    sns.lineplot(x="X", y="Y", data=mydf2, palette="tab10", linewidth=2.5)
    plt.show()
