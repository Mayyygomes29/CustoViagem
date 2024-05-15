#Calcular o custo da viagem
distancia = int(input("Digite a distância da viagem: KM "))
if distancia <= 200:
    cal = distancia * 0.50
    print(" A viagem custará R${:.2f}".format(cal))
else:
    cal = distancia * 0.45  
    print(" A viagem custará R$ {:.2f}".format(cal))