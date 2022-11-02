def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=data.split(',')
    return list
f=open('txt_file/data01.txt')
d=f.read()

print((main(d)))

# Read data from file