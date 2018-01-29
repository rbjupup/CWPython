import sys


def process_file(fileName):
    '''process_file line to line'''
    input_file = open(fileName,"r")
    for line in input_file:
        line = line.strip()
        print(line)
    input_fille.close()

if __name__ == "main":
    process_file(sys.argv[1])