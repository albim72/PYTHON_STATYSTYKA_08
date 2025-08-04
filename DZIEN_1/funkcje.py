def informacja():
    print("To jest funkcja: informacja nr 43455654")

informacja()

def policz(a,b,c=1):
    return (a+b)*c

print(policz(4,5,3))
print(policz(4,5))

liczby = [1,2,3,4,5,9,11,4,23,7,9,19]
def liczby_parzyste(lista):
    return [x for x in lista if x%2==0]

print(liczby_parzyste(liczby))

#funkcja z listą i słownikiem argumentów
def show_info(*args,**kwargs):
    print(f"lista argumentów: {args}")
    print(f"słownik argumentów: {kwargs}")

show_info(1,7,2,name="Leon",age=27)

#funkcja anonimowa lambda
print((lambda x,y: x+y)(1,2))

u = lambda x,y: x*y
print(u(2,3))

def multi(a):
    return lambda x: x*a

print(multi(2)(3))
