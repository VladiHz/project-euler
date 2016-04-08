sumsq = 0
sqsum = 0
for n in xrange(1,101):
	sumsq += n*n
	sqsum += n
sqsum *= sqsum
diff = sqsum - sumsq
print diff