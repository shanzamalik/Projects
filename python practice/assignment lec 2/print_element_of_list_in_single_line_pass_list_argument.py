ran_list=["shanza","waqas","malik",27]
sub_list=["phy","chem","english"]
cartoon_name=["diana","nastya","cococmelon","tiny_tony","jungle_cartoon","princess"]

def length_of_element_in_list(list):
    print("length of element:",len(list))

def print_element_of_list(list):
   for item in list:
       print(item,end=" ")

print_element_of_list(cartoon_name)
print(end="\n")
print_element_of_list(ran_list)