
def getCounter(str, dict):
   length = len(str)
   for x in range(0,length,1):
     key = str[x]
     value= dict.get(key,0)
     dict[key]=value+1
   return dict


def compare(note_dict, magazine_dict):

    for x in note_dict.keys():
        if(note_dict.get(x) <= magazine_dict.get(x, 0)):
            pass
        else:
           return False
    return True    
       
if __name__ == "__main__":

  note_dict = getCounter(input("Enter the note:"), {})
  magazine_dict = getCounter(input("Enter the Magazine:"), {})
  
  print("Result : ", compare(note_dict, magazine_dict))
  
  