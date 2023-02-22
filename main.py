import numpy as np

#dado as matrizes A e B de ordem, respectivamente, 2x3 e 3x2. Temos a seguinte visualização

matrizA = np.array([[3, 1, 3],[6, 5, 5]])
matrizB = np.array([[100, 50],[50, 100],[50, 50]])
resultado = np.zeros(2) #é preciso declarar um espaço para receber o resultado da multiplicação

#ao multiplicar A por B, usando o simbolo * que padrão para multiplicação, o algoritmo vai, ao invés de realizar a multiplição de matrizes, ele vai multiplicar um termo pelo seu corresponde na mesma posição da outra matriz. Então precisa-se indicar ao código como se quer que a multiplicação ocorra, então usa-se a função .dot da biblioteca numpy para isso.

resultado = np.dot(matrizA, matrizB)

#depois de calculado, agora é só mostrar o resultado

for i in resultado:
  print(i)