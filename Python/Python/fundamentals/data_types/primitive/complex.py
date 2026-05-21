# complex: numbers with a real and imaginary part

z = 3 + 4j
w = complex(1, -2)

print(z)              # (3+4j)
print(z.real)         # 3.0
print(z.imag)         # 4.0
print(type(z))        # <class 'complex'>

# Arithmetic
print(z + w)          # (4+2j)
print(z * w)          # (11-2j)
print(abs(z))         # magnitude → 5.0
