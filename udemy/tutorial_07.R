# test normal distribution

# initial settings
N <- 10000
counter <- 0

# for loop looping N turns
for(i in rnorm(N)){
  
  if(-1 < i & i < 1){
    counter <- counter + 1
  }
}
# get ratio
answer <- counter / N
answer
