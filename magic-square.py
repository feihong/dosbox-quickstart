import itertools

lst = list(range(1,10))

def sum(lst, i, j, k):
    return lst[i] + lst[j] + lst[k]

for p in itertools.permutations(lst, len(lst)):
  if sum(p, 0, 1, 2) != 15:
    continue
  if sum(p, 3, 4, 5) != 15:
     continue
  if sum(p, 6, 7, 8) != 15:
     continue
  if sum(p, 0, 3, 6) != 15:
     continue
  if sum(p, 1, 4, 7) != 15:
     continue
  if sum(p, 2, 5, 8) != 15:
     continue
  if sum(p, 0, 4, 8) != 15:
     continue
  if sum(p, 2, 4, 6) != 15:
     continue
  
  print(f'Solution: {p}')
  break
