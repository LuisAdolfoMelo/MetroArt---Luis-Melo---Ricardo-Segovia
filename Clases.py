class Artista:
    def __init__(self,nombre,nacionalidad,fecha_nacimiento,fecha_muerte):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte

    def show(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Fecha de muerte: {self.fecha_muerte}")

class Obra:
    def __init__(self,id,titulo,artista,departamento,año_creacion,imagen_url):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.departamento = departamento
        self.año_creacion = año_creacion
        self.imagen_url = imagen_url

    
    def show(self):
        print(f"id: {self.id}")
        print(f"titulo: {self.titulo}")
        print(f"artista: {self.artista}")
        print(f"departamento: {self.departamento}")
        print(f"año_creacion: {self.año_creacion}")
        print(f"imagen_url: {self.imagen_url}")
        print()

class Departamento:
    def __init__(self,id,nombre_departamento):
        self.id = id
        self.nombre_departamento = nombre_departamento

    def show(self):
        print(f"ID: {self.id}")
        print(f"Nombre del departamento: {self.nombre_departamento}")
        print()
        