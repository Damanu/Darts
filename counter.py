#/usr/bin/python!

import matplotlib.pyplot as plt
import numpy as np
import sys

def main(argv):
	if len(argv)==1:
		print "----Help----\nArguments:\n 1. Number of Players\n 2. Starting Points\n"
		sys.exit(0)

	playnum=float(argv[1])
	points=[]
	hpoints=[]
	average=[]
	startp=float(argv[2])
	i=0
	playround=0
	while i<int(playnum):
		points.append(float(argv[2]))
		hpoints.append(0)
		average.append(0)
		i+=1
	
	while min(points) >0:
		playround+=1
		i=1
		while i<=playnum:
			print "Player: ",i
			score=float(raw_input("score: "))
			if score<points[i-1]:
				points[i-1]=points[i-1]-score
			elif int(score) == int(points[i-1]):
				print "------------------"
				print "Winner: Player",i
				print "------------------"
				sys.exit()				
			hpoints[i-1]+=score
			average[i-1]=float((hpoints[i-1]))/float(playround)
			print "Round: ", playround
			print "Points to win: ",points[i-1]
			print "Average: ", average[i-1]
			i+=1	
			print"--------------------------"

if __name__=="__main__":
	main(sys.argv)
