import sqlite3

import numpy as np
import matplotlib.pyplot as plt

conn = sqlite3.connect('Face-DataBase3')
c = conn.cursor()

c.execute('SELECT Name,Presents FROM Students')
data = c.fetchall()

Name = []
Presents = []

print(data)
for row in data:
    Name.append(row[0])
    Presents.append(row[1])
plt.figure()
# data to plot
n_groups = len(Presents)

index = np.arange(n_groups)

plt.bar(index,Presents,align='center')


plt.xlabel('Names')
plt.ylabel('Presents')
plt.title('Attendance of Students')
plt.xticks(index,Name)
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', 
labelbottom='on')
plt.show()

c.close()
conn.close()
