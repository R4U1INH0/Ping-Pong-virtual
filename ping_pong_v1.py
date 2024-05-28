from pygame importar *

# Variables iniciales

#Escena del juego:
'''
el color de fondo debe tener estos valores RGB: 200, 255, 255 y deben ser seteados en la variable back
el ancho de la ventana es de 600, debe ser seteado en la variable win_width
el alto de la venta es de 500, debe ser seteado en la variable win_height
'''
back = 
win_width = 
win_height = 
window = display.set_mode((win_width, win_height))
window.fill(back)

#banderas responsables del estado del juego
game = True
finish = False
clock = time.Clock()
FPS = 60

imagen_raqueta = 'racket.png'
imagen_pelota = 'tenis_ball.png'

#clase principal para sprites, esta debe heredar de la clase sprite.Sprite
class GameSprite
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
         
        self.image = transform.scale(image.load(player_image), (wight, height)) # juntos 55,55 - parámetros
        self.speed = player_speed
 
        # cada sprite debe almacenar una propiedad  rect - el rectángulo en el que está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

'''
La clase heredera del sprite del jugador (controlada por flechas)
Se han definido dos métodos updates para el manejo de teclado para cada jugador
el método update_r debe controlar las flechas direccionales de arriba y abajo (K_UP, y K_DOWN)
el método update_l debe controlar las teclas w y s (K_w, y K_s)
'''        
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        #adicionar el codigo para el manejo de las teclas

    def update_l(self):
        keys = key.get_pressed()
        #adicionar el codigo para el manejo de las teclas


'''
Crear las raquetas y la pelota
instanciar la clase Player para crear las raquetas
La raqueta uno debe tener el objeto racket1 que al ser creado tendrá los parámetros:
imagen_raqueta, posición inicial x, y = 30,200, velocidad 4, ancho y alto 50 y 150

Para la segunda raqueta, el objeto debe tener el nombre racket2 con los siguientes parámetros:
imagen_raqueta, posición inicial x, y = 520,200, velocidad 4, ancho y alto 50 y 150

Para la pelota debe ser instanciado desde la clase GameSprite, el objeto debe tener el nombre de ball con los siguientes parámetros:
image_pelota, posición inicial x, y = 200,200, velocidad 4, ancho y alto 50 y 50
'''
racket1 = 
racket2 = 
ball = 

font.init()
font = font.Font(None, 35)
lose1 = font.render('JUGADOR 1 PERDISTE!', True, (180, 0, 0))
lose2 = font.render('JUGADOR 2 PERDISTE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:

    '''
    Implementar el cerrar la ventana
    '''
    for e in event.get():
        #poner código para cerrar la ventana
    
    if finish != True:

        #código para actualizar la ventana con el color de fondo configurado
        

        #Agregar código para llamar a los métodos updates de la clase Player
        

        #variables que manejarán las posiciones X,Y de la pelota
        #aqui no tiene que modificar.
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        '''
        Agregar código para las colisiones, debe usar el método collide_rect del sprite para
        detectar las colisiones de la raqueta 1 con la pelota y de la raqueta 2 con la pelota
        Si se detecta colisión de la pelota con cualquiera de estas raquetas entonces el valor
        de speed_x debe de multiplicarse por -1 y el speed_y debe de mulplicarse por 1
        speed_x *= -1
        speed_y *= 1
        '''
        
        
        # No se requiere que modifique este código:
        # si la pelota alcanza los límites de la pantalla, cambie la dirección de su movimiento
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        # Se requiere que coloque el mensaje cuando pierde el primer jugador        
        # si la pelota voló más allá de la raqueta, mostramos la condición de pérdida para el primer jugador
        if ball.rect.x < 0:
            finish = True
            #coloque el código aqui para mostrar el mensaje dentro de las coordenadas 200,200
            game_over = True

        # Se requiere que coloque el mensaje cuando pierde el segundo jugador        
        # si la pelota pasó volando por la raqueta, mostramos la condición de pérdida para el segundo jugador
        if ball.rect.x > win_width:
            finish = True
            #coloque el código aqui para mostrar el mensaje dentro de las coordenadas 200,200
            game_over = True


        '''
        Agregue el codigo para resetear las raquetas y la pelota, usar el método reset de GameSprite
        '''
        

    '''
    Agregar el código de actualización
    '''
    
    clock.tick(FPS)