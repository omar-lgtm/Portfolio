# Author: Syed Muhammad Omar Bukhari 
# Program: Solitaire Game Implementation
# This program implements a simple version of Solitaire using the CardPile and Solitaire classes. The player moves cards between piles until the game is won.

class CardPile:
    def __init__(self):
        self.items = []

    def add_top(self, item):
        self.items.insert(0, item)

    def add_bottom(self, item):
        self.items.append(item)

    def remove_top(self):
        if self.items:
            return self.items.pop(0)

    def remove_bottom(self):
        if self.items:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def peek_top(self):
        if self.items:
            return self.items[0]

    def peek_bottom(self):
        if self.items:
            return self.items[-1]

    def print_all(self, index):
        if self.size() == 0:
            print()
            return
        if index == 0:
            print(self.items[0], *["*" for _ in range(1, len(self.items))])
        else:
            print(*self.items)


class Solitaire:
    def __init__(self, cards):
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = self.num_cards * 2
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])

    def display(self):
        for i in range(self.num_piles):
            print(f"{i}:", end=" ")
            self.piles[i].print_all(i)

    def move(self, p1, p2):
        if p1 == 0 and p2 == 0:
            if self.piles[0].size() > 0:
                card = self.piles[0].remove_top()
                self.piles[0].add_bottom(card)

        elif p1 == 0 and p2 > 0:
            if self.piles[0].size() == 0:
                return
            card1 = self.piles[0].peek_top()
            if self.piles[p2].size() == 0 or card1 == self.piles[p2].peek_bottom() - 1:
                self.piles[p2].add_bottom(self.piles[0].remove_top())

        elif p1 > 0 and p2 > 0:
            if self.piles[p1].size() == 0 or self.piles[p2].size() == 0:
                return
            card1 = self.piles[p1].peek_top()
            card2 = self.piles[p2].peek_bottom()
            if card1 == card2 - 1:
                while self.piles[p1].size() > 0:
                    self.piles[p2].add_bottom(self.piles[p1].remove_top())

    def is_complete(self):
        if self.piles[0].size() != 0:
            return False
        count_non_empty = 0
        for i in range(1, self.num_piles):
            if self.piles[i].size() > 0:
                count_non_empty += 1
        return count_non_empty == 1

    def play(self):
        print("********************** NEW GAME *****************************")
        move_number = 1
        while move_number <= self.max_num_moves and not self.is_complete():
            self.display()
            print("Round", move_number, "out of", self.max_num_moves, end=": ")
            pile_a = int(input("Move from pile no.: "))
            print("Round", move_number, "out of", self.max_num_moves, end=": ")
            pile_b = int(input("Move to pile no.: "))
            if pile_a >= 0 and pile_b >= 0 and pile_a < self.num_piles and pile_b < self.num_piles:
                self.move(pile_a, pile_b)
            move_number += 1

        if self.is_complete():
            print("You Win in", move_number - 1, "steps!\n")
        else:
            print("You Lose!\n")
