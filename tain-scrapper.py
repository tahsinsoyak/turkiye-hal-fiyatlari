import pandas as pd
from bs4 import BeautifulSoup
import requests


dict1 = {'url2': 'https://ankara.bel.tr/hal-fiyatlari', 'il2': 'Ankara'}
dict2 = {'url2': 'https://biizmir.com/hal-fiyatlari', 'il2': 'İzmir'}
dict3 = {'url2': 'https://www.bimalatya.com/hal-fiyatlari', 'il2': 'Malatya'}
dict4 = {'url2': 'https://denizli.bel.tr/Default.aspx?k=halfiyatlari',
         'il2': 'Denizli'}
dict5 = {'url2': 'https://www.biadana.com/hal-fiyatlari', 'il2': 'Adana'}
dict6 = {'url2': 'https://www.bikonya.com/hal-fiyatlari', 'il2': 'Konya'}
dict7 = {'url2': 'https://www.biantep.com/hal-fiyatlari', 'il2': 'Gaziantep'}
dict8 = {'url2': 'https://www.bihatay.com/hal-fiyatlari', 'il2': 'Hatay'}
dict9 = {'url2': 'https://www.kayseri.bel.tr/hal-fiyatlari', 'il2': 'Kayseri'}
dict10 = {'url2': 'https://www.bisamsun.com/hal-fiyatlari', 'il2': 'Samsun'}
dict11 = {'url2': 'https://www.bitrabzon.com/hal-fiyatlari', 'il2': 'Trabzon'}
dict12 = {'url2': 'https://www.kutahya.bel.tr/hal.asp', 'il2': 'Kütahya'}
dict13 = {'url2': 'https://www.corum.bel.tr/hal-fiyatlari', 'il2': 'Çorum'}


def _scrape_data(url2, il2):
    url = url2
    il = il2

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=header)

    hal_ismi = []
    urun_ismi = []
    en_dusuk_fiyat = []
    en_yuksek_fiyat = []
    birim = []

    html_content = response.content
    html_content_string = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.select('table')
    for oneeach in tables:
        for row in oneeach.findAll('tr'):
            columns = row.findAll('td')
            if (il == 'Çorum'):
                print(row)
            if (columns != []):
                hal_ismi.append(il)
                if (len(columns) < 4):
                    birim.append('Kg/Adet')
                    urun_ismi.append(columns[0].text)
                    en_dusuk_fiyat.append(columns[1].text.strip())
                    en_yuksek_fiyat.append(columns[2].text.strip())
                else:
                    urun_ismi.append(columns[0].text)
                    en_dusuk_fiyat.append(columns[2].text.strip())
                    en_yuksek_fiyat.append(columns[3].text.strip())
                    birim.append(columns[1].text.strip())

    df = pd.DataFrame({'halismi': hal_ismi,
                       'urunismi': urun_ismi,
                       'birim': birim,
                       'endusukfiyat': en_dusuk_fiyat,
                       'enyuksekfiyat': en_yuksek_fiyat
                       })
    return df


def _kaydet():
    df = _scrape_data(**dict1)
    df2 = _scrape_data(**dict2)
    df3 = _scrape_data(**dict3)
    df4 = _scrape_data(**dict4)
    df5 = _scrape_data(**dict5)
    df6 = _scrape_data(**dict6)
    df7 = _scrape_data(**dict7)
    df8 = _scrape_data(**dict8)
    df9 = _scrape_data(**dict9)
    df10 = _scrape_data(**dict10)
    df11 = _scrape_data(**dict11)
    df12 = _scrape_data(**dict12)
    df13 = _scrape_data(**dict13)

    dataframes = df.append(df2)
    dataframe2 = dataframes.append(df3)
    dataframe3 = dataframe2.append(df4)
    dataframe4 = dataframe3.append(df5)
    dataframe5 = dataframe4.append(df6)
    dataframe6 = dataframe5.append(df7)
    dataframe7 = dataframe6.append(df8)
    dataframe8 = dataframe7.append(df9)
    dataframe9 = dataframe8.append(df10)
    dataframe10 = dataframe9.append(df11)
    dataframe11 = dataframe10.append(df12)
    dataframe12 = dataframe11.append(df13)

    result = dataframe12.to_json(orient="records")
    with open(f"src/halfiyatlari.json", "w") as file:
        file.write(result)
        file.close()


if __name__ == "__main__":
    _kaydet()
