y=open('s').readlines()
###PD
x=open('pd.allRecs.tsv').readlines()
a={}
for l in x[1:]:
	a[l.split('\t')[0]]=l.strip()
	
for i in range(1,len(y)):
	y[i]=y[i].strip()+'\t'+a[y[i].split(',')[2].strip()]

#MPD
x=open('mpd.allRecs.tsv').readlines()
a={}
for l in x[1:]:
	a[l.split('\t')[0]]=l.strip()

for i in range(1,len(y)):
	y[i]=y[i].strip()+'\t'+a[y[i].split(',')[2].split('\t')[0]]

#MNTD	
x=open('mntd.allRecs.tsv').readlines()
a={}
for l in x[1:]:
	a[l.split('\t')[0]]=l.strip()

for i in range(1,len(y)):
	y[i]=y[i].strip()+'\t'+a[y[i].split(',')[2].split('\t')[0]]



###########
#filtered by number of records
x=open('pd.atLeast3sources.tsv').readlines()
a={}
for l in x[1:]:
	a[l.split('\t')[0]]=l.strip()

for i in range(1,len(y)):
	y[i]=y[i].strip()+'\t'+a[y[i].split(',')[2].split('\t')[0]]


x=open('mpd.atLeast3sources.tsv').readlines()
a={}
for l in x[1:]:
	a[l.split('\t')[0]]=l.strip()

for i in range(1,len(y)):
	y[i]=y[i].strip()+'\t'+a[y[i].split(',')[2].split('\t')[0]]


x=open('mntd.atLeast3sources.tsv').readlines()
a={}
for l in x[1:]:
	a[l.split('\t')[0]]=l.strip()

for i in range(1,len(y)):
	y[i]=y[i].strip()+'\t'+a[y[i].split(',')[2].split('\t')[0]]
