fr = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\questionv3.txt',  'r' , encoding="utf8")
fw = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\questionv3b.txt',  'w' , encoding="utf8")



for line in fr:
	line2 = line[:-2]
	fw.write(line2 + '\n')