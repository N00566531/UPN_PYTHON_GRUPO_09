from models import Cliente, Mascota, Veterinario, Cita
from colores import celeste, rojo, verde
from datetime import datetime

class Veterinaria:
    def __init__(self):
        # DNI será la llave principal
        self.clientes = {}
        self.veterinarios = []
        self.citas = []
        self.cargar_veterinarios()

    # VETERINARIOS

    def cargar_veterinarios(self):
        self.veterinarios.append(
            Veterinario("Carlos Pérez", maximo_citas_diarias=4)
        )
        self.veterinarios.append(
            Veterinario("María Rodríguez", maximo_citas_diarias=4)
        )

    def listar_veterinarios(self, fecha=None):
        if fecha is None:
            print(celeste("\n--- VETERINARIOS ---"))
            veterinarios = self.veterinarios
        else:
            dia = self.obtener_dia(fecha)
            print(celeste(f"\n--- VETERINARIOS DISPONIBLES EL {dia} ---"))
            veterinarios = [
                veterinario for veterinario in self.veterinarios
                if self.veterinario_disponible(veterinario, fecha)
            ]

        if len(veterinarios) == 0:
            print(rojo("No hay veterinarios disponibles para ese día."))
            return []

        for veterinario in veterinarios:
            if fecha is None:
                print(verde(veterinario))
            else:
                cantidad = self.contar_citas_por_dia(veterinario, fecha)
                disponibles = veterinario.maximo_citas_diarias - cantidad
                print(verde(
                    f"{veterinario} | Cupos disponibles: {disponibles}"
                ))
        return veterinarios

    def buscar_veterinario_por_id(self, id_veterinario):
        for veterinario in self.veterinarios:
            if veterinario.id == id_veterinario:
                return veterinario
        return None

    def obtener_dia(self, fecha):
        return fecha.split()[0]

    def contar_citas_por_dia(self, veterinario, fecha):
        dia = self.obtener_dia(fecha)
        return sum(
            1 for cita in self.citas
            if cita.veterinario.id == veterinario.id
            and self.obtener_dia(cita.fecha) == dia
        )

    def veterinario_disponible(self, veterinario, fecha):
        cantidad = self.contar_citas_por_dia(veterinario, fecha)
        return cantidad < veterinario.maximo_citas_diarias

    # CLIENTES

    def registrar_cliente(self):
        print(celeste("\n--- REGISTRAR CLIENTE ---"))
        while True:
            dni = input("DNI: ").strip()
            if dni.isdigit():
                break
            print(rojo("El DNI debe contener solo números."))

        if dni in self.clientes:
            print(rojo("El cliente ya se encuentra registrado."))
            return self.clientes[dni]

        nombre = input("Nombre: ").strip()
        while True:
            telefono = input("Celular: ").strip()
            if telefono.isdigit():
                break
            print(rojo("El celular debe contener solo números."))

        cliente = Cliente(
            dni=dni,
            nombre=nombre,
            telefono=telefono
        )
        self.clientes[dni] = cliente
        print(verde("\nCliente registrado correctamente."))
        print(verde(cliente))
        return cliente

    def buscar_cliente(self, dni):
        return self.clientes.get(dni)

    def mostrar_cliente(self, cliente, mostrar_mascotas=True):
        if cliente is None:
            print(rojo("Cliente no encontrado."))
            return
        print(celeste("\n--- DATOS DEL CLIENTE ---"))
        print(verde(cliente))

        if not mostrar_mascotas:
            return

        print(celeste("\n--- MASCOTAS ---"))
        if len(cliente.mascotas) == 0:
            print(rojo("El cliente no tiene mascotas registradas."))
            return
        for mascota in cliente.mascotas:
            print(verde(mascota))

    def buscar_cliente_menu(self):
        print(celeste("\n--- BUSCAR CLIENTE ---"))
        while True:
            dni = input("Ingrese DNI: ").strip()
            if dni.isdigit():
                break
            print(rojo("El DNI debe contener solo números."))

        cliente = self.buscar_cliente(dni)
        if cliente is None:
            print(rojo("Cliente no encontrado."))
            return
        self.mostrar_cliente(cliente)

    # MASCOTAS

    def registrar_mascota(self, cliente):
        print(celeste("\n--- REGISTRAR MASCOTA ---"))
        nombre = input("Nombre de la mascota: ").strip()
        especie = input("Especie (Perro, Gato, etc.): ").strip()
        raza = input("Raza: ").strip()
        edad = input("Edad: ").strip()
        mascota = Mascota(
            nombre=nombre,
            especie=especie,
            raza=raza,
            edad=edad
        )
        cliente.agregar_mascota(mascota)
        print(verde("\nMascota registrada correctamente."))
        print(verde(mascota))
        return mascota

    def seleccionar_mascota(self, cliente):
        if len(cliente.mascotas) == 0:
            print(rojo("\nEl cliente no tiene mascotas registradas."))
            print(celeste("Se registrará una nueva mascota."))
            return self.registrar_mascota(cliente)

        print(celeste("\n--- MASCOTAS DEL CLIENTE ---"))

        for mascota in cliente.mascotas:
            print(verde(mascota))

        print("0 - Registrar nueva mascota")
        try:
            id_mascota = int(
                input("\nSeleccione mascota: ")
            )
        except ValueError:
            print(rojo("Debe ingresar un número."))
            return None

        if id_mascota == 0:
            return self.registrar_mascota(cliente)

        for mascota in cliente.mascotas:
            if mascota.id == id_mascota:
                return mascota

        print(rojo("Mascota no encontrada."))
        return None

    # CITAS

    def registrar_cita(self):

        print(celeste("\n=============================="))
        print(celeste("       REGISTRAR CITA"))
        print(celeste("=============================="))
        dni = input("Ingrese DNI del cliente: ").strip()
        cliente = self.buscar_cliente(dni)

        # Si cliente no existe
        if cliente is None:
            print(rojo("\nCliente no encontrado."))
            opcion = input(
                "¿Desea registrar al cliente? (s/n): "
            ).lower()

            if opcion == "s":
                cliente = self.registrar_cliente()
            else:
                return

        # Mostrar el cliente sin repetir la lista de mascotas.
        self.mostrar_cliente(cliente, mostrar_mascotas=False)

        # Seleccionar mascota
        mascota = self.seleccionar_mascota(cliente)

        if mascota is None:
            return

        # La fecha permite mostrar únicamente veterinarios disponibles.
        while True:
            fecha = input(
                "Ingrese fecha de la cita (DD/MM/YYYY HH:MM): "
            ).strip()
            try:
                datetime.strptime(fecha, "%d/%m/%Y %H:%M")
                break
            except ValueError:
                print(
                    rojo("Fecha y hora inválidas. "
                    "Use el formato DD/MM/YYYY HH:MM.")
                )

        veterinarios_disponibles = self.listar_veterinarios(fecha)
        if len(veterinarios_disponibles) == 0:
            return

        try:
            id_veterinario = int(
                input("\nSeleccione veterinario: ")
            )
        except ValueError:
            print(rojo("Debe ingresar un número."))
            return

        veterinario = self.buscar_veterinario_por_id(
            id_veterinario
        )

        if (
            veterinario is None
            or veterinario not in veterinarios_disponibles
        ):
            print(rojo("Veterinario no disponible para ese día."))
            return

        cita = Cita(
            cliente=cliente,
            mascota=mascota,
            veterinario=veterinario,
            fecha=fecha
        )

        self.citas.append(cita)

        print(verde("\nCita registrada correctamente."))
        print(verde(cita))

    def listar_cantidad_citas_por_dia(self):
        print(celeste("\n--- CANTIDAD DE CITAS POR DOCTOR Y DÍA ---"))

        if len(self.citas) == 0:
            print(rojo("No existen citas registradas."))
            return

        dias = sorted(
            {self.obtener_dia(cita.fecha) for cita in self.citas},
            key=lambda dia: datetime.strptime(dia, "%d/%m/%Y")
        )

        for dia in dias:
            print(celeste(f"\nFecha: {dia}"))
            for veterinario in self.veterinarios:
                cantidad = self.contar_citas_por_dia(veterinario, dia)
                disponibles = veterinario.maximo_citas_diarias - cantidad
                print(verde(
                    f"Dr(a). {veterinario.nombre}: "
                    f"{cantidad}/{veterinario.maximo_citas_diarias} citas | "
                    f"Cupos disponibles: {disponibles}"
                ))


    # ===============================
    # LISTADO DE CITAS
    # ===============================

    def ordenar_citas_quicksort(self, citas):
        if len(citas) <= 1:
            return citas

        pivote = citas[len(citas) // 2]
        menores = [
            cita for cita in citas
            if cita.id < pivote.id
        ]
        iguales = [
            cita for cita in citas
            if cita.id == pivote.id
        ]
        mayores = [
            cita for cita in citas
            if cita.id > pivote.id
        ]

        return (
            self.ordenar_citas_quicksort(menores)
            + iguales
            + self.ordenar_citas_quicksort(mayores)
        )

    def ordenar_citas_burbuja(self, citas):
        citas_ordenadas = citas.copy()

        for limite in range(len(citas_ordenadas) - 1, 0, -1):
            for indice in range(limite):
                if (
                    citas_ordenadas[indice].id
                    > citas_ordenadas[indice + 1].id
                ):
                    citas_ordenadas[indice], citas_ordenadas[indice + 1] = (
                        citas_ordenadas[indice + 1],
                        citas_ordenadas[indice]
                    )

        return citas_ordenadas

    def listar_citas(self, pedir_orden=True):

        print(celeste("\n--- TODAS LAS CITAS ---"))

        if len(self.citas) == 0:
            print(rojo("No existen citas registradas."))
            return

        citas_ordenadas = self.citas
        if pedir_orden:
            print(celeste("\n¿Cómo desea ordenar las citas?"))
            print("1. Quicksort")
            print("2. Burbuja")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                citas_ordenadas = self.ordenar_citas_quicksort(
                    self.citas
                )
            elif opcion == "2":
                citas_ordenadas = self.ordenar_citas_burbuja(
                    self.citas
                )
            else:
                print(rojo("Opción no válida."))
                return

        for cita in citas_ordenadas:
            print(verde(cita))
            print(verde("------------------------"))


    def buscar_citas_por_veterinario(self):
        self.listar_veterinarios()
        try:
            id_veterinario = int(
                input("\nIngrese ID del veterinario: ")
            )
        except ValueError:
            print(rojo("Debe ingresar un número."))
            return
        veterinario = self.buscar_veterinario_por_id(
            id_veterinario
        )
        if veterinario is None:
            print(rojo("Veterinario no encontrado."))
            return
        citas_encontradas = []
        for cita in self.citas:
            if cita.veterinario.id == id_veterinario:
                citas_encontradas.append(cita)
        print(celeste(
            f"\n--- CITAS DE DR(A). {veterinario.nombre} ---"
        ))

        if len(citas_encontradas) == 0:
            print(rojo("El veterinario no tiene citas."))
            return

        for cita in citas_encontradas:
            print(verde(cita))
            print(verde("------------------------"))

    # ANOTACIONES

    def agregar_anotacion_cita(self):
        if len(self.citas) == 0:
            print(rojo("\nNo existen citas registradas."))
            return
        self.listar_citas(pedir_orden=False)
        try:
            id_cita = int(
                input("\nIngrese el ID de la cita: ")
            )
        except ValueError:
            print(rojo("Debe ingresar un número."))
            return
        cita_encontrada = None
        for cita in self.citas:

            if cita.id == id_cita:
                cita_encontrada = cita
                break

        if cita_encontrada is None:
            print(rojo("Cita no encontrada."))
            return

        print(celeste("\nCita seleccionada:"))
        print(verde(cita_encontrada))

        anotacion = input(
            "\nIngrese la anotación del veterinario: "
        ).strip()

        cita_encontrada.agregar_anotacion(
            anotacion
        )
        print(verde("\nAnotación registrada correctamente."))
