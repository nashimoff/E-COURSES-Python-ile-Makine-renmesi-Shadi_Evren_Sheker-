# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

# ders 6 : kutuphanelerin yuklenmesi
#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# kod bolumu
# veri yukleme

veriler = pd.read_csv('veriler.csv')
#pd.read_csv("veriler.csv")

print(veriler)

#veri on isleme
boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy','kilo']]
print(boykilo)

x = 10

class insan:
    boy = 180
    def kosmak(self,b):
        return b + 10
    
ali = insan()
print(ali.boy)
print(ali.kosmak(90))
