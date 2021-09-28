#========== bubble sort

def bubble1(sp):
    
    if len(sp) <= 1:
        return sp
    else:
        for i in range(len(sp)):
            for j in range(len(sp)-1):
                if sp[j] > sp[j+1]:
                    sp[j], sp[j+1] = sp[j+1], sp[j]
        
        return sp

def bubble2(sp):
    if len(sp) <= 1:
        return sp
    else:
        sorted = True
        
        while sorted:
            sorted = False
            
            for i in range(len(sp)-1):
                if sp[i] > sp[i+1]:
                    sp[i], sp[i+1] = sp[i+1], sp[i]
                    sorted = True
                
        return sp


#========== merge sort

def merge(sp):
    if len(sp) <= 1:
        return sp
    else:
        HALF = len(sp)//2

        left = sp[:HALF]
        right = sp[HALF:]

        merge(left)
        merge(right)

        i=j=k=0

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                sp[k] = left[i]
                i+=1
            else:
                sp[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            sp[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            sp[k] = right[j]
            j+=1
            k+=1

        return sp



