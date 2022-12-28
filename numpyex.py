import  numpy as np
''''numpy_a=np.array([1,2,3,4,7])
numpy_b=np.array([2,1,3,4])
print(numpy_a*numpy_b)
print(numpy_a.dtype)
print(numpy_a.itemsize)
print(numpy_a.size)'''

'''array_2d=np.array([[1,2], [4,5], [7,8]])
array_3d=np.array([[[1,2,3],[3,5,4],[7,6,8]],[[1,2,3],[3,5,4],[7,6,8]],[[1,2,3],[3,5,4],[7,6,8]]])
print(array_3d)
print(array_3d.ndim)
print(array_3d.shape)
print(array_2d.dtype)'''
'''numpy_a=np.array([[1,2,3,4],[3,5,8,5]])
print(numpy_a[1,2])
print(numpy_a[0,2])
print(numpy_a[:, 2])
print(numpy_a[:, -3])
        #step - start :end:stepsize
print(numpy_a[1, 0:4:1])
print(numpy_a[:,0:4:2])'''

'''array_3d=np.array([[[1,2,3],[3,3,4],[7,4,8]],[[1,1,3],[3,5,4],[2,6,1]],[[1,2,3],[3,7,4],[7,6,1]]])
print(array_3d[:,:,0])
print(array_3d.shape)
array_3d[:,:,0]=[[1,1,1],[1,1,1],[1,1,1]]
print(array_3d)'''

'''p=np.zeros((3,3,2))
print(p)
print(np.full((8,4),[1,2,3,4]))'''


'''arr_st=[[3,6,8,3],[1,7,4,6],[1,0,4,6]]
print(np.sum(arr_st,axis=0))'''


a=np.arange(32).reshape(4,2,2,2)
print(a)
