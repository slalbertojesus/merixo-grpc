import grpc
import uuid 
import chat_pb2 as structure
import chat_pb2_grpc as grpc_chat
from Usuario import Usuario

class Cliente():

    def IniciarCliente(self):
        id = uuid.uuid1() 
        channel = grpc.insecure_channel('localhost:50051')
        conn = grpc_chat.ChatAdminStub(channel)
        usuario = "Choco"
        id = id.hex
        estado = True
        request = structure.Usuario(id = id,usuario = usuario, activo = estado)
        confirmacion = conn.Subscribirse(request)
        conn.Subscribirse
        print(confirmacion)

if __name__ == '__main__':
    cliente = Cliente()
    cliente.IniciarCliente()