# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:44:47 2020

@author: Rafa
"""


import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import scipy.stats as st


sb.set()


 # loc='média', scale='desvio padrão'

def f(x):
    return 0.3*st.norm.pdf(x, loc=3, scale=1) + 0.7*st.norm.pdf(x, loc=8, scale=2)
def g(x):
    return st.norm.pdf(x, loc=6, scale=np.sqrt(10))

x = np.arange(-100, 100)


M = max(f(x) / g(x))


def amostra_rej(n=1000):
    
    amostras = []
    for j in range(n):
        u = np.random.uniform(0, 1)
        z = np.random.normal(6, np.sqrt(10))
        

        if u < f(z)/(M*g(z)):
            amostras.append(z)

    return np.array(amostras)

A = amostra_rej(n=100000)

sb.distplot(A)