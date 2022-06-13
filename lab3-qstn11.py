def file_size(fname):
    import os 
    statinfo = os.stat(fname)
    return statinfo.st_size
print("File size in bytes of the plain file : ",file_size("C:\lab\python\mysample.txt"))