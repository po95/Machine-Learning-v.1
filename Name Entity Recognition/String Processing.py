data = open("total_data.txt",'r',encoding='utf-8')
data2= open('split.txt', 'w',encoding='utf-8')

for line in data:
    str = line
    st_processed = str.split(' ')
    # print(st_processed)
    for i in range(len(st_processed)):
        list_item = st_processed[i]
        select = list_item.split("'\'")
        word = select[0]
        #print(word)

        #if(word.find("\\NC") or word.find(r"\NP")):
        if (word.find('\\NC') !=-1 or word.find('\\NP') !=-1):
            #print(word)
            word1=word.split('.')
            word2=word1[0]
            print(word2)
            word3=word2.split("\\")
            print(word3[0]+","+word3[1])
            str=word3[0]+","+word3[1]
            data2.write("%s\n" % str )

data2.close()
data.close()

