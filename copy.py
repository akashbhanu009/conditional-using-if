from sys import argv
from os.path import exists

from_file, to_file = argv
print(f"Doe's input file exixts {exists(from_file)}")
print(f"copying from this file {from_file} to this{to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"Length of input data {len(indata)}")
print(f"Doe's output file exists {exists(to_file)}")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright DONE")

out_file.close()
in_file.close()
