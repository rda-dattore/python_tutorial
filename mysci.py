# Initialize my data variable as an empty list
data = []

# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, "r") as datafile:

    # read the first three lines (header)
    for _ in range(3):
        datafile.readline()

    # read and parse the rest of the file
    for line in datafile:
        datum = line.split()
        data.append(datum)

