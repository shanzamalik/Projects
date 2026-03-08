tup_el=(1,4,9,16,25,36,49,64,81,100)
idx=0
search_el=36

while idx<len(tup_el):
   
    if tup_el[idx]==search_el:
        print("search found at index:" ,idx)
        break
    else:
        print("finding.......")
    idx+=1
print("end of loop")