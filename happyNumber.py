def isHappy(n: int) -> bool:
    def summing(n):
        summ = 0
        while n > 0:
            n, remains = divmod(n,10)
            summ += pow(remains,2)
        return summ
    buff = set()
    while n != 1 and n not in buff:
        buff.add(n)
        n = summing(n)
    return n ==1