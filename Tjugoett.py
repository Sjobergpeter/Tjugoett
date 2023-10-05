import random
import os
import time

# skapar en kortlek och blandar den
def setDeck():
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ["hearts", "Diamonds", "Clubs", "Spades"]
    i = 0
    deck = []
    for rank in ranks:
        i += 1
        for suit in suits:
            card = {"rank": rank, "suit": suit, "value": i}
            deck.append(card)
    random.shuffle(deck)
    return deck

# Jämför poängen mellan spelaren och datorn och skriver ut vem vinnaren är samt vilka kort dom höll
def winnerIs():
    os.system("cls" if os.name == "nt" else "clear")
    print((".And the winner is.").center(50))
    time.sleep(0.8)
    os.system("cls" if os.name == "nt" else "clear")
    print(("..And the winner is..").center(50))
    time.sleep(0.8)
    os.system("cls" if os.name == "nt" else "clear")
    print((f"...And the winner is...").center(50))
    time.sleep(0.8)
    print(" ")

    if computer.value >= player.value:
        print ("Computer!".center(50))
        print(f"With a final score of {computer.value} against Player's {player.value}".center(50))
    else:
        print("Player!".center(50))
        print(f"With a final score of {player.value} against Computer's {computer.value}".center(50))
    
    print("*"*50)
    print("Player's hand".center(50))
    print("-"*50)

    loop = len(player.hand)

    for i in range(loop):
        time.sleep(0.5)
        print(f"{player.hand[i]['rank']} of {player.hand[i]['suit']}".center(50))

    time.sleep(0.5)
    print("*"*50)
    print("Computer's hand".center(50))
    print("-"*50)

    loop = len(computer.hand)

    for i in range(loop):
        time.sleep(0.5)
        print(f"{computer.hand[i]['rank']} of {computer.hand[i]['suit']}".center(50))

    time.sleep(0.5)
    print("-"*50)
    input("Press Enter for main menu")

# Spelarens / datorns kort i handen
class hand():
    def __init__(self, name):
        self.hand = []
        self.value = 0
        self.aceValue = 22
        self.name = name

    # plockar upp det övre kortet i kortleken in i handen
    def PickACard(self, card):
        self.hand.append(card)
        self.value += card['value']
        if card['rank'] == "Ace":
            self.aceValue = self.value + 13
        del deck[0]
    
    # Efter spelaren / datorn plockar kort körs denna funktion som kollar om man får för mycket i handen och skriver ut nuvarande poäng och kort i handen
    def printHand(self):
        if self.value > 21:
            print(f"{self.name} picked up {self.hand[-1]['rank']} of {self.hand[-1]['suit']} and lost with {self.value}")
            print(f"{self.name} lost")
            print("-"*40)

            print(f"{self.name}'s hand was")
            for cards in self.hand:
                print(f"{cards['rank']} of {cards['suit']}")
            print("-"*40)

            input("Press Enter to continue")

        else:
            if self.aceValue <= 21:
                self.aceValue = self.value + 13
                
            if self.aceValue <= 21:
                    print(f"{self.name} have {self.value} or {self.aceValue}")

            else:
                print(f"{self.name} have {self.value}")
            
            if len(self.hand) > 1:
                print("-"*40)
                print(f"{self.name} is holding:")

                for cards in self.hand:
                    print(f"{cards['rank']} of {cards['suit']}")
            print("-"*40)


       # Programmet börjar, skapar en hand för spelare och dator och skapar kortlek. topCard pekar på det första / översta kortet i kortleken.
       # Låter användaren välja om man ska spela, se regler eller stänga av
while True:
    player = hand("Player")
    computer = hand("Computer")
    deck = setDeck()
    topCard = deck[0]

    os.system("cls" if os.name == "nt" else "clear")
    print(".:              Twentyone             :.")
    print("-"*40)
    print("Welcome to a game of Twentyone")
    print("-"*40)
    print("Rules / Start / Exit")
    
    user_input = input("> ")
    if user_input.lower() == "rules":
        os.system("cls" if os.name == "nt" else "clear")
        print("""the user receives one card at a time and after each card, they decide whether they wantto pick another card or not.

The goal for the user is to try to get the sum of the card values as close to 21 as possible without exceeding this number.

Aces can be counted as either 1 or 14.

If the user goes over 21, they lose, and the computer wins.

If the user decides to stop under 21, the computer also draws one card at a time and after each card decides whether to continue or not.

If the computer gets more than 21 points or fewer points than the user, the user wins. Otherwise, the computer wins.
""")
        input("Press Enter to continue")
        continue
    
    elif user_input.lower() == ("start"):
        #
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"You picked up {topCard['rank']} of {topCard['suit']}")
            print("-"*40)
            player.PickACard(topCard)
            topCard = deck[0]
            player.printHand()

            if player.value > 21:
                break

            while True:
                user_input = input("Do you want to pick another card? y/n > ")
                if user_input.lower() == "y" or user_input.lower() == "n":
                    break
                else:
                    continue

            if user_input.lower() == "y":
                continue
    
        
            elif user_input.lower() == "n":
                if player.aceValue > player.value and player.aceValue <= 21:
                    player.value = player.aceValue

            os.system("cls" if os.name == "nt" else "clear")
            print("Computer's turn!")
            print("-"*40)
            input("Press Enter to continue!")

            # Efter spelaren väljer att inte plocka ett nytt kort så börjar datorn spela här
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                computer.PickACard(topCard)
                print(f"Computer picks a card, it's {topCard['rank']} of {topCard['suit']}")
                topCard = deck[0]
                print("-"*40)
                computer.printHand()
                
                # Får datorn över 21 vinner Spelaren och spelet avslutas
                if computer.value > 21:
                    break

                    # Får datorn värdet 19-21 av Ess (Värde 14) så stannar datorn och sedan annonseras vinnaren
                elif computer.aceValue >= 19 and computer.aceValue <= 21:
                    print("Computer stops at", computer.aceValue, "on Ace")
                    computer.value = computer.aceValue
                    input("Press Enter to continue!")
                    winnerIs()
                    break

                    #Får datorn 17 - 21 så stannar datorn, (Då är Ess värt 1, om Ess finns i handen) och sedan annonseras vinnaren
                elif computer.value >= 17:
                    print ("Computer stops at", computer.value)
                    input("Press Enter to continue!")
                    winnerIs()
                    break

                input("Press Enter to continue!")
                
            
            break

    elif user_input.lower() == "exit":
        break

    continue