import random

# 2) Gera os 12 dígitos base do CNPJ:
#    – 8 dígitos aleatórios + filial "0001"
base = [random.randint(0, 9) for _ in range(8)] + [0, 0, 0, 1]

# 3) Calcula o 1º dígito verificador (c1)
weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
sum1 = sum(d * w for d, w in zip(base, weights1))
r1 = sum1 % 11
c1 = 0 if r1 < 2 else 11 - r1

# 4) Calcula o 2º dígito verificador (c2)
digits13 = base + [c1]
weights2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
sum2 = sum(d * w for d, w in zip(digits13, weights2))
r2 = sum2 % 11
c2 = 0 if r2 < 2 else 11 - r2

# 5) Monta e envia o CNPJ completo (14 dígitos)
cnpj = "".join(str(d) for d in base) + str(c1) + str(c2)
keyboard.send_keys(cnpj)
