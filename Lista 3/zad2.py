import random

Matrix=[random.randint(0, 11)  if j==i else 0 for i in range(0,5,1) for j in range(0,5,1)]
print(Matrix)
