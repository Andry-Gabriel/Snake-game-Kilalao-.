#-*-coding:utf8;-*- # encodage amin'ny norme utf8 no ampiasaina eto, izay ihany koa no tena akaiky ny Python V3
#qpy:console # andrana QPython no tiko havoaka eto fa tsy mbola vita hatramin'ny farany ny tiko haseho. 
#ity indray ny andrana aminy QPython fa mbol mila gestion écran tactile. 

import random
import time
import os

try:
    import androidhelper as android
except ImportError:
    android = None

# Définition de la taille du plateau de jeu
WIDTH = 20 # velarany tokotany hilalaovana
HEIGHT = 10 # halavany miakatra ny tokotany hilalaovana

# Initialisation du serpent @ et de la nourriture #
snake = [(WIDTH // 2, HEIGHT // 2)]
food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))

# Direction initiale
direction = (0, -1)  # Haut

# Score
score = 0 # tarehimarika 

def clear_screen(): # famaritana ny tokotany ilalaovana izay mila fafana isakin'ny seho vaovao
    if android:
        print("\n" * 100)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

def draw_board(): # fihetsehana ao anatinu lalao
    board = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    #satria ASCII art no endrika ny lalao dia ny caractère ~ sy ny * ary ny # no safidiko ho kirakiraiko eto
    # Dessiner le serpent
    for segment in snake:
        board[segment[1]][segment[0]] = 'O'  
    
    # Dessiner la tête du serpent
    head = snake[0] #ny lohany ilay bibilava
    board[head[1]][head[0]] = '~'# rehefa voky ilay bibilava dia mitombo ary ity ny halavany
    
    # Dessiner la nourriture 
    board[food[1]][food[0]] = '*' # ity ny sakafo hifanenjehana eto
    
    # Afficher le plateau # fanehoana ny tokotany ilalaovana ity
    print(f"Score: {score}")
    print('+' + '-' * WIDTH + '+')
    for row in board:
        print('|' + ''.join(row) + '|')
    print('+' + '-' * WIDTH + '+')

def move_snake(): #fihetsefan'ilay bibilava
    global food, score
    new_head = (
        (snake[0][0] + direction[0]) % WIDTH,
        (snake[0][1] + direction[1]) % HEIGHT
    )
    
    if new_head in snake:
        return False
    
    snake.insert(0, new_head)
    
    if new_head == food:
        score += 1
        food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    else:
        snake.pop()
    
    return True

def get_input(): # fampidirana ny baiko avy aminy mpilalao
    global direction
    if android:
        droid = android.Android()
        event = droid.eventWait().result
        if event and event['name'] == 'key':
            key = event['data']['key']
            if key == '19':  # Haut
                direction = (0, -1)
            elif key == '20':  # Bas
                direction = (0, 1)
            elif key == '21':  # Gauche
                direction = (-1, 0)
            elif key == '22':  # Droite
                direction = (1, 0)
    else:
        key = input()
        if key == 'w':
            direction = (0, -1)
        elif key == 's':
            direction = (0, 1)
        elif key == 'a':
            direction = (-1, 0)
        elif key == 'd':
            direction = (1, 0)

def main(): #eto no fanatanterahana ny code rehetra ka mila faritana tsara ny tokony hatao eto
    while True:
        clear_screen()
        draw_board()
        if not move_snake():
            print("Game Over ianao e!")
            break
        get_input()
        time.sleep(0.2)

if __name__ == "__main__":
    main()
    
    
##tsy azo adika fa mba mamorona ihany koa azafady 
