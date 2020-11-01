# The p-value

You should now really have a good handle on these hypothesis tests.  Furthermore, now that we have introduced the following statistic in the previous task:

![](https://render.githubusercontent.com/render/math?math=T=\frac{1}{\sigma\sqrt{n}}\sum_{i=1}^{n}(X_i-\mu_0))

we have ensured that for the tests on sample means we have been doing thus far and under the assumption of the null hypothesis, the __statistic__, T, is always a sample from a standard normal distribution.  When we employ the flowchart below, we can thus always use the same distribution for the statistic under the assumption of the __null hypothesis__:

![](hypo-testing.001.jpeg)

Let's suppose that we were sharing the results of our statistical analysis with some stakeholder.  Lets further suppose that our stakeholder is going to decide something based on our analysis.  Using what we have learned thus far we might tell them that the data suggests that the null-hypothesis can be rejected at the 5% significance level or not.  They may, however, be uncomfortable with this level of risk when it comes to the decision that they have to make.  They may, for instance, feel that we have been too conservative (we have set the significance level for our test too small) or they may feel that we have not been conservative enough (we have set the significance level for our test to be too large).  We may, therefore, be sent back to do all our analysis again.  

For these reasons we are, from here onwards, going to discard the flow chart above.  We will instead perform hypothesis tests using the flow chart below:

![](hypo-testing.003.jpeg)

the difference between this new flowchart and the previous one is that we are no longer determining the size of the __critical region__.  We instead compute the __p-value__ from the probability distribution that is assumed under the __null hypothesis__, the value of the __statistic__ and the __alternative hypothesis__.  This __p-value__ gives the maximum probability that the __null hypothesis__ is true given the value of the __statistic__.  We calculate the __p-value__ by setting the boundary of the __critical region__ to value of the __statistic__ and by calculating the total probability that a resample falls from the distribution that is sampled under the __null hypothesis__ would fall within this __critical region__.  

This idea is not as hard to understood if we consider an example.  __You are thus going to write code to perform a very simple hypothesis test__.  The null and alternative hypotheses are:

1. __null hypothesis__: sample is a normal random variable with expectation 0 and variance 1.
2. __alternative hypothesis__: sample is a normal random variable with an expectation that is less than 0

__To complete the exercise you will need to complete the function called `pvalue`__. This function takes the value of the statistic (`data`) in input.  It should return the probability that the __null hypothesis__ is true and the __alternative hypothesis__ is false given the value of the statistic.  For this particular __alternative hypothesis__ this is the probability that a sample from the distribution that is assumed under the __null hypothesis__ is less than or equal to the value of the __statistic__.  

Remember we can calculate the value of the cumulative probability distribution, `px`, for a standard normal distribution at x using:

````
px = scipy.stats.norm.cdf(x)
````
