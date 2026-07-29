n = int(input('Escolha um numero entre 0 e 9999:' ))
milhar = n // 1000
centena = (n % 1000) // 100
dezena = (n % 100) // 10
unidade = n % 10
print(f'Milhar: {milhar}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Unidade: {unidade}')