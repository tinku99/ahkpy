import getopt, sys


print sys.argv
opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
output = None
verbose = False
for o, a in opts:
    if o == "-v":
        verbose = True
    elif o in ("-h", "--help"):
        print "you needhelp"
        sys.exit()
    elif o in ("-o", "--output"):
        output = a
    else:
        assert False, "unhandled option"
