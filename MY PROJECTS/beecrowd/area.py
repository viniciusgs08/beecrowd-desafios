from builtins import map

PI = 3.14159

A, B, C = map(float, input().split())

triangulo = (A * C) / 2.0
circulo = PI * (C ** 2)
trapezio = ((A + B) * C) / 2.0
quadrado = B ** 2
retangulo = A * B

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")