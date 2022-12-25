import itertools
inp=int(input())
# declaring 
thisdict = {
  26:"TOI",
  20.5:"Hindu",
 34: "ET",
  10.5:"BM",
  16.4:"HT",
};
val=[26,20.5,34,10.5,16.4]
newspaper=[]
combination=list(itertools.combinations(val, 2))
for i in combination:
    if sum(i)<=inp:
        newspaper.append(i)

np=[]
for i in range(len(newspaper)):
        val1=newspaper[i][0]
        val2=newspaper[i][1]
        np.append((thisdict[val1],thisdict[val2]))
print(np)