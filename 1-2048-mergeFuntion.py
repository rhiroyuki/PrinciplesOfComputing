"""
Merge function for 2048 game. Python 2
"""

def zeroToRight(newlst):
    """
    Place all zeros to the right side of the list (end of the list)
    """
    lst = []
    for dummy_j in range(len(newlst)):
        if(newlst[dummy_j] != 0):
            lst.append(newlst[dummy_j])
    while(len(lst)<len(newlst)):
        lst.append(0)
    return lst

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    newlst = zeroToRight(line)
    lst2 = []
    aux = 0

    while(aux < len(line)):
        if(aux+1<len(line) and newlst[aux] == newlst[aux+1]):
            lst2 = newlst[:aux]
            lst2.append(newlst[aux] * 2)
            lst2[aux+1:] = newlst[aux+2:]
            lst2.append(0)
        else:
            lst2 = newlst
        newlst = lst2
        lst2 = []
        aux += 1
    return newlst

if __name__ == '__main__':
    print (merge([1, 1, 1, 1]),'should return [2, 2, 0, 0]')
    print (merge([2, 0, 2, 4]),'should return [4, 4, 0, 0]')
    print (merge([0, 0, 2, 2]),'should return [4, 0, 0, 0]')
    #print merge([2, 2, 0, 0]),'should return [4, 0, 0, 0]'
    #print merge([2, 2, 2, 2, 2]),'should return [4, 4, 2, 0, 0]'
    #print merge([8, 16, 16, 8]),'should return [8, 32, 8, 0]'
    ##print merge([4, 2, 2]),'should return [4, 4, 0]'
    #print merge([8, 8]), 'should return [16, 0]'
    #print merge([4, 2, 8, 2, 0, 8, 8]), 'should return [4, 2, 8, 2, 16, 0, 0]' 