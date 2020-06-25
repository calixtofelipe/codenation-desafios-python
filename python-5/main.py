from datetime import datetime
import timeit

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
        'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
        'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
        'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
        'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
        'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
        'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
        'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
        'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
        'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
        'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564627800, 'start': 1564626000}
]

# importante tratar as tarifas separado caso tenham mudanças no futuro
VLR_FIXO_DIURNO = 0.36
VLR_MINUTO_DIURNO = 0.09
VLR_FIXO_NOTURNO = 0.36
VLR_MINUTO_NOTURNO = 0

# importante tratar os horários separados caso no futuro
# mude os intervalos. Como a separação é feita em diurno e noturno,
# só precisamos do intervalo diurno, fora dele será noturno.
HR_INICIO_DIURNO = 6
HR_FINAL_DIURNO = 22


def tarifacao(vlrFixo, vlrMinuto, QtdMinutos):
    # A tarifação é uma equação linear
    tarifacao = vlrFixo + (vlrMinuto * QtdMinutos)
    return round(tarifacao, 2)


def calcMinutos(dt_inicio, dt_final, periodo):
    # calculo dos minutos na situação de periodo diurno e noturno
    if periodo == 'Diurno':
        dtFinalAjust = dt_inicio.replace(
            hour=HR_FINAL_DIURNO) if dt_final.hour > HR_FINAL_DIURNO \
            else dt_final
        timeTotal = dtFinalAjust - dt_inicio
        qtdMinutos = (timeTotal.total_seconds() // 60)
    else:
        dt_inicioAjust = dt_inicio.replace(
            hour=HR_FINAL_DIURNO) if dt_inicio.hour < HR_FINAL_DIURNO \
            else dt_inicio
        timeTotal = dt_final - dt_inicioAjust
        qtdMinutos = (timeTotal.total_seconds() // 60)
    return round(qtdMinutos, 2)


def classify_by_phone_number(records):
    # lista que será salva os registros com os valores agrupados.
    registros = {}
    for record in records:
        dt_inicio = datetime.fromtimestamp(record['start'])
        dt_final = datetime.fromtimestamp(record['end'])

        # Vou mudar a escala para facilitar as condições
        # Se considerar a hora 6 como hora inicial e somar 24 (horas do dia)
        # nos valores menor que 6 consigo tratar os valores menor que 22 como
        # diurno valores maior que 22 como noturno
        hourStartScale = 24+dt_inicio.hour \
            if dt_inicio.hour < HR_INICIO_DIURNO else dt_inicio.hour
        hourEndScale = 24+dt_final.hour if dt_final.hour < HR_INICIO_DIURNO \
            else dt_final.hour

        # Dessa forma a ligação pertencente menor que  22 unidades é uma taxa
        # E a ligação pertencente ao periodo maior que 22 unidades é outra taxa

        # calculo tarifacao diurna
        # só tem tarifa diurna se start menor hourStartScale que 22
        tarifa_diurna = 0
        tarifa_noturna = 0
        if hourStartScale < HR_FINAL_DIURNO:
            QtdMinutos = calcMinutos(dt_inicio, dt_final, 'Diurno')
            tarifa_diurna = tarifacao(VLR_FIXO_DIURNO,
                                      VLR_MINUTO_DIURNO, QtdMinutos)

        # calculo tarifacao noturna
        if hourEndScale > HR_FINAL_DIURNO:
            QtdMinutos = calcMinutos(dt_inicio, dt_final, 'Noturno')
            tarifa_noturna = tarifacao(VLR_FIXO_NOTURNO,
                                       VLR_MINUTO_NOTURNO, QtdMinutos)

        # somatório das duas tarifas caso exista
        tarifa_total = round((tarifa_diurna + tarifa_noturna), 2)

        # Daqui em diante ficaria mais fácil usando a biblioteca bandas
        # e a performance ficaria melhor já que fazia o agrupamento/ordenação
        # pelo pandas
        # mas fiz sem como aprendizado
        if registros.get(record["source"]) is None:
            registros[record["source"]] = tarifa_total
        else:
            registros.update(
                {record["source"]:
                 round(registros.get(record["source"]) + tarifa_total, 2)})
    lista_final = []

    for k, v in registros.items():
        dicio = {}
        dicio['source'] = k
        dicio['total'] = v

        lista_final.append(dicio)
        lista_final = sorted(
            lista_final, key=lambda x: x['total'], reverse=True)
    return lista_final


start = timeit.timeit()
print(classify_by_phone_number(records))
end = timeit.timeit()
print(end - start)
