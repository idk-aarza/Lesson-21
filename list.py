emptylist=[]
boyslist=["Aashman", "Anhad", "Advik", "Rohan", "Hariom"]
print(boyslist)
print(len(boyslist))

girlslist=["Avisha", "Vaanika", "Suhani", "Serene", "Myra"]
value=[7,8,9,1,2]
print(girlslist)
p=boyslist + girlslist
print(p)

print(boyslist[2:4])
print(girlslist[1:3])

for items in boyslist:
    print(items)
    
nestedlist=[[boyslist] ,[girlslist]]
for i in nestedlist:
    print("list", i,"elements")
    for j in i:
        print(j)