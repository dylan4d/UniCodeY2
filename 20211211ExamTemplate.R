#load and attach datasets + options
x.df <- read.table('', header = T)
attach(x.df)
head(x.df)
options(contrasts = c(factor = 'contr.treatment', ordered = 'contr.poly'))

'Question 1'
#scatterplot for data
plot(x.df$ , x.df$ , main = 'insert V insert axis', xlab = 'insert', ylab = 'insert')
#insert points stand out 
#dependent variable should be on the y axis
#What is the relationship between the variables?

#model
x.lm <- lm(x.df$insert ~ x.df$insert + x.df$insert + x.df$insert )
abline(x.lm) #added to the plot above

summary(x.lm)
#intercept of insert
#slope of insert

#CI
#slope + (standarderror * qt(0.975, df))
#slope - (standarderror * qt(0.975, df))
# insert% confident that true slope lies between insert and insert

# insert% if the variability in insert can be explained by insert
# insert is useful but other variables would help
# add other variables that would further explain variability in insert

'Question 2'
#model
y.lm <- lm(x.df$ ~ x.df$ + x.df$ + x.df$ + x.df$ )
summary(y.lm)
# insert correlation between insert(will be conc equivalent) and insert(will be time equivalent)
# insert correlation between insert(will be conc equivalent) and insert(will be time equivalent)
# insert correlation between insert(will be conc equivalent) and insert(will be time equivalent)
# insert correlation between insert(will be conc equivalent) and insert(will be time equivalent)
# insert and insert are likely useful predictors, unlike insert and insert
#possible collinearity?

#insert is the estimate of insert
# for every insert insert increase/decrease in insert, there is an expected insert insert increase/decrease in insert, assuming ceteris paribus.

# insert is now adjusted for the effects of other predictors
# correlation between the predictors is insert?
# should consider more variables?
# additional variables help explain more variability?

#H0: insert = insert = insert = insert
#H1: insert, insert, insert, insert, insert are all not 0
#accept/reject H0
#must accept insert
#insert insert insert insert should be dropped
#insert insert insert insert at least one should be kept in the model

#H0: insert = insert = 0
noinsertinsert.lm <- lm(x.df$ ~ x.df$ + x.df$)
anova(y.lm, noinsertinsert.lm)
#Fval of insert
#Pval of insert
#must accept insert
#insert and insert should be dropped from the model
# at least of insert insert should be kept in the model

cor.df <- subset(x.df, select = (-c(insert, insert)))
cor(cor.df)\
#VIF, the variance of the estimated slope for the factors would be x times
#what it would be if all the predictors were uncorrelated
1/(1 - summary(lm(x.df$ ~ x.df$ + x.df$ + x.df$ + x.df$))$r.squared)
1/(1 - summary(lm(x.df$ ~ x.df$ + x.df$ + x.df$ + x.df$))$r.squared)
1/(1 - summary(lm(x.df$ ~ x.df$ + x.df$ + x.df$ + x.df$))$r.squared)
1/(1 - summary(lm(x.df$ ~ x.df$ + x.df$ + x.df$ + x.df$))$r.squared)
1/(1 - summary(lm(x.df$ ~ x.df$ + x.df$ + x.df$ + x.df$))$r.squared)
#the VIF are insert, insert, insert, insert, and insert.
# as insert has/nt VIF above 10 there is/not a serious problem with collinearity
#there is/not serious issue with collinearity.
#I suggest insert changes to the model to reduce collinearity


'Question 3'
#observed value - fitted value
resid(y.lm)[1]
# under/over estimation of insert for the first case

#outlier is a case with a large residual
#if the modulus of the studentised residual exceeds 2 or -2
#ri ~ N(0, 1). Approximately 95% of studentised residuals should lie within -2,2
#insert number of outliers

h <- lm.influence(x.lm)$hat #leverages
e <- resid(x.lm) #residuals
s <- summary(x.lm)$sigma
r <- e / (s * (1 - h)^0.5 )
ppprime <- length(coef(x.lm))
d <- (1/pprime) * (h/(1-h)) * r^2


#plot studentised residuals
plot(r, type = 'h', main = 'Plot of Studentised Residuals vs. Obervation Number', ylab = 'Studentised Residuals', ylim = c(-4,4))
abline(h=c(-2,2), lty = 2)
#studentised residuals for case:
r[insert] #insert
r[insert] #insert
r[insert] #insert

# a case is said to be high leverage if the corresponding is far from the mean of x's.
# insert number of cases of high leverage
# Case insert: insert, insert, insert, insert are all maxima

#plot leverages
plot(h, type = "h", main = "Plot of Leverage vs. Observation Number", ylab = 'Leverage')
h[insert] #insert
h[insert] #insert
h[insert] #insert
#they are of high leverage because the leverage of each point is above 2p'/n... insert*insert / insert ... insert


#A case is said to be of high influence if omitting this case from the data set would cause large changes in the values of the least squares estimates

#plot of Cook's distance
plot(d, type = 'h', main = 'Plot of Cooks Distance vs. Observation Number', ylab = 'Cooks Distance')
d[insert] #insert
d[insert] #insert
d[insert] #insert
#a case of high influence and also almost an outlier
#None/ Investigate case insert, insert, and insert

'Question 4'
#Plot 1/3
#ScatterPlot -> insert relationship insert variance
#Residual V Fitted Values -> insert relationship and insert Variance
#Histogram -> insert insert Residuals
#Normal Probability Plot -> insert insert Residuals
par(mfrow = c(2, 2))
q4.1.lm <- lm(insert ~ insert)
scatter.smooth(insert, insert, main = 'Scatter.smooth Plot')

plot(fitted(q4.1.lm), resid(q4.1.lm), main = 'Plot of Residual V Fitted Values')
abline(h=0, lty = 2)

hist(resid(q4.1.lm), main = 'Histogram of Residuals')
qqnorm(resid(q4.1.lm), main = 'Normal Probability of Residuals')
qqline(resid(q4.1.lm))
par(mfrow = c(1,1))

#Plot 2/3
#ScatterPlot -> insert relationship insert variance
#Residual V Fitted Values -> insert relationship and insert Variance
#Histogram -> insert insert Residuals
#Normal Probability Plot -> insert insert Residuals
par(mfrow = c(2, 2))
q4.2.lm <- lm(insert ~ insert)
scatter.smooth(insert, insert, main = 'Scatter.smooth Plot')

plot(fitted(q4.2.lm), resid(q4.2.lm), main = 'Plot of Residual V Fitted Values')
abline(h=0, lty = 2)

hist(resid(q4.2.lm), main = 'Histogram of Residuals')
qqnorm(resid(q4.2.lm), main = 'Normal Probability of Residuals')
qqline(resid(q4.2.lm))
par(mfrow = c(1,1))

#Plot 3/3
#ScatterPlot -> insert relationship insert variance
#Residual V Fitted Values -> insert relationship and insert Variance
#Histogram -> insert insert Residuals
#Normal Probability Plot -> insert insert Residuals
par(mfrow = c(2, 2))
q4.3.lm <- lm(insert ~ insert)
scatter.smooth(insert, insert, main = 'Scatter.smooth Plot')

plot(fitted(q4.3.lm), resid(q4.3.lm), main = 'Plot of Residual V Fitted Values')
abline(h=0, lty = 2)

hist(resid(q4.3.lm), main = 'Histogram of Residuals')
qqnorm(resid(q4.3.lm), main = 'Normal Probability of Residuals')
qqline(resid(q4.3.lm))
par(mfrow = c(1,1))

#The model for which diagnostic plots are best is insert
# insert satisfies insert assumptions

#insert further models should be considered
#assumptions are/not satisfied, can/not be improved upon

'Question 5'
#weighted regression is required here because each response is a mean of
#varying numbers of insert
#as the response is an average of n equally variable observations,
#then var(y) = sigma^2 / n = sigma^2 / w therefore weights should equal n

q5.weighted.lm <- lm(insert ~ insert, weights = insert)
q5.unweighted.lm <- lm(insert ~ insert)
summary(q5.weighted.lm)
#for a insert insert increase, the expected increase/decrease in mean insert is
#insert insert


#lack of fit test assuming standard deviation is given
#H0: no lack of fit
variance = insert ^2 #given standard deviation
anova(q5.unweighted.lm)
RSS.SS <- insert
tval <- RSS.SS / variance
tval
#teststat is insert
pval <- 1 - pchisq(teststat, df)
pval
#pval is insert
#pval >< 0.05
#we must reject/accept H0
#there is insert lack of fit


#lack of fit test when sd is unknown
#H0: no lack of fit
#RSS = PE.SS + LOF.SS.DEVIANCE
RSSweighted <- deviance(q5.weighted.lm)
RSSweighted
RSS.DF <- insert
#RSSweighted is insert
LOF.DF.RESIDUAL <- q5.weighted.lm$df.residual
LOF.DF.RESIDUAL
#LOF.DF.RESIDUAL is insert
LOF.SS.DEVIANCE <- deviance(q5.weighted.lm)
LOF.SS.DEVIANCE
#LOF.SS.DEVIANCE is insert
PE.SS <- RSS.SS - LOF.SS.DEVIANCE
PE.SS
#PE.SS is insert
PE.DF <- RSS.DF - LOF.DF.RESIDUAL
PE.DF
#PE.DF is insert
LOF.DF.RESIDUAL <- RSS.DF - PE.DF
fval <- (LOF.SS.DEVIANCE / LOF.DF.RESIDUAL) / (PE.SS / PE.DF)
fval
#fval is insert
pval <- pf(fval, PE.DF, LOF.DF.RESIDUAL)
pval
#pval is insert
#pval >< 0.05
#we must reject/accept H0
#there is insert lack of fit

#Suppose it was known that the standard deviation of the weights of individual
#items was insert. Use this to perform a LOF test for the unweighted regression
#model.
#might be equivalent to first option above.
#H0: no lack of fit
#RSS / (givenSigma ^ 2) ~ chi2(n - (p + 1)) ~ (df - (1 + noOfVariables))
#is insert
#cval of chi(0.05, df - 2) is insert and pval is insert
fval <- qchisq(0.05, df - 2, lower.tail = F)
fval
#compare this to insert, as this is insert than the tval of insert it
#is/not alright
#there is/not lack of fit



#vals might differ due to rounding in the file

#perform lof test in a different way
q5.aov <- aov(insert ~ factor(insert), data = insert)
anova(q5.unweighted.lm, q5.aov)
#fval is insert
#pval is insert
#pval sig/nosig
#accept/reject H0


'Question 6'
# insert is a categorical variable and needs to be presented by a numeric variable in the model
# insert becomes insert = insert +- insertX
# insert becomes insert = insert +- insertX

q6.1.lm <- lm(insert ~ insert)
summary(q6.1.lm)
anova(q6.1.lm)

q6.2.lm <- lm(insert ~ insert + insert)
model.matrix(q6.2.lm)
summary(q6.2.lm)
anova(q6.2.lm)

q6.3.lm <- lm(insert ~ insert + insert + (insert * insert))
summary(q6.3.lm)
anova(q6.3.lm)


#plot of subsets
q6.x.lm <- lm(insert ~ insert, subset = insert == 'insert')
q6.y.lm <- lm(insert ~ insert, subset = insert == 'insert')
q6.standard.lm <- lm(insert~ insert)
plot(insert, insert)
abline(q6.x.lm)
abline(q6.y.lm)
summary(q6.x.lm)
#intercept insert
summary(q6.y.lm)
#intercept insert
summary(q6.standard.lm)
#intercept insert
plot(insert, insert, main = 'Same regression line for both insert', xlab = 'insert', ylab = 'insert', pch = c('insert', 'insert'))
print(sort(x.df[1,,], decreasing = T)) #Just using to verify that the max value is the right categorical variable
legend(insert, insert, pch = 'FM', legend = c('Female', 'Male'))
abline(q6.standard.lm)

#same intercept
#H0: B2 = 0
anova(q6.1.lm, q6.2.lm)
#pval of insert
#conclude that they insert

#parallel slopes
#H0: b3 = 0
anova(q6.3.lm, q6.2.lm)
#pval of insert
#conclude that they are insert

#lines coincide
#H0: b2 = b3 = 0
anova(babies1.lm, babies3.lm)
#pval of insert
#conclude that they insert

#the insert insert regression line
#we have concluded that the lines are insert

#there is a insert relationship between insert and insert
#as insert increases, insert increases/decreases
#the relation does/not differ based on insert
