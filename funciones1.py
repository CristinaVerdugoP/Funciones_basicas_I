#1
def número_de_grupos_alimentarios():
    return 5
print(número_de_grupos_alimentarios())
#entregará el numero 5

#2
def numero_de_ramas_militares():
    return 5
#print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo() + número_de_ramas_militares())
#el numero de ramas militares entregara el numero 5, pero la otra funcion no esta definida asi que habrá un error

#3
def número_de_libros_en_espera():
    return 5
    return 10
print(número_de_libros_en_espera())
#entregara el numero 5

#4
def numero_de_dedos():
    return 5
    print(10)
print(numero_de_dedos())
#entregara el numero 5, ya que el print esta debajo del return

#5
def número_de_lagos_grandes():
    print(5)
x = número_de_lagos_grandes()
#print(x)
#habra un error

#6
def add(b,c):
    print(b+c)

#print(add(1,2) + add(2,3))
#entregara la suma de las funciones con sus respectivos parametros, es decir 8

#7
def concatenar(b,c):
    return str(b)+str(c)
#="función de soporte python from-rainbow">print(concatenar(2,5))
#Tambien habra un error de sintaxis

#8
def numero_de_oceanos_o_dedos_o_continentes():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(numero_de_oceanos_o_dedos_o_continentes())
#primero imprime a b, como b no es menor que 10, entonces entregara 54

#9
def número_de_días_en_una_semana_silicona_o_lados_del_triángulo(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
    print(número_de_días_en_una_semana_silicona_o_lados_de_triángulo(2,3))
#print(número_de_días_en_una_semana_silicona_o_lados_de_triángulo(5,3))
#print(número_de_días_en_una_semana_silicona_o_lados_de_triángulo(2,3) + número_de_días_en_una_semana_silicona_o_lados_de_triángulo(5,3))
#entregara un error4

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#ahora si entregara la suma de los numeros 3 y 5 = 8

#11
b = 500
print(b)
def foobar():
    #b ="operador de palabra clave from-rainbow">= 300
    print(b)
#print(b)
#foobar()
#print(b)
#primero imprime 500, pero luego habra un error con la funcion por la sintaxtis de b


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#ahora si imprimira 500 cada vez que llame a b, pero cuando llama a la funcion b es 300, asi que entregara 300

#13
b = 500
print("seccion 13:",b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#imprime 500, 500, 300, 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#dará error

#15
def foo():
    print(1) #imprime 1
    x = bar() #bar imprime 3 y entrega 5
    print(x) 
    return 10 #finalmente entrega 10

def bar():
    print(3)
    return 5

y = foo()
print(y)
#imprime 1, 3, 5, 10