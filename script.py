
#coding: utf-8
import time
from datetime import datetime
import requests

url_base = 'sua/url/base'

endpoint1 = url_base + 'endpoint/1'
endpoint2 = url_base + 'endpoint/2'

date_format = '%d/%m/%Y %H:%M:%S'


# requisicoes_intervalo = 29
requisicoes_intervalo = 29

def req1():
    hora_inicio = datetime.now()

    data = {}

    resp = requests.post(endpoint1, data=data)

    hora_fim = datetime.now()

    diff_milis = get_millis(hora_fim - hora_inicio)

    print 'Req Tipo 1 - Inicio: ' + str(hora_inicio.strftime(date_format)) + '; Fim: ' + str(hora_fim.strftime(date_format))
    print 'Tempo de resposta: ' + str(diff_milis) + ' milisegundos - Tipo 1'
    print 'Status Code: ' + str(resp.status_code)
    print '================'
    


def req2():
    hora_inicio = datetime.now()

    data = {}

    resp = requests.post(endpoint2, data=data)

    hora_fim = datetime.now()

    diff_milis = get_millis(hora_fim - hora_inicio)

    print 'Req - Tipo 2 - Inicio: ' + str(hora_inicio.strftime(date_format)) + '; Fim: ' + str(hora_fim.strftime(date_format))
    print 'Tempo de resposta: ' + str(diff_milis) + ' milisegundos - Tipo 2'
    print 'Status Code: ' + str(resp.status_code)
    print '================'
    

def get_millis(diff):
	return (diff.days * 86400000) + (diff.seconds * 1000) + (diff.microseconds / 1000)


print '================'
print 'Iniciando medicao em: ' + str(datetime.now().strftime(date_format))
print '----------------'

while True:
    req1()

    time.sleep(requisicoes_intervalo)

    req2()

    time.sleep(requisicoes_intervalo)



