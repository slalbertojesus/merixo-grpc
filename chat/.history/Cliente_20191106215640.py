import grpc
import uuid 
import chat_pb2 as structure
import chat_pb2_grpc as grpc_chat
from Usuario import Usuario

class Cliente():

    def IniciarCliente(self):
        id = uuid.uuid1() 
        channel = grpc.insecure_channel('localhost:50051')
        try:
            grpc.channel_ready_future(channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            sys.exit('Error al conectar con el servidor')
        else:
            conn = grpc_chat.ChatAdminStub(channel)
            confirmacion = conn.Subscribirse(
                Usuario(id = id.hex,
                usuario = 'Choco',
                activo = True)
            )
            metadata = [('ip', '127.0.0.1')]
            response = stub.CreateUser(
                users_messages.CreateUserRequest(username='tom'),
                metadata=metadata,
            )
            if response:
                print("User created:", response.user.username)
            print(confirmacion)


if __name__ == '__main__':
    cliente = Cliente()
    cliente.IniciarCliente()