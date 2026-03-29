import numpy as np
arr1=np.array([10,20,30,40,50,60])
arr2=np.array([1,2,3,4,5,6])
print("array1:",arr1)
print("array2",arr2)
sum_arr=arr1+arr2
diff_arr=arr1-arr2
prod_arr=arr1*arr2
div_arr=arr1/arr2
print("\nelement-wise addition",sum_arr)
print("\nelement-wise subtraction",diff_arr)
print("\nelement-wise multiplication",prod_arr)
print("\nelement-wise division",div_arr)
reshaped_arr=arr1.reshape(2,3)
print("\nreshaped array(2*3):\n",reshaped_arr)