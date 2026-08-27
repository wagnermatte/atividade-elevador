''''
entrada:
1. perguntar elevador
1. contabilizar usando +=
2. perguntar periodo
1. contabilizar usando +=

processamento
1. validar Count Elevador A > Count Elevador B = PRINT A OU B
1. validar Count Evelador A > Count Elevador C = PRINT A OU C
1, Validar Count Elevador B > Count Elevador C = PRINT B OU C

2. Validar Count M > Count V = PRINT M OU V
2. Validar Count M > Count N = PRINT M OU N
2. Validar Count V > Count N = PRINT V OU N

3. Calcular Count M + Count V + Count N = totalUsoPeriodo
3. Calcular Count M / totalUsoPeriodo
3. Calcular Count V / totalUsoPeriodo
3. Calcular Count N / totalUsoPeriodo

3. Calcular Count Elevador A + Count Elevador B + Count Elevador C = totalUsoElevadores
3. Calcular Count Elevador A / totalUsoElevadores
3. Calcular Count Elevador B / totalUsoElevadores
3. Calcular Count Elevador C / totalUsoElevadores

saida
1. elevador mais utilizado
2. periodo mais utilizado
3. delta percentual do horário
'''

usoElevador = str(input("Qual Elevador voce mais usa? (A, B OU C)")).upper

countElevador_A = 0
countElevador_B = 0
countElevador_C = 0

if usoElevador == "A":
    countElevador_A += 1
elif usoElevador == "B":
    countElevador_B += 1
if usoElevador == "C":
    countElevador_C += 1

usoPeriodo = str(input("Qual Período voce mais usa? (M=Matutino, V=Vespertino, N=Noturno)")).upper

countPeriodo_M = 0
countPeriodo_V = 0
countPeriodo_N = 0

if usoPeriodo == "A":
    countPeriodo_M += 1
if usoPeriodo == "B":
    countPeriodo_V += 1
if usoPeriodo == "C":
    countPeriodo_N += 1

totalUsoPeriodo = countPeriodo_M + countPeriodo_V + countPeriodo_N
totalUsoElevador = countElevador_A + countElevador_B + countElevador_C

deltaPercentualPeriodo = (countPeriodo_M / totalUsoPeriodo)*100
deltaPercentualPeriodo = (countPeriodo_V / totalUsoPeriodo)*100
deltaPercentualPeriodo = (countPeriodo_N / totalUsoPeriodo)*100

deltaPercentualElevador = (countElevador_A / totalUsoPeriodo)*100
deltaPercentualElevador = (countElevador_B / totalUsoPeriodo)*100
deltaPercentualElevador = (countElevador_C / totalUsoPeriodo)*100

if countElevador_A > countElevador_B:
    print("Elevador mais usado foi o A")
elif countElevador_A > countElevador_C:
    print("Elevador mais usado foi o A")
elif countElevador_B > countElevador_C:
    print("Elevador mais usado foi o B")
else:
    print("Elevador mais usado foi o C")

if countPeriodo_M > countPeriodo_V:
    print("Elevador mais usado foi o M")
elif countPeriodo_M > countPeriodo_N:
    print("Elevador mais usado foi o N")
elif countPeriodo_V > countPeriodo_N:
    print("Elevador mais usado foi o V")
else:
    print("Elevador mais usado foi o N")