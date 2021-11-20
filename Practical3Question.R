bmi.df <- read.table('//Users//dylan//OneDrive//Documents//School Files Y2//IntroductionToRegression//BMI.txt', header = T)
bmi.lm <- lm(formula = BMI ~ Waist + Leg + Elbow + Wrist + Arm)

#a
resid(bmi.lm)[1]
#-1.244233

#b
e <- resid(bmi.lm)
s <- summary(bmi.lm)$sigma
r <- e / (s * (1 - h)^0.5)
#plot studentised residuals
plot(r, type = 'h', main = 'Plot of Studentised Residuals vs. Obervation Number', ylab = 'Studentised Residuals', ylim = c(-4,4))
abline(h=c(-2,2), lty = 2)
#identify(r, n=1)
#studentised residuals for case:
r[17] #2.132953
r[60] #-2.123783
r[62] #2.955531
r[65] #-2.195846
r[73] #2.240534
r[79] #2.077713

#c
#calculate the leverages h
h <- lm.influence(bmi.lm)$hat
#plot leverages
plot(h, type = "h", main = "Plot of Leverage vs. Observation Number", ylab = 'Leverage')
#identify(h, n = 1)...
#leverage for case: 
h[73] #0.3083268
h[62] #0.1661601
h[55] #0.278467
h[13] #0.2081216
h[12] #0.2915915
#they are of high leverage because the leverage of each point is above 2p'/n... 2*6/80... 0.15
#the individual deviations of x-xbar are large.

#d
pprime <- length(coef(bmi.lm))
d <- (1/pprime) * (h/(1-h)) * r^2
plot(d, type = 'h', main = 'Plot of Cooks Distance vs. Observation Number', ylab = 'Cooks Distance')
#identify(d, n=1)
d[62] #0.2901108 has a comparabaly large Cooks Distance due to the fact it is both an outlier and high leverage
d[73] #0.3729599, and is the most extreme case. It also has a comparably large Cooks Distance due to the fact it
#is both high leverage and an outlier.
#both have considerably larger cooks distance than the rest of the observations. Furthermore, we have
#already shown that both of the observations are high leverage and outliers. These two facts combine
#to create a large Cooks Distance.

#e
#I would suggest to remove cases 62 and 73 from the model. They are points of high influence which
#unduly impact the model. We have shown that both of the cases are outliers and have high leverage.
#It would be prudent to recommend removing them from the model. Case 62 has a grotesquely large
#studentised residual, and case 73 has a very high leverage.
