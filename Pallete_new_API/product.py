def Max_array():
    A=[6,8,3,2,3,0,-4,3, -1]
    P_0=1
    P_x=0
    N_zero=0
    P_max=0
    P_min=0
    for i in range(0, len(A)):
        if A[i]!= 0:
                   P_0 =P_0*A[i]
        else:
            N_zero=N_zero+1


        #print (P_0)

    if(N_zero>1):
        return 0
    else:
        for i in range(0,len(A)):
            if A[i] !=0:
                P_x= P_0/A[i]
            else:
                    P_x=0
            if P_x> P_max:
                P_max=P_x
            if P_x< P_min:
                P_min=P_x
           # print(P_0, P_x, P_max, P_min)
        return P_max


print(Max_array())