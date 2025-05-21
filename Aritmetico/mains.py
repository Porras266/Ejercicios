
from modulox import convertir_infija_a_postfija, evaluar_postfija
  
  

# Lista de expresiones infijas (como en la imagen)
expresiones_infijas = [
    "5*4+(9/3+8*2)",
    "7+3*(9+5*2^3-8)",
    "4*(2+3-2)*(4+8-5)",
    "8+4+((5^2+6)*4)",
    "6*2+8-3*2/2"
]

# Procesar cada expresión
for i, expr in enumerate(expresiones_infijas, 1):
    print(f"\n Ejercicio {i}")
    print("Expresión infija:  ", expr)

    # Convertir a postfija
    postfija = convertir_infija_a_postfija(expr)
    print("Expresión postfija:", postfija)

    