f = open("test")
r = open("result", "w")
i = 0
for line in f:
     r.write("</tr>\n<tr>\n")
   r.write("  <td>\n    "+line+"  </td>\n")
   i = i + 1
 
r.close()
f.close()

