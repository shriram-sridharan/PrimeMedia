f = open("theatrelist-UVC")
r = open("table-UVC", "w")
i = 0
for line in f:
   if(i%2 == 0) :
     r.write("</tr>\n<tr>\n")
   r.write("  <td>\n    "+line+"  </td>\n")
   i = i + 1
 
r.close()
f.close()

