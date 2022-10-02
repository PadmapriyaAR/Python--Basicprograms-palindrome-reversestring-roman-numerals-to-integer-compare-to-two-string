
def so(string):
    r = " "
    l=len(string)
    for i in range(l-1,-1,-1):
       
        r = r + string[i]
        print(r)
    print(r)
        
    
 
if __name__ == "__main__":
    
    so(input("Enter"))
    