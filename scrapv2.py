from bs4 import BeautifulSoup
import requests 


def getMoneyStats(bank,url,classTable):
    row_num = 0
    try:
        request= requests.get(url)
        if request.status_code == 200:
            soup = BeautifulSoup(request.content,"html.parser")
            print(bank)
            for table in soup.findAll("table",class_=classTable):
                header = table.th.get_text()
                if row_num < 1:
                    for row in table.findAll("tr"):
                        out_row = [ header ]
                        for col in row.findAll("td"):                            
                                out_row.append(col.get_text())
                                print(out_row)
                row_num = row_num + 1     
        else:
            print('unable to connect ')
    except requests.HTTPError as e:
        print('Unable to open url',e)

if __name__ == "__main__":
    getMoneyStats("BANCO NACION",'''http://www.bna.com.ar/Personas''',"table cotizacion")

if __name__ == "__main__":
    getMoneyStats("BANCO SANTANDER RIO",'''https://banco.santanderrio.com.ar/exec/cotizacion/index.jsp''',None)    

if __name__ == "__main__":
    getMoneyStats("BANCO CORDOBA",'''https://www.bancor.com.ar/718_APP/''',"None")    

