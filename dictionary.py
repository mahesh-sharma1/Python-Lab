dict = {"key1": 1,"key2": "2","key3": [3,3,3],"key4": (4,4,4),"key5": 5,(0,1):6 }
print(dict)
print(dict["key1"])
print(dict[(0,1)]) # accessing tuple of dictionary

print(dict.keys())
print(dict.values())

dict["key6":] = "This is ai" #appending element in dict
print(dict)
