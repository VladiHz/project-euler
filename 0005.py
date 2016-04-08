num = 20

goon = True
while goon == True:
    fail = False
    #print num, 
    for x in xrange(1,21):
    #	print num%x, 
        if num%x != 0:
        	fail = True
        	break
    #print fail
    if fail == False:
    	print "Solution:", num
    	goon = False
    # if num == 3000:
    # 	goon = False
    num += 1