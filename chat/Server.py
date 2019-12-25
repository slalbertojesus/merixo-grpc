import grpc
import time
import chat_pb2 as structure
import chat_pb2_grpc as grpc_chat
from concurrent import futures

class Servidor(grpc_chat.ChatAdminServicer):

    def __init__(self):
        self.clientes = []
        self.listaChat = []

    def EliminaMensaje(self, request, context):
        print("Hi")

    def Subscribirse(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        usuario = request.usuario
        print("El usuario  "+usuario.id+" ha sido agregado al servidor ")
        self.clientes.append(usuario)
        EXITO = "Usuario "+usuario.username+" agregado"
        return structure.Respuesta(respuesta = EXITO)

    def MandarMensaje(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        #Va a checar que entre la lista de chats, esten los dos ids 
        #(Osea, el request lleva los dos usuarios)
        #Si encuentra los dos, abre un canal bidireccional entre los dos
        #por cada mensaje que se mande, solo hace el yield si el id coindice con el del usuario 

    def IniciaChat(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        print(request)
        usuario = structure.usuario
        #Checa que los usuarios esten en la lista de clientes
        #Si estan los dos, los agrega a un chat entre los dos  
        #Cada mensaje que ese usuario mande solo podra
        

    def iniciar(self):
        print('Iniciando server. Escuchando en puerto 50051.')
        with open('server.key', 'rb') as f:
            private_key = f.read()
        with open('server.crt', 'rb') as f:
            certificate_chain = f.read()
        with open('rootCA.crt', 'rb') as f:
            ca_cert = f.read()
        server_credentials = grpc.ssl_server_credentials(  [(private_key, certificate_chain)],
        root_certificates=ca_cert,
            require_client_auth=False
            )
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        grpc_chat.add_ChatAdminServicer_to_server(self, server)
        server.add_secure_port('159.89.50.94:50051', server_credentials)
        server.start()
        try:
            while True:
                time.sleep(10000)
        except KeyboardInterrupt:
            server.stop(0)

if __name__ == '__main__':
    servidor = Servidor()
    servidor.iniciar()