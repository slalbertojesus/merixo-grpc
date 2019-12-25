class Usuario: 
    def __init__(self, id, username, estado):
        self.id = id
        self.username = username
        self.estado = estado
    
    def __iter__(self):
        return self