"""Colores ANSI claros para la interfaz de la terminal."""

ROJO_CLARO = "\033[91m"
CELESTE_CLARO = "\033[96m"
VERDE_CLARO = "\033[92m"
RESTABLECER = "\033[0m"


def rojo(texto):
    return f"{ROJO_CLARO}{texto}{RESTABLECER}"


def celeste(texto):
    return f"{CELESTE_CLARO}{texto}{RESTABLECER}"


def verde(texto):
    return f"{VERDE_CLARO}{texto}{RESTABLECER}"
