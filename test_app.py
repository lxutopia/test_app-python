import sys, getopt

###############
#  By Lexx Damm
###############

helpMessage = """
Just a test app, using Python 3
"""

argv = sys.argv[1:0]
opts, args = getopt.getopt(argv, "h")
for opt, arg in opts:
    if opt in ['-h']:
        print(helpMessage)
        sys.exit()
