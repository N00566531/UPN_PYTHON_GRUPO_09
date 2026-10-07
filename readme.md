## Proyecto: Veterinaria

# Flujo de reserva: 

Cliente llega
   ↓
Buscar por DNI
   ↓
¿Existe?
   ├── NO → Registrar cliente
   │
   └── SÍ
        ↓
Mostrar sus mascotas
        ↓
Elegir mascota
   ├── existente
   └── registrar nueva
        ↓
Elegir veterinario
        ↓
Ingresar fecha
        ↓
Registrar cita
        ↓
Veterinario posteriormente
puede agregar anotaciones

# Para ejecutar

python3 main.py


# Algoritmos usados - Dónde se usa

Búsqueda directa por clave - Buscar cliente por DNI
Búsqueda secuencial o lineal - Buscar veterinario, mascota o cita por ID
Filtrado secuencial - Buscar citas por veterinario
Autoincremento - Cliente, Mascota, Veterinario y Cita
Inserción en colección - Registrar mascotas, veterinarios y citas
Inserción por clave - Inserción por clave
Validación condicional - Registro, búsquedas y selección
Iteración - Menú y recorridos de información



## Gestión de citas

- Cada cita dura 30 minutos y se crea en estado `pendiente`.
- Al registrar una cita, ingrese el día, seleccione el doctor y elija la hora.
  Enter acepta el siguiente turno después de la última cita de ese doctor
  en el día seleccionado; para el primer turno se sugiere 09:00.
- Se rechazan horarios que se superponen, incluso parcialmente, con otra cita
  del mismo doctor. Se mantiene el máximo de cuatro citas diarias por doctor.
- La opción 7 permite ordenar por ID con Quicksort o Burbuja y muestra el tiempo
  del algoritmo en milisegundos, sin incluir la impresión de las citas.
- La opción 10 busca por DNI, muestra las citas pendientes y el historial completo.
  Permite marcar una cita pendiente como `atendida`, agregar anotaciones y
  reprogramar. Las anotaciones nuevas se acumulan sin borrar las anteriores.
- Reprogramar conserva la fecha y las anotaciones originales, marca la cita como
  `reprogramada` y crea otra `pendiente`, enlazando ambas mediante sus IDs.
  La cita reprogramada libera el horario y el cupo diario originales.
- Los datos se mantienen en memoria durante la ejecución del programa.

## Pruebas

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```
