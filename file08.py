def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
  
    l=0
    for i in data:
        
        if i.isdigit() and l<int(i):
             l=int(i)
        
        
        
    

          

    return l
f=open('txt_file/data08.txt')
d=f.read()

print((main(d)))
# Read data from file