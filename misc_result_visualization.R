library(ggplot2)
library(reshape)
library(gridExtra)

x=read.table('/Users/limingcai/Downloads/result.tsv',header=T,sep = '\t')
#m=melt(x[,c('Lep_family','Lep_accepted_name','Num.families','PD','mpd.obs','mntd.obs')])
a=melt(x[,c('Lep_family','Lep_accepted_name','Num.families')])
b=melt(x[,c('Lep_family','Lep_accepted_name','PD')])
c=melt(x[,c('Lep_family','Lep_accepted_name','mpd.obs','mntd.obs')])
d=melt(x[,c('Lep_family','Lep_accepted_name','mpd.obs.z','mntd.obs.z')])

p1=ggplot(a, aes(x=Lep_family, y=value))+geom_violin(trim = FALSE)+
	labs(x=NULL, y = "Plant family number",main='Host plant richness')+
	theme(axis.text=element_text(size=7,angle = 30))

p2=ggplot(b, aes(x=Lep_family, y=value))+geom_boxplot()+
	labs(x=NULL, y = "PD",main='Host plant richness')+
	theme(axis.text=element_text(size=7,angle = 30))

p3=ggplot(c, aes(x=Lep_family, y=value,color=variable))+geom_boxplot(aes(color = variable))+
	labs(x=NULL, y = "MPD/MNTD",main='Host plant divergence')

p4=ggplot(d, aes(x=Lep_family, y=value,color=variable))+geom_boxplot(aes(color = variable))+
	labs(x=NULL, y = "DSI",main='Host plant divergence')

pdf('PD_analysis.pdf',width = 8,height = 6)

grid.arrange(p1,p2,p3,p4,
  widths = c(1, 1),
  layout_matrix = rbind(c(1, 2),c(3, 3),c(4,4))
)

dev.off()