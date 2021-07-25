---
layout: post
title: Bayesian Variational Inference
subtitle: Bayesian Inference
subsubtitle: Principle of bayesian varitaional inference
date: 2020-01-20
description: The post introduce the basics principle of bayesian varitaional inference  as one of the approach used to approximate difficult probability distribution.
author: Anthony Faustine 
image: bayesvariational.jpg
---

Bayesian method offer a different paradigm for doing statistical analysis. It is practical method for making inferences from data using probability models. Unlike other statistical approach, bayesian models are easy to interpret and incorporate uncertainty. In bayesian method  we start with a belief which is also called a **prior**. We then update our belief after observing some data. The outcome is called a **posterior**. The process repeats as we keep on observing more data where the old *posterior* becomes a new *prior*. The  process employs the Bayes rule. 

Consider the Bayesian theorem, which allows us to use some knowledge or belief that we already have. Given data point $$\mathcal{D} = \{x \in \mathbb{R}^{N\times d}, y \in \mathbb{R}^{N\times c}\}$$. The Bayesian  approach  treat the latent variable or parameter $$z$$ as random variable with some prior distribution $$p(z)$$. This is the probability of parameters $$z$$ before hand.

$$
p(z | \mathcal{D}  ) = \frac{p(\mathcal{D} | z )\cdot p(z)}{p(\mathcal{D})}
$$

where 

$$
p(\mathcal{D}) = \int p(\mathcal{D} |z )\cdot p(z) dz
$$

From the bayesian theorem above,  $$z$$ is the hypothesis about the world, and $$\mathcal{D}$$ is the data or evidence. The probability $$p(\mathcal{D} \mid z)$$ is called  **likeli-hood**; the probability of data given the latent variable and $$p(\mathcal{D})$$ is the **marginal-likelihood** and $$p(z \mid \mathcal{D}  )$$ is the **posterior**.

### Bayesian Inference

Given data set $$\mathcal{D}$$ and latent variable $$z$$ that relate $$x$$ and $$y$$ such that:
$$
y = f_{z}(x:z)
$$
The first step in bayesian inference is to identify the parameter $$z$$ and express our lack of knowledge  about this parameter in term of probability distribution $$p(z)$$. This is the prior knowledge about the parameter $$z$$. After that we express a *likelihood*  $$p(\mathcal{D} \mid z)$$ which tell us how the data $$\mathcal{D}$$ interact with  parameter $$z$$. Together the prior and the likelihood make our model (generative model). It tell us how we can simulate from our data.

In **training** stage we apply Bayesian theorem to get posterior distribution:

$$
p(z|\mathcal{D}) = \frac{p(\mathcal{D}|, z)}{p(\mathcal{D})}
$$ 

In testing stage we find **predictive-distribution**

$$
p(\hat{y}| x, \mathcal{D}) = \int p(\hat{y} | x, z)\cdot p(z | x, y) dz
$$

Theoretically this is how bayesian inference work, however the big challenge is how to compute the posterior distribution. The integral $$\int p(\mathcal{D} \mid z )\cdot p(z) dz$$ is usually intractable. Therefore we need to approximate this integral. There several approach used for approximation. 

The first and simple approach is to use *analytical integration* which is only applicable with the use of [conjugate prior](https://en.wikipedia.org/wiki/Conjugate_prior) and thus possible only for very simple cases. However the approach does not scale well. Alternatively *[Gaussian (Laplace) approximation](https://metacademy.org/graphs/concepts/laplace_approximation)* can be applied where the posterior is  approximated  with Gaussian. This works well when there are lot of data. [Markov Chain Monte Carlo (MCMC)](https://metacademy.org/graphs/concepts/markov_chain_monte_carlo) are among other popular techniques used for approximating the integral. The method is applicable to wide variety of problems however is very slow. The popular and recently widely used approach for approximating prior in bayesian method is *Variational Inference*. This approach convert the integral into optimization problem and thus Work faster than MCMC. 

Before we dive into varitiaonl infrence let us revisit one example of bayesian inference in regression problem. Given data point $$X = \{x_1,\ldots x_N \}$$ and corresponding target $$Y = \{y_1,\ldots y_N \}$$. Linear regression assume that data is generated from the following model: 

$$y= f_{\theta}(x: \theta) + \in
$$
 where $$\in$$ is the noise due to measurement and 
$$f_{\theta}(X: \theta)$$ is the hypothesis function given;

$$ 
f_{\theta}(X: \theta) = b + \sum_{i=1}^N w_i \phi (x_i) = \theta^T\cdot \phi(X)
$$

where $$\phi(X)$$ is the basis function and $$\theta$$ is the model parameters such that 
$$
\theta_{0} =b$$  and $$\phi_0=1
$$ 

The  output of this model is the single point estimate for the best model parameter. The Bayesian modelling approach to this problem offer a systematic framework for learning distribution over values of the parameters and not a single estimate. The bayesian linear regression model $$y= f_{\theta}(x: \theta) + \in
$$ as a Gaussian  distribution such that:

$$
p(y|x, \theta) = \mathcal{N}(y|f_{\theta}(x: \theta), \beta^{-1})
$$

Assuming the data point are drawn independently and identically distributed the likelihood is expressed as:

$$
p(Y| X, \theta) = \prod_{i=1}^N \mathcal{N}(y_i|f_{\theta}(x_i: \theta_i), \beta^{-1})
$$

Let choose a prior that is conjugate to the likelihood 

$$
p(\theta|X) = \mathcal{N}(\theta|0, \alpha^{-1})
$$

Thus the posterior is given as:

$$
p(\theta|Y, X) \propto \mathcal{N}(\theta|0, \alpha^{-1})\cdot \prod_{i=1}^N \mathcal{N}(y_i|f_{\theta}(x_i: \theta_i), \beta^{-1})
$$


## Variational Inference (VI)

In the previous section we show that inference in probabilist model is often intractable and introduced several approach used to approximate the inference. Variational Inference (VI) is one of the approach used to approximate difficult probability distribution by turning the calculation about model into optimization. 

Consider a probabilistic model which is joint distribution $$p(x,z)$$ of the latent variable  $$z$$ observed variables $$x$$. To draw inference on the latent variable $$z$$ we compute the posterior

$$
p(z|x) = \frac{p(x,z)}{p(x)} = \frac{p(x|z)\cdot p(z)}{p(x)}
$$

where 

$$
p(x)=\int p(x|z)\cdot p(z) dz
$$

To approximate $$p(z\mid x)$$ we first choose an approximating family of distribution $$q(z)$$ over latent variable  $$z$$. Then we find set of parameters that makes $$q(z)$$ close to posterior distribution $$p(z\mid {\bf x})$$. Thus VI approximate $$p(z\mid x)$$ with new distribution $$q(z)$$ such that $$q(z)$$ is close to $$p(z\mid x)$$. To achieve this we minimize KL divergence between $$q(z)$$ and $$p(z\mid x)$$ such that:

$$
q^*(z) = \arg \min D_{KL}(q(z)||p(z|x))
$$

where 

$$
D_{KL}(q(z)||p(z|x)) = \int q(z)\log \frac{q(z)}{p(z|x)}
$$

It clear that we can not minimize KL divergence since it is directly depend on posterior $$p(z\mid x)$$. However we can minimize a function that is equal to KL divergence plus constant. This function is called **Evidence Lower Bound**(ELBO) $$\mathcal{L}_{VI}(q)$$.

### Evidence Lower Bound (ELBO)

To derive the ELBO we first consider the [Jensen's inequality](https://en.wikipedia.org/wiki/Jensen%27s_inequality) which relates the value of a convex function of an integral to the integral of the convex function such that $$f(\mathbb{E}[x]) \geq \mathbb{E}[f(x)]$$ where $$f(.)$$ is the concave function. Since logarithmic are strictly concave function it is clear that

$$
\log \int p(x)g(x) dx \geq \int p(x)\log g(x)
$$

Let us consider a log of marginal evidence.

$$
\begin{aligned} 
\log p(x) & = \log \int_z p(x,z) dz\\
          & =\log \int_z p(x,z)\cdot \frac{q(z)}{q(z)} dz \\
          & =\log \int_z q(z)\frac{p(x,z)}{q(z)} dz\\
          & =\log \left(\mathbb{E}_q[\frac{p(x,z)}{q(z)}] \right)\\
          &\geq \mathbb{E}_q[ \log p(x,z)] - \mathbb{E}_q[\log q(z)]
\end{aligned}
$$

The final line is the ELBO which is the lower bound for the evidence. Thus the evidence lower bound for probability model $$p(x,z)$$ and approximation $$q(z)$$ to the posterior is

$$
\mathcal{L}_{VI}(q) = \mathbb{E}_q[ \log p(x,z)] - \mathbb{E}_q[\log q(z)]
$$

We can now show that KL divergence to the posterior is equal to the negative ELBO plus constant.

$$
\begin{aligned} 
D_{KL}(q(z)||p(z|x)) &= \int q(z)\log \frac{q(z)}{p(z|x)}\\
                     &= \mathbb{E}_q[\log q(z)] - \mathbb{E}_q[\log p(x,z)] + \mathbb{E}_q[\log p(x)]\\
                     &=-\left(\mathbb{E}_q[\log p(x,z)] - \mathbb{E}_q[\log q(z)] \right) +\log p(x)\\
                     &= -\mathcal{L}_{VI}(q) +\log p(x)\\
\mathcal{L}_{VI}(q) &=\log p(x) + D_{KL}(q(z)||p(z|x))
\end{aligned}
$$

From the equation above it clear that minimizing the KL divergence is equivalent to maximizing the ELBO. Recall that we want to find $$q(z)$$ such that KL divergence is small, the variational objective function becomes

$$
q^*(z) = \arg \min D_{KL}(q(z)||p(z|x)) = \arg \max \mathcal{L}_{VI}(q)
$$



### Mean Field Variational Inference

One of the important question on VI, is how to construct the family of variational distributions from which we want to draw $$q(z)$$ from. The simplest family is where each latent parameter $$z_i$$ has its own
independent distribution. This means that we can easily factorize the variational distributions into groups:

$$
q(z_1, \ldots, z_m) = \prod_{i=1}^m q(z_i)
$$

This family of distribuion are known as Mean-Field Variational Family that make use of [mean field theory](https://en.wikipedia.org/wiki/Mean_field_theory). Inference using this factorization is known as Mean-Field Variational Inference (MFVI). 

It possible to further parameterize the approximating distributions $$q(z)$$ with variational parameters $$\lambda$$ such that the approximating distribution become $$ q(z_i ; \lambda_i)$$. For example if we set our family of approximating distributions as a set of
independent gauasian distributions $$\mathcal{N}(\mu_i, \sigma^2_i)$$ and parameterize this distributions with the mean and variance where $$\lambda_i = (\mu_i, \sigma^2_i)$$ is the set of variational parameters.

The common algorithms used in practise to do VI under mean filed assumptions are coordinate ascent optimization (CAVI) and stochastic gradient based method. 

### Coordinate Ascent Variational Inference (CAVI)

The CAVI algorithm derive variational updates by hand and perform coordinate ascent (iteratively updating each latent variable $$z_i$$ ) on the latent until convergence of the ELBO. A common procedure to conduct CAVI is:

- Choose variational distributions $$q(z)$$
- Compute ELBO;
- Optimize individual $$q(z_i)$$ ’s by taking the gradient for each latent variable;
- Repeat until ELBO converges.

The coordinate ascent update for a latent variable can be derived by maximizing the ELBO function above. First, recall ELBO

$$
\mathcal{L}_{VI}(q) = \mathbb{E}_q[ \log p(x,z)] - \mathbb{E}_q[\log q(z)]
$$ 

Using chain rule we can decomopse the joint  $$p(x,z)$$ as;

$$
p(x_{1:n}, z_{1:m}) = p(x_{1:n}) \prod_{i=1}^m p(z_i|z_{1:(i-1)}, x_{1:n})
$$

Using mean field approximation, we can decompose the entropy term of the ELBO as

$$
\mathbb{E}_q[\log q(z)] = \sum_{i=1}^m \mathbb{E}_q[\log q(z_i)]
$$

Under the above assumption the ELBO become:

$$
\mathcal{L}_{ELBO}(q) = \log p(x_{1:n}) + \sum_{i=1}^m \mathbb{E}_q[\log p(z_i|z_{1:(i-1)}, x_{1:n}) ] - \mathbb{E}_q[\log q(z_i)
$$


To find this $$\arg \max_{q(z_i)} \mathcal{L}_{ELBO}(q)$$ we take derivative of ELBO with respect to $$q(z_i)$$ using Lagrange multipliers and set the derivative to zero. It can be shown that the coordinate ascent update rule is equal to 

$$
q^*(z_i) \propto \{  \mathbb{E}_{q-i}[\log q(z_i,z_{\neg},x)]\}
$$

where the notation $$\neg$$ denotes all indices other than the $$i^{th}$$

Despite being very fast  method for some models  only  work with  conditionally conjugate models. 

### Reference

1. [ICML 2018 tutorial](http://www.tamarabroderick.com/tutorial_2018_icml.html):Variational Bayes and Beyond: Bayesian Inference for Big Data.
2. [Shakir Mohamed](https://www.shakirm.com/papers/VITutorial.pdf):Variational Inference  for Machine Learning. 
3. [DS3 workshop](https://emtiyaz.github.io/teaching/ds3_2018/ds3.html):Approximate Bayesian Inference: Old and New.
4. [Variational Inference and Deep Generative Models](https://github.com/philschulz/VITutorial):Variational Inference for NLP audiences
