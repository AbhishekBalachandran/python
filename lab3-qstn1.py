f = open("sample.txt","a")
f.write("Hello.\nThis is a sample file.\nThank You\n")
f.close()
f = open("sample.txt","r")
print(f.read())

