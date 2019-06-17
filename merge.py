def mergesort(array):
  if len(array) > 1:
    mid = len(array)//2
    leftarr = array[:mid]
    rightarr = array[mid:]
    mergesort(leftarr)
    mergesort(rightarr)
    
    i = 0
    j = 0
    k = 0
    while i < len(leftarr) and j < len(rightarr):
    
      if leftarr[i] < rightarr[j]:
        array[k] = leftarr[i]
        i += 1
      else:
        array[k] = rightarr[j]
        j += 1
      
      
      k +=1
      
    while i < len(leftarr):
    
       array[k] = leftarr[i]
       i += 1
       k += 1
      
    while j < len(rightarr):
       array[k] = rightarr[j]]
       j += 1
       k += 1
        
    return array
      
   
    
