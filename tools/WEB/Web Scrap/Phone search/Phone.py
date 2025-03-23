import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import sys
path=r'D:\Google Drive\Obsidian\Python\My_codes\My_module'
sys.path.append(path)
import fonctions as fct
from tabulate import tabulate


from bs4 import BeautifulSoup as bst
import re
import requests

def get_data(url,lst_critere):
    result = requests.get(url).text
    doc = bst(result, "html.parser")

    price = [str(doc.find(class_="prices-list__price-value").contents)[4:-4].strip()[0:3]]
    name = doc.find('h1').contents
    
    lst = []
    data = []

    for i in doc.find_all("div",class_='pl-5 pr-5') :
        lst.append(i.text.replace('\n','').replace('Ã©','e').replace('Ã¨','e').replace('Ã\x89','e').replace('é','e').replace('è','e').strip())
    
    for i in lst_critere:
        try : 
            print('Je trouve ',i,'qui vaut ',lst[lst.index(i)+1])
            data.append(lst[lst.index(i)+1])
        except : 
            print('problème avec : ',i)
            data.append(np.nan)
    Headers = lst_critere
    # Data = [str(lst[i].contents)[4:-4].strip() for i in range(0,len(lst)) if i %2 == 1]
    return(name + price + data)


directory = r"D:\Google Drive\Obsidian\Python\My_codes\Projets\WebScrap\link_list.txt"
criteres = r"D:\Google Drive\Obsidian\Python\My_codes\Projets\WebScrap\Critère.txt"
url = "https://www.frandroid.com/produits/oneplus/smartphones/1338583-oneplus-nord-2t#product-prices"
data=[]
errors=[]
links = [line.strip() for line in open(directory)]
lst_critere = [line.strip() for line in open(criteres)]

#%%

head = ['Nom', "Prix"] + lst_critere

for i in links:
    try : data.append(get_data(i,lst_critere))
    except: errors.append(i)

if len(errors) != 0 : print("\nListe d'erreurs : \n",errors)
df = pd.DataFrame(data, columns=head)

#%%
fct.analyse_df(df)
# print('\nAperçu : ')
# print(tabulate(df.head(), headers=df.columns,tablefmt="github"))

with open(r"D:\Google Drive\Obsidian\Python\My_codes\Projets\WebScrap\results.txt",'w') as f:
    f.write(tabulate(df, headers=head, tablefmt="github"))
try : df.to_csv(r"D:\Google Drive\Obsidian\Python\My_codes\Projets\WebScrap\results.csv", sep=';')
except : print("impossible d'écrire sur csv, fichier ouvert")

#%% One

# url = "https://www.frandroid.com/produits/oneplus/smartphones/1338583-oneplus-nord-2t#product-prices"
# url = "https://www.frandroid.com/produits/xiaomi/smartphones/1376569-xiaomi-poco-f4"
# url = "https://www.frandroid.com/produits/nokia/smartphones/1537490-nokia-g60"

# result = requests.get(url).text
# doc = bst(result, "html.parser")

# name = doc.find('h1').text
# price = str(doc.find(class_="prices-list__price-value").contents)[4:-4].strip()[0:3]
# ''.join(doc.find('div', text=re.compile('aille')).parent.text.split()[1:])

# Headers = [str(lst[i].contents)[4:-4].strip() for i in range(0,len(lst)) if i %2 ==0]
# print(len(Headers))
# head = ['Name', 'Price'] + Headers
