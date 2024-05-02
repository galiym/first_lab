def perimetr(a,b,c,d):
    return a+b+c+d
def ploshad(a,b,c,d):
    return round(((a+b)/2)*((c**2-(((b-a)**2+c**2-d**2)/(2*(b-a)))**2))**0.5, 2)
def sred_lin(a,b,c,d):
    return (a+b)/2
def main():
    a = int(input("введите длину нижнего основания: "))
    b = int(input("введите длину верхнего основания: "))
    c = int(input("введите длину боковой стороны: "))
    d = int(input("введите длину боковой стороны: "))
    print("Периметр =",perimetr(a,b,c,d),"\nПлощадь =",ploshad(a,b,c,d),"\nСредняя линия =", sred_lin(a,b,c,d))
main()
