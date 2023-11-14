# 10tr vs lãi xuất 5,1%/năm. Tính: 1. sau 10 năm có bn tiền 
import math

m = int(input("Số tiền gửi vào ngân hàng là:  "))
a = float(input("Lãi xuất 1 năm là: ")) 
t = int(input("Số tiền có ít nhất sau n năm: "))
s =int(m*(1+a)**10)
n =int(math.log(t/m,1+a))

print ("Sau 10 năm bạn có số tiền là: ", s)
#2. sau bn năm có ít nhất 50tr
print ("Sau", n, "năm thì có ít nhất 50tr")
