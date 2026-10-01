from veterinaria import Veterinaria
from colores import celeste, rojo, verde

def mostrar_menu():
    print("\n")
    print(celeste("===================================="))
    print(celeste("     SISTEMA DE VETERINARIA"))
    print(celeste("===================================="))
    print("1. Registrar cliente")
    print("2. Buscar cliente")
    print("3. Registrar mascota")
    print("4. Listar veterinarios")
    print("5. Registrar cita")
    print("6. Buscar citas por veterinario")
    print("7. Listar todas las citas")
    print("8. Agregar anotación a una cita")
    print("9. Listar cantidad de citas por doctor y día")
    print(rojo("0. Salir"))
    print(celeste("===================================="))


def main():
    veterinaria = Veterinaria()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            veterinaria.registrar_cliente()
            input(celeste("\nPresione Enter para continuar..."))

        elif opcion == "2":
            veterinaria.buscar_cliente_menu()
            input(celeste("\nPresione Enter para continuar..."))

        elif opcion == "3":
            dni = input(
                "\nIngrese DNI del cliente: "
            ).strip()
            cliente = veterinaria.buscar_cliente(dni)
            if cliente is None:
                print(rojo("Cliente no encontrado."))
                input(celeste("\nPresione Enter para continuar..."))
                continue
            veterinaria.registrar_mascota(cliente)
            input(celeste("\nPresione Enter para continuar..."))

        elif opcion == "4":
            veterinaria.listar_veterinarios()
            input(celeste("\nPresione Enter para continuar..."))

        elif opcion == "5":
            veterinaria.registrar_cita()
            input(celeste("\nPresione Enter para continuar..."))

        elif opcion == "6":
            veterinaria.buscar_citas_por_veterinario()
            input(celeste("\nPresione Enter para continuar..."))

        elif opcion == "7":
            veterinaria.listar_citas()
            input(celeste("\nPresione Enter para continuar..."))

        elif opcion == "8":
            veterinaria.agregar_anotacion_cita()
            input(celeste("\nPresione Enter para continuar..."))

        elif opcion == "9":
            veterinaria.listar_cantidad_citas_por_dia()
            input(celeste("\nPresione Enter para continuar..."))

        elif opcion == "0":
            print(verde("\nHasta luego."))
            print(verde("Programa finalizado."))
            break

        else:
            print(rojo('Opción incorrecta'))
            input(celeste("\nPresione Enter para volver al menú..."))

if __name__ == "__main__":
    main()
