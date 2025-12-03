import os
def winner(find_bidder):
    highest_bid=0
    for i in find_bidder:
        highest=find_bidder[i]
        if highest>highest_bid:
            highest_bid=highest
            winner=i
    print(f"Here the details of other bidder name & amount {find_bidder}")
    print(f"The winner is {winner} with a bid of {highest_bid}")





game_over=False
bidding={}
while not game_over:
    name=input("Enter your name: ")
    bid=int(input("Enter your bid amount: "))
    bidding[name]=bid
    another=input("is there another bidder YES/NO: ")
    if another=="NO" or another=="no":
        game_over=True
        winner(bidding)
    elif another=="YES" or another=="yes":
        os.system('cls')
    else:
        break
