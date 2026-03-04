import sys
import example_7

if len(sys.argv) == 2:
    example_7.hello(sys.argv[1])
    example_7.goodbye(sys.argv[1])