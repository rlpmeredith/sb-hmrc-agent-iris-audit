import csv

f = open('C:\\users\\rmeredith\\desktop\\exported.csv','r')
iris_data = csv.reader(f)
iris_list = list(iris_data)
iris_list_nh = iris_list[2:]

f2 = open('C:\\users\\rmeredith\\desktop\\SAAgentClientList.csv','r')
hmrc_data = csv.reader(f2)
hmrc_list = list(hmrc_data)
hmrc_list_nh = hmrc_list[1:]

print(hmrc_list_nh)

for irisrow in iris_list_nh:
    rowmatch = 0
    if irisrow[4] == '':
            print(irisrow[0],"is missing utr in Iris")
    else:
        for hmrcrow in hmrc_list_nh:
            if irisrow[4] == hmrcrow[2]:
                rowmatch = 1
 #               print(irisrow[0],"is in Iris and hmrc")
                break
                
    if rowmatch == 0:
        print(irisrow[0],irisrow[1], "is in Iris but not in HMRC")
        
for hmrcrow in hmrc_list_nh:
    rowmatch = 0
    for irisrow in iris_list_nh:
            if hmrcrow[2] == irisrow[4]:
                rowmatch = 1
 #               print(irisrow[0],"is in HMRC and Iris")
                break
                
    if rowmatch == 0:
        print(hmrcrow[0],hmrcrow[1],"is in HMRC but not in Iris")
