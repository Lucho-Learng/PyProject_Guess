import random
import time

def ShowIntroducción():
    print('Esta es una tierra de Dragones. Frente a tí')
    print('hay dos cuevas. En una de ellas el Dragón es generoso y')
    print('amigable y compartirá su tesoro contigo. El otro Dragón')
    print('es codicioso y está hambriento y te devorará inmediatamente.')
    print()

def elegirCueva():
    cueva = ''
    while cueva != '1' and cueva != '2':
        print('¿A qué cueva quieres entrar? (1 ó 2)')
        cueva = input()

    return cueva

def explorarCueva(cuevaElegida):
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print('¡Un gran Dragón aparece súbitamente frente a tí! Abre sus fauces...')

    print()
    time.sleep(2)

    cuevaAmigable = random.randint(1, 2)

    if cuevaElegida == str(cuevaAmigable):
        print('¡Compartirá su morada!')
    else: 
        print('¡Te engulle de un bocado!')

jugarDeNuevo = 'yes'
while jugarDeNuevo == 'yes' or jugarDeNuevo == 'yes':

    ShowIntroducción()
        
    númeroDeCueva = elegirCueva()

    explorarCueva(númeroDeCueva)

    print('¡Quieres jugar de nuevo? (yes or no)')
    jugarDeNuevo = input()
