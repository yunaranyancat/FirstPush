#(c) Copyright : ZulfiqarW
import random
#I'm going to create a class called Game
class Game(object):
    game_counter=1
    head_counter=0
    tail_counter=0

    def __init__(self):
        print('Flipping coin starts')
        print('First round : ')
#When this class has been instantiated by a reference, the game starts
#Since I assume that the probability for the coin to flip whether on head or tail side is the same, then tail:50%, head:50%
    def head_or_tail(self):
        val = random.randint(0,1)
        if val==0:
            return 'Tail'
        else:
            return 'Head'

#Calculate how many times the game is repeated
    def add_game_countby1(self):
        self.game_counter+=1

#Continue the game after the first one?
    def continue_game(self):
        while True:
            res=input('Would you like to continue the game or not? y/n= ').lower()
            if res=='y' or res=='n':
                if res=='y':
                    return True
                    break
                else:
                    return False
                    break
            else:
                print('Value invalid! Please re-enter (y or n)')
                continue

#Head and tail counters.
    def add_head_countby1(self):
        self.head_counter+=1

    def add_tail_countby1(self):

        self.tail_counter+=1
#Head and Tail Getters.
    def get_head_count(self):
        return self.head_counter

    def get_tail_count(self):
        return self.tail_counter

#NewGame.
NewGame1 = Game()
a = NewGame1.head_or_tail()
print('You got a :',a)
if a == 'Head':
    NewGame1.add_head_countby1()
else:
    NewGame1.add_tail_countby1()

#Continue the game?
while NewGame1.continue_game():
    a = NewGame1.head_or_tail()
    print('You got a :', a)
    NewGame1.add_game_countby1()
    if a=='Head':
        NewGame1.add_head_countby1()
    else:
        NewGame1.add_tail_countby1()

#Print necessary texts.
print('Total games played: ',NewGame1.get_head_count()+NewGame1.get_tail_count())
print('Total heads gained: ',NewGame1.get_head_count())
print('Total tails gained: ',NewGame1.get_tail_count())

#Self note: This algorithm can be optimised by combining the first instatiation with (x>=2) games.
