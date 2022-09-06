def isPalindrome(self, x: int) -> bool:
    strValue = str(x)
    if strValue == strValue[::-1]:
        return True
    return False