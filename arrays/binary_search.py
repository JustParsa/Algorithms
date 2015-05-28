# I stole this because it was nice and makes a lot of sense.
def binary_search(array, target):
  lower = 0
  upper = len(array)
  while lower < upper:   # use < instead of <=
    x = lower + (upper - lower) // 2
    val = array[x]
    if target == val:
      return x
    elif target > val:
      if lower == x:   
        break        
      lower = x
    elif target < val:
      upper = x
