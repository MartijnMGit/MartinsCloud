import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def adjust_for_ace(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return hand

def compare_scores(player_score, pc_score):
    if player_score > 21:
        return "You went over. You lose 😭"
    elif pc_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > pc_score:
        return "You win! 🎉"
    elif player_score < pc_score:
        return "You lose 😞"
    else:
        return "It's a draw 😐"
