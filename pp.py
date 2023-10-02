N=12
sent="insert 0 2"
cList=[1]
if sent._contains_("insert"):
    one=sent.split()
    cList.insert(int(one[1]),int(one[2]))