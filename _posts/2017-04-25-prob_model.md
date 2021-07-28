---
layout: post
title: Learning Probabilistic Models
subtitle: Learning Probabilistic Models
subsubtitle: Pthe principle of probabilistic modelling 
date: 2017-04-25
description: The post introduce the principle of probabilistic modelling with focus on how to learn parameters of probabilistic model using maximum likehood, bayesian estimation and the maximum aposterior approximation.
author: Anthony Faustine 
image: bayesvariational.jpg
---

Given some data $$ \mathbf{x}=[x_1\ldots x_m]$$  that come from some probability density function characterized by
an unknown parameter $$ \theta$$ . How can we find $$ \hat{\theta}$$  that is the best estimator of $$ \theta$$. For example suppose we have flipped a particular coin $$ 100$$  times and landed head $$ N_H = 55$$  times and tails $$ N_T = 45$$  times. We are interested to know what is the probability that it will come-up head if we flip it again. In this case the behaviour of the coin can be summerized with parameter  $$ \theta$$  the probability that a flip land head (H) which in this case is independent and identically ditributed Bernoulli distribution. The key question is how do we find parameter  $$ \hat{\theta}$$  of this distribution that fit the data. This is called parameter estimation in which three approaches can be used:

1. Maximum-Likehood estimation
2. Bayesian parameter estimation and 
3. Maximum a-posterior approximation

### Like-hood and log-likehood function

Let firts define the **like-hood function** $$L(\theta)$$ which is the probability of the observed data as function of $$\theta$$ given as:

$$
L(\theta) = P(x_1,\ldots x_m; \theta) = \prod_i^m P(x_i;\theta)
$$

The like-hood function indicates how likely each value of the parameter is to have generated the data. In the case of coin example above, the like-lihood is the probability of particular seqeuence of H and T generated:

 $$
 L(\theta) = \theta ^{N_H}(1 - \theta ^{N_T})
 $$ 

We also define the **log-likelihood function** $$\mathcal{L}(\theta)$$ which is the log of the likelihood function $$L(\theta)$$.

$$
\begin{aligned}
\mathcal{L}(\theta) &= \log L(\theta) \\
 & = \log \prod_i^m P(x_i;\theta) \\
  & = \sum_i^M P(x_i;\theta)
\end{aligned}
$$

For the above coin example the log-likelihood is 

$$ 
\mathcal{L}(\theta)= N_H\log\theta + N_T\log(1-\theta)
$$


## Maximum-Likelihood Estimation
The main objective of maximum likelihood estimation (MLE) is to determine the value of $$\theta$$ that is most likely to have generated the vector of observed data, $$\mathbf{x}$$ where $$\theta$$ is assumed to be  fixed point (point-estimation). MLE achieve this by finding the parameter that maximize the probability of the observed data. The parameter $$\hat{\theta}$$ is selected such that it maximize $$  \mathcal{L}(\theta)$$:
 
 $$
\hat{\theta}=\arg\max_{\theta} \mathcal{L}(\theta)
$$

For the coin example the MLE is :

$$
\begin{aligned}
\frac{\partial \mathcal{L}(\theta)}{\partial \theta} & = \frac{\partial }{\partial \theta}(N_H\log\theta + N_T\log(1-\theta) \\
 &= \frac{N_H}{\theta} - \frac{N_T}{1-\theta}
\end{aligned}
$$

Set $$\frac{\partial \mathcal{L}(\theta)}{\partial \theta} = 0$$  and  solve for $$\theta$$ we obtain the MLE: 

$$
\hat{\theta} =\frac{N_H}{N_H + N_T}
$$

which is simply the fraction of flips that cameup head.

Now suppose we are observing power-meta data which can be modelled as gaussian ditribution with mean $$\mu$$ and standard deviation $$\sigma$$. We can use MLE to estimate $$\hat{\mu}$$ and $$\hat{\sigma}$$. The log-likehood for gausian distribution is given as 

$$
\begin{aligned}
\mathcal{L}(\theta) &= \sum_{i=1}^M \log \left[ \frac{1}{\sqrt{2} \pi \sigma} \exp \frac{-(x_i - \mu)}{2\sigma ^2}\right] \\
 & = -\frac{M}{2}\log 2\pi - M\log \sigma - \frac{1}{2\sigma^2} \sum_i^M (x_i - \mu)^2
\end{aligned}
$$

Let find $$ \frac{\partial \mathcal{L}(\theta)}{\partial \mu} $$ and $$\frac{\partial \mathcal{L}(\theta)}{\partial \sigma} $$ and set  equal to zero.

$$
\begin{aligned}
\frac{\partial \mathcal{L}(\theta)}{\partial \mu} &=  -\frac{1}{2\sigma^2} \sum_i^M \frac{\partial}{\partial \mu}(x_i - \mu)^2 \\
& = \sum_i^M (x_i - \mu) = 0 \\
&\Rightarrow \hat{\mu} = \frac{1}{M} \sum_{i=1}^M x_i
\end{aligned}
$$

which is the mean of the observed values.

Similary:

$$
\begin{aligned}
\frac{\partial \mathcal{L}(\theta)}{\partial \sigma} &=  \frac{M}{\sigma} + \frac{1}{\sigma^3}\sum_i^M (x_i - \mu)^2 \\
&\Rightarrow \hat{\sigma} = \sqrt{\frac{1}{M} \sum_{i=1}^M (x_i - \mu)^2}
\end{aligned}
$$

In the two examples above  we manged to obtain the exact maximum likelihood solution analytically. But this is not always the case, let’s consider how to compute the maximum likelihood estimate of the parameters of the gamma distribution, whose PDF is defined as:

$$
P(x) = \frac{b^a}{\Gamma(a)}x^{x-1}\exp(-bx)
$$

where $$\Gamma (a)$$ is the gamma function which is the generalization of the factorial function to continous values given as:

$$
\Gamma(t) = \int_0^{-\infty} x^{t-1}\exp(-x) \,dx
$$

The model parameters for gamma distribution is $$a$$ and $$b$$ both of which are $$\geq 0$$. the log-likelihood is therefore:

$$
\begin{aligned} \mathcal{L}( a, b) & = \sum_{i=1}^M a\log b -\log \Gamma (a) + (a -1) \log x_i - bx_i \\
 & = Ma\log b - M \log \Gamma (a) + (a - 1) \sum_{i=1}^M \log x_i - b \sum_{i=1}^M x_i
\end{aligned}
$$

To get MLE we need employ gradient descent which consists of computing the derivatives:
$$
\frac{\partial \mathcal{L}}{\partial a}
$$ and 
$$
\frac{\partial \mathcal{L}}{\partial b}
$$ and then updating;

$$
a_{k+1}= a_k + \alpha \frac{\partial \mathcal{L}}{\partial a}
$$

and 

$$
b_{k+1}= b_k + \alpha \frac{\partial \mathcal{L}}{\partial b}
$$

where $$\alpha$$ is the learning rate.


### Limitation of MLE

Despite the fact that MLE is very powerful technique, it has a pitfall for little training data which can lead into seriously overfit. The most painful issue is when it assign a $$0$$ probability to items that were never seen in the training data but which still might actually happen. Take an example if we flipped  a coin twice and $$N_H = 2$$, the MLE of $$\theta$$, the probability of H would be $$1$$. This imply that we are considering it impossible for the coin to come up T. This problem is knowas *data sparsity*.

## Bayesian Parameter Estimation

Unlike MLE which treat only the observation $$\mathbf{x}$$ as random variable and the parameter $$\theta$$ as a fixed point, the bayesian approach treat the parameter $$\theta $$ as random varibale as well with some known prior distribution. Let define the model for joint distribution $$p(\theta, \mathcal{D})$$ over parameter  $$\theta$$ and data $$\mathcal{D}$$. To further define this joint distribution we aslo need the following two distribution:

* A distribution of $$P(\theta)$$ knowas **prior distribution** which is the probability of paratemeter $$\theta$$ availabe beforehand, and before making any additional observations. It account for everything you believed about the parameter $$\theta$$ before observing the data. In practise choose prior that is computational convinient.

* The **likelihood** $$P(\mathcal{D}\mid \theta)$$ which is the probability of data given the parameter like in maximum likelihood.

With this two distributions, we can compute the posterior distribution and the posterior predictive distribution. The posterior distribution $$P(\theta \mid \mathcal{D})$$ which correspond to uncertainty about $$\theta$$ after observing the data given by:

$$
\begin{aligned}
P(\theta  \mid  \mathcal{D}) &= \frac{P(\theta)p(\mathcal{D}  \mid  \theta)}{P(\mathcal{D})} &= \frac{P(\theta)P(\mathcal{D} \mid  \theta)}{ \displaystyle \int P(\theta ^ {\prime} ) P(\mathcal{D} \mid  \theta ^{\prime})}
\end{aligned} 
$$

The denominator is usually considered as a normalizing constant and thus the posterior distribution become:

$$
P(\theta  \mid  \mathcal{D}) \propto P(\theta)P(\mathcal{D}  \mid \theta)
$$

On the other hand the posterior predictive distribution $$P(\mathcal{D}^{\prime}\mid)\mathcal{D}$$ is the distribution of future observation given past observation defined by:

$$
P(\mathcal{D}^{\prime} \mid \mathcal{D} )= \int P(\theta\mid \mathcal{D}) P(\mathcal{D}^{\prime} \mid \theta)
$$

Generaly the Bayesian approach to parameter estimation works as follows: 

1. First we need to formulate our knowledge about a situation by defining a distribution model which expresses qualitative aspects of our knowledge about the situation and then specify a prior probability distribution which expresses our subjective
beliefs and subjective uncertainty about the unknown parameters, before seeing the data.
2. Gather data
3. Obtain posterior knowledge that updates our beliefs by computing the posterior probability distribution which estimates the unknown
parameters. 

Let apply the bayesian estimation to the coin example in which we have specified the likelihood equal to $$\theta^{N_H}(1-\theta)^{N_T}$$. We only required to specify the prior in which several approches can be used. One of the approach is relay upon lifetime experince of flipping coins in which most coins tend to be fair which implies $$p(\theta) = 0.5$$. We can also use various distribution to specify prior density but in practise a most useful distribution is the **beta distribution** parameterized by $$a , b > 0$$ and defined as:

$$
p(\theta; a, b) = \frac{\Gamma (a + b)}{\Gamma(a) \Gamma (b)} \theta ^{a-1}(1-\theta ^{b - 1})
$$

From the above eqution it is clear that the first term (with all $\Gamma$)is just a normalizing constant and thus we can rewrite the beta distribution as:

$$
p(\theta; a, b) \propto \theta ^{a-1}(1-\theta) ^{b - 1}
$$

Note the beta distribution has the following properties

* It is centered around $$\frac{a}{a + b}$$ and it can be shown that if $$\theta \sim \text{Beta}(a,b)$$ then $$\mathbb{E}(\theta)=\frac{a}{a + b}$$.
* It becomes more peaked for larger values of $$a$$ and $$b$$
* It become normal distribution when $$a = b = 1$$

Now let compute the posterior and posterior predictive distribution

$$
\begin{aligned}
p(\theta | \mathcal{D}) & \propto p(\theta)p(\mathcal{D} |\theta) \\
& \propto \theta^{N_H}(1-\theta)^{N_T}\theta ^{a-1}(1-\theta) ^{b - 1} \\
& = \theta ^{a-1+N_H}(1-\theta) ^{b - 1 + N_T}
\end{aligned}
$$