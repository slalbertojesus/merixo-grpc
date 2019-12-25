class Usuario: 
    def __init__(self, username, id, estado):
        self.username = username
        self.id = id
        self.estado = estado
    
    def __iter__(self):
        return self