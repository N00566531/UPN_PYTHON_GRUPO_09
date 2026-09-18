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



