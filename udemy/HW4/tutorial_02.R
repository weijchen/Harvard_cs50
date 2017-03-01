#name factors
Charlie<- 1:5
Charlie

#give names
names(Charlie) <- c("a", "b", "c", "d", "e")
Charlie
Charlie["d"]

#clear names
names(Charlie) <- NULL   #NULL: nothing
Charlie


#--------------------------

#naming matrix dimensions 1, rename, indexation
temp.vec <- rep(c("a", "B", "zZ"), each=3)
temp.vec

Bravo <- matrix(temp.vec, 3, 3)
Bravo
rownames(Bravo) <- c("How", "are", "you?")
Bravo

colnames(Bravo) <- c("X", "Y", "Z")
Bravo

Bravo["are", "Y"] <- 0
Bravo
