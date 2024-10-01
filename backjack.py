# This code will run through a simple game of blackjack. Some code
# has already been provided for you, which you will not need to modify
# (most of it involved concepts we haven't yet learned)

#Create the deck and shuffle it
import random
deck = ["AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC",
         "AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD",
         "AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH",
         "AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS"]
random.shuffle(deck)
random.shuffle(deck)
random.shuffle(deck)
random.shuffle(deck)

#A function that deals the cards. It takes the deck, and returns the card,
# and a new deck that is now missing the dealt card. You will not need to modify it.
def deal(cards):
    return cards[0], cards[1:]

#Write a function that takes in a card label (a string) and returns the blackjack value
#Jacks, Queens, and Kinds are worth 10; Aces are worth 11; all others are worth their value
def value(card):
    cardNumber = label[:-1] #this gets just the number of the card, eliminating the suit
    ###YOUR CODE HERE###

#Calculate the score of a total of 2-5 cards. You will need to determine what the parameters are
def calculateScore("""???"""):
    ###YOUR CODE HERE###

#A function to print out the current situation. You will need to determine the parameters.
# The format should be:
## Your cards are:
## Card1
## Card2
## Card 3 (if applicable)
## Card 4 (if applicable)
## Card 5 (if applicable)
## The dealer has:
## DealerCard
def printCurrentSit("""???"""):
    ###YOUR CODE HERE###

#Function to determine the winner based on total scores (yours and the dealer's).
#Remember if one person is over 21, the other wins.
#If both are at 21 or under, the higher score wins
#In the case of a tie or both players over 21, no one wins
#Should return "you", "the dealer", or "no one" for the winner
#You will need to determine the parameters
def determineWinner("""???"""):
    ###YOUR CODE HERE###

print("Let's play Blackjack!")
#Deal 2 cards to yourself and one to the dealer.
# The first card is dealt to you below as an example
yours1, deck = deal(deck)


#Print the current situation
#Determine if your score is already over 21. If it is, print
#"I'm sorry, you went over 21 and lost the game!"
#Otherwise, ask the user if they want to stand or hit
#By default, if they input anything other than "stand", assume they want to hit

#If they want to hit, deal them an additional card and repeat the above pieces
#(print situation, determine if score is over, ask if want to stand or hit)

#If somehow a player has 5 cards and is still not over 21, DO NOT ask if they want to
#stand or hit. Instead, print
#"You have reached the card maximum."
#and move to the end of the game


##END OF GAME

print("Your final total was:")
#print user score here

print("The dealer's second card was:")
#Deal a card to the dealer, and print out what that card is

print("So the dealer's total was:")
#Calculate and print the dealer's score

#Determine the winner and print out who won, in the format
#"The winner is _____!"



