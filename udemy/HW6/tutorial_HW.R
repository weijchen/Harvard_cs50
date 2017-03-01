# ---------------------------------------- initail settings
setwd("C:\\code\\R\\HW6\\Section6-Homework-Data")
getwd()
mov <- read.csv("Section6-Homework-Data.csv")
head(mov)
tail(mov)
str(mov)
summary(mov$Studio)
# ---------------------------------------- made new dataset
fil <- (mov$Genre == "action") | (mov$Genre == "adventure") | (mov$Genre == "animation") | (mov$Genre == "comedy") | (mov$Genre == "drama")
fil2 <- (mov$Studio == "Buena Vista Studios")|(mov$Studio == "Fox")|(mov$Studio == "Paramount Pictures")|(mov$Studio == "Sony")|(mov$Studio == "Universal")|(mov$Studio == "WB")

newmov <- mov[fil & fil2,]
newmov
summary(newmov)
str(newmov)


library(ggplot2)
# ----------------------------------------
summary(movies$Studio)
summary(movies$Gross...US)

p <- ggplot(data=newmov, aes(x=Genre, y=Gross...US))
  
q<- p +
  geom_jitter(aes(size=Budget...mill., color=Studio)) +
  geom_boxplot(alpha=0.7, outlier.color=NA)
q
?geom_boxplot
