## PPA Project

## Version 1.0

## Objective : To deduce a package pricing model, based on the data set provided

##             provided by Mission Health 


#####


#Setting the libraries

setwd("C:/Users/GIM/Desktop/Project")

library(car)

library(corrplot)

library(caret)

library(caTools)

library(dplyr)

library(psych)

hospitalRawDAta=read.csv("dataset.csv")

View(hospitalRawDAta)

summary(hospitalRawDAta)

str(hospitalRawDAta)

#####Data is read from the file and basic summaries are observed



##Observation - Missing Values

## BP..HIGH  NA's   :23 Systolic BP

## BP.LOW  NA's   :23  Diastolic BP

## HB NA's :2 

## UREA  NA's   :13  

## CREATININE NA's   :33  


hospitalData = hospitalRawDAta

data = hospitalRawDAta

###############################Start Of Missing Value Treatment ########### 

data$BP..HIGH[ is.na (data$BP..HIGH) ] = median(hospitalRawDAta$BP..HIGH, na.rm = TRUE)

data$BP.LOW[ is.na (data$BP.LOW) ] = median(hospitalRawDAta$BP.LOW, na.rm = TRUE)


##Observe Hameglobin missing.

View(data[is.na(data$HB),])

##both are female

femaleData = data[data$GENDER == "F",]


data$HB[is.na(data$HB)] =  median(femaleData$HB, na.rm = TRUE)


summary(data)




##observe UREA



View(data[is.na(data$UREA),]) 

a = data[is.na(data$UREA),]

data[is.na(data$UREA),]$UREA  = ifelse(data[is.na(data$UREA),]$AGE > 18,11.5,13.5)

View(data)


View(data[is.na(data$CREATININE),])


summary(data[!is.na(data$CREATININE),]$CREATININE)




hist (data[data[!is.na(data$CREATININE),]$GENDER=='F',]$CREATININE)


hist( data[data[!is.na(data$CREATININE),]$GENDER=='M',]$CREATININE)



##Temp Step

data$CREATININE[is.na(data$CREATININE)] =  median(data$CREATININE, na.rm = TRUE)


data$CREATININE[is.na(data$CREATININE)] = ifelse(data$CREATININE[is.na(data$CREATININE)]$GENDER=="M", median(data[data[!is.na(data$CREATININE),]$GENDER=='M',]$CREATININE), median(data[data[!is.na(data$CREATININE),]$GENDER=='F',]$CREATININE) )


##Temp Step


data[data[is.na(data$CREATININE),]$GENDER=='F',]$CREATININE = median(data[data[!is.na(data$CREATININE),]$GENDER=='F',]$CREATININE)

data[data[is.na(data$CREATININE),]$GENDER=='M',]$CREATININE = median(data[data[!is.na(data$CREATININE),]$GENDER=='M',]$CREATININE)





summary(data)

# missing values replace


# Summary Statistics


str(data)

######################## End of Missing Value Treatment######




##As there are dummy variables already created for catagorical variables

##Getting only the numeric part of hospital data for modelling


hospitalDataN = data %>%
  
  select_if(is.numeric)



## There are 44 Variable in the hospitalDataN

## Plotting the correlations between these varables can be exported 

## To Excel


##Plotting Correlations into newcorr##

write.csv(cor(hospitalDataN),"newcorr.csv")

##End ##


## Modelling of Variables

model1 = lm(TOTAL.COST.TO.HOSPITAL ~ CREATININE, data = hospitalDataN)
summary(model1)
plot(model1$fitted.values,model1$residuals)

#Low R-Squared


#Total lenghth of stay is highly correlated to ICU Stay and more General 
# Hence use total length of stay instead
model2 = lm(TOTAL.COST.TO.HOSPITAL ~ TOTAL.LENGTH.OF.STAY, data = hospitalDataN)
summary(model2)
plot(model2$fitted.values,model2$residuals)


#Lower R-Squared



model3 = lm(TOTAL.COST.TO.HOSPITAL ~ TOTAL.LENGTH.OF.STAY+ COST.OF.IMPLANT, data = hospitalDataN) 
summary(model3)
plot(model3$fitted.values,model3$residuals)


#Incresed R-Squared


model4 = lm(TOTAL.COST.TO.HOSPITAL ~ TOTAL.LENGTH.OF.STAY+ COST.OF.IMPLANT +AGE , data = hospitalDataN)  ### also have an option to use just implant instead
summary(model4)
plot(model4$fitted.values,model4$residuals)

## Explore newer variables
model5 = lm(TOTAL.COST.TO.HOSPITAL ~ TOTAL.LENGTH.OF.STAY+ COST.OF.IMPLANT +AGE + Diabetes2  , data = hospitalDataN)  ### also have an option to use just implant instead and also Body weight/ height can be used instead of age
summary(model5)
plot(model5$fitted.values,model5$residuals)



## Explore newer variables
model6 = lm(sqrt(TOTAL.COST.TO.HOSPITAL) ~ TOTAL.LENGTH.OF.STAY+ COST.OF.IMPLANT +AGE + Diabetes2+ LENGTH.OF.STAY..WARD  , data = hospitalDataN)  ### also have an option to use just implant instead and also Body weight/ height can be used instead of age
summary(model6)
plot(model6$fitted.values,model6$residuals)



## final Model
model7 = lm(TOTAL.COST.TO.HOSPITAL ~TOTAL.LENGTH.OF.STAY+ COST.OF.IMPLANT +AGE + Diabetes2 + LENGTH.OF.STAY..WARD, data = hospitalDataN)
summary(model7)




## Linnear transformation to remove hetroscedacity
model8 = lm(log(TOTAL.COST.TO.HOSPITAL) ~(TOTAL.LENGTH.OF.STAY+ COST.OF.IMPLANT +AGE + Diabetes2 + LENGTH.OF.STAY..WARD)^2 , data = hospitalDataN)  
plot(model8$fitted.values,model8$residuals)


prediction <- predict(model7,hospitalDataN)
plot((hospitalDataN$TOTAL.COST.TO.HOSPITAL),type = "l", col = "Green")
lines(prediction, type = "l", col="Blue")





##End Of PPA Project 