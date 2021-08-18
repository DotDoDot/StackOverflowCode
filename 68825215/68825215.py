#https://stackoverflow.com/questions/68825215/how-do-i-replace-a-value-in-a-string-for-a-csvfile-without-the-use-of-imports/68825361#comment121635090_68825361
f = open("file.csv", "r")
lines = f.readlines()
count = 0
for line in lines:
    if count != 0: #skip the header line
        x = line.split("\"")
        if len(x) == 3:
            print(x[0].lstrip() + x[1].replace(",", "") + x[2])
    count += 1