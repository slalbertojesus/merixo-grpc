from concurrent import futures

import grpc
from Usuario import Usuario
import time

import chat_pb2 as structure
import chat_pb2_grpc as grpc_chat

class Servidor(grpc_chat.ChatAdminServicer):

    def __init__(self):
        self.clientes = []

    def EliminaMensaje(self, request, context):
        print("Hi")

    def Subscribirse(self, request, context):
        id = request.id
        usuario = request.usuario
        estado = request.estado
        usuario = Usuario(usuario, id, estado)
        self.clientes.append(usuario)
        respuesta = "Usuario agregado"
        avisoSubscripcion = structure.Respuesta = respuesta
        return avisoSubscripcion

    def IniciaChat(self, request, context):
        print("Usuario agregado") 

    def iniciar(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        grpc_chat.add_ChatAdminServicer_to_server(self, server)
        print('Iniciando server. Escuchando en puerto 50051.')
        server.add_insecure_port('[::]:50051')
        server.start()
        try:
            while True:
                time.sleep(10000)
        except KeyboardInterrupt:
            server.stop(0)

if __name__ == '__main__':
    servidor = Servidor()
    servidor.iniciar()