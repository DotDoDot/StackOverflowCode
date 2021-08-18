#https://stackoverflow.com/a/68836212/839573
from configparser import ConfigParser
config = ConfigParser()
config.read("demo.ini")

# cutting the values of file from column 3 
keys = [ x.split("|")[2].rstrip("\n") for x in open("dm.txt").readlines()]
vals = [config["DEMFILE"][x] for x in keys]
print(vals)