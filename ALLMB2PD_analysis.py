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



###########################################
##Add crown group age for all species to reduce missing data in MPD analysis
###########################################
import csv

#format species names in ALLMB
ALLMB_sp=open('ALLMB.sp.list').readlines()
#ALLMB_sp=['_'.join(l.strip().split('_')[:2]) for l in ALLMB_sp]
ALLMB_sp=[l.strip() for l in ALLMB_sp]
ALLMB_sp=set(ALLMB_sp)

#get focus family list
families=open('Hosts_families.list').readlines()
families=[l.strip() for l in families]

def find_crown(fam):
	PL_sp=[]
	valid_sp=[]
	try:
		plantlist=csv.reader(open('plantlist_csv'+fam+'.csv'), delimiter=',')
		for row in c:
			PL_sp.append(row[4]+'_'+row[6])
		#find overlap between ALLMB_sp and this family PL_sp
		valid_sp=list(set(PL_sp) & ALLMB_sp)
		#get the two most distantly related sp in the valid species list of the family
		sp1=valid_sp[0]
		max_dist=0
		sp1_node=t&sp1
		for sp in valid_sp:
			cur_dist=sp1_node.get_distance(sp)
			if cur_dist > max_dist:
				dis=cur_dist
				sp2=sp
		return([sp1,sp2])
	except IOError:print fam
	

crown_sp={}
crown_sp['Asphodelaceae']=['Asphodelus_aestivus','Dianella_sandwicensis']
crown_sp['Francoaceae']=['Melianthus_villosus','Greyia_flanaganii']

from ete3 import Tree
t=Tree('ALLMB.tre',format=1)
