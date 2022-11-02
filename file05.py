def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    f=0
    d=0
    for i in range(len(data)):
        
        if not data[i].isdigit():
            f+=1
            
        if  data[i].isdigit():
            d+=1
        
        
    

    
    l.append(d)    
    l.append(f)
    return l
f=open('txt_file/data05.txt')
d=f.read()
print((main(d)))
# Read data from file