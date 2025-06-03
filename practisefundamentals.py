==> Sum of Two-digit numbers

def double():
    n=[3,5,34,72,1,2]
    sum=0
    for x in n:
        if 10 <= x < 100:
            sum+=x
    print(sum)
double()


==> Password Valid or Not

password=123
x=int(input())

if x==password:
    print("login successful")
else:
    print("login fail")
	
	
	
==> Password Check for n times

password=123

while True:
    print("enter the password ")
    n=int(input())
    if n==password:
        print("login successful")
        break
    else:
        print("login fail")
		
		
		
	
==> Password check for 3 attempts

password=123
for i in range(3):
    print("enter the password ")
    n=int(input())
    if n==password:
        print("login successful")
        break
    else:
        print(i+1,"attempts is done in 3 attempts",3-i-1,"attempts remain")
else:
    print("login fail and account blocked")



==> Armstrong Number

n=int(input())
temp=n
count=0
while n:
    n//=10
    count+=1
print(count)
sum=0
n=temp
while n:
    x=n%10
    sum+=x**count
    n//=10
if(temp==sum):
    print(temp," is armstrong")
else:
    print(temp," is not armstrong")




==> Count of increasing values in a string of numbers until the decreasing number occurred
n = 134532
x = str(n)
count = 1
for i in range(len(x) - 1):

    if x[i] < x[i + 1]:
        count += 1
    else:
        break
print("The increasing values count is", count)



==> Nth digit in fibbonacci series

n=6
if n<=1:
    print(n)
else:
    first=0
    second=1
    for i in range(2,n+1):
        third=first+second
        first=second
        second=third
    print(third)




==> number is even or odd

print("enter number")
n=int(input())
if n%2==0:
    print(n," is even")
else:
    print(n," is odd")
	

	


==> Lowercase letters in String

n="HeLlo WoRlD"
for i in n:
    if 97<= ord(i) <=122:
        print(i)
		



==> Code to display the Total marks and Average of students

class cse:
    def __init__(self, name):
        print(f"Details of {name}")
        self.dsa = int(input("DSA : "))
        self.py = int(input("PYTHON : "))
        self.java = int(input("JAVA : "))

    def total(self):
        return (self.dsa + self.py+ self.java)

    def avg(self):
        return self.total() / 3


narasimha = cse("NARASHIMA")
yuvaraj = cse("yuvaraj")
pavan = cse("pavan")

print("Narasimha Total is",narasimha.total())
print("Narasimha Average is",narasimha.avg())

print("Yuvaraj Total is",yuvaraj.total())
print("Yuvaraj Average is",yuvaraj.avg())

print("Pavan Total is",pavan.total())
print("Pavan Average is",pavan.avg())




==> Checking if the number 'n' comes in 'k' table or not

n=int(input("enter the main number: "))
x=int(input("enter the checking number: "))
if n%x==0:
    print(n," will come in ",x,"table")
else:
    print(n," will not come in ",x,"table")




==>Printing numbers n to 1

def num(n):
    for i in range(1,n+1):
        print(n)
        n -= 1
n=int(input())
num(n)

or

def num(n):
    i=1
    while n>=i:
        print(n)
        n-=1
n=int(input())
num(n)




==> Print n numbers

def num(n):
    for i in range(1,n+1):
        print(i)
n=int(input())
num(n)


def num(n):
    i=1
    while i<=n:
        print(i)
        i+=1
n=int(input())
num(n)
		


==> Print Numbers & Characters Separately

n="Hi087b59saer31"
characters=""
numbers=""
for i in n:
    if 65<= ord(i) <=90 or 97<= ord(i) <=122:
        characters+=i
    elif 48<=ord(i)<=57:
        numbers+=i
print(numbers, end=" ")
print(characters, end=" ")




n="Hi087b59saer31"
char=""
num=""
for i in n:
    if 65<= ord(i) <=90 or 97<= ord(i) <=122:
        char+=i
    else:
        num+=i
print(char, num)


==> Print Numbers in String

n="Hi087b59saer31"
for i in n:
    if 48<=ord(i)<=57:
        print(i)
		


n="Hi087b59saer31"
for i in n:
    if ord(i) in range(48,57):
        print(i)



==> Check which is greater among the even index element sum or odd index element sum

n=[1,2,3,4,5]
odd_sum=0
even_sum=0
for i in n:
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print("even index elements sum is",even_sum)
print("odd index elements sum is",odd_sum)
if even_sum>odd_sum:
    print(even_sum,"is greater than odd index elements sum",odd_sum)
elif odd_sum>even_sum:
    print(odd_sum,"is greater than even index elements sum",even_sum)
else:
    print("both are equal")




n=[1,2,3,4,5]
even=odd=0
for i in range(1,len(n),2):
    even+=n[i-1]
    odd+=n[i]
if (len(n)-1)%2==0:
    even+=n[-1]

print(even, end=" ")
print(odd)
if even>odd:
    print(even,"even is greater than odd")
elif odd>even:
    print(odd,"odd is greater than even")
else:
    print("both are equal")
	




==> Recursive Function

def a(n):
    if n==1:
        return
    a(n-1)
    print(n, end=" ")
    a(n-1)
a(5)


==> Recursive Function2

def a(n):
    if n==1:
        return
    a(n-1)
    print(n, end=" ")
a(5)


==> Single digit numbers in list


def single():
    n=[3,5,34,72,1,2]
    for x in n:
        if x<10:
            print(x)
single()


==> Small numbers in List


def small(n,i=0):
    if i==len(n)-1:
        return n[i]
    return min(n[i],small(n,i+1))
print(small([342,532,123,323,324]))



==> Adding each digit until sum equals to single digit


n=9789
def digit_sum(n):
    total = 0
    while n:
        total+=n%10
        n//=10
    if total>=10:
        digit_sum(total)
    else:
        print("The single digit after all sum is",total)
digit_sum(n)




n=9789
while n>9:
    total = 0
    while n:
        total += n % 10
        n //= 10
    n=total
print(n)




==> Sum of digits in Number


def sum(n):
    if n<10:
        return n
    return n%10+sum(n//10)
print(sum(9789))


==> Sum of single digit numbers in list

def single():
    n=[3,5,34,72,1,2]
    sum=0
    for x in n:
        if x<10:
            sum+=x
    print(sum)
single()


==> Sum of even digit in goven number


n=98762
sum=0
while n:
    x=n%10
    if x%2==0:
        sum+=x
    n//=10
print(sum)



==> Sum of Index and element in that index is even or odd

def evenSum():
    n=[4,5,35,71,1,2]
    for i in range(len(n)):
        sum=i+n[i]
        if sum%2==0:
            print("sum of index ",i," and element ",n[i]," is even that is: ",sum)
        else:
            print("sum of index ",i," and element ",n[i]," is odd that is: ",sum)
evenSum()



==> Sum of Prime digits in given number


n=98762
sum=0
while n:
    x=n%10
    for i in range(2,(x//2)+1):
        if x%i==0:
            break
    else:
        sum+=x
    n//=10
print(sum)



n=98762
sum=0
while n:
    x=n%10
    if x in [2,3,5,7]:
        sum+=x
    n//=10
print(sum)


