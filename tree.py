import csv
from sklearn import tree

x=[]
y=[]

with open('ghadvaznkafsh.csv', 'r') as csvlfile:
    data = csv.reader(csvlfile)
    for line in data:
        x.append(line[2:5])
        y.append(line[5])

    print(x[1])
    print(y[1])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x , y)

new_data = [[190, 89 , 43], [160, 56, 39]]
answer = clf.predict(new_data)
print(answer[0])