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

#create genus level phylogeny of only plant families of interest
#remove species not in the plant list
ALLMB_sp_not_in_theplantlist=open('in_ALLMBtr_not_in_theplantlist.txt').readlines()
ALLMB_sp_not_in_theplantlist=[l.strip() for l in ALLMB_sp_not_in_theplantlist]
both_in_ALLMB_theplantlist = ALLMB_sp - set(ALLMB_sp_not_in_theplantlist)
both_in_ALLMB_theplantlist=list(both_in_ALLMB_theplantlist)

genera=[i.split('_')[0] for i in both_in_ALLMB_theplantlist]
genera=list(set(genera))
len(genera)
#12,914 genera

#keep only one species per genera
sp2keep=[]
for sp in both_in_ALLMB_theplantlist:
	if sp.split('_')[1]!='.sp' and sp.split('_')[1]!='sp' and sp.split('_')[0] in genera:
		sp2keep.append(sp)
		genera.remove(sp.split('_')[0])


#prune ALLMB 
from ete3 import Tree
t=Tree('ALLMB.tre',format=1)
t.prune(sp2keep,preserve_branch_length=True)
t.write(outfile='ALLMB.genus.tre',format=1)

#########################################
#2 species per family
t=Tree('ALLMB.genus.tre',format=1)

#format species names in ALLMB.genus
ALLMB_genus_sp=open('ALLMB.genus.list').readlines()
ALLMB_genus_sp=[l.strip() for l in ALLMB_genus_sp]
ALLMB_genus_sp=set(ALLMB_genus_sp)


def find_crown(fam):
	PL_sp=[]
	valid_sp=[]
	try:
		plantlist=csv.reader(open('plantlist_csv/'+fam+'.csv'), delimiter=',')
		for row in plantlist:
			PL_sp.append(row[4]+'_'+row[6])
		#find overlap between ALLMB_sp and this family PL_sp
		valid_sp=list(set(PL_sp) & ALLMB_genus_sp)
		#get the two most distantly related sp in the valid species list of the family
		for sp in valid_sp:
			tip=t&sp
			tip.add_features(family=fam)
		#sp_num_in_node=0
		#for node in t.get_monophyletic(values=[fam],target_attr="family"):
		#	if len([leaf for leaf in node])>sp_num_in_node:
		#		node4output=node
		#		sp_num_in_node=len([leaf for leaf in node])
		#sp1=[leaf.name for leaf in node4output.get_children()[0]]
		#sp2=[leaf.name for leaf in node4output.get_children()[1]]
		sp=[]
		for node in t.get_monophyletic(values=[fam],target_attr="family"):
			sp=sp+[leaf.name for leaf in node4output.get_children()[0]+leaf.name for leaf in node4output.get_children()[1]]
		#sp1=valid_sp[0]
		#max_dist=0
		#sp1_node=t&sp1
		#for sp in valid_sp:
		#	cur_dist=sp1_node.get_distance(sp)
		#	if cur_dist > max_dist:
		#		max_dist=cur_dist
		#		sp2=sp
		return(sp)
	except IOError:print('family not found: '+ fam)
	

crown_sp={}
crown_sp['Asphodelaceae']=['Asphodelus_serotinus','Dianella_prunina']
crown_sp['Francoaceae']=['Melianthus_elongatus','Greyia_flanaganii']

for fam in families:
	try:
		print fam
		crown_sp[fam]=find_crown(fam)
	except:pass

#prune the tree
d=[]
for i in crown_sp.keys():
	try:
		d=d+crown_sp[i] 
	except:print i

len(d)

t.prune(d,preserve_branch_length=True)
t.write(format=1, outfile="ALLMB.pruned_2spPerFam.tre")

#modify name
d={}
for k in crown_sp.keys():
	try:
		d[crown_sp[k][0]]=k+'1'
		d[crown_sp[k][1]]=k+'2'
	except:
		pass

for leaf in t:
	leaf.name=d[leaf.name]

t.write(format=1, outfile="ALLMB.pruned_2spPerFam.family_nam.tre")
