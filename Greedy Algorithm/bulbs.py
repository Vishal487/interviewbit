def minSwitch(A):
    switchs_pressed = 0
    for e in A:
        if switchs_pressed  % 2 == 0:
            if e == 0:
                switchs_pressed += 1
        else:
            if e == 1:
                switchs_pressed += 1
    return switchs_pressed


A = [0,1,0,1]
print(minSwitch(A))
