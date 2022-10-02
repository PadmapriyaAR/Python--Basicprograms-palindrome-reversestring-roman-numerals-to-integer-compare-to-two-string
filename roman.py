roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def rCharToInt(rChar):
    return roman_dict.get(rChar, 0)

def convertRomanToInt(roman):
    length = len(roman)
    result = 0
    x = 0
    while(x < length):  
        if x + 1 < length and rCharToInt(roman[x]) < rCharToInt(roman[x+1]):
            result = result+ rCharToInt(roman[x+1]) - rCharToInt(roman[x])
            x = x + 2
        else:
            result = result + rCharToInt(roman[x])
            x = x + 1
    return result
    
if __name__ == "__main__":    
    print("Result ", convertRomanToInt(input("Enter the Roman literal:")))

        
        