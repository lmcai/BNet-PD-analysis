library(gridExtra)

x=read.csv('PD.csv',stringsAsFactors = F)
y=read.csv('host_module.csv')

for (i in 1:1355){
	if (x$Lep_accepted_name[i] %in% y$Species){x$host.module[i]=y$Module..[which(y$Species==x$Lep_accepted_name[i])]}
}

p1=ggplot(x, aes(x=host.module, y=PD)) + geom_boxplot(outlier.size=0.5,lwd=0.3)+ylim(0,1500)
p2=ggplot(x, aes(x=host.module, y=Num.families)) + geom_boxplot(outlier.size=0.5,lwd=0.3)+ylim(0,15)
p3=ggplot(x, aes(x=host.module, y=mpd.obs)) + geom_boxplot(outlier.size=0.5,lwd=0.3)+ylim(0,400)
p4=ggplot(x, aes(x=host.module, y=mntd.obs)) + geom_boxplot(outlier.size=0.5,lwd=0.3)+ylim(0,400)
p5=ggplot(x, aes(x=host.module, y=mpd.obs.z)) + geom_boxplot(outlier.size=0.5,lwd=0.3)+ylim(-3,1)
p6=ggplot(x, aes(x=host.module, y=mntd.obs.z)) + geom_boxplot(outlier.size=0.5,lwd=0.3)+ylim(-4,1)

pdf('PD_by_host_modules.pdf',width = 6,height = 8)
grid.arrange(p1,p2,p3,p4,p5,p6,
  widths = c(1, 1),
  layout_matrix = rbind(c(1, 2),c(3, 4),c(5,6))
)
dev.off()