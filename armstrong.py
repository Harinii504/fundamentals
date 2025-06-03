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

