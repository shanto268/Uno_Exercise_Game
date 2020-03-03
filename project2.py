#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:32:05 2020

@author: sshanto
Need to do: zero instruction, deletion of action cards
"""
import random

class Card:
    def __init__(self):
        self.count = 0
        self.special = ["wild", "wild four"]
        self.colors = ["red","blue","yellow","green"]
        self.numbers = ["zero", "one", "two", "three", "four", "five","six","seven", "eight", "nine", "skip", "reverse", "draw two"]
        self.cindex = random.randint(0,len(self.colors)-1)
        self.rindex = random.randint(0,len(self.numbers)-1)
    
    def getRandomCard(self):
        i = random.randint(0,1)
        if random.random() <= 0.075:
            return self.special[i]
        else:
            return self.colors[self.cindex], self.numbers[self.rindex]
        
    def getCardsByColor(self, color):
        k = 0
        c = []
        while k < 2: 
            for i in self.numbers:
                temp = color,i
                c.append(temp)
            k+=1
        c.remove(c[0])
        return c
    
    def getSpecialCards(self):
        k = 0
        c = []
        while k < 4:
            c.append(self.special[0])
            c.append(self.special[1])
            k+=1
        return c
    
class Deck:
    def __init__(self):
        self.cards = []
        self.card = Card()
        self.deck = self.getDeck()
        self.discardPile = []
        
    def getDeck(self):
        deck = self.card.getCardsByColor("green")+self.card.getCardsByColor("blue") + self.card.getCardsByColor("red")+self.card.getCardsByColor("yellow") +self.card.getSpecialCards()
        return deck
    
    def shuffleDeck(self, deck):
        random.shuffle(deck)
        self.deck = deck
        return deck    
    
    def showDeck(self):
        print(self.deck)
        print()
    
    def showDeckNumber(self):
        print(len(self.deck))
        print()
        
        
    def showDiscardPile(self):
        print(self.discardPile)
    
class Hand:
    def __init__(self, deck, Deck, Card):
        self.deck = deck
        self.hand = []
        self.Deck = Deck
        self.Card = Card
        self.blueCards = []
        self.greenCards = []
        self.redCards = []
        self.yellowCards = []
        self.specialCards = []
        
    def getHand(self):
        i = 0
        h = []
        while i != 7:
            h.append(self.deck[i])
        #    self.deck.remove(self.deck[i])
        #    self.Deck.discardPile.append(self.deck[i])
            i+=1
       # self.discardCards(h)
        return h
    
    def sortByColor(self, hand):
        for i in hand:
            if len(i) == 2:
                col = i[0]
                if col=="blue":
                    self.blueCards.append(i)
                elif col=="green":
                    self.greenCards.append(i)
                elif col=="red":
                    self.redCards.append(i)
                elif col=="yellow":
                    self.yellowCards.append(i)
            else:
                self.specialCards.append(i)
        return hand
    
    def sortByRank(self, cards, dict_val):
        norm = []
        spec = []
        sorted_hand = []
        for card in cards:
            if card[1] in dict_val:
                norm.append(card)
            else:
                spec.append(card)
        sorted_hand.append(norm) 
        sorted_hand.append(spec)
        return sorted_hand
        
    def sortedHand(self, sorted_blue_cards, sorted_green_cards, sorted_red_cards,sorted_yellow_cards):
        arrangedHand = []
        arrangedHand.append(sorted_blue_cards) 
        arrangedHand.append(sorted_green_cards)
        arrangedHand.append(sorted_red_cards)
        arrangedHand.append(sorted_yellow_cards)
        arrangedHand.append(self.specialCards)
        return arrangedHand
        
    def skipAction(self,hand,col):
        print()
        
    def reverseAction(self,hand,col):
        print()  
    
    def draw2Action(self,hand,col):
        print()
    
    def wildAction(self,hand,col):
        print()
    
    def wild4Action(self,hand,col):
        print()
        
    def statsGenerte(self,hand):
        print()
    
    def sortBySpecial(self, z):
        x = ["skip", "reverse", "draw 2"]
        sindex = []
        dindex = []
        rindex = []
        for i in range(len(z)):
            if z[i] == x[0]:
                sindex.append([z[i]])
            elif z[i] == x[1]:
                dindex.append([z[i]])
            else:
                rindex.append([z[i]])
        zsort = sindex + dindex + rindex
        return zsort 
        
    def calculateExercise(self,hand,dict_col,dict_val):
        self.sortByColor(hand)     
        new_hand = self.sortedHand(self.sortByRank(self.blueCards, dict_val),self.sortByRank(self.greenCards, dict_val), self.sortByRank(self.redCards, dict_val),self.sortByRank(self.yellowCards, dict_val))
        wilds = new_hand[4]
        print(new_hand)
        print()
        print("The results to be passed to the Player/Main class")
        print()
        for i in range(len(new_hand)):
            if len(new_hand[i]) == 2 and i !=4: #all non special colored cards
                times = 0
                spec = ""
                exercise = ""
                colr = ""
                coler = ""
                spectemp = []
                for j in range(len(new_hand[i][0])):
                    colr = new_hand[i][0][j][0]
                    exercise = dict_col[new_hand[i][0][j][0]]
                    times += dict_val[new_hand[i][0][j][1]]
                for k in range(len(new_hand[i][1])):
                    coler = new_hand[i][1][k][0]
                    spec = new_hand[i][1][k][1]
                    spectemp.append(spec)
                spec = self.sortBySpecial(spectemp)
                cin = len(colr) - len(coler)
                if cin >= 0:
                    color = colr
                else:
                    color = coler
          #      print(new_hand[i])
                self.determineExercise(exercise,new_hand[i][0],spec,color, dict_val,new_hand[i])    
                #action of wild cards
        print()
        print("Action of wild cards have not been implemented yet!")
        
    def determineExercise(self,exercise,reps,spec,color,dict_val,cards):    
        brake = False
        times = 0
        for i in range(len(reps)):
            if reps[i][1] != "zero":
                times += dict_val[reps[i][1]]
            else:
                brake = True
        if len(spec) != 0:
            instr = spec.pop(0)[0]
            if instr == "skip":
                times = 0
                self.discardCards(cards)
           #     print()
            elif instr == "reverse":
                times = -1
                #put back cards to the bottom of the game pile
            else:
                times = 2*times
        results = [color, exercise,times,brake]
        print(results)
        
        
    def discardCards(self, cards):
        for i in range(len(cards)):
            for j in range(len(cards[i])):
                self.Deck.discardPile.append(cards[i][j])
                self.deck.remove(cards[i][j])
            
    def doExercise(self, exercise,times,wilds):
        if exercise != "" :
                print("Do " + exercise + " " +str(times) + " times!" )
        print()
            
    def addColoredCards(self, cards):
        print()
        """
        for i in hand:
            if len(i) == 2:
                num = i[1]
                col = i[0]
                if num in dict_val:
                    print(num+" "+str(dict_val[num]))
                    print()
            else:
                print(i)
        """
    
    def interpretHand(self, hand):
        color = self.Card.colors
        val = self.Card.numbers
        exercise = ["Sit Ups", "Push Ups", "Squat", "Lounges"]  
        #access execrcise x = exc_col_dict[color]              
        exc_col_dict = {}
        reps = {}
        for i in range(len(color)):
            exc_col_dict[color[i]] = exercise[i]
        for i in range(10):
            reps[val[i]] = i
        self.calculateExercise(hand, exc_col_dict, reps)
    
    def showSortedHand(self, hand):
        color = self.Card.colors
        val = self.Card.numbers
        exercise = ["Sit Ups", "Push Ups", "Squat", "Lounges"]  
        dict_col = {}
        dict_val = {}
        for i in range(len(color)):
            dict_col[color[i]] = exercise[i]
        for i in range(10):
            dict_val[val[i]] = i
        self.sortByColor(hand)     
        new_hand = self.sortedHand(self.sortByRank(self.blueCards, dict_val),self.sortByRank(self.greenCards, dict_val), self.sortByRank(self.redCards, dict_val),self.sortByRank(self.yellowCards, dict_val))
        print(new_hand)
    
    def showHand(self):
        print(self.getHand())
        
# main function calls
c1 = Card()
d1 = Deck()
deck1 = d1.getDeck()
print("\n\n The deck is: ")
d1.showDeck()
deck2 =d1.shuffleDeck(deck1)
print("\n\n The shuffled deck is: ")
d1.showDeck()
h1 = Hand(deck2,d1,c1)
h2 = h1.getHand()
print("\n\n The hand is: ")
h1.showHand()
#print()
#h1.showSortedHand(h2)
#d1.showDeckNumber()
#d1.showDiscardPile()
#print()
print("\n\n The sorted hand is: ")
h1.interpretHand(h2)
#print()
#d1.showDiscardPile()
#print()
#h1.showHand()
