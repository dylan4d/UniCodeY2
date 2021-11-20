fuel.df <- read.table("C:\\Users\\120309116\\Documents\\R\\R Datasets\\fuel.txt", header=T)
attach(fuel.df)


fuel.df.lm <- lm(formula = FUEL ~ TAX + DLIC + INC + ROAD)
summary(fuel.df.lm)

#a
#the estimate of B1 is -34.790, for every one unit increase in motor fuel consumption
#there is a -34.790 unit fall in the motor fuel tax rate in cents per gallon


#b
#the R^2 value is 0.6787, this means that 0.6787 of the output can be explained by our inputs
#this is a weak-moderate correlation


#c
#we have sufficient evidence to reject the null hypothesis
#as the p-val is less than 0.05, pval = 0.010332


#d
#we have sufficient evidence to reject the null hypothesis,
#as the p-val is less than 0.05, pval = 3.907e^-10


taxRoad.lm <- lm(formula = FUEL ~ TAX + ROAD)
summary(taxRoad.lm)

#e
#we have sufficient evidence to reject the null hypothesis
#as the p-val is less than 0.05, pval= 0.0008904

#Plot  the  residuals  from  the  model  of  FUEL  on  DLIC,  INC  and  ROAD  (on  the  Y-axis)
#against the residuals form the model of TAX on DLIC, INC and ROAD (on the X-axis).This  is  theadded
#variable  plot  of  TAX  after DLIC, INC and ROAD.  TAX  is  the  added variable.  