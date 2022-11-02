def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1=data.split(',')
    l=[]
    
    for i in range(len(list1)):
        l.append(int(list1[i]))

   
   


    return l
f=open('txt_file/data01.txt')
d=f.read()

print((main(d)))

# Read data from file