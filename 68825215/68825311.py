#https://stackoverflow.com/questions/68825311/python-regular-expression-to-get-date-and-price-from-a-list-of-string-texts/68825436#68825436
txt = "ID1|0|1|;2;2;2;5;12/11/2020;3;10.0000;5;06/11/2021;3;9.0000;|"

x = txt.split("|")
y = x[3].split(";")

print(x[0] + " " + y[5] + " " + y[7])