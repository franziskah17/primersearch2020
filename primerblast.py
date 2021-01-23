#!/usr/bin/python3

import argparse
import sys

parser= argparse.ArgumentParser(description="basically blast")

parser.add_argument("-q", required=True, dest="query", type=argparse.FileType("r"))
parser.add_argument("-f", required=True, dest="forward", type=argparse.FileType("r"))
parser.add_argument("-r", dest="reverse", type=argparse.FileType("r"))

args = parser.parse_args()

myquery= ""
for line in args.query: 
	if line.startswith(">") == False: 
		myquery = myquery + line.strip("\n")


fwprimer= ""
for line in args.forward: 
	if line.startswith(">") == False: 
		fwprimer = fwprimer + line.strip("\n")


if args.reverse is not None:
	revprimer= ""
	for line in args.reverse: 
		if line.startswith(">") == False: 
			revprimer = revprimer + line.strip("\n")
	


#print (myquery)
#print (fwprimer)
#print (revprimer)

fwstart = myquery.find (fwprimer)
print ("Your fw primer starts at", fwstart)
fwend = fwstart+len(fwprimer)
print ("fw primer ends at", fwend)
print ("fw primer length=", len(fwprimer), "\n")

if args.reverse is not None: 
	revstart = myquery.find (revprimer)
	if revstart == -1:
                revprimer = revprimer.replace("A", "t")
                revprimer = revprimer.replace("T", "a")
                revprimer = revprimer.replace("G", "c")
                revprimer = revprimer.replace("C", "g")
                revprimer = revprimer.replace("a", "A")
                revprimer = revprimer.replace("t", "T")
                revprimer = revprimer.replace("g", "G")
                revprimer = revprimer.replace("c", "C")
                revstart = myquery.find (revprimer)
                if revstart == -1:
                        revprimer = revprimer [::-1]
                        print ("Reverse-complementary revprimer sequence used.")
                        print (revprimer)
                        revstart = myquery.find (revprimer)
                else:
                        print ("Complementary revprimer sequence used.")
                        print (revprimer)
                        
	print ("Your rev primer starts at", revstart)
	revend = revstart+len(revprimer)
	print ("rev primer ends at", revend)
	print ("rev primer length=", len(revprimer))

	amplicon= revstart-fwend
	print ("\nAmplicon length=", amplicon)


# addtional things I've learned: 
#myquery= "".join(myquery)
# joined alles aus der list myquery to einem string (daher "".join) zusammen. achtung wegen der ganzen newlines!

# also: sometimes > if blank == True doesn't work. > if blank is not None worked in this case!
