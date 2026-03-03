import sys

if len(sys.argv) < 2:
    print("Please provide a name as an argument.")
elif len(sys.argv) > 2:
    print("Please provide only one name as an argument.")
else:
    print(f"Hello, {sys.argv[1]}!")