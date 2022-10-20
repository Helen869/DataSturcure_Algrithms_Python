# Function: Sort squared array , the arry is in order
# Time=O(n) Space=O(n)
#Input: Array in order for example: [-3,-1,0,3,5]  
#Output: Squared Array in order

def Sort_Squared(array):
    leftpointer = 0
    rightpointer = len(array)-1
    newArray = [0]*len(array)
    for i in range(len(array)):
      left_squa = array[leftpointer]**2
      right_squa = array[rightpointer]**2
      if left_squa > right_squa:
         newArray[len(array)-1-i] = left_squa
         leftpointer += 1
      else:
          newArray[len(array)-1-i] = right_squa
          rightpointer -=  1
    return newArray

arrb = [-3,-1,0,3,5]
print(Sort_Squared(arrb))