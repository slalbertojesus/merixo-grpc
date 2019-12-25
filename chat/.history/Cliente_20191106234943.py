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
            metadata = [('ip', '127.0.0.1')]
            structure.Usuario
            respuestaServidor = conn.Subscribirse(
                structure.CrearUsuarioRequest(
                usuario = Usuario
                    (
                    id = id.hex,
                    username = 'Choco',
                    estado = False
                    ),
                metadata=metadata,
                )                
            )
            if respuestaServidor:
                print("Usuario subscrito:", respuestaServidor.respuesta)

if __name__ == '__main__':
    cliente = Cliente()
    cliente.IniciarCliente()