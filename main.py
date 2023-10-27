roman_nums = {"I": 1, "V": 5, "X": 10, "C": 100, "D": 500, "M": 1000}

def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if roman_nums[left] < roman_nums[right]:
            sum -= roman_nums[left]
        else:
            sum += roman_nums[left]
    sum += roman_nums[romanNumeral[-1]]
    return sum


print("Integer form of Roman Numeral is"),
print(RomanNumeralToDecimal("CVI"))