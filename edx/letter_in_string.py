def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    low = 0
    high = len(aStr)
    mid = (low + high) // 2

    i = 0
    while i < 50:
        i += 1
        if len(aStr) <= 0:
            return False
        if char == aStr[mid]:
            return True
        if (low == mid or high == mid) and (char != aStr[mid]):
            return False
        else:
            if char > aStr[mid]:
                low = mid
                return isIn(char, aStr[low:high])
            else:
                high = mid
                return isIn(char, aStr[low:high])

print (isIn("v","abcdefghixyz"))