# Smart-Maze

This project is the implementation of the Smart Maze using genetic algorithm in Python  

The project is done using Python 3.6 with the following dependencies:
- numpy: http://www.numpy.org/
- pygame: http://www.pygame.org/download.shtml

# Genetic Algorithm

A genetic algorithm is a search heuristic that is inspired by Charles Darwin’s theory of natural evolution. This algorithm reflects the process of natural selection where the fittest individuals are selected for reproduction in order to produce offspring of the next generation.
<img src="https://github.com/androfly/Smart-Maze/blob/master/Images/img1.png" alt="Genetic Algorithm" style="width:200px;height:50px;"></img>
## Notion of Natural Selection

The process of natural selection starts with the selection of fittest individuals from a population. They produce offspring which inherit the characteristics of the parents and will be added to the next generation. If parents have better fitness, their offspring will be better than parents and have a better chance at surviving. This process keeps on iterating and at the end, a generation with the fittest individuals will be found.
This notion can be applied for a search problem. We consider a set of solutions for a problem and select the set of best ones out of them.
Five phases are considered in a genetic algorithm.
1. Initial population
2. Fitness function
3. Selection
4. Crossover
5. Mutation
## Initial Population
The process begins with a set of individuals which is called a Population. Each individual is a solution to the problem you want to solve.
An individual is characterized by a set of parameters (variables) known as Genes. Genes are joined into a string to form a Chromosome (solution).
In a genetic algorithm, the set of genes of an individual is represented using a string, in terms of an alphabet. Usually, binary values are used (string of 1s and 0s). We say that we encode the genes in a chromosome.

<img src="https://github.com/androfly/Smart-Maze/blob/master/Images/img2.png" alt="Genetic Algorithm" style="width:200px;height:50px;"></img>

## Fitness Function
The fitness function determines how fit an individual is (the ability of an individual to compete with other individuals). It gives a fitness score to each individual. The probability that an individual will be selected for reproduction is based on its fitness score.
## Selection
The idea of selection phase is to select the fittest individuals and let them pass their genes to the next generation.
Two pairs of individuals (parents) are selected based on their fitness scores. Individuals with high fitness have more chance to be selected for reproduction.
## Crossover
Crossover is the most significant phase in a genetic algorithm. For each pair of parents to be mated, a crossover point is chosen at random from within the genes.
For example, consider the crossover point to be 3 as shown below.
<img src="https://github.com/androfly/Smart-Maze/blob/master/Images/img2.png" alt="Genetic Algorithm" ></img>

 **Offspring** are created by exchanging the genes of parents among themselves until the crossover point is reached.
 
<img src="https://github.com/androfly/Smart-Maze/blob/master/Images/img3.png" alt="Genetic Algorithm" ></img>

The new offspring are added to the population.

<img src="https://github.com/androfly/Smart-Maze/blob/master/Images/img4.png" alt="Genetic Algorithm" ></img>

## Mutation
In certain new offspring formed, some of their genes can be subjected to a mutation with a low random probability. This implies that some of the bits in the bit string can be flipped.

<img src="https://github.com/androfly/Smart-Maze/blob/master/Images/img5.png" alt="Genetic Algorithm" ></img>

Mutation occurs to maintain diversity within the population and prevent premature convergence.

## Termination
The algorithm terminates if the population has converged (does not produce offspring which are significantly different from the previous generation). Then it is said that the genetic algorithm has provided a set of solutions to our problem.
### Note
The population has a fixed size. As new generations are formed, individuals with least fitness die, providing space for new offspring.
The sequence of phases is repeated to produce individuals in each new generation which are better than the previous generation.
