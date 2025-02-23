from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LobbyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IDLE: _ClassVar[LobbyStatus]
    MATCHMAKING: _ClassVar[LobbyStatus]
    IN_GAME: _ClassVar[LobbyStatus]
IDLE: LobbyStatus
MATCHMAKING: LobbyStatus
IN_GAME: LobbyStatus

class ConnectRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LobbyInfoPublic(_message.Message):
    __slots__ = ('lobby_id', 'name', 'host_player_id', 'player_count', 'status')
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    lobby_id: str
    name: str
    host_player_id: str
    player_count: int
    status: LobbyStatus

    def __init__(self, lobby_id: _Optional[str]=..., name: _Optional[str]=..., host_player_id: _Optional[str]=..., player_count: _Optional[int]=..., status: _Optional[_Union[LobbyStatus, str]]=...) -> None:
        ...

class GameState(_message.Message):
    __slots__ = ('player_state', 'lobby_state', 'match_state', 'timestamp')

    class MatchState(_message.Message):
        __slots__ = ('match_id', 'player_info', 'credit_pots', 'own_cards', 'player_bet_amounts', 'poker_phase', 'can_i_act')

        class PlayerInfoEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: GameState.MatchState.MatchStatePlayerPublicInfo

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[GameState.MatchState.MatchStatePlayerPublicInfo, _Mapping]]=...) -> None:
                ...

        class CreditPotsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: GameState.MatchState.MatchStateCreditPot

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[GameState.MatchState.MatchStateCreditPot, _Mapping]]=...) -> None:
                ...

        class PlayerBetAmountsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int

            def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
                ...

        class MatchStatePlayerPublicInfo(_message.Message):
            __slots__ = ('player_id', 'starting_credits', 'remaining_credits', 'pot_credits', 'hand_card_count')

            class PotCreditsEntry(_message.Message):
                __slots__ = ('key', 'value')
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: int

                def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
                    ...
            PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
            STARTING_CREDITS_FIELD_NUMBER: _ClassVar[int]
            REMAINING_CREDITS_FIELD_NUMBER: _ClassVar[int]
            POT_CREDITS_FIELD_NUMBER: _ClassVar[int]
            HAND_CARD_COUNT_FIELD_NUMBER: _ClassVar[int]
            player_id: str
            starting_credits: int
            remaining_credits: int
            pot_credits: _containers.ScalarMap[str, int]
            hand_card_count: int

            def __init__(self, player_id: _Optional[str]=..., starting_credits: _Optional[int]=..., remaining_credits: _Optional[int]=..., pot_credits: _Optional[_Mapping[str, int]]=..., hand_card_count: _Optional[int]=...) -> None:
                ...

        class MatchStateCreditPot(_message.Message):
            __slots__ = ('pot_id', 'is_main_pot', 'total_credits', 'player_credits')

            class PlayerCreditsEntry(_message.Message):
                __slots__ = ('key', 'value')
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: int

                def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
                    ...
            POT_ID_FIELD_NUMBER: _ClassVar[int]
            IS_MAIN_POT_FIELD_NUMBER: _ClassVar[int]
            TOTAL_CREDITS_FIELD_NUMBER: _ClassVar[int]
            PLAYER_CREDITS_FIELD_NUMBER: _ClassVar[int]
            pot_id: str
            is_main_pot: bool
            total_credits: int
            player_credits: _containers.ScalarMap[str, int]

            def __init__(self, pot_id: _Optional[str]=..., is_main_pot: bool=..., total_credits: _Optional[int]=..., player_credits: _Optional[_Mapping[str, int]]=...) -> None:
                ...
        MATCH_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_INFO_FIELD_NUMBER: _ClassVar[int]
        CREDIT_POTS_FIELD_NUMBER: _ClassVar[int]
        OWN_CARDS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_BET_AMOUNTS_FIELD_NUMBER: _ClassVar[int]
        POKER_PHASE_FIELD_NUMBER: _ClassVar[int]
        CAN_I_ACT_FIELD_NUMBER: _ClassVar[int]
        match_id: str
        player_info: _containers.MessageMap[str, GameState.MatchState.MatchStatePlayerPublicInfo]
        credit_pots: _containers.MessageMap[str, GameState.MatchState.MatchStateCreditPot]
        own_cards: _containers.RepeatedCompositeFieldContainer[Card]
        player_bet_amounts: _containers.ScalarMap[str, int]
        poker_phase: GameState.PokerPhase
        can_i_act: bool

        def __init__(self, match_id: _Optional[str]=..., player_info: _Optional[_Mapping[str, GameState.MatchState.MatchStatePlayerPublicInfo]]=..., credit_pots: _Optional[_Mapping[str, GameState.MatchState.MatchStateCreditPot]]=..., own_cards: _Optional[_Iterable[_Union[Card, _Mapping]]]=..., player_bet_amounts: _Optional[_Mapping[str, int]]=..., poker_phase: _Optional[_Union[GameState.PokerPhase, _Mapping]]=..., can_i_act: bool=...) -> None:
            ...

    class PokerPhase(_message.Message):
        __slots__ = ('ante', 'dealing', 'first_betting', 'drawing', 'second_betting', 'showdown')

        class PokerPhaseBetting(_message.Message):
            __slots__ = ('highest_bet_amount', 'own_bet_amount')
            HIGHEST_BET_AMOUNT_FIELD_NUMBER: _ClassVar[int]
            OWN_BET_AMOUNT_FIELD_NUMBER: _ClassVar[int]
            highest_bet_amount: int
            own_bet_amount: int

            def __init__(self, highest_bet_amount: _Optional[int]=..., own_bet_amount: _Optional[int]=...) -> None:
                ...

        class PokerPhaseDrawing(_message.Message):
            __slots__ = ('discard_stage', 'own_discarded_cards')
            DISCARD_STAGE_FIELD_NUMBER: _ClassVar[int]
            OWN_DISCARDED_CARDS_FIELD_NUMBER: _ClassVar[int]
            discard_stage: bool
            own_discarded_cards: _containers.RepeatedCompositeFieldContainer[Card]

            def __init__(self, discard_stage: bool=..., own_discarded_cards: _Optional[_Iterable[_Union[Card, _Mapping]]]=...) -> None:
                ...

        class PokerPhaseShowdown(_message.Message):
            __slots__ = ('results',)

            class ShowdownResults(_message.Message):
                __slots__ = ('winning_rank', 'winner_ids', 'pot_distribution')

                class PokerHandRank(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    RoyalFlush: _ClassVar[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank]
                    StraightFlush: _ClassVar[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank]
                    FourOfAKind: _ClassVar[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank]
                    FullHouse: _ClassVar[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank]
                    Flush: _ClassVar[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank]
                    Straight: _ClassVar[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank]
                    ThreeOfAKind: _ClassVar[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank]
                    TwoPair: _ClassVar[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank]
                    Pair: _ClassVar[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank]
                    HighCard: _ClassVar[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank]
                RoyalFlush: GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank
                StraightFlush: GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank
                FourOfAKind: GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank
                FullHouse: GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank
                Flush: GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank
                Straight: GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank
                ThreeOfAKind: GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank
                TwoPair: GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank
                Pair: GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank
                HighCard: GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank

                class ShowdownPotDistribution(_message.Message):
                    __slots__ = ('pot_id', 'player_ids', 'total_credits', 'credits_per_winner')
                    POT_ID_FIELD_NUMBER: _ClassVar[int]
                    PLAYER_IDS_FIELD_NUMBER: _ClassVar[int]
                    TOTAL_CREDITS_FIELD_NUMBER: _ClassVar[int]
                    CREDITS_PER_WINNER_FIELD_NUMBER: _ClassVar[int]
                    pot_id: str
                    player_ids: _containers.RepeatedScalarFieldContainer[str]
                    total_credits: int
                    credits_per_winner: int

                    def __init__(self, pot_id: _Optional[str]=..., player_ids: _Optional[_Iterable[str]]=..., total_credits: _Optional[int]=..., credits_per_winner: _Optional[int]=...) -> None:
                        ...
                WINNING_RANK_FIELD_NUMBER: _ClassVar[int]
                WINNER_IDS_FIELD_NUMBER: _ClassVar[int]
                POT_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
                winning_rank: GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank
                winner_ids: _containers.RepeatedScalarFieldContainer[str]
                pot_distribution: _containers.RepeatedCompositeFieldContainer[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.ShowdownPotDistribution]

                def __init__(self, winning_rank: _Optional[_Union[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank, str]]=..., winner_ids: _Optional[_Iterable[str]]=..., pot_distribution: _Optional[_Iterable[_Union[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.ShowdownPotDistribution, _Mapping]]]=...) -> None:
                    ...
            RESULTS_FIELD_NUMBER: _ClassVar[int]
            results: GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults

            def __init__(self, results: _Optional[_Union[GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults, _Mapping]]=...) -> None:
                ...
        ANTE_FIELD_NUMBER: _ClassVar[int]
        DEALING_FIELD_NUMBER: _ClassVar[int]
        FIRST_BETTING_FIELD_NUMBER: _ClassVar[int]
        DRAWING_FIELD_NUMBER: _ClassVar[int]
        SECOND_BETTING_FIELD_NUMBER: _ClassVar[int]
        SHOWDOWN_FIELD_NUMBER: _ClassVar[int]
        ante: _empty_pb2.Empty
        dealing: _empty_pb2.Empty
        first_betting: GameState.PokerPhase.PokerPhaseBetting
        drawing: GameState.PokerPhase.PokerPhaseDrawing
        second_betting: GameState.PokerPhase.PokerPhaseBetting
        showdown: GameState.PokerPhase.PokerPhaseShowdown

        def __init__(self, ante: _Optional[_Union[_empty_pb2.Empty, _Mapping]]=..., dealing: _Optional[_Union[_empty_pb2.Empty, _Mapping]]=..., first_betting: _Optional[_Union[GameState.PokerPhase.PokerPhaseBetting, _Mapping]]=..., drawing: _Optional[_Union[GameState.PokerPhase.PokerPhaseDrawing, _Mapping]]=..., second_betting: _Optional[_Union[GameState.PokerPhase.PokerPhaseBetting, _Mapping]]=..., showdown: _Optional[_Union[GameState.PokerPhase.PokerPhaseShowdown, _Mapping]]=...) -> None:
            ...
    PLAYER_STATE_FIELD_NUMBER: _ClassVar[int]
    LOBBY_STATE_FIELD_NUMBER: _ClassVar[int]
    MATCH_STATE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    player_state: PlayerState
    lobby_state: LobbyState
    match_state: GameState.MatchState
    timestamp: _timestamp_pb2.Timestamp

    def __init__(self, player_state: _Optional[_Union[PlayerState, _Mapping]]=..., lobby_state: _Optional[_Union[LobbyState, _Mapping]]=..., match_state: _Optional[_Union[GameState.MatchState, _Mapping]]=..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class PlayerState(_message.Message):
    __slots__ = ('player_id', 'name')
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    player_id: str
    name: str

    def __init__(self, player_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class LobbyState(_message.Message):
    __slots__ = ('lobby_id', 'name', 'host_player_id', 'player_ids', 'status', 'game_acceptance', 'settings')

    class GameAcceptanceEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool

        def __init__(self, key: _Optional[str]=..., value: bool=...) -> None:
            ...
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GAME_ACCEPTANCE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    lobby_id: str
    name: str
    host_player_id: str
    player_ids: _containers.RepeatedScalarFieldContainer[str]
    status: LobbyStatus
    game_acceptance: _containers.ScalarMap[str, bool]
    settings: LobbySettings

    def __init__(self, lobby_id: _Optional[str]=..., name: _Optional[str]=..., host_player_id: _Optional[str]=..., player_ids: _Optional[_Iterable[str]]=..., status: _Optional[_Union[LobbyStatus, str]]=..., game_acceptance: _Optional[_Mapping[str, bool]]=..., settings: _Optional[_Union[LobbySettings, _Mapping]]=...) -> None:
        ...

class LobbySettings(_message.Message):
    __slots__ = ('game_mode', 'min_players', 'max_players', 'ante_amount')

    class GameMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SINGLE: _ClassVar[LobbySettings.GameMode]
    SINGLE: LobbySettings.GameMode
    GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    MIN_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    MAX_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    ANTE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    game_mode: LobbySettings.GameMode
    min_players: int
    max_players: int
    ante_amount: int

    def __init__(self, game_mode: _Optional[_Union[LobbySettings.GameMode, str]]=..., min_players: _Optional[int]=..., max_players: _Optional[int]=..., ante_amount: _Optional[int]=...) -> None:
        ...

class GetLobbiesResponse(_message.Message):
    __slots__ = ('lobbies',)
    LOBBIES_FIELD_NUMBER: _ClassVar[int]
    lobbies: _containers.RepeatedCompositeFieldContainer[LobbyInfoPublic]

    def __init__(self, lobbies: _Optional[_Iterable[_Union[LobbyInfoPublic, _Mapping]]]=...) -> None:
        ...

class CreateLobbyRequest(_message.Message):
    __slots__ = ('lobby_name',)
    LOBBY_NAME_FIELD_NUMBER: _ClassVar[int]
    lobby_name: str

    def __init__(self, lobby_name: _Optional[str]=...) -> None:
        ...

class JoinLobbyRequest(_message.Message):
    __slots__ = ('lobby_id',)
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    lobby_id: str

    def __init__(self, lobby_id: _Optional[str]=...) -> None:
        ...

class Card(_message.Message):
    __slots__ = ('rank', 'suit')

    class CardSuit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Diamonds: _ClassVar[Card.CardSuit]
        Hearts: _ClassVar[Card.CardSuit]
        Clubs: _ClassVar[Card.CardSuit]
        Spades: _ClassVar[Card.CardSuit]
    Diamonds: Card.CardSuit
    Hearts: Card.CardSuit
    Clubs: Card.CardSuit
    Spades: Card.CardSuit

    class CardRank(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Ace: _ClassVar[Card.CardRank]
        Two: _ClassVar[Card.CardRank]
        Three: _ClassVar[Card.CardRank]
        Four: _ClassVar[Card.CardRank]
        Five: _ClassVar[Card.CardRank]
        Six: _ClassVar[Card.CardRank]
        Seven: _ClassVar[Card.CardRank]
        Eight: _ClassVar[Card.CardRank]
        Nine: _ClassVar[Card.CardRank]
        Ten: _ClassVar[Card.CardRank]
        Jack: _ClassVar[Card.CardRank]
        Queen: _ClassVar[Card.CardRank]
        King: _ClassVar[Card.CardRank]
    Ace: Card.CardRank
    Two: Card.CardRank
    Three: Card.CardRank
    Four: Card.CardRank
    Five: Card.CardRank
    Six: Card.CardRank
    Seven: Card.CardRank
    Eight: Card.CardRank
    Nine: Card.CardRank
    Ten: Card.CardRank
    Jack: Card.CardRank
    Queen: Card.CardRank
    King: Card.CardRank
    RANK_FIELD_NUMBER: _ClassVar[int]
    SUIT_FIELD_NUMBER: _ClassVar[int]
    rank: Card.CardRank
    suit: Card.CardSuit

    def __init__(self, rank: _Optional[_Union[Card.CardRank, str]]=..., suit: _Optional[_Union[Card.CardSuit, str]]=...) -> None:
        ...

class SetLobbyMatchmakingStatusRequest(_message.Message):
    __slots__ = ('status',)

    class MatchmakingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_MATCHMAKING: _ClassVar[SetLobbyMatchmakingStatusRequest.MatchmakingStatus]
        MATCHMAKING: _ClassVar[SetLobbyMatchmakingStatusRequest.MatchmakingStatus]
    NOT_MATCHMAKING: SetLobbyMatchmakingStatusRequest.MatchmakingStatus
    MATCHMAKING: SetLobbyMatchmakingStatusRequest.MatchmakingStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: SetLobbyMatchmakingStatusRequest.MatchmakingStatus

    def __init__(self, status: _Optional[_Union[SetLobbyMatchmakingStatusRequest.MatchmakingStatus, str]]=...) -> None:
        ...

class RespondLobbyMatchmakingRequest(_message.Message):
    __slots__ = ('decision',)

    class MatchmakingDecision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCEPT: _ClassVar[RespondLobbyMatchmakingRequest.MatchmakingDecision]
        DECLINE: _ClassVar[RespondLobbyMatchmakingRequest.MatchmakingDecision]
    ACCEPT: RespondLobbyMatchmakingRequest.MatchmakingDecision
    DECLINE: RespondLobbyMatchmakingRequest.MatchmakingDecision
    DECISION_FIELD_NUMBER: _ClassVar[int]
    decision: RespondLobbyMatchmakingRequest.MatchmakingDecision

    def __init__(self, decision: _Optional[_Union[RespondLobbyMatchmakingRequest.MatchmakingDecision, str]]=...) -> None:
        ...

class RespondBettingPhaseRequest(_message.Message):
    __slots__ = ('bet', 'call', 'raise_bet', 'fold')
    BET_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_NUMBER: _ClassVar[int]
    RAISE_BET_FIELD_NUMBER: _ClassVar[int]
    FOLD_FIELD_NUMBER: _ClassVar[int]
    bet: int
    call: _empty_pb2.Empty
    raise_bet: int
    fold: _empty_pb2.Empty

    def __init__(self, bet: _Optional[int]=..., call: _Optional[_Union[_empty_pb2.Empty, _Mapping]]=..., raise_bet: _Optional[int]=..., fold: _Optional[_Union[_empty_pb2.Empty, _Mapping]]=...) -> None:
        ...

class RespondDrawingPhaseRequest(_message.Message):
    __slots__ = ('discarded_cards',)
    DISCARDED_CARDS_FIELD_NUMBER: _ClassVar[int]
    discarded_cards: _containers.RepeatedCompositeFieldContainer[Card]

    def __init__(self, discarded_cards: _Optional[_Iterable[_Union[Card, _Mapping]]]=...) -> None:
        ...