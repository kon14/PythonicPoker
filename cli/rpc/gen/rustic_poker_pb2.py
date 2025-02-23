"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'rustic_poker.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12rustic_poker.proto\x12\x0crustic_poker\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x10\n\x0eConnectRequest"\x8a\x01\n\x0fLobbyInfoPublic\x12\x10\n\x08lobby_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0ehost_player_id\x18\x03 \x01(\t\x12\x14\n\x0cplayer_count\x18\x04 \x01(\r\x12)\n\x06status\x18\x05 \x01(\x0e2\x19.rustic_poker.LobbyStatus"\x99\x15\n\tGameState\x12/\n\x0cplayer_state\x18\x01 \x01(\x0b2\x19.rustic_poker.PlayerState\x12-\n\x0blobby_state\x18\x02 \x01(\x0b2\x18.rustic_poker.LobbyState\x12<\n\x0bmatch_state\x18\x03 \x01(\x0b2".rustic_poker.GameState.MatchStateH\x00\x88\x01\x01\x12-\n\ttimestamp\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x93\t\n\nMatchState\x12\x10\n\x08match_id\x18\x01 \x01(\t\x12G\n\x0bplayer_info\x18\x02 \x03(\x0b22.rustic_poker.GameState.MatchState.PlayerInfoEntry\x12G\n\x0bcredit_pots\x18\x03 \x03(\x0b22.rustic_poker.GameState.MatchState.CreditPotsEntry\x12%\n\town_cards\x18\x04 \x03(\x0b2\x12.rustic_poker.Card\x12T\n\x12player_bet_amounts\x18\x05 \x03(\x0b28.rustic_poker.GameState.MatchState.PlayerBetAmountsEntry\x127\n\x0bpoker_phase\x18\x06 \x01(\x0b2".rustic_poker.GameState.PokerPhase\x12\x11\n\tcan_i_act\x18\x07 \x01(\x08\x1ap\n\x0fPlayerInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12L\n\x05value\x18\x02 \x01(\x0b2=.rustic_poker.GameState.MatchState.MatchStatePlayerPublicInfo:\x028\x01\x1ai\n\x0fCreditPotsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12E\n\x05value\x18\x02 \x01(\x0b26.rustic_poker.GameState.MatchState.MatchStateCreditPot:\x028\x01\x1a7\n\x15PlayerBetAmountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x028\x01\x1a\x94\x02\n\x1aMatchStatePlayerPublicInfo\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x18\n\x10starting_credits\x18\x02 \x01(\x04\x12\x19\n\x11remaining_credits\x18\x03 \x01(\x04\x12b\n\x0bpot_credits\x18\x04 \x03(\x0b2M.rustic_poker.GameState.MatchState.MatchStatePlayerPublicInfo.PotCreditsEntry\x12\x17\n\x0fhand_card_count\x18\x05 \x01(\r\x1a1\n\x0fPotCreditsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x028\x01\x1a\xea\x01\n\x13MatchStateCreditPot\x12\x0e\n\x06pot_id\x18\x01 \x01(\t\x12\x13\n\x0bis_main_pot\x18\x02 \x01(\x08\x12\x15\n\rtotal_credits\x18\x03 \x01(\x04\x12a\n\x0eplayer_credits\x18\x04 \x03(\x0b2I.rustic_poker.GameState.MatchState.MatchStateCreditPot.PlayerCreditsEntry\x1a4\n\x12PlayerCreditsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x028\x01\x1a\x98\n\n\nPokerPhase\x12&\n\x04ante\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12)\n\x07dealing\x18\x02 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12M\n\rfirst_betting\x18\x03 \x01(\x0b24.rustic_poker.GameState.PokerPhase.PokerPhaseBettingH\x00\x12G\n\x07drawing\x18\x04 \x01(\x0b24.rustic_poker.GameState.PokerPhase.PokerPhaseDrawingH\x00\x12N\n\x0esecond_betting\x18\x05 \x01(\x0b24.rustic_poker.GameState.PokerPhase.PokerPhaseBettingH\x00\x12I\n\x08showdown\x18\x06 \x01(\x0b25.rustic_poker.GameState.PokerPhase.PokerPhaseShowdownH\x00\x1a{\n\x11PokerPhaseBetting\x12\x1f\n\x12highest_bet_amount\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x1b\n\x0eown_bet_amount\x18\x02 \x01(\x04H\x01\x88\x01\x01B\x15\n\x13_highest_bet_amountB\x11\n\x0f_own_bet_amount\x1a[\n\x11PokerPhaseDrawing\x12\x15\n\rdiscard_stage\x18\x01 \x01(\x08\x12/\n\x13own_discarded_cards\x18\x02 \x03(\x0b2\x12.rustic_poker.Card\x1a\xa0\x05\n\x12PokerPhaseShowdown\x12[\n\x07results\x18\x01 \x01(\x0b2E.rustic_poker.GameState.PokerPhase.PokerPhaseShowdown.ShowdownResultsH\x00\x88\x01\x01\x1a\xa0\x04\n\x0fShowdownResults\x12i\n\x0cwinning_rank\x18\x01 \x01(\x0e2S.rustic_poker.GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.PokerHandRank\x12\x12\n\nwinner_ids\x18\x02 \x03(\t\x12w\n\x10pot_distribution\x18\x03 \x03(\x0b2].rustic_poker.GameState.PokerPhase.PokerPhaseShowdown.ShowdownResults.ShowdownPotDistribution\x1ap\n\x17ShowdownPotDistribution\x12\x0e\n\x06pot_id\x18\x01 \x01(\t\x12\x12\n\nplayer_ids\x18\x02 \x03(\t\x12\x15\n\rtotal_credits\x18\x03 \x01(\x04\x12\x1a\n\x12credits_per_winner\x18\x04 \x01(\x04"\xa2\x01\n\rPokerHandRank\x12\x0e\n\nRoyalFlush\x10\x00\x12\x11\n\rStraightFlush\x10\x01\x12\x0f\n\x0bFourOfAKind\x10\x02\x12\r\n\tFullHouse\x10\x03\x12\t\n\x05Flush\x10\x04\x12\x0c\n\x08Straight\x10\x05\x12\x10\n\x0cThreeOfAKind\x10\x06\x12\x0b\n\x07TwoPair\x10\x07\x12\x08\n\x04Pair\x10\x08\x12\x0c\n\x08HighCard\x10\tB\n\n\x08_resultsB\x07\n\x05phaseB\x0e\n\x0c_match_state".\n\x0bPlayerState\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t"\xb0\x02\n\nLobbyState\x12\x10\n\x08lobby_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0ehost_player_id\x18\x03 \x01(\t\x12\x12\n\nplayer_ids\x18\x04 \x03(\t\x12)\n\x06status\x18\x05 \x01(\x0e2\x19.rustic_poker.LobbyStatus\x12E\n\x0fgame_acceptance\x18\x06 \x03(\x0b2,.rustic_poker.LobbyState.GameAcceptanceEntry\x12-\n\x08settings\x18\x07 \x01(\x0b2\x1b.rustic_poker.LobbySettings\x1a5\n\x13GameAcceptanceEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x028\x01"\x9f\x01\n\rLobbySettings\x127\n\tgame_mode\x18\x01 \x01(\x0e2$.rustic_poker.LobbySettings.GameMode\x12\x13\n\x0bmin_players\x18\x02 \x01(\r\x12\x13\n\x0bmax_players\x18\x03 \x01(\r\x12\x13\n\x0bante_amount\x18\x04 \x01(\x04"\x16\n\x08GameMode\x12\n\n\x06SINGLE\x10\x00"D\n\x12GetLobbiesResponse\x12.\n\x07lobbies\x18\x01 \x03(\x0b2\x1d.rustic_poker.LobbyInfoPublic"(\n\x12CreateLobbyRequest\x12\x12\n\nlobby_name\x18\x01 \x01(\t"$\n\x10JoinLobbyRequest\x12\x10\n\x08lobby_id\x18\x01 \x01(\t"\xa8\x02\n\x04Card\x12)\n\x04rank\x18\x01 \x01(\x0e2\x1b.rustic_poker.Card.CardRank\x12)\n\x04suit\x18\x02 \x01(\x0e2\x1b.rustic_poker.Card.CardSuit";\n\x08CardSuit\x12\x0c\n\x08Diamonds\x10\x00\x12\n\n\x06Hearts\x10\x01\x12\t\n\x05Clubs\x10\x02\x12\n\n\x06Spades\x10\x03"\x8c\x01\n\x08CardRank\x12\x07\n\x03Ace\x10\x00\x12\x07\n\x03Two\x10\x01\x12\t\n\x05Three\x10\x02\x12\x08\n\x04Four\x10\x03\x12\x08\n\x04Five\x10\x04\x12\x07\n\x03Six\x10\x05\x12\t\n\x05Seven\x10\x06\x12\t\n\x05Eight\x10\x07\x12\x08\n\x04Nine\x10\x08\x12\x07\n\x03Ten\x10\t\x12\x08\n\x04Jack\x10\n\x12\t\n\x05Queen\x10\x0b\x12\x08\n\x04King\x10\x0c"\xaf\x01\n SetLobbyMatchmakingStatusRequest\x12P\n\x06status\x18\x01 \x01(\x0e2@.rustic_poker.SetLobbyMatchmakingStatusRequest.MatchmakingStatus"9\n\x11MatchmakingStatus\x12\x13\n\x0fNOT_MATCHMAKING\x10\x00\x12\x0f\n\x0bMATCHMAKING\x10\x01"\xa4\x01\n\x1eRespondLobbyMatchmakingRequest\x12R\n\x08decision\x18\x01 \x01(\x0e2@.rustic_poker.RespondLobbyMatchmakingRequest.MatchmakingDecision".\n\x13MatchmakingDecision\x12\n\n\x06ACCEPT\x10\x00\x12\x0b\n\x07DECLINE\x10\x01"\xa1\x01\n\x1aRespondBettingPhaseRequest\x12\r\n\x03bet\x18\x01 \x01(\x04H\x00\x12&\n\x04call\x18\x02 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12\x13\n\traise_bet\x18\x03 \x01(\x04H\x00\x12&\n\x04fold\x18\x04 \x01(\x0b2\x16.google.protobuf.EmptyH\x00B\x0f\n\rBettingAction"I\n\x1aRespondDrawingPhaseRequest\x12+\n\x0fdiscarded_cards\x18\x01 \x03(\x0b2\x12.rustic_poker.Card*5\n\x0bLobbyStatus\x12\x08\n\x04IDLE\x10\x00\x12\x0f\n\x0bMATCHMAKING\x10\x01\x12\x0b\n\x07IN_GAME\x10\x022\xa2\x07\n\x0bRusticPoker\x12?\n\x07Connect\x12\x1c.rustic_poker.ConnectRequest\x1a\x16.google.protobuf.Empty\x12<\n\nDisconnect\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12?\n\nWatchState\x12\x16.google.protobuf.Empty\x1a\x17.rustic_poker.GameState0\x01\x12F\n\nGetLobbies\x12\x16.google.protobuf.Empty\x1a .rustic_poker.GetLobbiesResponse\x12N\n\x0bCreateLobby\x12 .rustic_poker.CreateLobbyRequest\x1a\x1d.rustic_poker.LobbyInfoPublic\x12C\n\tJoinLobby\x12\x1e.rustic_poker.JoinLobbyRequest\x1a\x16.google.protobuf.Empty\x12<\n\nLeaveLobby\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12c\n\x19SetLobbyMatchmakingStatus\x12..rustic_poker.SetLobbyMatchmakingStatusRequest\x1a\x16.google.protobuf.Empty\x12_\n\x17RespondLobbyMatchmaking\x12,.rustic_poker.RespondLobbyMatchmakingRequest\x1a\x16.google.protobuf.Empty\x12@\n\x0eStartLobbyGame\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12W\n\x13RespondBettingPhase\x12(.rustic_poker.RespondBettingPhaseRequest\x1a\x16.google.protobuf.Empty\x12W\n\x13RespondDrawingPhase\x12(.rustic_poker.RespondDrawingPhaseRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rustic_poker_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_GAMESTATE_MATCHSTATE_PLAYERINFOENTRY']._loaded_options = None
    _globals['_GAMESTATE_MATCHSTATE_PLAYERINFOENTRY']._serialized_options = b'8\x01'
    _globals['_GAMESTATE_MATCHSTATE_CREDITPOTSENTRY']._loaded_options = None
    _globals['_GAMESTATE_MATCHSTATE_CREDITPOTSENTRY']._serialized_options = b'8\x01'
    _globals['_GAMESTATE_MATCHSTATE_PLAYERBETAMOUNTSENTRY']._loaded_options = None
    _globals['_GAMESTATE_MATCHSTATE_PLAYERBETAMOUNTSENTRY']._serialized_options = b'8\x01'
    _globals['_GAMESTATE_MATCHSTATE_MATCHSTATEPLAYERPUBLICINFO_POTCREDITSENTRY']._loaded_options = None
    _globals['_GAMESTATE_MATCHSTATE_MATCHSTATEPLAYERPUBLICINFO_POTCREDITSENTRY']._serialized_options = b'8\x01'
    _globals['_GAMESTATE_MATCHSTATE_MATCHSTATECREDITPOT_PLAYERCREDITSENTRY']._loaded_options = None
    _globals['_GAMESTATE_MATCHSTATE_MATCHSTATECREDITPOT_PLAYERCREDITSENTRY']._serialized_options = b'8\x01'
    _globals['_LOBBYSTATE_GAMEACCEPTANCEENTRY']._loaded_options = None
    _globals['_LOBBYSTATE_GAMEACCEPTANCEENTRY']._serialized_options = b'8\x01'
    _globals['_LOBBYSTATUS']._serialized_start = 4523
    _globals['_LOBBYSTATUS']._serialized_end = 4576
    _globals['_CONNECTREQUEST']._serialized_start = 98
    _globals['_CONNECTREQUEST']._serialized_end = 114
    _globals['_LOBBYINFOPUBLIC']._serialized_start = 117
    _globals['_LOBBYINFOPUBLIC']._serialized_end = 255
    _globals['_GAMESTATE']._serialized_start = 258
    _globals['_GAMESTATE']._serialized_end = 2971
    _globals['_GAMESTATE_MATCHSTATE']._serialized_start = 477
    _globals['_GAMESTATE_MATCHSTATE']._serialized_end = 1648
    _globals['_GAMESTATE_MATCHSTATE_PLAYERINFOENTRY']._serialized_start = 856
    _globals['_GAMESTATE_MATCHSTATE_PLAYERINFOENTRY']._serialized_end = 968
    _globals['_GAMESTATE_MATCHSTATE_CREDITPOTSENTRY']._serialized_start = 970
    _globals['_GAMESTATE_MATCHSTATE_CREDITPOTSENTRY']._serialized_end = 1075
    _globals['_GAMESTATE_MATCHSTATE_PLAYERBETAMOUNTSENTRY']._serialized_start = 1077
    _globals['_GAMESTATE_MATCHSTATE_PLAYERBETAMOUNTSENTRY']._serialized_end = 1132
    _globals['_GAMESTATE_MATCHSTATE_MATCHSTATEPLAYERPUBLICINFO']._serialized_start = 1135
    _globals['_GAMESTATE_MATCHSTATE_MATCHSTATEPLAYERPUBLICINFO']._serialized_end = 1411
    _globals['_GAMESTATE_MATCHSTATE_MATCHSTATEPLAYERPUBLICINFO_POTCREDITSENTRY']._serialized_start = 1362
    _globals['_GAMESTATE_MATCHSTATE_MATCHSTATEPLAYERPUBLICINFO_POTCREDITSENTRY']._serialized_end = 1411
    _globals['_GAMESTATE_MATCHSTATE_MATCHSTATECREDITPOT']._serialized_start = 1414
    _globals['_GAMESTATE_MATCHSTATE_MATCHSTATECREDITPOT']._serialized_end = 1648
    _globals['_GAMESTATE_MATCHSTATE_MATCHSTATECREDITPOT_PLAYERCREDITSENTRY']._serialized_start = 1596
    _globals['_GAMESTATE_MATCHSTATE_MATCHSTATECREDITPOT_PLAYERCREDITSENTRY']._serialized_end = 1648
    _globals['_GAMESTATE_POKERPHASE']._serialized_start = 1651
    _globals['_GAMESTATE_POKERPHASE']._serialized_end = 2955
    _globals['_GAMESTATE_POKERPHASE_POKERPHASEBETTING']._serialized_start = 2055
    _globals['_GAMESTATE_POKERPHASE_POKERPHASEBETTING']._serialized_end = 2178
    _globals['_GAMESTATE_POKERPHASE_POKERPHASEDRAWING']._serialized_start = 2180
    _globals['_GAMESTATE_POKERPHASE_POKERPHASEDRAWING']._serialized_end = 2271
    _globals['_GAMESTATE_POKERPHASE_POKERPHASESHOWDOWN']._serialized_start = 2274
    _globals['_GAMESTATE_POKERPHASE_POKERPHASESHOWDOWN']._serialized_end = 2946
    _globals['_GAMESTATE_POKERPHASE_POKERPHASESHOWDOWN_SHOWDOWNRESULTS']._serialized_start = 2390
    _globals['_GAMESTATE_POKERPHASE_POKERPHASESHOWDOWN_SHOWDOWNRESULTS']._serialized_end = 2934
    _globals['_GAMESTATE_POKERPHASE_POKERPHASESHOWDOWN_SHOWDOWNRESULTS_SHOWDOWNPOTDISTRIBUTION']._serialized_start = 2657
    _globals['_GAMESTATE_POKERPHASE_POKERPHASESHOWDOWN_SHOWDOWNRESULTS_SHOWDOWNPOTDISTRIBUTION']._serialized_end = 2769
    _globals['_GAMESTATE_POKERPHASE_POKERPHASESHOWDOWN_SHOWDOWNRESULTS_POKERHANDRANK']._serialized_start = 2772
    _globals['_GAMESTATE_POKERPHASE_POKERPHASESHOWDOWN_SHOWDOWNRESULTS_POKERHANDRANK']._serialized_end = 2934
    _globals['_PLAYERSTATE']._serialized_start = 2973
    _globals['_PLAYERSTATE']._serialized_end = 3019
    _globals['_LOBBYSTATE']._serialized_start = 3022
    _globals['_LOBBYSTATE']._serialized_end = 3326
    _globals['_LOBBYSTATE_GAMEACCEPTANCEENTRY']._serialized_start = 3273
    _globals['_LOBBYSTATE_GAMEACCEPTANCEENTRY']._serialized_end = 3326
    _globals['_LOBBYSETTINGS']._serialized_start = 3329
    _globals['_LOBBYSETTINGS']._serialized_end = 3488
    _globals['_LOBBYSETTINGS_GAMEMODE']._serialized_start = 3466
    _globals['_LOBBYSETTINGS_GAMEMODE']._serialized_end = 3488
    _globals['_GETLOBBIESRESPONSE']._serialized_start = 3490
    _globals['_GETLOBBIESRESPONSE']._serialized_end = 3558
    _globals['_CREATELOBBYREQUEST']._serialized_start = 3560
    _globals['_CREATELOBBYREQUEST']._serialized_end = 3600
    _globals['_JOINLOBBYREQUEST']._serialized_start = 3602
    _globals['_JOINLOBBYREQUEST']._serialized_end = 3638
    _globals['_CARD']._serialized_start = 3641
    _globals['_CARD']._serialized_end = 3937
    _globals['_CARD_CARDSUIT']._serialized_start = 3735
    _globals['_CARD_CARDSUIT']._serialized_end = 3794
    _globals['_CARD_CARDRANK']._serialized_start = 3797
    _globals['_CARD_CARDRANK']._serialized_end = 3937
    _globals['_SETLOBBYMATCHMAKINGSTATUSREQUEST']._serialized_start = 3940
    _globals['_SETLOBBYMATCHMAKINGSTATUSREQUEST']._serialized_end = 4115
    _globals['_SETLOBBYMATCHMAKINGSTATUSREQUEST_MATCHMAKINGSTATUS']._serialized_start = 4058
    _globals['_SETLOBBYMATCHMAKINGSTATUSREQUEST_MATCHMAKINGSTATUS']._serialized_end = 4115
    _globals['_RESPONDLOBBYMATCHMAKINGREQUEST']._serialized_start = 4118
    _globals['_RESPONDLOBBYMATCHMAKINGREQUEST']._serialized_end = 4282
    _globals['_RESPONDLOBBYMATCHMAKINGREQUEST_MATCHMAKINGDECISION']._serialized_start = 4236
    _globals['_RESPONDLOBBYMATCHMAKINGREQUEST_MATCHMAKINGDECISION']._serialized_end = 4282
    _globals['_RESPONDBETTINGPHASEREQUEST']._serialized_start = 4285
    _globals['_RESPONDBETTINGPHASEREQUEST']._serialized_end = 4446
    _globals['_RESPONDDRAWINGPHASEREQUEST']._serialized_start = 4448
    _globals['_RESPONDDRAWINGPHASEREQUEST']._serialized_end = 4521
    _globals['_RUSTICPOKER']._serialized_start = 4579
    _globals['_RUSTICPOKER']._serialized_end = 5509