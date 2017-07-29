def bsort(array):
    if len(array) < 2:
        return array
    else:
        high = []
        low = []
        mid = array[0]
        midd = [mid]
        print (str(mid) + "mid")
        for n in array:
            
            if n > mid:
                high.append(n)
                print (high)
            elif n < mid:
                low.append(n)
                print (low)
        return bsort(low) + midd + bsort(high)
                
        
            


xx = [4,2,5,8,6,5,3,6,7,8,4,4,4,999,5,4,2]

print (bsort(xx))
