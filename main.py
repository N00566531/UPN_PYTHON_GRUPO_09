from veterinaria import Veterinaria

def mostrar_menu():
    print("\n")
    print("====================================")
    print("     SISTEMA DE VETERINARIA")
    print("====================================")
    print("1. Registrar cliente")
    print("2. Buscar cliente")
    print("3. Registrar mascota")
    print("4. Listar veterinarios")
    print("5. Registrar cita")
    print("6. Buscar citas por veterinario")
    print("7. Listar todas las citas")
    print("8. Agregar anotación a una cita")
    print("0. Salir")
    print("====================================")


def main():
    veterinaria = Veterinaria()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            veterinaria.registrar_cliente()

        elif opcion == "2":
            veterinaria.buscar_cliente_menu()

        elif opcion == "3":
            dni = input(
                "\nIngrese DNI del cliente: "
            ).strip()
            cliente = veterinaria.buscar_cliente(dni)
            if cliente is None:
                print("Cliente no encontrado.")
                continue
            veterinaria.registrar_mascota(cliente)

        elif opcion == "4":
            veterinaria.listar_veterinarios()

        elif opcion == "5":
            veterinaria.registrar_cita()

        elif opcion == "6":
            veterinaria.buscar_citas_por_veterinario()

        elif opcion == "7":
            veterinaria.listar_citas()

        elif opcion == "8":
            veterinaria.agregar_anotacion_cita()

        elif opcion == "0":
            print("\nGracias por utilizar el sistema.")
            print("Programa finalizado.")
            break

        else:
            print(
                "\nOpción incorrecta. "
                "Seleccione nuevamente."
            )

if __name__ == "__main__":
    main()
