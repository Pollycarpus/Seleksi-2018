import json
import urllib.request
from bs4 import BeautifulSoup as soup 

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


if __name__ == '__main__':

    headers = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64); Basis Data/Admin Basis Data/basisdata@std.stei.itb.ac.id'}

    my_url = 'https://www.alodokter.com/cari-dokter/dokter-gigi/jakarta'
    req = urllib.request.Request(my_url, None, headers)
    response = urllib.request.urlopen(req)
    page_html = response.read()

    page_soup = soup(page_html, "html.parser")

    doclist = page_soup.findAll("div", {"class": "row row-doctor"})
    id = 0
    data = {}

    for doc in doclist:
        id += 1
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

        print("=============================")
        print("ID :" + str(id))
        print("Nama Dokter : " + name)
        print("Spesialis : " + speciality)
        print("Tempat praktik : " + hospital)
        print("Lokasi : " + location)
        print("Tarif : " + tarif)
