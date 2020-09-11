import csv
a=open('Hosts_families.list').readlines()
a=[l.strip() for l in a]
b={}
for i in a:
	try:
		c=csv.reader(open('plantlist_csv/'+i+'.csv'), delimiter=',')
		for row in c:
			try:
				b[i].append(row[4]+'_'+row[6])
			except KeyError:
				b[i]=[row[4]+'_'+row[6]]
	except IOError:print i

#Gymnosperms and others
Selaginellaceae
Selaginnaceae
Zamiaceae
Podocarpaceae
Cycadaceae
Pinaceae
Cupressaceae
lichen

#angiosperms
Asphodelaceae
Asteraceae
Francoaceae
Areceae
Viburnaceae
Fabaceae

#carnivorous
Aphididae
Tettigometridae
Pseudococcidae
Eriosomatinae
Coccidae
Hemiptera
Coccoidea
Cyanophyta
Fulgoridae
Jassidae
Pemphigidae
leaf litter
Psyllidae
Cicadellidae
Aphididae
Membracidae
Formicidae
Hormaphididae


#there are 6 flowering plant families within this list
#add these families manually
b['Asphodelaceae']=['Asphodelus_aestivus']
b['Asteraceae']=['Helianthus_divaricatus']
b['Francoaceae']=['Francoa_sonchifolia']
b['Areceae']=['Dictyosperma_album']
b['Viburnaceae']=['Viburnum_witteanum']
b['Fabaceae']=['Mimosa_camporum']

#only preserve names that is in ALLMB tree
a=open('ALLMB.sp.list').readlines()
a=[l.strip() for l in a]
c={}

for k in b.keys():
	for i in b[k]:
		c[k]=i
		if i in a:break

c['Zamiaceae']='Zamia_vazquezii'
c['Cycadaceae']='Cycas_multipinnata'
c['Pinaceae']='Pinus_veitchii'
c['Cupressaceae']='Juniperus_utahensis'
c['Podocarpaceae']='Podocarpus_zamiifolia'
#prune
from ete3 import Tree
t=Tree('ALLMB.tre',format=1)
d=[c[i] for i in c.keys()]
len(d)
#184=179 angiosperms + 5 gymnosperms
t.prune(d,preserve_branch_length=True)
t.write(format=1, outfile="ALLMB.pruned184sp.tre")

#modify name
d={}
for k in c.keys():
	d[c[k]]=k

for leaf in t:
	leaf.name=d[leaf.name]

t.write(format=1, outfile="ALLMB.pruned184sp.family_nam.tre")