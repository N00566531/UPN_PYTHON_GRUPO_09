class Cliente:
    contador_id = 1

    def __init__(self, dni, nombre, telefono):
        self.id = Cliente.contador_id
        Cliente.contador_id += 1

        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def __str__(self):
        return f"{self.id} - {self.nombre} | DNI: {self.dni} | Teléfono: {self.telefono}"


class Mascota:
    contador_id = 1

    def __init__(self, nombre, especie, raza, edad):
        self.id = Mascota.contador_id
        Mascota.contador_id += 1

        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad

    def __str__(self):
        return (
            f"{self.id} - {self.nombre} | "
            f"{self.especie} | Raza: {self.raza} | Edad: {self.edad}"
        )


class Veterinario:
    contador_id = 1

    def __init__(self, nombre):
        self.id = Veterinario.contador_id
        Veterinario.contador_id += 1

        self.nombre = nombre

    def __str__(self):
        return f"{self.id} - Dr(a). {self.nombre}"


class Cita:
    contador_id = 1

    def __init__(self, cliente, mascota, veterinario, fecha):
        self.id = Cita.contador_id
        Cita.contador_id += 1

        self.cliente = cliente
        self.mascota = mascota
        self.veterinario = veterinario
        self.fecha = fecha
        self.anotaciones = ""

    def agregar_anotacion(self, anotacion):
        self.anotaciones = anotacion

    def __str__(self):
        anotacion = self.anotaciones if self.anotaciones else "Sin anotaciones"

        return (
            f"\nCita #{self.id}\n"
            f"Fecha: {self.fecha}\n"
            f"Cliente: {self.cliente.nombre} - DNI: {self.cliente.dni}\n"
            f"Mascota: {self.mascota.nombre} ({self.mascota.especie})\n"
            f"Veterinario: Dr(a). {self.veterinario.nombre}\n"
            f"Anotaciones: {anotacion}"
        )
    