install.packages("ggplot2")

?qplot()
?ggplot()
?diamonds

# activate package
library(ggplot2)

qplot(data=diamonds, carat, price,
      colour=clarity, facets=.~clarity)