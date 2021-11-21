# cambiando la public key
# Cap. 1 : Constants and Variables
x = 2        # integer
y = 12.2     # float
a = 'hola'   # string

type(a)      # -> Saca el tipo de variable
type(y)
type(x)

# Conversión de tipos de variable
i_var = '123'
s_var = str(i_var) # convierte en string

print(s_var)

# Operadores
op = 2 + 2   # Suma
op = 2 - 2   # Resta
op = 2 * 2   # Multiplicar
op = 2 / 2   # Dividir
op = 2 ** 2  # Potenciar
op = 2 % 2   # Modulo -- Toma el primer número, lo divide por el segundo y devuelve el resto.

# Orden: Parentesis > Potencia > Mult > Suma > LtoR

inp_s = input('Meter un número') # la función input siempre devuelve un string, hay que transf.
inp_i = int(inp_s) + 20 # al transformar en int se puede operar.
print('la variable vale', inp_i)

# conditional execution
if inp_i < 10:
    print('Es')
elif inp_i == 22:            # si se cumple el primer elif se saltea los demás, aunque haya varios
    print('Le pegaste')
    print("sos un groso")
elif inp_i != 21:
    print('Sos boludo')
else:
    print('No es')
print('Terminó')