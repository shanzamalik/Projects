def search_word_by_line():
    word="lhr"
    data=True
    line_no=1


    with open("practice.txt","r") as f:
        
        while data :
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
      
    return -1

print(search_word_by_line())
        
    

