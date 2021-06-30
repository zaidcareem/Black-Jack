import random

heart_list = ["h_ace", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hK", "hQ", "hJ"]
spade_list = ["s_ace", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sK", "sQ", "sJ"]
diamond_list = ["d_ace", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dK", "dQ", "dJ"]
club_list = ["c_ace", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cK", "cQ", "cJ"]

card_pack = heart_list + spade_list + diamond_list + club_list

h = {}
s = {}
d = {}
c = {}


def card_points(card_list, dictionary):
    i = 0
    while i <= 9:
        dictionary[card_list[i]] = i + 1
        i += 1
    j = 9
    while 9 <= j < len(card_list):
        dictionary[card_list[j]] = 10
        j += 1


class Color:

    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def bj__start():

    global objct

    class Player:

        def __init__(self, cards):
            self.cards = cards

    print(
        Color.DARKCYAN + Color.BOLD + "\n\n\n\n            =========================================================== TWO PLAYER LIMITED GAME ==========================================================\n" + Color.END)
    t = 1
    dealer = Player([])
    while t == 1:
        objct = Player([])
        t += 1
    print(Color.BLUE + Color.BOLD + "\n\n            ===========================================================  WELCOME TO" + Color.END, end=" ")
    print(Color.YELLOW + Color.BOLD + "BLACK JACK " + Color.END, end=" ")
    print(Color.BLUE + Color.BOLD + "===========================================================\n\n" + Color.END)

    random.shuffle(card_pack)

    def play():

        g = {}
        card_points(heart_list, h)
        card_points(spade_list, s)
        card_points(diamond_list, d)
        card_points(club_list, c)
        h.update(s)
        h.update(d)
        h.update(c)
        g.update(h)
        money = float(input(Color.CYAN + "\nEnter your amount: "))
        f = 1
        while len(card_pack) > 3 or money >= 0:

            if money <= 0:
                print(Color.BOLD + "You are bankrupt".center(201))
                print(Color.BOLD + Color.RED + "GAME OVER".center(201) + Color.END)
                break

            print(
                "\n\n" + f"--------------------------------------------------------------- Round: {f} ---------------------------------------------------------------".center(
                    190))
            f += 1
            bet = float(input("Enter your bet: "))
            while bet > money:
                print("\n\n$$$$$$ Bet should be lesser than the money you have now $$$$$$")
                bet = float(input("Enter your bet: "))
            else:
                pass

            money -= bet
            print("\nmoney at hand: $ " + str(money))
            objct.cards.append(card_pack[-1])
            p = g.get(card_pack[-1])
            card_pack.pop()
            dealer.cards.append(card_pack[-1])
            x = g.get(card_pack[-1])
            card_pack.pop()
            objct.cards.append(card_pack[-1])
            m = g.get(card_pack[-1])
            card_pack.pop()

            print("\nPlayer cards : ")
            print(objct.cards)
            if p == 1 or m == 1:
                r = int(input("Enter the value of your ace, 1 or 11: "))
                if p == 1:
                    p = r
                elif m == 1:
                    m = r
            score = p + m
            d_score = x
            print("                                            Your score            : " + str(score) + "\n")
            print("\nDealers cards: ")
            print(dealer.cards)
            print("                                            Dealers partial score : " + str(d_score) + "\n")

            k = input("Enter \"h\" to Hit or any other character to stand: ")
            if k == "h" and len(card_pack) > 0:
                while k == "h":
                    objct.cards.append(card_pack[-1])
                    print("\nNew card: " + objct.cards[-1])
                    u = g.get(card_pack[-1])
                    print(objct.cards)
                    if u == 1:
                        e = int(input("Enter the value of your ace: "))
                        u = e
                    score += u
                    print("                                            Your score            : " + str(score) + "\n")
                    card_pack.pop()
                    if score >= 21:
                        break
                    q = input("Do you want to Hit again? y/n? :")
                    if q == "n":
                        break
                    else:
                        pass
                    objct.cards.clear()
            objct.cards.clear()

            dealer.cards.append(card_pack[-1])
            y = g.get(card_pack[-1])
            card_pack.pop()
            print("Dealers cards: ")
            print(dealer.cards)
            if (y == 1 and x == 10) or (x == 1 and y == 10):
                d_score = 21
            elif y == 1 and d_score < score:
                y = 11
            elif x == 1 and d_score < score:
                x = 11
            d_score = y + x
            print("                                            Dealers score         : " + str(d_score) + "\n")
            dealer.cards.clear()

            if score > 21:
                print(Color.BOLD + "You are bust, bet lost!".center(201) + Color.END)
            else:

                if score == 21:
                    print(Color.YELLOW + Color.BOLD + "---------- YOU GOT BLACKJACK !!! ----------".center(201))
                    award = bet * 2.5
                    money += award
                    print(Color.CYAN + "You win " + str(award))

                elif score >= d_score:
                    print("\nPlayer wins the round\n")
                    award = bet * 2
                    money += award
                    print("You win " + str(award))

                elif score < d_score:
                    print("\nPlayer loses the round\n")
                    print("Bet lost")

                elif d_score == 21:
                    print(Color.BOLD + "Dealer won BLACKJACK !!!")
                    print("Bet lost")

            print(Color.CYAN + "\n>>>>>> Money at round's end: $ " + str(money))

    play()


bj__start()
