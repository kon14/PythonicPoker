"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import rustic_poker_pb2 as rustic__poker__pb2
GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in rustic_poker_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class RusticPokerStub(object):
    """***** RPCs *****

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Connect = channel.unary_unary('/rustic_poker.RusticPoker/Connect', request_serializer=rustic__poker__pb2.ConnectRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.Disconnect = channel.unary_unary('/rustic_poker.RusticPoker/Disconnect', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.WatchState = channel.unary_stream('/rustic_poker.RusticPoker/WatchState', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=rustic__poker__pb2.GameState.FromString, _registered_method=True)
        self.GetLobbies = channel.unary_unary('/rustic_poker.RusticPoker/GetLobbies', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=rustic__poker__pb2.GetLobbiesResponse.FromString, _registered_method=True)
        self.CreateLobby = channel.unary_unary('/rustic_poker.RusticPoker/CreateLobby', request_serializer=rustic__poker__pb2.CreateLobbyRequest.SerializeToString, response_deserializer=rustic__poker__pb2.LobbyInfoPublic.FromString, _registered_method=True)
        self.JoinLobby = channel.unary_unary('/rustic_poker.RusticPoker/JoinLobby', request_serializer=rustic__poker__pb2.JoinLobbyRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.LeaveLobby = channel.unary_unary('/rustic_poker.RusticPoker/LeaveLobby', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.SetLobbyMatchmakingStatus = channel.unary_unary('/rustic_poker.RusticPoker/SetLobbyMatchmakingStatus', request_serializer=rustic__poker__pb2.SetLobbyMatchmakingStatusRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.RespondLobbyMatchmaking = channel.unary_unary('/rustic_poker.RusticPoker/RespondLobbyMatchmaking', request_serializer=rustic__poker__pb2.RespondLobbyMatchmakingRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.StartLobbyGame = channel.unary_unary('/rustic_poker.RusticPoker/StartLobbyGame', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.RespondBettingPhase = channel.unary_unary('/rustic_poker.RusticPoker/RespondBettingPhase', request_serializer=rustic__poker__pb2.RespondBettingPhaseRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.RespondDrawingPhase = channel.unary_unary('/rustic_poker.RusticPoker/RespondDrawingPhase', request_serializer=rustic__poker__pb2.RespondDrawingPhaseRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)

class RusticPokerServicer(object):
    """***** RPCs *****

    """

    def Connect(self, request, context):
        """[Authentication]
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disconnect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchState(self, request, context):
        """[Game]
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLobbies(self, request, context):
        """[Lobby]
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateLobby(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinLobby(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LeaveLobby(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetLobbyMatchmakingStatus(self, request, context):
        """rpc KickLobbyPlayer(KickLobbyPlayerRequest) returns (google.protobuf.Empty);
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondLobbyMatchmaking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartLobbyGame(self, request, context):
        """rpc SetLobbySettings(LobbySettings) returns (google.protobuf.Empty);
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondBettingPhase(self, request, context):
        """[Game]
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondDrawingPhase(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_RusticPokerServicer_to_server(servicer, server):
    rpc_method_handlers = {'Connect': grpc.unary_unary_rpc_method_handler(servicer.Connect, request_deserializer=rustic__poker__pb2.ConnectRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'Disconnect': grpc.unary_unary_rpc_method_handler(servicer.Disconnect, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'WatchState': grpc.unary_stream_rpc_method_handler(servicer.WatchState, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=rustic__poker__pb2.GameState.SerializeToString), 'GetLobbies': grpc.unary_unary_rpc_method_handler(servicer.GetLobbies, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=rustic__poker__pb2.GetLobbiesResponse.SerializeToString), 'CreateLobby': grpc.unary_unary_rpc_method_handler(servicer.CreateLobby, request_deserializer=rustic__poker__pb2.CreateLobbyRequest.FromString, response_serializer=rustic__poker__pb2.LobbyInfoPublic.SerializeToString), 'JoinLobby': grpc.unary_unary_rpc_method_handler(servicer.JoinLobby, request_deserializer=rustic__poker__pb2.JoinLobbyRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'LeaveLobby': grpc.unary_unary_rpc_method_handler(servicer.LeaveLobby, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'SetLobbyMatchmakingStatus': grpc.unary_unary_rpc_method_handler(servicer.SetLobbyMatchmakingStatus, request_deserializer=rustic__poker__pb2.SetLobbyMatchmakingStatusRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'RespondLobbyMatchmaking': grpc.unary_unary_rpc_method_handler(servicer.RespondLobbyMatchmaking, request_deserializer=rustic__poker__pb2.RespondLobbyMatchmakingRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'StartLobbyGame': grpc.unary_unary_rpc_method_handler(servicer.StartLobbyGame, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'RespondBettingPhase': grpc.unary_unary_rpc_method_handler(servicer.RespondBettingPhase, request_deserializer=rustic__poker__pb2.RespondBettingPhaseRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'RespondDrawingPhase': grpc.unary_unary_rpc_method_handler(servicer.RespondDrawingPhase, request_deserializer=rustic__poker__pb2.RespondDrawingPhaseRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('rustic_poker.RusticPoker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('rustic_poker.RusticPoker', rpc_method_handlers)

class RusticPoker(object):
    """***** RPCs *****

    """

    @staticmethod
    def Connect(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rustic_poker.RusticPoker/Connect', rustic__poker__pb2.ConnectRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def Disconnect(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rustic_poker.RusticPoker/Disconnect', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def WatchState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/rustic_poker.RusticPoker/WatchState', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, rustic__poker__pb2.GameState.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetLobbies(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rustic_poker.RusticPoker/GetLobbies', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, rustic__poker__pb2.GetLobbiesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateLobby(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rustic_poker.RusticPoker/CreateLobby', rustic__poker__pb2.CreateLobbyRequest.SerializeToString, rustic__poker__pb2.LobbyInfoPublic.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def JoinLobby(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rustic_poker.RusticPoker/JoinLobby', rustic__poker__pb2.JoinLobbyRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def LeaveLobby(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rustic_poker.RusticPoker/LeaveLobby', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SetLobbyMatchmakingStatus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rustic_poker.RusticPoker/SetLobbyMatchmakingStatus', rustic__poker__pb2.SetLobbyMatchmakingStatusRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RespondLobbyMatchmaking(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rustic_poker.RusticPoker/RespondLobbyMatchmaking', rustic__poker__pb2.RespondLobbyMatchmakingRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def StartLobbyGame(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rustic_poker.RusticPoker/StartLobbyGame', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RespondBettingPhase(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rustic_poker.RusticPoker/RespondBettingPhase', rustic__poker__pb2.RespondBettingPhaseRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RespondDrawingPhase(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rustic_poker.RusticPoker/RespondDrawingPhase', rustic__poker__pb2.RespondDrawingPhaseRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)