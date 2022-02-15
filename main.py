import numpy as np


# img = np.random.random((3,3,3))
img = [[[ 0  0  0]
        [ 0  1  0 ]
        [ 0  0  0]]
         
       [[ 0  0  0]
        [ 0  1  0 ]
        [ 0  0  0]]
         
       [[ 0  0   0]
        [ 0  1  0]
        [ 0  0  0]]]

segment = []
first = 1
num = 1
around_g = ###
new_num = ###
for i in img:    # RGB
    for m in i:    # line
        for g in m:    # pixel
            if first == num:    # g = 1 if first pixel
                first = 0
                segment.append(num)
            else:
                if {g close to {around_g}}:    # g = 
                    g = {around_g}
                    segment.append(g)
                else:
                    g = new_num    # newest_num
                    segment.append(g)
  
