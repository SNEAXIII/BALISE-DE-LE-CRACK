def valideur(a, b):
    print(a == b)


## s5
## ex 1
def convertir(l, res=0):
    for i, a in enumerate(l[::-1]):
        res += a * 2**i
    return res


valideur(convertir([1, 0, 1, 0, 0, 1, 1]), 83)

## ex 2

def tri_insertion(L):
  n = len(L)
  if L is None: return L
  for j in range(1,n):
    e = L[j] 
    i = j
    # A l'étape j, le sous-liste L[0,j-1] est trié
    # et on insère L[j] dans ce sous-liste en déterminant
    # le plus petit i tel que 0 <= i <= j et L[i-1] > L[j].
    while i > 0 and L[i-1] > e:
      i = i - 1
    # si i != j, on décale le sous liste L[i,j-1] d’un cran
    # vers la droite et on place L[j] en position i
    if i != j:
      for k in range(j,i,...):
        L[k] = L[...]
      L[i] = ...
  return L

"""
def tri_insertion(L):
    if L is None: return L
    for i,element in enumerate(L):
        
    return L
"""