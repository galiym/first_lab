a = int(input("введите длину нижнего основания: "))
b = int(input("введите длину верхнего основания: "))
c = int(input("введите длину боковой стороны: "))
d = int(input("введите длину боковой стороны: "))
P = a+b+c+d
S = round(((a+b)/2)*((c**2-(((b-a)**2+c**2-d**2)/(2*(b-a)))**2))**0.5, 2)
m = (a+b)/2
print("Периметр =",P,"\nПлощадь =",S,"\nСредняя линия =", m)
