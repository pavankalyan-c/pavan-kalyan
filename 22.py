def largest(arr,n): 
  
    # Initialize maximum element 
    max = arr[0] 
  
    # Traverse array elements from second 
    # and compare every element with  
    # current max 
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max
  
# Driver Code 
arr = [20, 345, 55, 90, 9760] 
n = len(arr) 
Ans = largest(arr,n) 
print ("Largest in given array is",Ans) 
  
