## Variables del módulo
PI = 3.1415925635
EULER = 2.71828182845

## Funciones del módulo
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

# print("No estoy en el main")

## Sector "main" del archivo
if __name__ == "__main__":
    from main import multiplicacion
    resultado = multiplicacion(3,3)
    print("El resultado es:", resultado)