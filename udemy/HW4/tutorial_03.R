



Games
rownames(Games)
colnames(Games)

Games["LeBronJames","2012"]

#element by element
FieldGoals
round(FieldGoals / Games, 1)
ggplot(round(FieldGoals / FieldGoalAttempts, 3))
