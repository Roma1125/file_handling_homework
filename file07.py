def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    
    l=0
    for i in range(len(data)):
        
        if data[i].isdigit():
            l+=(int(data[i]))
        
        
        
    

        

    return l
f=open('txt_file/data07.txt')
d=f.read()

print((main(d)))
    
# Read data from file