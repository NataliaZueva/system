f = open("text.txt")
s = open('xyz.txt','w')
m = ['\t', ' ', '\n', '		', '		', '\t\t', '		']
for line in f.readlines():
    if not (m and line.startswith("	#") or line.startswith("#") or  line.startswith("		#")):
        s.write(str(line))
        print(line)

s.close()