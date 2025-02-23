from typing import List

from app.rpc.gen.rustic_poker_pb2 import Card


def str_to_card(card_str: str) -> Card:
    card_str = card_str.upper()
    if len(card_str) < 2 or len(card_str) > 3:
        raise Exception(f"Invalid card string length: {card_str}")

    rank_str = card_str[:-1]
    suit_str = card_str[-1]

    rank_mapping = {
        "A": Card.CardRank.Ace,
        "K": Card.CardRank.King,
        "Q": Card.CardRank.Queen,
        "J": Card.CardRank.Jack,
        "10": Card.CardRank.Ten,
        "9": Card.CardRank.Nine,
        "8": Card.CardRank.Eight,
        "7": Card.CardRank.Seven,
        "6": Card.CardRank.Six,
        "5": Card.CardRank.Five,
        "4": Card.CardRank.Four,
        "3": Card.CardRank.Three,
        "2": Card.CardRank.Two,
    }

    try:
        rank = rank_mapping.get(rank_str)
        if rank is None:
            raise Exception(f"Invalid rank: {rank_str}")
    except ValueError:
        raise Exception(f"Invalid rank format: {rank_str}")

    if suit_str == "H":
        suit = Card.CardSuit.Hearts
    elif suit_str == "D":
        suit = Card.CardSuit.Diamonds
    elif suit_str == "C":
        suit = Card.CardSuit.Clubs
    elif suit_str == "S":
        suit = Card.CardSuit.Spades
    else:
        raise Exception(f"Invalid suit: {suit_str}")

    return Card(rank=rank, suit=suit)


def str_to_cards(cards_str: str) -> List[Card]:
    card_strs = cards_str.split()
    cards = []
    for card_str in card_strs:
        try:
            card = str_to_card(card_str)
            cards.append(card)
        except Exception as err:
            raise Exception(f"Invalid card string '{card_str}': {err}")
    return cards
