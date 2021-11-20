bmi.df <- read.table("//Users//dylan//OneDrive//Documents//School Files Y2//IntroductionToRegression//BMI.txt", header = T)
attach(bmi.df)


#A
bmi.df.lm <- lm(formula = BMI ~ Waist + Leg + Elbow + Wrist + Arm)
summary(bmi.df.lm)
#b3 is estimated to be -0.53240
#every one unit change in elbow breadth, ceteris paribus, the BMI will have a
#change of -0.053240.


#B
#The value of R^2 is 0.894, this means that 0.894 of
#the variability can be explained by our inputs, this is a
#strong relationship.

#C
#F-statistic is 124.8 and p-value is 2.2e^-16
#as the p value is less than 0.05, we have sufficient evidence
#to reject H0. This implies we have sufficient evidence to say that
#b1=b2=b3=b4=b5=0 is false. The inputs are able to explain some variability
#in our data. Our model is useful in predicting BMI.

#D
bmi.NoElbowWrist <- lm(formula = BMI ~ Waist + Leg + Arm)
anova(bmi.NoElbowWrist, bmi.df.lm)
#H0 b3=b4=0
#H1 not both are 0
#f stat is 4.0245 and the p-val of 0.02192
#pvalue is less than 0.05, we have sufficient evidence to reject H0
#b3 and/or b4 have a significant impact on our
#we should include both wrist and elbow as they have a beneficial impact 
#on our model. It would make sense to include them when we have the chance.

#E
cor.df <- subset(bmi.df, select = (-c(Case, BP)))
cor(cor.df)
#VIF, the variance of the estimated slope for the factors would be x times what
#it would be if all the predictors were uncorrelated.
1/(1-summary(lm(Waist ~ Leg + Elbow + Wrist + Arm))$r.squared)
1/(1-summary(lm(Leg ~ Waist + Elbow + Wrist + Arm))$r.squared)
1/(1-summary(lm(Elbow ~ Leg + Waist + Wrist + Arm))$r.squared)
1/(1-summary(lm(Wrist ~ Leg + Elbow + Waist + Arm))$r.squared)
1/(1-summary(lm(Arm ~ Leg + Elbow + Wrist + Waist))$r.squared)
#the two highest VIF are 4.482263 and 4.663142. As none exceed a VIF of 10
#there is no serious issue with collinearity.
#I do not suggest any changes to the model to reduce collinearity.
#It is expected for body measurements to be somewhat collinear.


#F
#H0: the value of b3 is 0
#H1: the value of b3 is not equal to zero.
#p value of 0.3440
#p>0.05, we do not have sufficient evidence to reject the null hypothesis.
#we must accept that b3 = 0.
#the value of 0 falls between the range of values we have for the slope of b3.






