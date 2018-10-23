f = open("trade-wars-news1.txt","r+")
content1 = f.read()
f.close()
g = open("trade-wars-news2.txt","r+")
content2 = g.read()
g.close()
h = open("trade-wars-news3.txt","r+")
content3 = h.read()
h.close()
i = open("trade-wars-news4.txt","r+")
content4 = i.read()
i.close()
j = open("trade-wars-news5.txt","r+")
content5 = j.read()
j.close()

A = str.split(content1)
B = str.split(content2)
C = str.split(content3)
D = str.split(content4)
E = str.split(content5)

all_words = A + B + C + D + E
all_worddict = {}
for i in range(0,len(all_words)):
    wordcount = all_words.count(all_words[i])
    worddict = {all_words[i]: wordcount}
    all_worddict.update(worddict)
# print(all_worddict)
ranklist = sorted(all_worddict,key=all_worddict.get,reverse=True)
# print(ranklist)

for s in range(0,14):
    m = ranklist[s]
    print(m,all_worddict.get(m))



  








