tup_el=(1,4,9,16,25,36,49,64,81,100)
search_el=36
idx=0
for el in tup_el:

    if el==search_el:
        print(search_el,"is found at index:",idx)
        break
    else:
        print("searching...")
        idx+=1
print("element found")