qplot(data=data, x=Region, y=Fertility.Rate, size=I(3),
      color=Year, alpha=I(0.6))

data1960

data2013

#-----------------------import data
data <- read.csv("t.csv")
head(data)
tail(data)
str(data)
summary(data)
#-----------------------filter data
data1960 <- data[data$Year <= 1960,]
data1960
data2013 <- data[data$Year > 1960,]
data2013
