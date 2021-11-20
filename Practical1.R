bmi.df <- read.table("/Users/dylan/OneDrive/Documents/School Files Y2/IntroductionToRegression/BMI.txt", header = T)

plot(bmi.df$Waist, bmi.df$BMI, main = "Waist Circumference against BMI", pch = 16)

#Relatively strong, positive linear correlation

bmi.lm <- lm(BMI ~ Waist)
abline(bmi.lm)
summary(bmi.lm)

#0.32985 is our value for the slope
#0.02017 is our value for the standard error

0.32985 + ( qt(0.975, 78) * 0.02017)
0.32985 - ( qt(0.975, 78) * 0.02017)
#we are 95% certain that the value for the slope lies
#between 0.3700054 and 0.2896946


((0.32985 - 0.3) / 0.02017)^2

#1.479920606 t test result (sqrt of f stat)
#2.190165 f-statistic
#0.071464 p value
#the result is not significant

predict(bmi.lm, data.frame(Waist = 88), se.fit = T, interval = 'prediction', level = 0.95)
#our predicted value is 25.81639, we also believe there to be a 95% chance that
#the bmi to be between 21.06582 and 30.56695



