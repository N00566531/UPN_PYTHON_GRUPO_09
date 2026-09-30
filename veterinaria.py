from models import Cliente, Mascota, Veterinario, Cita

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
            Veterinario("Carlos Pérez")
        )
        self.veterinarios.append(
            Veterinario("María Rodríguez")
        )

    def listar_veterinarios(self):
        print("\n--- VETERINARIOS ---")
        for veterinario in self.veterinarios:
            print(veterinario)

    def buscar_veterinario_por_id(self, id_veterinario):
        for veterinario in self.veterinarios:
            if veterinario.id == id_veterinario:
                return veterinario
        return None

    # CLIENTES

    def registrar_cliente(self):
        print("\n--- REGISTRAR CLIENTE ---")
        while True:
            dni = input("DNI: ").strip()
            if dni.isdigit():
                break
            print("El DNI debe contener solo números.")

        if dni in self.clientes:
            print("El cliente ya se encuentra registrado.")
            return self.clientes[dni]

        nombre = input("Nombre: ").strip()
        telefono = input("Teléfono: ").strip()
        cliente = Cliente(
            dni=dni,
            nombre=nombre,
            telefono=telefono
        )
        self.clientes[dni] = cliente
        print("\nCliente registrado correctamente.")
        print(cliente)
        return cliente

    def buscar_cliente(self, dni):
        return self.clientes.get(dni)

    def mostrar_cliente(self, cliente):
        if cliente is None:
            print("Cliente no encontrado.")
            return
        print("\n--- DATOS DEL CLIENTE ---")
        print(cliente)
        print("\n--- MASCOTAS ---")
        if len(cliente.mascotas) == 0:
            print("El cliente no tiene mascotas registradas.")
            return
        for mascota in cliente.mascotas:
            print(mascota)

    def buscar_cliente_menu(self):
        print("\n--- BUSCAR CLIENTE ---")
        while True:
            dni = input("Ingrese DNI: ").strip()
            if dni.isdigit():
                break
            print("El DNI debe contener solo números.")

        cliente = self.buscar_cliente(dni)
        if cliente is None:
            print("Cliente no encontrado.")
            return
        self.mostrar_cliente(cliente)

    # MASCOTAS

    def registrar_mascota(self, cliente):
        print("\n--- REGISTRAR MASCOTA ---")
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
        print("\nMascota registrada correctamente.")
        print(mascota)
        return mascota

    def seleccionar_mascota(self, cliente):
        if len(cliente.mascotas) == 0:
            print("\nEl cliente no tiene mascotas registradas.")
            print("Se registrará una nueva mascota.")
            return self.registrar_mascota(cliente)

        print("\n--- MASCOTAS DEL CLIENTE ---")

        for mascota in cliente.mascotas:
            print(mascota)

        print("0 - Registrar nueva mascota")
        try:
            id_mascota = int(
                input("\nSeleccione mascota: ")
            )
        except ValueError:
            print("Debe ingresar un número.")
            return None

        if id_mascota == 0:
            return self.registrar_mascota(cliente)

        for mascota in cliente.mascotas:
            if mascota.id == id_mascota:
                return mascota

        print("Mascota no encontrada.")
        return None

    # CITAS

    def registrar_cita(self):

        print("\n==============================")
        print("       REGISTRAR CITA")
        print("==============================")
        dni = input("Ingrese DNI del cliente: ").strip()
        cliente = self.buscar_cliente(dni)

        # Si cliente no existe
        if cliente is None:
            print("\nCliente no encontrado.")
            opcion = input(
                "¿Desea registrar al cliente? (s/n): "
            ).lower()

            if opcion == "s":
                cliente = self.registrar_cliente()
            else:
                return

        # Mostrar cliente
        self.mostrar_cliente(cliente)

        # Seleccionar mascota
        mascota = self.seleccionar_mascota(cliente)

        if mascota is None:
            return

        # Seleccionar veterinario
        self.listar_veterinarios()
        try:
            id_veterinario = int(
                input("\nSeleccione veterinario: ")
            )
        except ValueError:
            print("Debe ingresar un número.")
            return

        veterinario = self.buscar_veterinario_por_id(
            id_veterinario
        )

        if veterinario is None:
            print("Veterinario no encontrado.")
            return

        # Fecha
        fecha = input(
            "Ingrese fecha de la cita (DD/MM/YYYY HH:MM): "
        ).strip()

        cita = Cita(
            cliente=cliente,
            mascota=mascota,
            veterinario=veterinario,
            fecha=fecha
        )

        self.citas.append(cita)

        print("\nCita registrada correctamente.")
        print(cita)


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

        print("\n--- TODAS LAS CITAS ---")

        if len(self.citas) == 0:
            print("No existen citas registradas.")
            return

        citas_ordenadas = self.citas
        if pedir_orden:
            print("\n¿Cómo desea ordenar las citas?")
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
                print("Opción no válida.")
                return

        for cita in citas_ordenadas:
            print(cita)
            print("------------------------")


    def buscar_citas_por_veterinario(self):
        self.listar_veterinarios()
        try:
            id_veterinario = int(
                input("\nIngrese ID del veterinario: ")
            )
        except ValueError:
            print("Debe ingresar un número.")
            return
        veterinario = self.buscar_veterinario_por_id(
            id_veterinario
        )
        if veterinario is None:
            print("Veterinario no encontrado.")
            return
        citas_encontradas = []
        for cita in self.citas:
            if cita.veterinario.id == id_veterinario:
                citas_encontradas.append(cita)
        print(
            f"\n--- CITAS DE DR(A). {veterinario.nombre} ---"
        )

        if len(citas_encontradas) == 0:
            print("El veterinario no tiene citas.")
            return

        for cita in citas_encontradas:
            print(cita)
            print("------------------------")

    # ANOTACIONES

    def agregar_anotacion_cita(self):
        if len(self.citas) == 0:
            print("\nNo existen citas registradas.")
            return
        self.listar_citas(pedir_orden=False)
        try:
            id_cita = int(
                input("\nIngrese el ID de la cita: ")
            )
        except ValueError:
            print("Debe ingresar un número.")
            return
        cita_encontrada = None
        for cita in self.citas:

            if cita.id == id_cita:
                cita_encontrada = cita
                break

        if cita_encontrada is None:
            print("Cita no encontrada.")
            return

        print("\nCita seleccionada:")
        print(cita_encontrada)

        anotacion = input(
            "\nIngrese la anotación del veterinario: "
        ).strip()

        cita_encontrada.agregar_anotacion(
            anotacion
        )
        print("\nAnotación registrada correctamente.")
