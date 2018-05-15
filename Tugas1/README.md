This program scrapes information about dentists across Indonesian big cities from [Alodokter](https://www.alodokter.com/cari-dokter/dokter-gigi) 

### Spesifications
This program will fetch each dentist's detailed information and preprocess it into JSON object. And the program will do the normalization job to the existing JSON file.

### Prerequisites
1. Python 3.6
2. BeautifulSoup4, to fetch the source code of the webpage.
```
$ pip install beautifulsoup4

```
3. Pandas, to normalize JSON object into dataframe
 ```
$ pip install pandas

```
4. Internet connection

### How to Use
1. Execute Makefile with command bellow. 
'''
$ mingw32-make
'''

### JSON Structure (Normalized)

[{"1.Lokasi":"Jatinegara, Jakarta","1.Nama Dokter":"Dr. drg. Dewi Anggraini Margono Rompas, Sp.KG(K)","1.Spesialis":"Dokter Gigi","1.Tarif":"Mulai Dari Rp 350.000","1.Tempat Praktik":"Rumah Sakit Premier Jatinegara"}]

### Author
Rabbi Fijar Mayoza
13516081
Teknik Informatika ITB