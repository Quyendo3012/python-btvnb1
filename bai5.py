x = int(input("Nhập x = "))
dem = 1 
while(x>9):
    x = x/10
    x = int(x)
    dem+=1
    
print("Có", dem, "chữ số")
print("Chữ số đầu tiên là: ",x)