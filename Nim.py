#Nim

import random
import math

def Menu():
    quit = False
    bad_choice = True
    while bad_choice == True:
        print('\nNIP MENU:')
        print('~~~~~~~~~~~~')
        print('1 : play against an AI')
        print('2 : rules')
        print('3 : quit')

        Choice = raw_input("What would you like to do? (1/2/3) ")

        if (Choice[0] != '1' and Choice[0] != '2' and Choice[0] != '3'):
            print('The input was not a 1,2 or 3')
        else:
            bad_choice = False

    if Choice[0] == '1':
        play()
    elif Choice[0] == '2':
        rules()
    else:
        quit = True
        print 'Goodbye!'

    return quit

def InitializeHeaps():

    Heap_A = random.randint(1,12)
    Heap_B = random.randint(1,12)
    Heap_C = random.randint(1,12)

    return (Heap_A,Heap_B,Heap_C)

def rules():
    Rules_Input = -1
    print('\nNIP RULES:')
    print('~~~~~~~~~~~~')

    print ('Basic Rules:\n - There are 3 heaps with a random amount of items in each heap\n' \
        ' - You are allowed to take any amount from 1 heap per turn.' \
        '\n - The win conditions differ, dependent on which mode you are playing')
    print 'Normal: you win if you take the last item remaining'
    print('Misere: you win if you force the other player to take the last item remaining')
    print('Enter 0 when you are ready to go back to the main menu')
    while Rules_Input != 0:
        Rules_Input = raw_input('Please enter \'0\' to quit: ')
        try:
            Rules_Input = int(Rules_Input)
        except:
            pass

    Menu()

def ChooseMode():
    bad_choice = True
    while bad_choice == True:
        print('\nWhice mode would you like to play?')
        print('1 : Normal')
        print('2 : Misere')
        Mode_Choice = raw_input('Choose a mode (1/2): ')

        if (Mode_Choice != '1' and Mode_Choice != '2'):
            print('The input was not a 1 or 2')
        else:
            bad_choice = False

    #1 is Normal
    #2 is Misere

    return int(Mode_Choice)

def PrintHeap(Item_Group):

    print('\nA  |  B  |  C')
    print Item_Group['a'],'   ',Item_Group['b'],'   ',Item_Group['c']

def CheckWin(Mode,Last_Player,Before_Player,Item_Group):
    win = False

    if Item_Group['a'] + Item_Group['b'] + Item_Group['c'] == 0:
        win = True
        if Mode == 1:
            PrintHeap(Item_Group)
            print '\nThe winner is:', Last_Player,'!'
        else:
            PrintHeap(Item_Group)
            print '\nThe winner is:', Before_Player,'!'

    return win

def PlayerMove(Item_Group):
    print('\ntype \'q\' at any time to quit')
    print('\nIt is your turn')
    bad_heap = True
    x = 0

    while bad_heap == True:
        Heap_Choice = raw_input('What amount would you like to remove (ex. a2 \ b4 \ a1)')


        if Heap_Choice.lower() == 'q':
            quit = True
            break
        else:
            quit = False

        if Heap_Choice[0].lower() != 'a' and Heap_Choice[0].lower() != 'b' and Heap_Choice[0].lower() != 'c':
            bad_heap = True
        else:
            bad_heap = False

        try:
            x = int(Heap_Choice[1:3])
        except:
            try:
                x = int(Heap_Choice[1])
            except:
                bad_heap = True
                pass

        if x <= 0:
            bad_heap = True


        if bad_heap == False:

            if Item_Group[Heap_Choice[0]] - int(Heap_Choice[1]) >= 0:

                if x >= 10:
                    Item_Group[Heap_Choice[0]] = Item_Group[Heap_Choice[0]] - int(Heap_Choice[1:3])

                else:
                    Item_Group[Heap_Choice[0]] = Item_Group[Heap_Choice[0]] - int(Heap_Choice[1])
            else:
                bad_heap = True

        if bad_heap == True:
            print('The input did not work, please try again')

    return quit

def AiPlay(Item_Group,Mode):

    print('\nIt is the AI\'s turn')

    Nim_Sum = Item_Group['a']^Item_Group['b']^Item_Group['c']

    if Nim_Sum == 0:
        #There are no winnable moves unless the player makes a mistake
        for i in Item_Group:
            #remove 1 from a random heap
            if Item_Group[i] > 0:
                Item_Group[i] = (Item_Group[i] - random.randint(1,Item_Group[i]))
                break

    else:

        Temp = [Item_Group['a'],Item_Group['b'],Item_Group['c']]
        for i in range(0,Temp[0]):
            if (i^Item_Group['b']^Item_Group['c'] == 0):
                Temp[0] = i
                break

        for i in range(0,Temp[1]):
            if (Item_Group['a']^i^Item_Group['c'] == 0):
                Temp[1] = i
                break

        for i in range(0,Temp[2]):
            if (Item_Group['a']^Item_Group['b']^i == 0):
                Temp[2] = i
                break

        if max(Temp) <= 2:
            #Misere
            if Mode == 2:

                if (sum(Temp)%2) == 0:
                    if max(Temp) > 0:
                        Temp[Temp.index(max(Temp))] -= 1

            else:

                if (sum(Temp)%2) == 1:
                    Temp[Temp.index(max(Temp))] -= 1

        Item_Group['a'] = Temp[0]
        Item_Group['b'] = Temp[1]
        Item_Group['c'] = Temp[2]

def play():

    win = False
    Mode = ChooseMode()
    (Heap_A,Heap_B,Heap_C) = InitializeHeaps()
    Item_Group = {'a':Heap_A , 'b':Heap_B , 'c':Heap_C}
    quit = False

    while (win == False and quit == False):
        PrintHeap(Item_Group)
        quit = PlayerMove(Item_Group)
        win = CheckWin(Mode,'you','the AI',Item_Group)
        if (win == False and quit == False):
            PrintHeap(Item_Group)
            AiPlay(Item_Group,Mode)
            win = CheckWin(Mode,'the AI','you',Item_Group)

        if quit == True:
            print('GoodBye!')

if __name__ == '__main__':
    PlayAgain = True
    while PlayAgain == True:

        quit = Menu()

        if quit == False:
            PlayAgain = raw_input('Would you like to play again?\n' \
            ' (type \'y\' to play again, anything else will exit) ')

            if PlayAgain.lower() == 'y':
                PlayAgain = True
            else:
                PlayAgain = False
        else:
            PlayAgain = False
