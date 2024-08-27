# GrnController

This repository is here to evolve a controller using the git modules GRNEAT (https://github.com/scussatb/GRNEAT.git), this controller aim to control the paddle of Pong (git@github.com:joaoMartinSaquet/PongEnv.git)

## GRNEAT

This is a java package that implements the EA algorithms for a GRN models, to evolve a GRN controller you need to define an evaluator. 
This evaluator has the role to create a fitness that the EA aim to maximize.

### Compile + execute 

To compile the project, go to GrnController and in term

```
mvn compile -f GRNEAT/pom.xml
```

to execute 
```
mvn -f GRNEAT/pom.xml exec:java -Dexec.mainClass="PACKAGE.MAINCLASS"
```

example 

```
mvn -f GRNEAT/pom.xml exec:java -Dexec.mainClass="evaluators.PongEvaluator"
```


## Pong Env 

is a package that provides a client server that simulate the pong environment with all the command to run an episodes.


