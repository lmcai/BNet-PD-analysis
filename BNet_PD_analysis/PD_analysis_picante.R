##############################
#one tip per family
##############################

#prepare input
x=read.csv('Hosts_genus_revised_Sep2.csv')
y=read.csv('Hosts_families4picante_null.csv',row.names=1)

##all records included
for (i in 1:length(x$Tree_label)){
	y[x$Lep_accepted_name[i],x$Host_family[i]]=1
}

write.csv(y,'Hosts_families4picante_all_recs.tsv')

##only include host plants records from more than one resource
y=read.csv('Hosts_families4picante_null.csv',row.names=1,stringsAsFactors = F)
for (i in 1:length(x$Tree_label)){
	if (as.integer(x$Count.of.Lep_accepted_name[i])>1){
		y[as.character(x$Lep_accepted_name[i]),as.character(x$Host_family[i])]=1
	}
}
#write.csv(y,'Hosts_families4picante_atLeast3sources.csv')
write.csv(y,'Hosts_families4picante_atLeast1source.csv')

y=read.csv('Hosts_families_2sp_per_fam_4picante_null.csv',row.names=1,stringsAsFactors = F)
for (i in 1:length(x$Tree_label)){
	if (as.integer(x$Count.of.Lep_accepted_name[i])>1){
		y[as.character(x$Lep_accepted_name[i]),paste(x$Host_family[i],'1',sep='')]=1
	}
}

#if the butterfly has only one host family, then mark the second species within this family to use crown group age for PD
z=read.table('./misc/result_sum.tsv',sep='\t',header=T)
for (i in 1:length(z$Tree_label)){
	if (z$Num.families[i]==1){
		if (!is.null(y[as.character(x$Lep_accepted_name[i]),paste(x$Host_family[i],'1',sep='')])){
		if (!is.na(y[as.character(x$Lep_accepted_name[i]),paste(x$Host_family[i],'1',sep='')])){
			y[as.character(z$Lep_accepted_name[i]),paste(x$Host_family[x$Lep_accepted_name==z$Lep_accepted_name[i]][1],'2',sep='')]=1
		}
		}
	}
}

write.csv(y,'Hosts_families_2sp_per_fam_4picante_atLeast1source.csv')



#SRR6727422_X_Lycaenidae_Polyommatinae_Polyommatini_Cyclargus_thomasi does not have source information

#calculating PD in picante
library(picante)
setwd('/Users/limingcai/Documents/GitHub/BNet-PD-analysis/')
sptree=read.tree('ALLMB.pruned184sp.family_nam.tre')
host_recs=read.csv('Hosts_families4picante_allRecs.csv',row.names = 1)
pd.result <- pd(host_recs, sptree, include.root=TRUE)
#41 species have no host plant recs (lichens, ants, etc.)
write.table(pd.result,'pd.allRecs.tsv',sep='\t')

#MPD
phydist=cophenetic(sptree)
ses.mpd.result <- ses.mpd(host_recs, phydist, null.model = "taxa.labels",abundance.weighted = FALSE, runs = 99)
write.table(ses.mpd.result,'mpd.allRecs.tsv',sep='\t')
#417 species have MPD values (more than two host plant families)
ses.mntd.result <- ses.mntd(host_recs, phydist, null.model = "taxa.labels",abundance.weighted = FALSE, runs = 99)
write.table(ses.mntd.result,'mntd.allRecs.tsv',sep='\t')

###
#filter for number of records
host_recs_filtered=read.csv('Hosts_families4picante_atLeast1source.csv',row.names = 1)
pd.filtered.result <- pd(host_recs_filtered, sptree, include.root=TRUE)
write.table(pd.filtered.result,'pd.atLeast1soource.tsv',sep='\t')

sptree=read.tree('ALLMB.pruned_2spPerFam.family_nam.tre')
phydist=cophenetic(sptree)

host_recs_filtered=read.csv('Hosts_families_2sp_per_fam_4picante_atLeast1source.csv',row.names = 1)
ses.mpd.filtered.result <- ses.mpd(host_recs_filtered, phydist, null.model = "taxa.labels",abundance.weighted = FALSE, runs = 99)
ses.mntd.result <- ses.mntd(host_recs_filtered, phydist, null.model = "taxa.labels",abundance.weighted = FALSE, runs = 99)
write.table(ses.mpd.filtered.result,'mpd.atLeast3soources.tsv',sep='\t')
write.table(ses.mntd.result,'mntd.atLeast3soources.tsv',sep='\t')

##############################
#two tips per family
##############################
y=read.csv('Hosts_families4picante_null.tsv',row.names=1)
for (i in 1:length(x$Tree_label)){
	y[as.character(x$Lep_accepted_name[i]),paste(x$Host_family[i],'1',sep='')]=1
}

#if the butterfly has only one host family, then mark the second species within this family to use crown group age for PD
z=read.table('result_sum.tsv',sep='\t',header=T)
for (i in 1:length(z$Tree_label)){
	if (z$Num.families[i]==1){
		y[as.character(z$Lep_accepted_name[i]),paste(x$Host_family[x$Lep_accepted_name==z$Lep_accepted_name[i]],'2',sep='')]=1
	}
}

write.csv(y,'Hosts_families_2sp_per_fam_4picante_all_recs.csv')


#calculating PD in picante
library(picante)
sptree=read.tree('ALLMB.pruned_2spPerFam.family_nam.tre')
host_recs=read.csv('Hosts_families_2sp_per_fam_4picante_all_recs.csv',row.names = 1)
#pd.result <- pd(host_recs, sptree, include.root=TRUE)
#41 species have no host plant recs (lichens, ants, etc.)
#write.table(pd.result,'pd.allRecs.tsv',sep='\t')

#MPD
phydist=cophenetic(sptree)
ses.mpd.result <- ses.mpd(host_recs, phydist, null.model = "taxa.labels",abundance.weighted = FALSE, runs = 99)
write.table(ses.mpd.result,'mpd.allRecs.tsv',sep='\t')
#417 species have MPD values (more than two host plant families)
ses.mntd.result <- ses.mntd(host_recs, phydist, null.model = "taxa.labels",abundance.weighted = FALSE, runs = 99)
write.table(ses.mntd.result,'mntd.allRecs.tsv',sep='\t')

