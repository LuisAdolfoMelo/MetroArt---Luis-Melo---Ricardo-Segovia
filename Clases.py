class Artista:
    def __init__(self,nombre,nacionalidad,fecha_nacimiento,fecha_muerte):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte

    def show(self):
        print(f"""Nombre: {self.nombre}
        Nacionalidad: {self.nacionalidad}
        Fecha de nacimiento: {self.fecha_nacimiento}
        Fecha de muerte: {self.fecha_muerte}""")

class Obra:
    def __init__(self,id,titulo,artista,departamento,año_creacion,imagen_url):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.departamento = departamento
        self.año_creacion = año_creacion
        self.imagen_url = imagen_url

    
    def show(self):
        print(f"id: {self.id}
        Titulo: {self.titulo}
        Artista: {self.artista}
        Departamento: {self.departamento}
        Año de creacion: {self.año_creacion}
        Imagen_url: {self.imagen_url}""")
        print()

class Departamento:
    def __init__(self,id,nombre_departamento):
        self.id = id
        self.nombre_departamento = nombre_departamento

    def show(self):
        print(f"""ID: {self.id}
        Nombre del departamento: {self.nombre_departamento}""")
        print()
        
