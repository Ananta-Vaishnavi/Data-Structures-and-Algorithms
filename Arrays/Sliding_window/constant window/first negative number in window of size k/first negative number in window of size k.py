def FirstNegativeInteger( A, N, K):
    answer=[]
    neg=[]
    for i in range(K):
        if A[i]<0:
            neg.append(A[i])
    start=0 
    end=K-1
    while end!=len(A):
        if A[end]<0 and start!=0:
            neg.append(A[end])
        if neg and start>0 and A[start-1]==neg[0]:
            neg.pop(0)
        if neg:
            answer.append(neg[0])
        else:
            answer.append(0)
        end+=1
        start+=1
    return answer
print(FirstNegativeInteger( A, N, K))
