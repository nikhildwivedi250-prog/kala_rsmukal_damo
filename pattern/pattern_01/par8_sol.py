num = 4


for i in range(num, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()
for i in range(2, num+1):
    for j in range(0, i):
        print("*", end=" ")
    print()

* * * *
* * *
* *
* 
* *
* * *
* * * * 