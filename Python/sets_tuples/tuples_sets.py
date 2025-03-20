
#import timeit
#import sys

#list = ["Rop","Enock","Dororthy","kirui","kipngeno","kirui"] 
#tup = tuple(list)

#print("Tuple:",timeit.timeit(stmt="tup = ('Rop','Enock','Dororthy','kirui','kipngeno','kirui') * 1000",number=1000))
#print("List:",timeit.timeit(stmt="list = ['Rop','Enock','Dororthy','kirui','kipngeno','kirui'] * 1000",number=1000))
#print("Tuple:",sys.getsizeof(tup))
#print("List:",sys.getsizeof(list))

#print(help(tup))
#print(dir(tup))


#Methods available in tuples
#print(tup.index("Enock"))

#print(tup.count("kirui"))
#print(len(tup))

#print("kirui" in tup)

#SET
my_set = {"Rop","Enock","Dororthy","kirui","kipngeno","kirui"}
another_set = {"Enock","Ben","Joan"}

#my_set.remove("Enock")
#print(my_set)
#combined_set = my_set.union(another_set)

#my_set.add("Joan")
#print(combined_set)
#my_set.difference_update(another_set)
#print(my_set.issubset(another_set))
#print(my_set.issuperset(another_set))
#print(my_set.symmetric_difference(another_set))
#print(my_set <= another_set)
#my_set.discard("Joan") 
#print(my_set)

#print(my_set | another_set)
#print(my_set.intersection(another_set))


