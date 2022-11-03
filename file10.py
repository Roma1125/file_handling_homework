def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=data.split('\n')
    l=0
    for i in f:
        
        if  l<len(i):
             l=int(i)
        
        
        
        

          

    return l
f=open('txt_file/data10.txt')
d=f.read()

print((main(d)))
# Read data from file
# Read data from file