from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    prefix = strs[0]
    if len(strs) > 1:
        for i in strs:
            checkPrefix = ''
            for j in range(min(len(i), len(prefix))):
                if prefix[j] == i[j]:
                    checkPrefix += i[j]
                elif j != 0:
                    break
                else:
                    return ''
            prefix = checkPrefix
    return prefix