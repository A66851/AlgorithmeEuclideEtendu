# -*- coding: utf-8 -*-
"""
@author: hbouia (Created on Sun Nov 19 11:05:51 2017)
Algoritme d'Euclide étendu
Sitographie : https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide_%C3%A9tendu
"""
def igcd(a,b):
    # Initialisation
    d,u,v,d1,u1,v1=a,1,0,b,0,1
    # Calcul
    while d1!=0:
        q=d//d1
        d,u,v,d1,u1,v1=d1,u1,v1,d-q*d1,u-q*u1,v-q*v1
    return (d,u,v)

a, b = 488456,18546
a, b = 4445847,64545454
a, b = 52, 36
d,u,v=igcd(a,b)
print('pgcd(%d,%d) = %d' % (a, b, d))
print('(%d)*%d + (%d)*%d = %d' %(u, a, v, b, d))

# Exemple :
# pgcd(488456,18546) = 2
# (-317)*488456 + (8349)*18546 = 2