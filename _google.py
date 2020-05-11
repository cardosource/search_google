from requests import get as iniciar
import re
import csv
import sys
def conexao(url):
    try:
        c = iniciar(str(url))
        print(f"[status ] - {c.status_code}")
        return c.text
    except Exception  as erro:
        print(f"[ net ] - {erro}")

def pesquisar(domaintxt,searchtxt):
    n_pag = f"&start={0}"
    search = open(f"searchsTXT/{searchtxt}").readline()
    organizar = []
    f = open(f"{domaintxt}.csv", "a", encoding='UTF-8')
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    quantidade_de_pesquisa=1
    for d in open(f"domain/{domaintxt}.txt"):
        d = str(d).replace("\n","")
        print("[ dk ] dominio - %s" %d)
        consult_google = f' {search} :{d}'
        urlmont = f'https://www.google.com/search?q={consult_google} {n_pag}'
        html = conexao(urlmont)
        tais_doork = re.compile('url\?q=(.*?)&amp')
        for results in tais_doork.findall(str(html)):
            if 'accounts.google' != results[8:23] and f'www.google.com/' != results[8:23] and results[0:4] == 'http' and 'http://www.google.com/sorry/' != results[0:28] and results[0:28] != "https://support.google.com/":
                links = str(results).replace("%3F", '?').replace('%3D', '=s')
                print(f"< {quantidade_de_pesquisa} > | {links}")
                organizar = organizar + [links]
                quantidade_de_pesquisa+=1
    quantidade = 1
    for remove_repetidos in list(set(organizar)):
        print(f"{[quantidade]}- Escrevendo :::: %s" % remove_repetidos)
        if remove_repetidos:
            writer.writerow([remove_repetidos])
        quantidade += 1




pesquisar("asia","iniciar.txt")

