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
    def __init__(self,id, titulo, nombre_artista, nacionalidad_artista, fecha_nacimiento_artista, fecha_muerte_artista, tipo, año_creacion, imagen_url, departamento):
        self.id = id
        self.titulo = titulo
        self.nombre_artista = nombre_artista
        self.nacionalidad_artista = nacionalidad_artista
        self.fecha_nacimiento_artista = fecha_nacimiento_artista
        self.fecha_muerte_artista = fecha_muerte_artista
        self.tipo = tipo
        self.año_creacion = año_creacion
        self.imagen_url = imagen_url
        self.departamento = departamento

    def show(self):
        print(f"ID: {self.id}")
        print(f"Titulo: {self.titulo}")
        print(f"Nombre del Artista: {self.nombre_artista}")
        print(f"Nacionalidad del Artista: {self.nacionalidad_artista}")
        print(f"Fecha de Nacimiento del Artista: {self.fecha_nacimiento_artista}")
        print(f"Fecha de Muerte del Artista: {self.fecha_muerte_artista}")
        print(f"Tipo: {self.tipo}")
        print(f"Año de Creacion: {self.año_creacion}")
        print(f"Imagen URL: {self.imagen_url}")
        print(f"Departamento: {self.departamento}")
        print()

class Departamento:
    def __init__(self,id,nombre_departamento):
        self.id = id
        self.nombre_departamento = nombre_departamento

    def show(self):
        print(f"ID: {self.id}")
        print(f"Nombre del departamento: {self.nombre_departamento}")
        print()
        