import itertools

binaries = open('binaries.txt', 'w')

for i in range(2,9):
    list = ["".join(seq) for seq in itertools.product("01", repeat=i)]
    binaries.write( "%s\n" % list )
    
binaries.close()


    
