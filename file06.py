def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=data.split('\n')
    f=[]
    for i in range(len(l)):
        f.append(len(l[i]))

   
    
    return f
f=open('txt_file/data06.txt')
d=f.read()
print((main(d)))
# Read data from file
# Read data from file