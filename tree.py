import csv
from sklearn import tree

x=[]
y=[]

with open('ghadvaznkafsh.csv', 'r') as csvlfile:
    data = csv.reader(csvlfile)
    for line in data:
        x.append(line[1:4])
        y.append(line[4])

    # print(x[1])
    # print(y[1])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x , y)

new_data = [[190, 89 , 41], [174, 67, 41]]
answer = clf.predict(new_data)
print(answer[0], answer[1])