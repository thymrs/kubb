import sys

arguments = sys.argv[1:]
if len(arguments) > 2:
    print("none")
else:
    for argument in arguments[::-1]:
        print(argument)
