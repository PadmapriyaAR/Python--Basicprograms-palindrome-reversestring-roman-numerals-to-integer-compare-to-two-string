
def palindrome(str):
    length = len(str)
    rev_str = ""
    #reverse the given string.
    for x in range(length-1, -1, -1):
         rev_str += str[x]    
    if str == rev_str:
        print(str,"is a Palindrome")
    else:
        print(str,"ïs not a Palindrome")

if __name__ == "__main__":
    palindrome(input("Enter a String : "))