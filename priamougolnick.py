def perimetr(a,b):
    return (a+b)*2
def ploshad(a,b):
    return a*b
def diagonal(a,b):
    return round((a**2+b**2)**0.5, 2)
def main():
    a = int(input('введите ширину прямоугольника: '))
    b = int(input('введите длину прямоугольника: '))
    print("Периметр =", perimetr(a,b),"\nПлощадь =", ploshad(a,b), "\nДиагональ =", diagonal(a,b))
main()
