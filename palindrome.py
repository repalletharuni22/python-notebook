n = int(input())
a = n
rev = 0
while n > 0:
    d = n % 10
    rev = rev*10+d
    n=n//10
if rev==a:
    print("palindorme")
else:
    print("no")
