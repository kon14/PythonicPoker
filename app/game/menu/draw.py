from app.rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from app.rpc import respond_drawing_phase_rpc
from app.utils import str_to_cards
from ..player import PlayerIdentity


def draw_menu(
    stub: RusticPokerStub,
    player: PlayerIdentity,
):
    discard: bool or None = None
    while discard is None:
        choice = input("Discard cards (y/n):\t").strip().lower()
        if choice == 'y':
            discard = True
        if choice == 'n':
            discard = False

    try:
        discarded_cards = []
        if discard:
            discarded_cards = get_discarded_cards()
            print(discarded_cards)
        respond_drawing_phase_rpc(stub, player, discarded_cards)

    except Exception as err:
        print(f"Error:\n{err}")
        return

    print("Cards discarded successfully!")


def get_discarded_cards():
    cards_str = input('Specify cards to discard (ex: "AS 10C JD"):\n')
    return str_to_cards(cards_str)
