#Data
revenue <- c(14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50)
expenses <- c(12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96)

#Solution

#Profit for each month
profit <- round(revenue - expenses)

#Profit after tax for each month (tax rate 30%)
profit_tax <- round(profit * (1 - 0.3))

#Profit margin for each month (profit_tax / revenues)
profit_margin <- profit_tax / revenue

#Good month(profit_tax > mean for the year)
mean <- round(mean(profit_tax))

for(i in profit_tax){
  if(i > mean(profit_tax)){
    print(i)
  } 
}
#Bad month

for(i in profit_tax){
  if(i < mean(profit_tax)){
    print(i)
  } 
}

#The best month

max <- max(profit_tax)

#The worst month

min <- min(profit_tax)
