luchadores = [
{'nombre': '000' , 'peso': 64, 'estatura': 169, 'str': 3, 'agi': 8, 'res': 4},
{'nombre': '001' , 'peso': 77, 'estatura': 183, 'str': 6, 'agi': 6, 'res': 2},
{'nombre': '010' , 'peso': 73, 'estatura': 178, 'str': 7, 'agi': 4, 'res': 3},
{'nombre': '011' , 'peso': 59, 'estatura': 172, 'str': 7, 'agi': 8, 'res': 1},
{'nombre': '100' , 'peso': 70, 'estatura': 160, 'str': 6, 'agi': 10, 'res': 4},
{'nombre': '101' , 'peso': 50, 'estatura': 178, 'str': 3, 'agi': 5, 'res': 2},
{'nombre': '110' , 'peso': 129, 'estatura': 196, 'str': 10, 'agi': 3, 'res': 5},
{'nombre': '111' , 'peso': 80, 'estatura': 186, 'str': 4, 'agi': 8, 'res': 7}
]

i = 0
j = 0
winner = []
while j < 8:
    while i < 8:
        if (luchadores[j]['peso'] < 75 and luchadores[i]['peso'] < 75):
            absp1 =  (luchadores[j]['estatura'] / (luchadores[j]['agi'])) + (100 / luchadores[j]['estatura']) + luchadores[j]['agi']
            absp2 = (luchadores[i]['estatura'] / (luchadores[i]['agi'])) + (100 / luchadores[i]['estatura']) + luchadores[i]['agi']
    
        elif (luchadores[j]['peso'] >= 75 and luchadores[i]['peso'] >= 75):
            absp1 =  5 * luchadores[j]['peso'] + 2 * luchadores[j]['res'] 
            absp2 = 5 * luchadores[i]['peso'] + 2 * luchadores[i]['res'] 

        elif(luchadores[j]['peso'] == luchadores[i]['peso'] ):
            winner.append(luchadores[j]['nombre'])
        else:
            absp1 = (luchadores[j]['estatura'] / (luchadores[j]['agi'])) + (3 * luchadores[j]['peso']) + ((luchadores[j]['str'] + luchadores[j]['agi'] + luchadores[j]['res']) / 3)
            absp2 = (luchadores[i]['estatura'] / (luchadores[i]['agi'])) + (3 * luchadores[i]['peso']) + ((luchadores[i]['str'] + luchadores[i]['agi'] + luchadores[i]['res']) / 3)

        if (absp1 > absp2):
            winner.append(luchadores[j]['nombre'])
        else:
            winner.append(luchadores[i]['nombre'])
        i += 1
    i = 0
    j += 1

n=8
fighter=[winner[i:i + n] for i in range(0, len(winner), n)]
print(fighter)
