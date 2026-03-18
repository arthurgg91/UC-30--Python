ef verificar_numero(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "zero"

resultado = verificar_numero(-5)
print(resultado)