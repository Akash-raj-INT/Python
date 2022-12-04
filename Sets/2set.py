myset1 = {"car", "boat","train", "car"}
myset2 = {1,2,3,4,}
myset3 = {4,5,6,7}
#myset1.update(myset2)
#myset1.add("cycle")
#output =myset2.union(myset3)
output = myset2.intersection(myset3)
output1 = myset2.symmetric_difference(myset3)

print(output)
