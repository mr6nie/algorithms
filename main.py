# bubble sort

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
