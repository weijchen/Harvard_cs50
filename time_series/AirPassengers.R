# library()

# --------------------------------------------- lib install, import
# install.packages("ggplot2")
install.packages("tseries")
library(ggplot2)
library(tseries)
# --------------------------------------------- data import
# built-in data set
data("AirPassengers")
# show data format, 'ts': time series
class(AirPassengers)

start(AirPassengers)
end(AirPassengers)
# Cycle of AirPassengers data
frequency(AirPassengers)

summary(AirPassengers)
head(AirPassengers)
tail(AirPassengers)

plot(AirPassengers)
# add linear model
abline(reg=lm(AirPassengers~time(AirPassengers)))
cycle(AirPassengers)
plot(aggregate(AirPassengers))
plot(aggregate(AirPassengers, FUN=mean))
# boxplot, disp seasonal effect
boxplot(AirPassengers~cycle(AirPassengers))

#insight:
#1. yearly trend show the constant growing pace of passengers
#2. variance and mean are significantly strong among other years (seasonal effect)

acf(log(AirPassengers))
acf(diff(log(AirPassengers)))
pacf(diff(log(AirPassengers)))
adf.test(log(AirPassengers), alternative="stationary", k=0)
fit <- arima(log(AirPassengers), c(0, 1, 1),seasonal = list(order = c(0, 1, 1), period = 12))
fit
pred <- predict(fit, n.ahead = 10*12)
ts.plot(AirPassengers, 2.718^pred$pred, log = "y", lty = c(1,3))
