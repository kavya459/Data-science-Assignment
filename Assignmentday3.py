Question 1
import numpy as np
Arr=np.array([2,5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50])
print(Arr)


Question 2
import numpy as np
List1=[1,23,3,44,5]
List2=[63,7,18,94,11]
arr1=np.asarray(List1)
arr2=np.asarray(List2)
arr=np.concatenate((arr1,arr2))
print(np.sort(arr))

Question. 3
import numpy as np
arr=np.array([[1,9,3],[4,5,7],[5,8,4]])
print(arr.ndim,arr.size)
Question 4

import numpy as np 
arr1=print(np.arange(7))
arr2=print(np.expand_dims(arr1,axis=0).shape)

Question 5

import numpy as np
arr1=np.array([[1,9,3],[4,5,7],[5,8,4]])
arr2=np.array([[34,66,77],[2,7,8],[44,8,3]])
arr1=print(np.hstack(arr1))
arr2=print(np.vstack(arr2))

Question 6

import numpy as np 
arr1=np.array([1,2,2,5,1,7,8,1])
arr2=print(np.unique(arr1,return_counts=True))

  
