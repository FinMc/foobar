"""
Solution makes use of whole division to account for the fact numbers may be extremely large
"""

def solution(m,f):
    # converts to long to handle big integers
    m = long(m)
    f = long(f)
    
    counter = 0
    
    # base case that the values are more than one, when they are 1 or below the counter is displayed
    while m>1 or f>1:
        # if mach a lot more than facula it will shrink the size considerably depending on multiple
        if (m>f):
            if (m/f)<100:
                m-=f
                counter+=1
            else:
                counter+=(m//f)
                m-=f*(m//f)
        # if mach a lot more than facula it will shrink the size considerably depending on multiple
        elif (f>m):
            if (f/m)<100:
                f-=m
                counter+=1
            else:
                counter+=(f//m)
                f-=m*(f//m)
        else:
            return "impossible"
    return str(counter)