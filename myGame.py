import random
import math
def game():
    print(" Welcome to stone paper scisssor!!! ")
    i=0
    uscore=0
    cscore=0
    score=0
    while True:
        print('Do you wish to continue?')
        choice=input("Enter Y if you want to continue and N if exit : ")
        if choice!='N':
           
            things=['stone','paper','scissor']
        
        
           
            user=input("Enter stone/paper/scissor, Keep in mind to enter your choice exactly like the options given : ")
            computer=random.choice(things)
            if user=='stone':
                if computer=='paper':
                    cscore+=1
                    print('Computer chose',computer)
                    print('Computer won round',(i+1))
                elif computer=='scissor':
                    print('You won round',(i+1))
                    uscore+=1
                    print('Computer chose',computer)
                else : print('Both selected same option!!')
            elif user=='paper':
                if computer=='stone':
                    uscore+=1
                    print('You won round',(i+1))
                    print('Computer chose',computer)
                elif computer=='scissor':
                    cscore+=1
                    print('Computer won round',(i+1))
                    print('Computer chose',computer)
                else : print('Both selected same option in round',(i+1))
            elif user=='scissor':
                if computer=='stone':
                    cscore+=1
                    print('Computer won round',(i+1))
                    print('Computer chose',computer)
                elif computer=='paper':
                    uscore+=1
                    print('You won round',(i+1))
                    print('Compupter chose',computer)
                else : print('Both selected same option!!')
            i+=1
           
        elif choice=='N':
            print('Have a good day!!')
            break

            
            
    if uscore>cscore: 
        score=uscore
        print('You won the  game in',i,'rounds with score',uscore)
    elif cscore>uscore:
        score=cscore
        print('Computer won the game in',i,'rounds with score',cscore)
    else: 
        score=uscore
        print('Draw with score',score,'in',i,'rounds')
        return score
    
game()



        
