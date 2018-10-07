# Exploratory Data Analysis of Laptop Data Mix                                                                                               

laptopDataSet = read.csv(file.choose(), header = TRUE)
str(laptopDataSet)
View(laptopDataSet)
str(laptopDataSet)

##SampleAggregate =  aggregate(laptopDataSet$Price_euros,by=laptopDataSet$Company,laptopDataSet,mean)

## Listing All the Categorical Values that could be there

levels(laptopDataSet$Company)
levels(laptopDataSet$TypeName)
levels(laptopDataSet$ScreenResolution)
levels(laptopDataSet$Ram)
levels(laptopDataSet$TypeName)
levels(laptopDataSet$Memory.Storage..primary.)
levels(laptopDataSet$Storage.Type.Primary.)
levels(laptopDataSet$Memory.Storage.Secondary.)
levels(laptopDataSet$Storage.type.Secondary.)


## Listing all the useful numeric variables

n = length(colnames(laptopDataSet))
 
table1 = 0
print("The Following are the list of numeric variables")
for(i in 1:n){
  ## print( colnames(crime)[i])
  colvector =  as.vector(   laptopDataSet[[colnames(laptopDataSet)[i]]] )
  if(class(colvector) == "numeric" )
   { print(colnames(laptopDataSet)[i])
   table1 = cbind(table1,laptopDataSet[ colnames(laptopDataSet)[i]])
  }
  if(class(colvector) == "integer")
    {
      table1 = cbind(table1, laptopDataSet[ colnames(laptopDataSet)[i]]  )    
    }
}


table1 = cbind(table1,laptopDataSet[ colnames(laptopDataSet)[2]])

View(table1)
colnames(table1)

n = length(levels(laptopDataSet$Company))
levels(laptopDataSet$Company)[1]
paste("ASD","SADS")

cor(table1$Price_euros,table1$ProcessorSpeed.GHz. )
 
for(i in 1:n) {
  BrandName = levels(laptopDataSet$Company)[i];
  print(paste("###### Data For" ,BrandName));
  table2 = table1[table1$Company==BrandName,]
  model = lm(table2$Price_euros ~  table2$Weights.in.Kgs + table2$ProcessorSpeed.GHz.+ table2$Inches + table2$Hard.Disc.GB.+ table2$RAM.in.GB  )
  print(summary(model))
  Sys.sleep(1)
  print("###End Model###")
  
}

table2 = table1[table1$Company=="Apple",]
##cor(table1)



#Null Hypothesis is that Screen dimentions, processorSpeed, Weight are not related to price
# Alternate hypothesis is They are related
model = lm(table2$Price_euros~table2$Inches+table2$ProcessorSpeed.GHz.+table2$Weights.in.Kgs)
summary(model)

model1  = lm(formula = Price_euros~.,data = table2)
summary(model1)



## The Low P value suggests that the null hypothesis is rejected
## Hence it can be shown that it is related
