x=read.csv('BNet_traits_corrected_LCai.csv',stringsAsFactors = F)
y=read.csv('test.csv',stringsAsFactors = F)
for (j in colnames(x)[13:46]){
for (i in 1:length(x$Authority)){
	if (!is.na(x[[j]][i])){
	if (x[[j]][i]!=''){
		y[[j]][which(y$Genus==x$Genus[i] & y$Species.Epithet==x$Species.Epithet[i])]=1
	}
}
}
}
write.csv(y,'data_completeness_sum.csv')