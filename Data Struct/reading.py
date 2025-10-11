#đọc
#with open("Hello.txt", 'r') as file1:
#   line = file1.read()
#  print(line)


#viết
with open("Hello.txt", 'w') as file1 :
    line = file1.write("Chao buoi toi")

with open("Hello.txt", 'a') as file1:
    line = file1.write("Toi ten la Pham Tien Anh")

with open("Hello.txt", 'r') as file1:
    line = file1.read()
    print(line)