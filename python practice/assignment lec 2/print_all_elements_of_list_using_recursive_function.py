
this_list=["zarwa","apple","school","2"]


def print_list_item(list,idx=0):
   if (idx==len(list)):
      return 
   print(list[idx])
   print_list_item(list,idx+1)


# print_list_item(this_list)
print(this_list)