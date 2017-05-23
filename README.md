# Data-Science-course-Columbia-Note

Data Science is multidiscipline, collect, observe, process data ... -> prediction and recommendation

Data is now explorion ( people, sensors, social ....)

Data visulization and data summerization are important because from data visualiszation and summerization, people can find out what kind of data is important. It is one of the first steps of data science.

What a data science need ? Statitic, mathematic, machine learning, optimization

In the “map” stage, a programming task is divided into a number of identical subtasks, which are then distributed across many processors
the intermediate results are then combined by a single reduce task



The most popular open source implementation of MapReduce is the Hadoop project

II.1 Statitic

1. Some concept
Population interet -> who is used for sampling ?

Data gerenartion process -> Create Data->Analyse->Ouput

Data generation process ( affect by assumption) if good assumption -> good data -> good ouput
if bad assumption -> bad data -> bad output ( revise)

Data are number in context (the meaning of data depend on individual-context)
Statitic makes observation on individual (ex M. A, M. B ) on a set of variable (ex. size, age..)

Type of variable 
  -categorical ex, gender, national... don't have arithmetic meaning
  -quantatif have arithmetic meaning ex age, size
  -ordinal don't have arithmetic meaning but have order ( How often you learn ? every day, somtime ...)
Statitics are:

Summezise of numerical data
not tell hold story
useful and meaningful



2. Display numerical data
For categorical variable, we can display by count, percentage (ex number of femme, number of homme), we call area principle (pie, line)
For quantatif variable, we can display by count, percentage (histogram usally for interval of value age (1-10), age (10-20))

2.1 Center of variation:
mean (numerical average )
median (midpoint) (point that have the most individual values)
variance 1/(n-1)Sigma(Xi-Xmean)(Xi-Xmean)
standard deviation : sqrt(variance)
Quantile(percentile-threshold) the value that have %value that less than it
Quartile = the set of quantile that have 25%, 50%, 75% values that less than it

2.2
Box plot : Five value : min, Q1, median (Q2-50%), Q3, max ( we can add some outlier, extremes value)
2.3 Association between variables
ex P1=P(internet|young)
p2=P(internet|senior)
Relative risk rr=P1/P2
Odds ratio or=(P1/(1-P1))/(P2/(1-P2))

2.4 Relation between variables

correlation : assocation between quantative variables 
r=(1/n-1)Sigma((Xi-Xmean)/variance S)((Yi-Ymean)/variance Y)
r in [-1, 1]
r< 0 negative relation
r>0 positive relation
r=0 : pas de relation

2.6 Probability:

Random process (randomness):
  Unpredictable
  Trend
Describe randomness
  Write down all outcomes (sample spaces)
  Change, probability ( of each outcome )
  Probability of an event is the sum of the probabilities of the outcomes included in the definition of the event.
  
