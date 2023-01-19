#!/usr/bin/env python3

from pprint import pprint
from pyscbwrapper import SCB
import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()

# Konfigurering 2000-2021
years = range(2000, 1 + 2021, 1)
scb = SCB('sv', 'BE', 'BE0101', 'BE0101I', 'Dodstal')

def get_mortality_data(agegroup):
    # Hämta mortalitet från SCB
    scb.set_query(ålder=agegroup, år=[str(x) for x in years])
    raw_data = scb.get_data()

    # Extrahera data
    mortalitet = [float(x['values'][0]) for x in raw_data['data']]

    # Sortera efter mortalitet
    return [x for x in zip(years, mortalitet)]


def generate_barchart(data):
    dataSorted = sorted(data, key=lambda t: t[1])

    ## Konfigurera bild
    objects = [t[0] for t in dataSorted]
    y_pos = np.arange(len(objects))
    performance = [t[1] for t in dataSorted]
    colors = ['r' if x in [2020, 2021] else 'b' for x in objects]

    # Generera bild
    plt.bar(y_pos, performance, align='center', alpha=0.5, color=colors)
    plt.xticks(y_pos, objects, rotation='vertical')
    plt.ylabel('Mortality')
    plt.title(
        f"Dödsfall/1000/år (mortality) mellan {years[0]}-{years[-1]} (Källa SCB)"
    )
    plt.show()


def get_agegroups():
    return scb.get_variables()['ålder']


generate_barchart(get_mortality_data('samtliga åldrar'))
