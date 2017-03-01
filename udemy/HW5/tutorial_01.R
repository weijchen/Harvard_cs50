?read.csv()

#Method 1: Select the file manually
stats <- read.csv(file.choose())
stats

#Method 2: Set WD and Read Data
getwd()
#Windows:
setwd("C:\\code\\R")
#Mac()
setwd("/Users...")

getwd()
rm(stats)
stats <- read.csv("DemographicData.csv")
stats

#---------------------Exploring Data
stats
#Briefing data structure
nrow(stats)
ncol(stats)
head(stats, n=20)    #First 6 data
tail(stats)    #last 6 data
str(stats)    #structure #str(), runif() alike rnorm()
?str()
summary(stats)


#-------------------------Using the $ sign
stats
head(stats)
stats[3,3]
stats[2,1]
stats$Internet.users    #Extract specific vector
stats[,"Internet.users"]
stats$Internet.users[2]
levels(stats$Income.Group)


#---------------------------Basic Operations with a DF
stats[1:10,]    #subsetting
stats[3:9,]
stats[c(4,100),]
#Remember how the [] work:
is.data.frame(stats[1,])    #no need for drop=F
stats[,1]
stats[,1,drop=F]
is.data.frame(stats[,1,drop=F]) 
#multiply columns
head(stats)
stats$Birth.rate * stats$Internet.users
stats$Birth.rate + stats$Internet.users
#add column
head(stats)
stats$Mycalc <- stats$Birth.rate * stats$Internet.users
#test of knowledge
stats$xyz <- 1:5
head(stats,n=12)
#remove column
head(stats)
stats$Mycalc <- NULL
stats$xyz <- NULL


#---------------------Filtering data frames
head(stats)
filter <- stats$Internet.users < 2    #create filter
stats[filter,]    #use filter

stats[stats$Birth.rate > 40,]    #create and use filter
stats[stats$Birth.rate > 40&stats$Internet.users<2,]
stats[stats$Income.Group =="High income",]
levels(stats$Income.Group)    #check levels of specific column

stats[stats$Country.Name =="Malta",]

#--------------------------Introduction to qplot()
install.packages("ggplot2")
library(ggplot2)
?qplot
qplot(data=stats, x=Internet.users)
qplot(data=stats, x=Income.Group, y=Birth.rate)
qplot(data=stats, x=Income.Group, y=Birth.rate,size=I(3),
      color=I("blue"))
qplot(data=stats, x=Income.Group, y=Birth.rate,geom="boxplot")
 

#-----------------------------------Visualizing what we need
qplot(data=stats, x=Internet.users, y=Birth.rate)
qplot(data=stats, x=Internet.users, y=Birth.rate, 
      size=I(4))
qplot(data=stats, x=Internet.users, y=Birth.rate, 
      color=I("red"),size=I(4))               #with I, tell R it is not for mapping purpose
qplot(data=stats, x=Internet.users, y=Birth.rate, 
      color=Income.Group,size=I(3))

#---------------------Creating Data Frames
mydf <- data.frame(Countries_2012_Dataset,Codes_2012_Dataset, 
                   Regions_2012_Dataset)

head(mydf)
colnames(mydf) <- c("Country", "Code", "Region")
head(mydf)
rm(mydf)

mydf <- data.frame(Country=Countries_2012_Dataset,Code=Codes_2012_Dataset, 
                   Region=Regions_2012_Dataset)
head(mydf)
tail(mydf)
summary(mydf)
str(mydf)

#----------------------------Merging data frames
head(stats)
head(mydf)

merged <- merge(stats,mydf,by.x="Country.Code", by.y="Code")
head(merged)
merged$Country <- NULL
str(merged)
tail(merged)

#---------------------------Visualizing with new split
qplot(data=merged, x=Internet.users, y=Birth.rate)
#1. Shapes
qplot(data=merged, x=Internet.users, y=Birth.rate,
      color=Region, size=I(3), shape=I(2))
#2. Transparency
qplot(data=merged, x=Internet.users, y=Birth.rate,
      color=Region, size=I(3), shape=I(19),
      alpha=I(0.6))
#3. Title
qplot(data=merged, x=Internet.users, y=Birth.rate,
      color=Region, size=I(3), shape=I(19),
      alpha=I(0.6),
      main="Birth Rate vs Internet Users")
