import random
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
print('¿Cuánto es ' + str(num1) + ' + ' + str(num2) + ' ?')
respuesta = input()
if respuesta == num1 + num2: 
    print('¡Correct!')
else:
    print('¡Nops! La respuesta es ' + str(num1 + num2))
    #Open mode debugg>debugger all... and answer is correct...