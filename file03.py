def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    
    for i in range(len(data)):
        
        if data[i].isdigit():
            l.append(data[i])
        
        
        
    

        

    return l
f=open('txt_file/data03.txt')
d=f.read()

print((main(d)))
    
# Read data from file