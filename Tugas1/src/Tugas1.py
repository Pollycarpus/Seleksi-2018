import pandas as pd
import json
import urllib.request
from bs4 import BeautifulSoup as soup 

def writeToJSONFile(path, fileName, data):
    df = pd.io.json.json_normalize(data)
    out = df.to_json(orient='records')
    filePathNameWExt = path + '/' + fileName + '.json'
    #dirpath = 'D:/MyCodes/Python/DataScraping/Seleksi-2018/Tugas1/data/'+filePathNameWExt
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

    with open(filePathNameWExt, 'w') as f:
        f.write(out)
    

def addDentist(data, ID, dentist):
    for i in data:
        if i == ID:
            return
    data[ID] = dentist

if __name__ == '__main__':

    headers = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64); Basis Data/Admin Basis Data/basisdata@std.stei.itb.ac.id'}

    page = 1
    ID = 0
    data = dict()
    dentist = dict()

    while page <= 9: 
        my_url = 'https://www.alodokter.com/cari-dokter/dokter-gigi/page/'+str(page)
        req = urllib.request.Request(my_url, None, headers)
        response = urllib.request.urlopen(req)
        page_html = response.read()

        page_soup = soup(page_html, "html.parser")

        doclist = page_soup.findAll("div", {"class": "row row-doctor"})
        
        for doc in doclist:
            ID += 1
            doctor_name = doc.findAll("div", {"class": "doctor-name"})
            doctor_spec = doc.findAll("div", {"class": "doctor-speciality"})
            findHospital = doc.findAll("div", {"class": "px16 doctor-address"})
            findLocation = doc.findAll("div", {"class": "px16 doctor-desc"})
            findTarif = doc.findAll("div", {"class": "tindakan-desc px16"})
            name = doctor_name[0].text.strip()
            speciality = doctor_spec[0].text.strip()
            hospital = findHospital[0].text.strip()
            location = findLocation[0].text.strip()
            tarif = findTarif[0].text.strip()

            dentist['Nama Dokter'] = name
            dentist['Spesialis'] = speciality
            dentist['Tempat praktik'] = hospital
            dentist['Lokasi'] = location
            dentist['Tarif'] = tarif
            addDentist(data, str(ID), dentist)

            print("=============================")
            print("ID :" + str(ID))
            print("Nama Dokter : " + name)
            print("Spesialis : " + speciality)
            print("Tempat praktik : " + hospital)
            print("Lokasi : " + location)
            print("Tarif : " + tarif)
        page += 1

    writeToJSONFile('D:/MyCodes/Python/DataScraping/Seleksi-2018/Tugas1/data', 'JSONData', data)