import serial

#Conexao Serial entre python e arduino:
try:
    conectado = serial.Serial("COM3", 115200, timeout=0.5)
    print("Conexao com a porta, ", conectado.portstr)
except serial.SerialException:
    print("Nao encontrado nenhuma porta")
    pass

while True:
    print("#################################")
    print("Instruçoes: \n A = Liga led 1 \n B = Liga led 2 \n C = Liga led 3 \n D = Desliga led 1 \n E = Desliga led 2 \n F = Desliga led 3")
    comando = input("Digite uma letra para ligar um led: \n")
    if comando == "A":
        conectado.write(b'2') #b'1' significa que 1 é um numero binario
    if comando == "B":
        conectado.write(b'3')
    if comando == "C":
        conectado.write(b'4')
    if comando == "D":
        conectado.write(b'5')
    if comando == "E":
        conectado.write(b'6')
    if comando == "F":
        conectado.write(b'7')
        if input("Tecle ENTER para inserir outro comando Caso nao, Tecle N: \n").upper() == "N":
            break

conectado.close()
print("Conexao Finalizada")














