#!/usr/bin/python3
import os

# Open the CSV file
fdir = open("dir.csv", "r")

# Read line by line
for line in fdir:
  # Create Directory
  os.mkdir(line.strip())

# Close opened file
fdir.close
