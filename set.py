set1={"Mahesh","Sharma","Rock","soul","rock","disco"} #repeated element is taken as 1 in a set
print("Set1 is \n",set1)

my_list = ["Mahesh","Sharma",(1,3.1415,"CSIT"),"Study","AI","Study"]
print("List is:\n",my_list)

set2 = set(my_list) #list to set

print("Set2 is \n",set2)

print("Element is in or not in a set:\n")
set1.add("dancer") #adding element in set
set1.remove("rock") #remove element form set
print("Set1 is:\n",set1)

print("Mahesh" in set1)
print("Kiran" in set1)

print("Intersection of two sets:\n",set1 & set2,"\n", set1.intersection(set2))
print("Union of two sets:\n",set1 | set2,"\n",set1.union(set2))
print("Difference of two sets:\n",set1.difference(set2))

print("Chekc superset:\n",set1.issuperset(set2))
print("Check subset:\n",set1.issubset(set2))

list = [1,2,1,3,3]
set= set(list)
print(sum(list))
print(sum(set))
