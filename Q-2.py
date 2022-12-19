import numpy as np
inp = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
label = np.array([0, 0, 0, 1])
weight = [1, 0.5]
theta = 1.5
l = 0.1      #learning rate
epoch = 20
for j in range(0, epoch):
    print("Epoch: ", j)
    count = 0
    for i in range(0, inp.shape[0]):
        T = label[i]
        instance = inp[i]
        x1 = instance[0]
        x2 = instance[1]
        #net=(w11*x1)+(w21*x2)-theta
        net = (weight[0]*x1)+(weight[1]*x2)-theta   #equation
        if net > 0:
            y = 1
        else:
            y = 0
        delta = T-y
        if delta != 0:
            weight[0] = weight[0]+(l*delta*x1)
            weight[1] = weight[1]+(l*delta*x2)
            theta = theta+(l*delta*(-1))
        else:
            count = count+1
        print("Calculated value:", y, "   Actual value:", delta)
    if count == inp.shape[0]:
        break
    print(".............")