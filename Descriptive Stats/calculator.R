x <- mean(c(15, 12, 14, 11))
y <- mean(c(39, 45, 48, 60))
z <- mean(c(65, 45, 32, 38))

G <- mean(c(x, y, z))
n <- 4
SS_Bet <- 4*((x-G)^2 + (y-G)^2 + (z-G)^2)
SS_With <-862
numerator <-SS_Bet/2
denominator <- SS_With/9
F_ratio <- numerator/denominator

single <- mean(c(8, 7, 10, 6, 9))
twin <- mean(c(4, 6, 7, 4, 9))
tri <- mean(c(4, 4, 7, 2, 3))
G <- mean(c(single, twin, tri))
SS_between <- 5*((single-G)^2 + (twin-G)^2 + (tri-G)^2)
SS_within <- ((8-single)^2 + (7-single)^2 + (10-single)^2 + (6-single)^2+ (9-single)^2 +
                (4-twin)^2 + (6-twin)^2 + (7-twin)^2 + (4-twin)^2 + (9-twin)^2 +
                (4-tri)^2 + (4-tri)^2 + (7-tri)^2 + (2-tri)^2 + (3-tri)^2) 
df_between <- 2
df_within <- 12
MS_between <- SS_between/df_between
MS_within <- SS_within/df_within
F_ratio <- MS_between/MS_within
explain <- SS_between/(SS_within+SS_between)
