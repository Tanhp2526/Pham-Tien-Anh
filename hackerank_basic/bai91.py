import numpy as np

n, m = map(int, input().split())
a = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.mean(a, axis=1))   
print(np.var(a, axis=0))    
print(np.std(a, axis = None))  
