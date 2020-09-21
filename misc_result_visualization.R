library(ggplot2)
library(reshape)
library(gridExtra)

#x=read.table('/Users/limingcai/Downloads/result.tsv',header=T,sep = '\t')
x=read.table('results_sum_new_mpd_mntd.tsv',header=T,sep = '\t')
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

p3=ggplot(c, aes(x=Lep_family, y=value,color=variable))+geom_violin(trim = FALSE, aes(color = variable))+
	labs(x=NULL, y = "MPD/MNTD",main='Host plant divergence')

p4=ggplot(d, aes(x=Lep_family, y=value,color=variable))+geom_violin(trim = FALSE, aes(color = variable))+
	labs(x=NULL, y = "DSI",main='Host plant divergence')

pdf('PD_analysis_new_mpd_mntd.pdf',width = 8,height = 6)

grid.arrange(p1,p2,p3,p4,
  widths = c(1, 1),
  layout_matrix = rbind(c(1, 2),c(3, 3),c(4,4))
)

dev.off()


library(ggtree)
library(ape)

tree=read.nexus('tree7_AA_150tree_all_dated_summary_renamed.tre')
heatmapData=read.table("results_sum_new_mpd_mntd.tsv", sep='\t',header = T)
rn <- rownames(heatmapData)
heatmapData <- as.data.frame(sapply(heatmapData, as.character))
rownames(heatmapData) <- rn


#hdata4plot=heatmapData[c('Tree_label','mpd.obs','mntd.obs')]
#rn <- rownames(hdata4plot)
#hdata4plot <- as.data.frame(sapply(hdata4plot, as.character))
#rownames(hdata4plot) <- rn

#plot PD
ggtree(tree, ladderize = F, layout='circular') %<+% heatmapData + 
  geom_tippoint(aes(color=as.numeric(PD)),size=0.5) + 
  geom_tiplab2(aes(label=Lep_accepted_name), align=T, linetype=NA, offset=8, hjust=0.5, size = 0.5) +
  scale_color_continuous(name='PD',low="blue", high="red", limits=c(325, 800))+
  labs(title = "PD")

ggtree(tree, ladderize = F, layout='circular') %<+% heatmapData + 
  geom_tippoint(aes(color=as.numeric(mpd.obs)),size=0.5) + 
  geom_tiplab2(aes(label=Lep_accepted_name), align=T, linetype=NA, offset=8, hjust=0.5, size = 0.5) +
  scale_color_continuous(name='mpd.obs',low="blue", high="yellow")+
  labs(title = "MPD")

#plot DSI/mpd.z
ggtree(tree, ladderize = F, layout='circular') %<+% heatmapData + 
  geom_tippoint(aes(color=as.numeric(mpd.obs.z)),size=0.5) + 
  geom_tiplab2(aes(label=Lep_accepted_name), align=T, linetype=NA, offset=8, hjust=0.5, size = 0.5) +
  scale_color_continuous(name='mpd.obs.z',low="blue", high="yellow")+
  labs(title = "DSI")