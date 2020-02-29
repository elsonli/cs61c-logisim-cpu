import sys

def main(args):
	file = open(args[1])
	lines = [l for l in file.readlines()]
	
	def mapper(strr):
		return hex(int(strr, 2))[2:]
	
	results = []
	for l in lines:
		hexes = map(mapper,l.split())
		r1 = ''.join(hexes[:8])
		r2 = ''.join(hexes[8:16])
		r3 = ''.join(hexes[16:24])
		r4 = ''.join(hexes[24:32])
		r5 = ''.join(hexes[32:40])
		r6 = ''.join(hexes[40:48])
		r7 = ''.join(hexes[48:56])
		r8 = ''.join(hexes[56:60])
		r9 = ''.join(hexes[60:68])
		r10 = ''.join(hexes[68:])
		result = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
		results.append(result)
	print "v1\t v2\t  v3\t   v4\t    v5\t     v6\t      v7       Line# PC\t     Inst"
	for r in results:
		string = ' '.join(r)
		print string
		print '\n'

########################################################
# 						sample usage				   #
# python binary_to_hex.py reference_outout/CPU-mem.out #
########################################################

if __name__ == "__main__":
	main(sys.argv)