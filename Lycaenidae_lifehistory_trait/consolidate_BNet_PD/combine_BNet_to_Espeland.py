import csv
results=csv.reader(open('../../BNet_PD_analysis/PD_results_sum_new_mpd_mntd.tsv'), delimiter='\t')

num_fam={}
pd={}
mpd={}
mntd={}
dsi_mpd={}
dsi_mntd={}


num_fam_genus={}
pd_genus={}
mpd_genus={}
mntd_genus={}
dsi_mpd_genus={}
dsi_mntd_genus={}


for row in results:
	#spnam=row[0]
	try:
		tribe=row[0].split('_')[4]
		genus=row[0].split('_')[5]
	except:
		print(row)
		continue
	try:
		num_fam[tribe].append(row[4])
		pd[tribe].append(row[3])
		mpd[tribe].append(row[5])
		mntd[tribe].append(row[11])
		dsi_mpd[tribe].append(row[9])
		dsi_mntd[tribe].append(row[15])
		
		num_fam_genus[genus].append(row[4])
		pd_genus[genus].append(row[3])
		mpd_genus[genus].append(row[5])
		mntd_genus[genus].append(row[11])
		dsi_mpd_genus[genus].append(row[9])
		dsi_mntd_genus[genus].append(row[15])
	except KeyError:
		num_fam[tribe]=[row[4]]
		pd[tribe]=[row[3]]
		mpd[tribe]=[row[5]]
		mntd[tribe]=[row[11]]
		dsi_mpd[tribe]=[row[9]]
		dsi_mntd[tribe]=[row[15]]
		
		num_fam_genus[genus]=[row[4]]
		pd_genus[genus]=[row[3]]
		mpd_genus[genus]=[row[5]]
		mntd_genus[genus]=[row[11]]
		dsi_mpd_genus[genus]=[row[9]]
		dsi_mntd_genus[genus]=[row[15]]

#seven tribes in the Espeland tribes but not in BNet tribes
['Anaeomorphini', 'Anthoptini', 'Calpodini', 'Moncini', 'Oxylidini', 'Stalachtini', 'Thymelicini']

#Anaeomorphini is not sampled in BNet
#Calpodini is not sampled in BNet
#Stalachtini is not sampled in BNet
#Anthoptini is not an accepted tribe in BNet, the genus Anthoptus is sampled BN000130_LEP32047_Hesperiidae_Hesperiinae_Hesperiini_Anthoptus_epictetus
#Moncini is not an accepted tribe in BNet (included in tribe Hesperiini instead)
#Thymelicini is represented as RE04C201_X_Hesperiidae_Hesperiinae_Hesperiini_Thymelicus_lineola_X_ME SRR1325130_X_Hesperiidae_Hesperiinae_Hesperiini_Thymelicus_sylvestris
#Oxylidini is represented as BN003962_NP95Y267_Lycaenidae_Theclinae_Loxurini_Eooxylides_tharis


x=open('/Users/limingcai/Documents/GitHub/BNet-PD-analysis/Lycaenidae_lifehistory_trait/consolidate_BNet_PD/all_phy_info.csv').readlines()


def return_median(value_string):
	return(str(median([float(i) for i in value_string.split()])))

out1=open('all_phy_info_all_PD_recs.csv','a')
out2=open('all_phy_info_PD_median.csv','a')

for l in x:
	try:
		num_fam_str=' '.join([i for i in num_fam[l.split(',')[4]] if not i =='0'])
		pd_str=' '.join([i for i in pd[l.split(',')[4]] if not i =='0'])
		mpd_str=' '.join([i for i in mpd[l.split(',')[4]] if not i =='NA'])
		mntd_str=' '.join([i for i in mntd[l.split(',')[4]] if not i =='NA'])
		dsi_mpd_str=' '.join([i for i in dsi_mpd[l.split(',')[4]] if not i =='NA'])
		dsi_mntd_str=' '.join([i for i in dsi_mntd[l.split(',')[4]] if not i =='NA'])
		out1.write(l.strip()+','+','.join([num_fam_str,pd_str,mpd_str,mntd_str,dsi_mpd_str,dsi_mntd_str])+'\n')
		out2.write(l.strip()+','+','.join([return_median(num_fam_str),return_median(pd_str),return_median(mpd_str),return_median(mntd_str),return_median(dsi_mpd_str),return_median(dsi_mntd_str)])+'\n')
	except (KeyError,statistics.StatisticsError):
		try:
			#if the genus is sampled in BNet
			num_fam_str=' '.join([i for i in num_fam_genus[l.split(',')[5]] if not i =='0'])
			pd_str=' '.join([i for i in pd_genus[l.split(',')[5]] if not i =='0'])
			mpd_str=' '.join([i for i in mpd_genus[l.split(',')[5]] if not i =='NA'])
			mntd_str=' '.join([i for i in mntd_genus[l.split(',')[5]] if not i =='NA'])
			dsi_mpd_str=' '.join([i for i in dsi_mpd_genus[l.split(',')[5]] if not i =='NA'])
			dsi_mntd_str=' '.join([i for i in dsi_mntd_genus[l.split(',')[5]] if not i =='NA'])
			out1.write(l.strip()+','+','.join([num_fam_str,pd_str,mpd_str,mntd_str,dsi_mpd_str,dsi_mntd_str])+'\n')
			out2.write(l.strip()+','+','.join([return_median(num_fam_str),return_median(pd_str),return_median(mpd_str),return_median(mntd_str),return_median(dsi_mpd_str),return_median(dsi_mntd_str)])+'\n')
		except (KeyError,statistics.StatisticsError):
			#this genus is not sampled in BNet or does not feed on plants
			out1.write(l.strip()+','+','.join(['NA','NA','NA','NA','NA','NA'])+'\n')
			out2.write(l.strip()+','+','.join(['NA','NA','NA','NA','NA','NA'])+'\n')

out1.close()
out2.close()

