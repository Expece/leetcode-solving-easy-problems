def romanToInt(s: str) -> int:
    roman_numerals = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
            'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    integer_num = int(0)
    flag = False
    i_plus = ''

    for idx, val in enumerate(s):
        if flag:
            flag = False
            continue
        if idx + 1 < len(s):
            i_plus = s[idx+1]
        if roman_numerals.get(val + i_plus):
            integer_num += roman_numerals.get(val + i_plus)
            flag = True
            continue
        for key in roman_numerals:
            if val == key:
                integer_num += roman_numerals.get(key)
    return integer_num