---
layout: post
title: Basics of Probability and Information Theory
subtitle: Probability and Information Theory
subsubtitle: for machine learning
date: 2017-04-25
description: The post introduce the basics principle of probability and information theory and their application to machine learning.
author: Anthony Faustine 
image: bayesvariational.jpg
---


Probability and Information theory are important field that has made significant contribution to deep learning and AI. Probability theory allows us to make *uncertain statements* and to *reason* in the presence of *uncertainty* where information theory enables us to *quantify* the amount of *uncertainty* in a probability distribution.

## 1. Probability Theory

Probability is a mathematical framework for representing uncertainty. It is very applicable in Machine learning and Artificial Intelligence as it allows to make *uncertain statements* and  *reason* in the presence of *uncertainty*. Probability theory allow us to design ML algorithms that take into consideration  of *uncertain* and sometimes *stochastic*  quantities. It further tell us tell us how ML systems should *reason* in the presence of uncertainty. This  is necessary because most things in the world  are uncertain, and thus  ML systems should reason using probabilistic rules. Probability theory can also be used to analyse the behaviour of  ML algorithms probabilistically. Consider evaluating ML classification algorithm using  accuracy metric which is  the probability that the model will give a correct prediction  given an example.

### 1.2 Random Experiment, Sample Space and Random Variable
Random experiment is the physical situation whose outcome cannot be predicted until it is observed. It is the process of observing event having uncertain outcome. When we repeat random experiment several times we call each of experiment a *trial* The set of all possible outcomes of random experiment is know as **sample space* $$S$$. Consider observing the number of goals in the soccer match as a random process. The sample space is the possible number of goals $$S = \{0,1,\ldots n\}$$. For coin tossing experiment the sample space is $$S = \{\text{Head, Tail}\}$$ and for handwritten digit recognition experiment the sample space is $$S = \{0,1,\ldots 9\}$$.

A measurable function $$X$$ which maps every member of the sample space $$S$$ to a real-number is called **random variable**. Random variables can be continuous or discrete. Discrete random variable take only countable number of distinct values for  example populations, movie ratings and number of votes. On the other hand continuous random variable take infinite number of possible values. Things like temperature, speed, time etc are all modelled as continuous variables.

### 1.3 Probability and Probability distribution

**Probability** is a measure of the likelihood that an event will occur in a random experiment. It is quantified as number between 0 and 1. The mathematical function that maps all possible outcome of a random experiment with its associated probability it is called **probability distribution**. It describe how likely a random variable or set of random variable is to take on each of its possible state. The probability distribution for discrete random variable is called probability mass function (PMF) which measures the probability $$X$$ takes on the value $$x$$, denoted denoted as $$P(X=x)$$.
To be PMF on random variable $$X$$  a function $$P(X)$$ must satisfy:

- Domain of $$P$$ equal to all possible states of $$X$$
- $$\forall x \in X, 0\leq P(X=x) \leq 1$$
- $$\sum_{x \in X} P(x) =1$$

Popular and useful PMF includes poison, binomial, bernouli, and uniform. Let consider a poison  distribution defined as:

$$
P(X=x) = \frac{\lambda ^x e^{ -\lambda}}{x!}
$$

$$\lambda >0$$ is called a parameter of the distribution, and it controls the distribution's shape. By increasing $$\lambda$$ , we add more probability to larger values, and conversely by decreasing $$\lambda$$  we add more probability to smaller values as shown in figure below.


Instead of a PMF, a continuous random variable has a probability density function (pdf) denoted as $$f_X(x)$$. An example of continuous random variable is a random variable with exponential density. 

$$
f_X(x\mid \lambda) = \lambda ^x e^{ -\lambda} \text{,  } x \geq 0
$$


To be a probability density function $$p(x)$$ must satisfy
- The domain of $$p$$ must be the set of all possible state
- $$\forall x \in X, f_X(x) \geq 0$$
- $$\int_{x \in X} f_X(x)dx =1$$

The pdf does not give the probability of a specific state directly. The probability that $$x$$ is between two point $$a, b$$ is 

$$\int_{a}^b f_X(x)dx$$

The probability of intersection of two or more random variables is called *joint probability* denoted  as $$
P(X, Y)
$$
Suppose we have two random variable $$X$$ and $$Y$$ and we know the joint PMF or pdf distribution between these variable. The PMF or pdf  corresponding to a single variable is called *marginal probability distribution* defined as

$$
P(x) = \sum_{y\in Y} P(x, y)
$$

for discrete random variable and 

$$
p(x) = \int p(x)dy
$$

Marginalization allows us to get the distribution of variable $$X$$ ignoring variable $$Y$$ from the joint distribution $$P(X,Y)$$. The probability that some event will occur given we know other events is called condition probability denoted as $$P(X\mid Y)$$. The  marginal, joint and conditional probability are linked by the following rule 

$$
P(X|Y) = \frac{P(X, Y)}{P(Y)}
$$

**Independence, Conditional Independence and Chain Rule**

Two random variables are said to be independent of each other if the probability that one random variables occur in no way affect the probability of the other random variable occurring. $$X$$ and $$Y$$ are said to be independent if $$P(X,Y) = P(X)\cdot P(Y)$$
On the other hand two random variable $$X$$ and $$Y$$ are conditionally independent given an event $$Z$$ with $$P(Z)>0$$ if 

$$
P(X,Y\mid Z) = P(X\mid Y)\cdot P(Y\mid Z)
$$
The good example of conditional independence can be found on this [link]()

Any joint probability distribution over many random variables may be decomposed into conditional distributions using *chain rule* as follows:

$$
P(X_1,X_2, \ldots, X_n ) = P(X_1)\prod_{i=2}^n P(X_i\mid X_i, \ldots X_{i-1})
$$

**Expectation, Variance and Covariance**

Expected value of some function $$f(x)$$ with respect to a probability distribution $$P(X)$$ is the average or mean value that $$f(x)$$ takes on when $$x$$ is drawn from $$P$$.

$$
\mathbb{E}_{x\sim P}[f(x)] = \sum P(x).f(x)
$$

for discrete random variable and 

$$
\mathbb{E}_{x\sim P}[f(x)] = \int P(x).f(x)dx
$$

Expectation are linear such that 
$$
\mathbb{E}_{x\sim P}[\alpha \cdot f(x) + \beta \cdot g(x)] = \alpha \mathbb{E}_{x\sim P}[f(x)] + \beta \mathbb{E}_{x\sim P}[g(x)]
$$

Variance is a measure of how much the value of a function of random variable $$X$$ vary as we sample different value of $$x$$ from its probability distribution.

$$
Var(f(x)) =\mathbb{E}([f(x)-\mathbb{E}[f(x)]^2])
$$

The square root of the variance is know as standard deviation. On the other hand the covarince give some sense of how much two value are linearly related to each other as well as the scale of these value.

$$
Cov(f(x), g(y)) = \mathbb{E}[(f(x)- \mathbb{E}[f(x)])(g(y)- \mathbb{E}[g(y)])]
$$

### 2. Information theory
Information theory deals with quantification of how much information is present in a signal. In context of machine learning, information theory we apply information theory to: *characterize probability distributions* and *quantify similarities between probability distributions*. The following are the key information concepts and their application to machine learning.

### 2.1 Entropy, Cross Entropy and Mutual information

Entropy give measure of uncertainty in a random experiment. It help us  quantify the amount of uncertainty in an entire probability distribution. The entropy of a probability distribution is the expected amount of information in an event drawn from that distribution defined as.

$$
H(X) = -\mathbb{E}_{x \sim P}[\log P(x)] = -\sum_{i=1}^n P(x_i)l\log P(x_i)
$$

Entropy is widely used in model selection based on principle of maximum entropy. On the other hand, cross entropy is used to compare two probability distribution. It tell how similar two distribution are. The cross entropy between two probability distribution $$P$$ and $$Q$$ defined over same set of outcome is given by 

$$
H(P,Q)= -\sum P(x)\log Q(x)
$$ 

Cross entropy loss function is widely used in machine learning for classification problem.

The mutual information over two random variables help us gain insight about the information that one random variable carries about the other. 

$$
\begin{aligned}
I(X, Y) &= \sum P(x, y)\log \frac{P(x,y)}{P(x).P(y)}\\
        &=H(X)- H(X\mid Y) = H(Y) - H(Y\mid X)
\end{aligned}
$$

From above equation the mutual information  give insight about how far $$X$$ and $$Y$$ from being independent from each other. Mutual information can be used in feature selection instead of correlation as it capture both linear and non linear dependency.


### 2.2 Kullback-leibler Divergence 

**Kullback-leibler Divergence** measure how one probability distribution diverge from the other. Given two probability distribution $$P(x)$$ and $$Q(X)$$ where the former is the modelled/estimated distribution and the later is the actual/expected distribution. The **KL** divergence is defined as 

$$
\begin{aligned}
D_{KL}(P||Q) & = \mathbb{E}_{x \sim P} [\log \frac{P(x)}{Q(x)}]\\
             & = \mathbb{E}_{x \sim P}[\log P(x)] - \mathbb{E}_{x \sim P}[\log Q(x)]
\end{aligned}
$$

For discrete random distribution 

$$
D_{KL}(P||Q) = \sum_{i} P(x_i)\log \frac{P(x_i)}{Q(x_i)}
$$

And for continuous random variable

$$
D_{KL}(p||q) = \int_{x} p(x) \log \frac{p(x)}{q(x)}
$$

KL divergence between $$P$$ and $$Q$$ tells how much information we lose when trying to approximate data given by $$P$$ with $$Q$$. It is non-negative $$D_{KL}(P\mid \mid Q) \geq 0$$ and  $$0$$ if $$P$$ and $$Q$$ are the same (distribution discrete) or equal almost anywhere in the case of continuous distribution. Apart from that KL divergence is not symmetric $$D_{KL}(P\mid \mid Q) \neq D_{KL}(P\mid \mid Q)$$ because of this it is not a true distance measure.

**Relation between KL divergence and Cross Entropy**

$$
\begin{aligned}
D_{KL}(P||Q) & = \mathbb{E}_{x \sim P} [\log \frac{P(x)}{Q(x)}]\\
             & = \mathbb{E}_{x \sim P}[\log P(x)] - \mathbb{E}_{x \sim P}[\log Q(x)]\\
             & = H(P) - H(P, Q)\\
\end{aligned}
$$

where $$\mathbb{E}_{x \sim P}[\log P(x)] = H(P)$$ and $$\mathbb{E}_{x \sim P}[\log Q(x)] = H(P, Q)$$

Thus 

$$
H(P,Q) = H(P) - D_{KL}(P||Q)
$$

This implies that minimizing cross entropy with respect to $$Q$$ is equivalent to minimizing the KL divergence.

KL divergence is used in unsupervised machine learning technique like variational auto-encoder. The KL divergence is also used  as objective function in variational bayesian method to find optimal value for approximating distribution.
