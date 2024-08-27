def fun(string):
    a=' '.join(char for char in string if char.isupper())
    return a
if __name__=='__main__':
    string='ASDFG dfghj ASDFG dfghjcv SDFGH'
    