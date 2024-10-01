fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    lines = fileref.readlines()           # step 2
    for lin in lines:                     # step 3
        #some code that references the variable lin
#some other code not relying on fileref   # step 4

with open(fname, 'r') as fileref:
 for lin in fileref:
     ## some code that uses line as the current line of the file
     ## some more code

filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()





fileconnection = open("olympics.txt", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}: {}; {}".format(
                vals[0],
                vals[4],
                vals[5]))


n = [0] * 12
for i in range(1,13):
    n[i-1] = i *12
outfile = open("Multiples of 12", "w")
for j in range(0, len(n)):
    outfile.write(str(j+1) + ',' + str(n[j]))
    # +1 to j since the array starts at 0 and we start counting at 1
    outfile.write('\n')
outfile.close()




olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()