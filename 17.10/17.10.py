f, s = open("text.txt"), open('xyz.txt','w')
m = ['\t', '\t\t', '		']
for line in f.readlines():
    if not (m and line.startswith("	#") or line.startswith("#") or  line.startswith("		#")):
        s.write(str(line))
s.close()