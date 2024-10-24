from itertools import groupby
import re

data = ['predstavenstvo', '  (od: 25.09.2001)', 'Ing. Pavol Butkovský - predseda', 'Nová 15', 'Banská Bystrica', 'Vznik funkcie: 19.07.1996', '', '  (od: 01.06.2004)', 'Ing. Jozef Machalík - člen', 'Poľná 19', 'Banská Bystrica', 'Vznik funkcie: 30.09.1996', '', '  (od: 01.06.2004)', 'Ing. Peter Poisel - člen', 'Lachova 13', 'Bratislava', 'Vznik funkcie: 25.09.2003', '', '  (od: 01.06.2004)']
#data = ['konateľ', '  (od: 13.10.2007)', 'Bc. Tomáš Lacko', 'Skladná 17/251', 'Košice - Juh 040 01', 'Vznik funkcie: 08.04.2010', '', '  (od: 23.04.2010)']
#data =['konatelia', '  (od: 25.06.1993)', 'Ing. Vladimír Urban', 'Starozagorská 43', 'Košice', 'Vznik funkcie: 25.06.1993', '', '  (od: 31.05.2005)', 'Antonia Urbanová', 'Starozagorská 43', 'Košice', 'Vznik funkcie: 05.01.1995', '', '  (od: 28.06.2017)']
#print(type(data[1]))

vysledok = []
meno = []



#vysledok.append(data[0])

for x in range(2,len(data),6):

    meno.append(data[0])

    if data[x].find('predseda') > -1:
        data[x] = data[x].replace('- predseda','')
        meno.append('predseda')
        meno.append(data[x])
        
    elif data[x].find('člen') > -1:
        data[x] = data[x].replace('- člen','')
        meno.append('člen')
        meno.append(data[x])

    else: 
        #vysledok.append(data[x])
        meno.append(data[x])
    
    vysledok.append(meno)
    meno = []


print(vysledok)
#print(meno)