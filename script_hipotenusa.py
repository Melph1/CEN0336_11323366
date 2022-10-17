a = float(input('Coloque um valor para A:')) #Esta variável pode ser inserida em decimal
b = float(input('Coloque um valor para B:')) #Esta variável pode ser inserida em decimal
n1 = int(a) #A variável "a" precisa ser inteira
n2 = int(b) #A variável "b" precisa ser inteira
z= a*2+b*2 #Fórmula para o quadrado da hipotenusa

if n1 == a: #Condição para a variável "a" ser inteira
    print('Numero inteiro') #Em caso positivo, é um numero inteiro
else: #Condição caso a variável "a" não for inteira
    print ('O numero precisa ser inteiro')#Em caso positivo, um aviso aparece no visor

if n2== b:#Condição para a variável "b" ser inteira
    print('Numero inteiro')#Em caso positivo, é um numero inteiro
else: #Condição caso a variável "b" não for inteira
    print ('O numero precisa ser inteiro')#Em caso positivo, um aviso aparece no visor

if a<0 or b<0: #Condição para as variáveis "a" e "b" serem positivas
  print('O número precisa ser positivo') #Aviso caso as variáveis sejam negativas

if n1 == a and n2 == b: #Condição para as variáveis serem inteiras
    print("o quadrado da hipotenusa para o retangulo é", round(z))#Em caso positivo, a conta é finalizada
else:
    print ('Não foi possível calcular a hipotenusa para este caso')#Em caso negativo, o aviso aparece no visor
