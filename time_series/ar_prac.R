# --------------------------------------------- lib install, import
library(ggplot2)
library(tseries)
library(readxl)
library(astsa)
getwd()
setwd("/Users/jimmyweicc/Github/Crawler/stockIndex")
price <- read.csv("price.csv")
head(price)
summary(price)


plot(x=price$close,y=price$qdate, type='l')


x=ts(price$close) # makes sure R knows that x is a time series
plot(x, type="l")
adf.test(diff(log(x)), alternative="stationary", k=0)
plot(x)
