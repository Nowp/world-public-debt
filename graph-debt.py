import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib as mpl

fig, ax = plt.subplots()

def read_data(path):
    with open(path, encoding='utf8') as file:
        return pd.read_csv(file, sep=';')

def add_country(chosen_country, years, countries):
    country = countries[chosen_country].to_numpy().astype(np.float32)
    line, = ax.plot(years[start_index:fin_index], country[start_index:fin_index])
    line.set_label(chosen_country)
    ax.legend()

df = read_data("data/public-debt-data.csv")
df['Country'] = df['Country'].str.lower()

years = np.array(df.columns[1:]).astype(np.int32)

first_date = years[0]

countries = df.set_index('Country').T

start_index = int(input("Date de début: ") or "1950") - first_date
fin_index = int(input("Date de fin: ")or "2022") - first_date

chosen_country = input("Entrer le pays: ").strip()
while chosen_country != '':
    add_country(chosen_country, years, countries)
    chosen_country = input("Entrer le pays: ").strip()

plt.show()