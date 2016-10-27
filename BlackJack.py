#(c) Copyright by github user : yunaranyancat
#Basic algorithm for Blackjack with certain applicable rules.

'''Self note :
-This is just a basic non-optimised version
-Some print tests are not removed
'''

import random

class Game(object):
    bankroll=0
    valPlayer=0
    valBot=0
    defaultbetamount=100

    def __init__(self):
        print('Welcome to the game!, mate')

    def askplayer(self):
        ans = input('Do you want to stand or hit? stand/hit  ').lower()
        if ans == 'h':
            return True
        elif ans == 's':
            print("Bot's turn :]")
            return False
        else:
            return False

    #def addbankroll(self,added_bankroll):
       # self.bankroll += int(added_bankroll)
        #return self.bankroll

    #def minusbankroll(self,reduced_bankroll):
        #self.bankroll -= int(reduced_bankroll)
        #return self.bankroll

    def finish(self,valPlayer,valBot):
        self.valPlayer=valPlayer
        self.valBot=valBot
        if valPlayer<=21 and valPlayer>valBot:
            print('U won, gratz')
            return str('win')
        elif valPlayer>21:
            print('BUST!')
            return str('bust')
        elif valPlayer==valBot:
            print('No winner, start a new game')
            return str('tie')
        else:
            print('U lose, noooob')
            return str('lose')

    def total(self,card1,card2):
        return card1+card2

    def set_bet_amount(self,newbetamount):
        self.defaultbetamount = newbetamount
        return self.defaultbetamount

    def aOnHand(self,maybeA1,maybeA2): #will return a total of both card if one of them has A
        if maybeA1=='A' and maybeA2!='A':
            maybeA1=11
            if maybeA1+maybeA2<=21:
                return int(maybeA1)+int(maybeA2)
            else:
                maybeA1=10
                if maybeA1 + maybeA2 <= 21:
                    return int(maybeA1) + int(maybeA2)
                else:
                    maybeA1 = 1
                    return int(maybeA1)+int(maybeA2)
        elif maybeA2 == 'A' and maybeA1 != 'A':
            maybeA2=11
            if maybeA1 + maybeA2 <= 21:
                return int(maybeA1) + int(maybeA2)
            else:
                maybeA2 = 10
                if maybeA1 + maybeA2 <= 21:
                    return maybeA1 + maybeA2
                else:
                    maybeA2 = 1
                    return int(maybeA1) + int(maybeA2)
        else:
            if maybeA1=='A' and maybeA2=='A':
                return 21
            else:
                return int(maybeA2)+int(maybeA1)

    def bustscheck(self,total):
        if total<=21:
            return True
        else:
            return False

class Deck(object):

    ListDeck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    def __init__(self):
        print('Card distribution begin')

    def add_card(self):
        test = random.randint(0,12)==12
        if test:
            while True:
                try:
                    self.ListDeck.remove('A')
                    break
                    #myval = int(input('Gratz, u got an A, what value you want it to be assigned to?'))
                except:
                    print('No A(s) left, generating new card')
                    continue
                finally:
                    print('New card generated')
            #return myval
            Elsebutwhat = str('A')
            return Elsebutwhat

        else:

            while True:
                Elsebutwhat = random.randint(1,10)
                try:
                    self.ListDeck.remove(Elsebutwhat)
                    break
                except:
                    print('This number card has been used up')
                    continue
                finally:
                    print('New card generated')

            #print('Your card number is : ',Elsebutwhat)
            return Elsebutwhat


class Player(Game):

    def __init__(self):
        print('Welcome, new challenger')

    def set_bankroll(self,newbankroll):
        self.bankroll=newbankroll
        return self.bankroll


    def newCard(self,card1,card2):
        print('Card 1, Card 2: ', card1,',' ,card2)
        return card1,card2

    def newtotal(self,card1,card2):
        return card1+card2

    def modifybankroll(self, result, betamount,newbankroll=0):
        if result =='win':
            newbankroll=int(self.bankroll)+betamount
            return newbankroll
        elif result =='lose':
            newbankroll = int(self.bankroll) - betamount
            return newbankroll
        elif result =='tie':
            return int(self.bankroll)
        else:
            newbankroll = int(self.bankroll) - betamount
            return newbankroll

class Bot(Game):

    def __init__(self):
        print('Bot is ready!')

    def BotCard(self,card1,card2):
        print('Card 1: , Card 2: ', card1, card2)
        return card1,card2

    def total(self,card1,card2):
        print('Bot total number card right now is : ', card1+card2)




''' START OF THE MAIN PROGRAM'''



NewGame = Game()
PlayerOne = Player()
NewBot = Bot()
MyDeck = Deck()

money = input('Initialisation of your bankroll(You can have a negative balance because we are loan sharks) : ')
PlayerOne.set_bankroll(money) #set the new bankroll
print('Your bankroll: ',PlayerOne.bankroll)

bet = int(input('Amount to bet : '))
betamount = NewGame.set_bet_amount(bet)
print('Your bet amount: ',betamount)

a1,a2 = PlayerOne.newCard(MyDeck.add_card(),MyDeck.add_card())
#print(a1,a2)

totPlayer = PlayerOne.aOnHand(a1,a2)
print('Player On Hand: ',totPlayer)

newtotal = totPlayer
if PlayerOne.askplayer():
    a = PlayerOne.aOnHand(newtotal,MyDeck.add_card())
    print('Your new card= ', a - newtotal)
    print('New total: ', a)
    while NewGame.bustscheck(a):
        if PlayerOne.askplayer():
            b = PlayerOne.aOnHand(a,MyDeck.add_card())
            print('b= ',b)
            a +=b
            print('New total: ',a)
        else:
            bot1, bot2 = NewBot.BotCard(MyDeck.add_card(), MyDeck.add_card())
            print(bot1, bot2)
            totBot = NewBot.aOnHand(bot1, bot2)
            print('Bot On Hand: ', totBot)
            res = NewGame.finish(a, totBot)
            print(res)
            #type(res)
            #print(bet)
            #type(bet)
            re = PlayerOne.modifybankroll(res, bet)
            print(re)
            print('Player 1 newbankroll : ', re)
            break
else:
    bot1, bot2 = NewBot.BotCard(MyDeck.add_card(), MyDeck.add_card())
    print(bot1, bot2)
    totBot = NewBot.aOnHand(bot1, bot2)
    print('Bot On Hand: ', totBot)
    res = NewGame.finish(totPlayer, totBot)
    print(res)
    #print(type(res))
    print(bet)
    #print(type(bet))
    re = PlayerOne.modifybankroll(res, bet)
    #print(re)
    print('Player 1 newbankroll : ', re)
