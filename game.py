import random
def main():
    player = 1
    winner = 1
    cards = int_deck()
    score = [9,9,9]
    trumpCount = 0
    trump = ['c','d','h','s','n']
    print('Welcome Gamer:')
    print('All suits use first letter')
    print('All numbers are in hex')
    print('Ace of spades is represented by s1')
    print('Ace = 1, 10 = a, J = b, Q = d, K = e')
    print('_'*40, '\n')
    while winState(score) == False:
        if trumpCount == 6:
            trumpCount = 0
        trumpCard = trump[trumpCount]
        scorePrint(score)
        tricks = [0,0,0]
        game = deal(shuffle(cards))
        trumpPrint(trumpCard)
        game = dummySwitch(game)
        while len(game[0]) != 0:
            player = winner
            table = []
            trumpPrint(trumpCard)
            while len(table) < 3:
                if player == 0:
                    print('On the table there is: ', end='')
                    cardPrint(table)
                    print('Your Hand is: ', end='')
                    handPrint(game[0])
                    personPlay(game[player], table)
                if len(table) == 0:
                    plays(game[winner], table, player)
                else:
                    plays(game[player], table, player)
                if player == 2:
                    player = 0
                else:
                    player += 1
            print('The final table state was: ', end='')
            cardPrint(table)
            winner = highestCard(table, winner, trumpCard)
            tricks[winner] = (tricks[winner]+1)
            print('-'*10)
            print('Player', winner, 'Wins', ':', tricks[winner], 'trick(s)')
            print('-'*10)

        trumpCount +=1
        
        for players in range(len(tricks)): 
            print('player', players, 'made', tricks[players], 'Trick(s)')
        print('')
        score = scoring(tricks, score)
    
    won = score.index(min(score))
    print('Player', won, 'HAS WON!')

def dummySwitch(lst):
    print('This is Your Hand:')
    handPrint(lst[0])
    user = input('Would you like to switch it with the Dummy? (y/n) ')
    while user != 'y' and user != 'n':
        print('Must by a \'y\' or \'n\'')
        user = input('Would you like to switch it with the Dummy? (y/n) ')
    if user == 'y':
        lst.append(lst[0])
        lst[0] = lst[3]
        del lst[3]
    print('-' *10)
    return lst 

def scorePrint(lst):
    print('Current Score: ')
    for index in range(len(lst)):
        print('Player', index, 'has', lst[index], 'point(s)')
    print('')

def trumpPrint(trumpCard):
    if trumpCard == 'c':
        print('Clubs is trump')
    if trumpCard == 'h':
        print('Hearts is trump')
    if trumpCard == 'd':
        print('Diamonds is trump')
    if trumpCard == 's':
        print('Spades is trump')

def handPrint(lst):
    print('')
    for card in lst:
        if identS(card) == 'c':
            print(card + ' ', end='')
    print('')
    for card in lst:
        if identS(card) == 'd':
            print(card + ' ', end='')
    print('')
    for card in lst:
        if identS(card) == 'h':
            print(card + ' ', end='')
    print('')
    for card in lst:
        if identS(card) == 's':
            print(card + ' ', end='')
    print('')

def winState(lst):
    for player in lst:
        if player <= 0:
            return True
    return False

def scoring(hand, final):
    diff = 0
    for player in range(len(hand)):
        diff = (4 - hand[player])
        final[player] = final[player] + diff
    return final

def cardPrint(lst):
    for item in lst:
        print(item + ' ', end='')
    print('')

def highestCard(table, winner, trump):
    player = 0
    lst = sort(table, winner)
    top = max(lst)
    for card in lst:
        if (identN(card) == 1) and identS(card) == identS(table[0]) and identS(top) != trump:
            top = card
        elif identS(card) == trump and identN(card) == 1:
            top = card
        elif identS(top) == trump and identN(card) > identN(top):
            top = card
        elif identS(top) != trump and identS(card) == trump:
            top = card
    return lst.index(top)

def sort(table, winner):
    sort = ['','','']
    if winner == 1:
        sort[0] = table[2]
        sort[1] = table[0]
        sort[2] = table[1]
    if winner == 2:
        sort[0] = table[1]
        sort[1] = table[2]
        sort[2] = table[0]
    if winner == 0:
        sort = table
    return sort

def plays(lst, top, player):
    matchingCards = 0
    count = 0
    if player != 0:
        if len(top) == 0:
            top.append(lst[0])
            del lst[0]
        else:
            for card in lst:
                if identS(card) == identS(top[0]):
                    matchingCards += 1
            if matchingCards >= 1:
                while identS(lst[count]) != identS(top[0]):
                    count += 1
                top.append(lst[count])
                del lst[count]
            else:
                top.append(lst[0])
                del lst[0]

def personPlay(lst, top):
    hasSuit = False
    noInp = True
    if len(top) != 0:
        for card in lst:
            if identS(card) == identS(top[0]):
                hasSuit = True
                break
    inp = playerInput(lst)
    while noInp == True:
        if (hasSuit == False):
            while (inp not in lst):
                print('That\'s not your card')
                inp = playerInput(lst)
            top.append(inp)
            lst.remove(inp)
            noInp = False
        if hasSuit == True:
            while (identS(inp) != identS(top[0])) or (inp not in lst):
                print('Not in Suit')
                inp = playerInput(lst)
            top.append(inp)
            lst.remove(inp)
            noInp = False


def playerInput(lst):
        goodChar = ['s','c','d','h']
        goodnums = ['1','2','3','4','5','6','7','8','9','a','b','d','e']
        user = input('What Card: ')
        while (len(user) != 2) or (user[0] not in goodChar) or (user[1] not in goodnums):
            print('bad input')
            user = input('What Card: ')
        return getCard(user)

# Takes card in for of s1, h2, etc
# returns the unicode card for that command
def getCard(string):
    char = ['0x1f0',0,0]
    if string[0] == 's':
        char[1] = 'a'
    if string[0] == 'h':
        char[1] = 'b'
    if string[0] == 'd':
        char[1] = 'c'
    if string[0] == 'c':
        char[1] = 'd'
    char[2] = str(string[1])
    return chr(int(''.join(char), 16))

def identS(char):
    char = hex(ord(char))
    if char[5] == 'a':
        return 's'
    elif char[5] == 'b':
        return 'h'
    elif char[5] == 'c':
        return 'd'
    elif char[5] == 'd':
        return 'c'

def identN(char):
    char = hex(ord(char))
    num = int(char[6], 16)
    return num

def deal(lst):
    player = 0
    game = [[], [], [], []]
    for card in lst:
        game[player].append(card)
        player += 1
        if player == 4:
            player = 0
    return game

def shuffle(lst):
    deck = []
    while len(deck) != 52:
        randIndex = random.randint(0, len(lst)-1)
        deck.append(lst[randIndex])
        del lst[randIndex]
    return deck

def int_deck():
    deck = []
    badchar = [ord('🃏'),ord('🃐'),ord('🃀'),ord('🂿'),ord('🂯'),ord('🂰'),ord('🃜'),ord('🃌'),ord('🂼'),ord('🂬')]
    char = ord('🂡')
    while char <= ord('🃞'):
        if char not in badchar:
            deck.append(chr(char))
        char += 1
    return deck

main()
