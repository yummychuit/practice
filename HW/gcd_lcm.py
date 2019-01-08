num1 = 9
num2 = 18

bigger_num = max(num1, num2)
smaller_num = min(num1, num2)

t = 1
while t > 0:
        t = bigger_num % smaller_num
        bigger_num, smaller_num = smaller_num, t
        gcd = bigger_num

lcm = num1 * num2 / gcd


for i in range(smaller_num + 1, 0, -1):
    if ((num1 % i == 0) and (num2 % i == 0)):
        gcd = i
        break
        
while(True):
        if((bigger_num % num1 == 0) and (bigger_num % num2 == 0)):
                lcm = bigger_num
                break
        bigger_num += 1


print(gcd) 
print(lcm) 