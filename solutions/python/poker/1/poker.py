from collections import Counter


def best_hands(hands: list[str]) -> list[str]:
    best_rank = max(hand_rank(hand) for hand in hands)
    return [hand for hand in hands if hand_rank(hand) == best_rank]


def hand_rank(hand: str):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    rank_value = {rank: value for value, rank in enumerate(ranks)}

    cards = hand.split()
    ranks_in_hand = [card[:-1] for card in cards]
    suits_in_hand = [card[-1] for card in cards]

    counts = Counter(ranks_in_hand)
    values = sorted((rank_value[rank] for rank in ranks_in_hand), reverse=True)
    unique_values = sorted(set(values))

    is_flush = len(set(suits_in_hand)) == 1
    is_wheel = unique_values == [0, 1, 2, 3, 12]
    is_straight = len(unique_values) == 5 and (
        max(unique_values) - min(unique_values) == 4 or is_wheel
    )
    straight_high = 3 if is_wheel else max(unique_values) if is_straight else None

    if is_straight and is_flush:
        return (8, straight_high)

    if 4 in counts.values():
        quad = max(rank_value[rank] for rank, count in counts.items() if count == 4)
        kicker = max(rank_value[rank] for rank, count in counts.items() if count == 1)
        return (7, quad, kicker)

    if 3 in counts.values() and 2 in counts.values():
        three = max(rank_value[rank] for rank, count in counts.items() if count == 3)
        pair = max(rank_value[rank] for rank, count in counts.items() if count == 2)
        return (6, three, pair)

    if is_flush:
        return (5, tuple(values))

    if is_straight:
        return (4, straight_high)

    if 3 in counts.values():
        three = max(rank_value[rank] for rank, count in counts.items() if count == 3)
        kickers = tuple(
            sorted(
                (rank_value[rank] for rank, count in counts.items() if count == 1),
                reverse=True,
            )
        )
        return (3, three, kickers)

    pairs = sorted(
        (rank_value[rank] for rank, count in counts.items() if count == 2),
        reverse=True,
    )
    if len(pairs) == 2:
        kicker = max(rank_value[rank] for rank, count in counts.items() if count == 1)
        return (2, pairs[0], pairs[1], kicker)

    if len(pairs) == 1:
        kickers = tuple(
            sorted(
                (rank_value[rank] for rank, count in counts.items() if count == 1),
                reverse=True,
            )
        )
        return (1, pairs[0], kickers)

    return (0, tuple(values))