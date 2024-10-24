import pandas as pd
import csv
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

x = 1

# read specific columns of csv file using Pandas
df = pd.read_csv("g4g.csv", sep=",",header=0, skipinitialspace=True,encoding='utf-8', engine='python',usecols=["dodavatel_ICO"])
df_filtered = df[df['dodavatel_ICO'] != '~']
df = df_filtered
df = df.dropna()
df['dodavatel_ICO'] = df['dodavatel_ICO'].str.replace('~', '', regex=True)
df = df.drop_duplicates()
#print(df)

################################
csv_file = open('test.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['udaje'])
#################################

ser = Service(executable_path="D:\webdrivers\geckodriver")

driver = webdriver.Firefox(service=ser)


driver.get("https://www.orsr.sk/search_ico.asp")
myPageTitle = driver.title
#print(myPageTitle)
#df.info()
#z = df['dodavatel_ICO'].values.tolist()
print(df)
for row in df.iterrows():
    
    elementICO = driver.find_element(By.NAME, "ICO")
    
    elementICO.send_keys(df[row])
    print(df[row])
    try:
        elementHLADAT = driver.find_element(By.XPATH, "//input[@title='Vyhľadávanie podľa zadaných kritérií']")
        elementHLADAT.click()
        #print("elementHLADAT")

        elementSUBJEKT = driver.find_element(By.XPATH, "//a[@title='Aktuálny výpis']")
        elementSUBJEKT.click()
        #print("elementSUBJEKT")

        #######################
        try:
        
            elementAKTUALNE = driver.find_element(By.CLASS_NAME, "wrn2")
            elementAKTUALNE.click()
        #print("elementAKTUALNE")
   
    
            elementOSOBY = driver.find_element(By.XPATH, "//*[text()='Štatutárny orgán:\u00a0']/parent::td/following-sibling::td").text
            print(elementOSOBY)
            csv_writer.writerow([elementOSOBY])
            #MENO = elementOSOBY.find_element(By.XPATH, ".//span[1]").text
            #PRIEZVISKO = elementOSOBY.find_element(By.XPATH, ".//span[2]").text
            
            #print(MENO)
            #print(PRIEZVISKO)
            

        except NoSuchElementException:
            x = x+1
        #######################

        elementOSOBY = driver.find_element(By.XPATH, "//*[text()='Štatutárny orgán:\u00a0']/parent::td/following-sibling::td").text
        print(elementOSOBY)
        #MENO = elementOSOBY.find_element(By.XPATH, ".//span[1]").text
        #PRIEZVISKO = elementOSOBY.find_element(By.XPATH, ".//span[2]").text
        
        #print(MENO)
        #print(PRIEZVISKO)
        csv_writer.writerow([elementOSOBY])
        vysledok = []
        meno = []

        #vysledok.append(data[0])

        for x in range(2,len(elementOSOBY),6):

            meno.append(elementOSOBY[0])

            if elementOSOBY[x].find('predseda') > -1:
                elementOSOBY[x] = elementOSOBY[x].replace('- predseda','')
                meno.append('predseda')
                meno.append(elementOSOBY[x])
                
            elif elementOSOBY[x].find('člen') > -1:
                elementOSOBY[x] = elementOSOBY[x].replace('- člen','')
                meno.append('člen')
                meno.append(elementOSOBY[x])

            else: 
                #vysledok.append(elementOSOBY[x])
                meno.append(elementOSOBY[x])
            meno.append(values)
            vysledok.append(meno)
            meno = []
    #####################################################################
    except NoSuchElementException:
        x = x+1
    
    #for udaje in elementOSOBY:
    

    driver.get("https://www.orsr.sk/search_ico.asp")
    

csv_file.close()
driver.quit()


#1click##<input type="text" name="ICO" size="28" style="width:250px;" maxlength="10" class="inp" title="Sem zadajte celé identifikačné číslo subjektu. Aplikácia ignoruje všetky znaky okrem cifier. To umožňuje zadávať čísla IČO aj s medzerami kvôli lepšej čitateľnosti a kontrole.">
#2click##<input type="submit" value=" Hľadaj " title="Vyhľadávanie podľa zadaných kritérií" class="but">
#3click##<a href="vypis.asp?ID=4670&amp;SID=4&amp;P=0" class="link" alt="Aktuálny výpis" title="Aktuálny výpis">Mestské lesy Košice a.s.</a>
#4click##<a href="vypis.asp?ID=46586&amp;SID=4&amp;P=0" class="link">
#5výpis##<span class="tl">Štatutárny orgán:&nbsp;</span>
#<span class="ra">  predstavenstvo </span>

