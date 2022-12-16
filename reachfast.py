number1 = input("Enter number and hit enter ")

if int(number1) > 500:
        number1 = 500 

for x in range(int(number1)):

        x, y, z = [int(x) for x in input().split()] 

        s = divmod(abs(y-x),z)
        if s[1] != 0:
                cnt = s[0] + 1
        else:
                cnt = s[0]
        print (cnt)