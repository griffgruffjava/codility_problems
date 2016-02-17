
def convert_and_strip(my_int):
	bin = "{0:b}".format(my_int)
	return bin.rstrip('0')

bin = convert_and_strip(1041)
binn = str(10001)
rec = 0
gap = 0

for num in binn:
	if num =='0':
		gap = gap + 1
		if gap > rec:
			rec = gap
        else:
		gap = 0

print rec


