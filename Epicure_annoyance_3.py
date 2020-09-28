hp1 = 30
hp2 = 30
att1 = 0
att2 = 0

roundnum = int(input())
c = []

while 1:
    player = input()
    
    if player == 'player1':      
        attway = input()
        if attway == 'Sugar Attack':
            hp2 = hp2 - (3 + att1)
            if hp1 <= 0:
                hp1 = 0
                c.append('Player2 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
                break
            elif hp2 <= 0:
                hp2 = 0
                c.append('Player1 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
                break
            else:
                try:
                    if hp1 > hp2 :
                        att2 = att2 + 1
                    elif hp1 < hp2:
                        att1 = att1 + 1
                except:
                    print('error')
 
        elif attway == 'Spicy Boomer':
            hp2 = hp2 - (6 + att1)
            if hp1 <= 0:
                hp1 = 0
                c.append('Player2 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
                break
            elif hp2 <= 0:
                hp2 = 0
                c.append('Player1 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
                break
            else:
                if hp1 > hp2 :
                    att2 = att2 + 1
                elif hp1 < hp2:
                    att1 = att1 + 1               
        else:
            hp2 = hp2 - (9 + att1)
            if hp1 <= 0:
                hp1 = 0
                c.append('Player2 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
                break
            elif hp2 <= 0:
                hp2 = 0
                c.append('Player1 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
                break
            else:
                if hp1 > hp2 :
                    att2 = att2 + 1
                elif hp1 < hp2:
                    att1 = att1 + 1
            
    elif player == 'player2':
        attway = input()
        if attway == 'Sugar Attack':
            hp1 = hp1 - (3 + att2)
            if hp1 <= 0:
                hp1 = 0
                c.append('Player2 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
                break
            elif hp2 <= 0:
                hp2 = 0
                c.append('Player1 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
                break
            else:
                if hp1 > hp2 :
                    att2 = att2 + 1
                elif hp1 < hp2:
                    att1 = att1 + 1       
        elif attway == 'Spicy Boomer':
            hp1 = hp1 - (6 + att2)
            if hp1 <= 0:
                hp1 = 0
                c.append('Player2 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
                break
            elif hp2 <= 0:
                hp2 = 0
                c.append('Player1 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
                break
            else:
                if hp1 > hp2 :
                    att2 = att2 + 1
                elif hp1 < hp2:
                    att1 = att1 + 1
        else:
            hp1 = hp1 - (9 + att2)
            if hp1 <= 0:
                hp1 = 0
                c.append('Player2 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
                break
            elif hp2 <= 0:
                hp2 = 0
                c.append('Player1 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
                break
            else:
                if hp1 > hp2 :
                    att2 = att2 + 1
                elif hp1 < hp2:
                    att1 = att1 + 1
        
    elif player == 'stop':
        
        if hp1 > hp2:
            c.append('Player1 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
            hp1 = 30
            hp2 = 30
            att1 = 0
            att2 = 0
            if len(c) == roundnum :
                break
        elif hp1 < hp2:
            c.append('Player2 wins.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
            hp1 = 30
            hp2 = 30
            att1 = 0
            att2 = 0
            if len(c) == roundnum :
                break
        else:
            c.append('Draw.\nPlayer1 HP: {}\nPlayer2 HP: {}'.format(hp1,hp2))
            hp1 = 30
            hp2 = 30
            att1 = 0
            att2 = 0
            if len(c) == roundnum :
                break
    
for i in c:
    print(i)
