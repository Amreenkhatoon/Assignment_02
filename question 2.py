#sample list of tuples
sample_list = [(2,5),(1,2),(4,4),(2,3),(2,1)]

#sorted list 
sorted_list = sorted(sample_list,key=lambda x: x[-1])

print(sorted_list)