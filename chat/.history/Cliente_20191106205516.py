import grpc
import uuid 
import chat_pb2 as structure
import chat_pb2_grpc as grpc_chat
from Usuario import Usuario

class Cliente():

    def IniciarCliente(self):
        id = uuid.uuid1() 
        print(id)
        channel = grpc.insecure_channel('localhost:50051')
        conn = grpc_chat.ChatAdminStub(channel)
        structure.Usuario.id = id.hex
        structure.Usuario.usuario = "Choco"
        structure.Usuario.activo = True
        structure.
        request = structure.Usuario
        #structure._USUARIO.id = id.hex
        #structure._USUARIO.usuario = "Choco"
        #structure._USUARIO.activo = True
        #request = structure._USUARIO
        confirmacion = conn.Subscribirse(request)
        print(confirmacion)

if __name__ == '__main__':
    cliente = Cliente()
    cliente.IniciarCliente()