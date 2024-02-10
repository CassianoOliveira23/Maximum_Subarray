
'''
Maximum Subarray Problem

Encontre o subarray contíguo (encostados) de maior valor.

Array [5, 6, -15, 2, 4, -1, 12, -8]

Subarrays:

[5] -> Sum: 5

[5, 6] -> Sum: 11

[6, -15, 2] -> Sum: -7

[2, 4, -1, 12] -> Sum: 17

'''


# Forma mais performatica de resolver

x = [5, 6, -15, 2, 4, -1, 12, -8]

max_soma = x[0]
soma = x[0]

for i in range(1, len(x)):
    if soma + x[i] > x[i]:
        soma += x[i]
    else: soma = x[i]
    
    if soma > max_soma:
        max_soma = soma
print(max_soma)



print('-'*10)



# Forma mais intuitiva, porém é mais ineficiente uma vez que tem 3 FOR percorrendo o array o que torna o algoritmo lento

x = [5, 6, -15, 2, 4, -1, 12, -8]

min_value = float('-inf')

for i in range(len(x)):
    for j in range(i, len(x)):
        soma = 0
        for k in range(i, j+1):
            soma += x[k]
            
        if soma > min_value:
            min_value = soma
print(min_value)