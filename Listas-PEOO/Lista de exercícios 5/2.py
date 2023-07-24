s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.- "

p1 = s[22] + s[10] + s[29] + s[14] + s[30] + s[28] + s[-1]
p2 = s[11] + s[10] + s[29] + s[18] + s[28] + s[29] + s[10] + s[-1]
p3 = s[10] + s[21] + s[22] + s[14] + s[18] + s[13] + s[10]

print(p1+p2+p3)