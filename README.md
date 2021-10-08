## Supervised Tasks
In supervised tasks models are created to establish a relationship between a number of independent variables (often called features), and a dependent variable. If the dependent variable is continuous, then it is defines a regression problem. If the dependent variable is categorical, then it is defines as a classification problem.

## Purpose
The purpose is to provide a brief demonstration of common machine learning models. The purpose is not on complex feature engineering, data preprocessing, or hyperparameter tuning. To that end a very simple data set was chosen, and models are only lightly tuned.

## 1_Decision_Tree (classification / regression)
**Approach**: A decision tree recursively divides up the feature space. The algorithm chooses to split a feature at a certain threshold by calculating an 'impurity score' for every possible split for each feature. The split is chosen that creates the most 'information gain' (i.e. does the best job at splitting the classes). In this case we set a maximum depth of 5 which indicates a maximum of 5 splits (this is a hyperparameter to be tuned).

**Advantages/Disadvantages**: Decision trees are good at learning non-linear relationships, are relatively inexpensive to compute and easy to understand. It tends to be pretty accurate, and works well with simple datasets. Depending on the hyperparameters it is easy to overfit a decision tree so pruning techniques might be needed. Another drawback, is decision trees don't work well in high dimension / sparse spaces, which makes it difficult to divide up the feature space. Furthermore, as shown graphically below, the decision boundary is restricted to being parallel to attribute axes.

## 2_Linear_Kernel_SVC (classification / regression)
**Approach**: SVC finds the hyperplane (division in the feature space) that creates the biggest *margin* between the training points for the different classes. The margin effectively forms a band each side of the hyperplane. Incorrectly classified data points near the margin contribute to errors, which SVC tries to minimize. This forms a constrained optimisation problem, where the SVC is trying to make the margin as large as possible, whilst minimizing the errors from misclassified points. The optimisation problem is a and is solved using the Lagrange function.

**Advantages/disadvantages**: SVC is a convex optimisation problem, which means we can be sure a global solution is found, and there are well established methods to find it. It is accurate and can handle very many, or very few features (even where no. of features > no. samples). In addition, SVM only focuses on the 'margin', i.e. the interesting data points around the hyperplane (it focuses on the hard to classify data). Disadvantages include over-fitting (although regularisation parameters exist) and potentially slow computation speeds.

**Kernels**: If a dataset does not demonstrate a linear relationship, we can map this data to a higher dimension feature space, and then apply LinearSVC in that feature space. The idea is that after transforming our dataset to a higher dimension, the classes might not be linearly separable. It is easier to demonstrate this visually. As shown below data points which are inseparable in a lower dimension become separable in a higher dimension. This can be very computationally expensive (mapping data up and down dimensions). However, Kernels can provide a nice shortcut... they allows us to calculate the LinearSVC in a higher dimension without actually transforming the data.

## 3_K_Nearest_Neighbors (classification)
**Approach**: KNN makes predictions by identifying the closest 'K' data points to a query point. 'Distance' is calculated in order to find the closest data points. Typically this is 'euclidean'. 'K' is a hyperparameter to be tuned. Low values of 'K' create very flexible models (with high variance) and high values of 'K' create stable / robust models (with high bias).

**Advantages/disadvantages**: KNN is very good at learning non-linear / complex functions as all that is considered is the local area around a query point. This makes it a poor classifier for sparse / high dimensional feature space. The main draw back is all computation is reserved until a query is made (no function is learnt). Computations can also become quite large because many distances need to be calculated before the closest neigbours can be found.

## 4_Logistic_Regression (classification / regression)
**Approach**: Logistic regression is used to predicted outcomes which fall into discrete categories. It is similar to linear regression, but involves fitting the data against an 'S' shaped logistic function. This 'S' curve is bounded by 0 and 1, and represents the probability of a prediction falling into one class vs. another class. 

**Advantages/disadvantages**: Logistic regression is much more suitable than linear regression for discrete classification problems (it can be used for multiple classes, the coefficients are easy to understand, won't get predictions outside of 0 or 1). Logistic regression does not work well for non-linear relationships, if the variables are highly correlated, or if there is a lot of noise of data (all of these apply to linear regression also).

## 5_Gaussian_Naive_Bayes (classification)
**Approach**: Bayes classification is based around Bayes theory. In classification problems the probability of a data point 'd' being in class 'c' is a function of the the probability of generating 'd' given 'c' and the probability of occurance of class 'c'. GaussianNB assumes that the underlying features are normally distributed, and conditionally independent. At prediction time, the closer a data point is to the mean of the features for a specific class, the more likely it belongs to that class.

**Advantages/disadvantages**: Bayes approaches are simple and powerful. They perform very well with multiple classes and high dimensions. They don't rely on complex algorithms to solve, and computations increase linearly. In my experience it often performs as well as much more complex classification models. There are no hyperparameters that need adjusting which need tuning. However, the underlying assumptions are often not satisfied (especially conditionally independence), and the quality of input data needs to be good (given no hyperparameters to tune).

## 6_Random_Forrest (classification / regression)
**Approach**: Random Forrest involves create multiple decision trees, and selecting the most common predictions from each tree. It is called 'random' because each tree is built around a sample of data with replacement, and at each node a limited number of features are randomly selected as potential splits. The general principle is to build a large number of small trees, which are likely over-fitted, but given the trees are built on different data, the errors are relatively independent and therefore will cancel out. This is referred to as an *ensemble* method.

**Advantages/Disadvantages**: The advantages are the same as a decision tree (highly flexible model, limited preprocessing, very little assumptions), however we have reduced variance, reduced noise, and reduced the chance of over-fitting (whilst keeping bias the same). The disadvantages are that random forrests can still overfit data, the model becomes less interpretable, and it can be computationally intensive.

## 7_Gradient_Boost (classification / regression)
**Approach**: Gradient Boosting is a *boosting* approach which builds a series of 'weak learners', with each weak learner trying to improve upon the previous mistakes. A loss function is used to create decision trees that minimize the errors generated from the previous weak learner. In gradient descent algorithms a loss function is minimized by taking steps in an appropriate direction. The same process is being applied here, we start off with a poor model with generates very high errors, and we keep building additional models to reduce these errors. Predictions are made by aggregating all these models together.

**Advantages/Disadvantages**: Decision trees are commonly use as the 'weak learners'. Decision trees are simple to build, are very flexible, and robust to outliers / different scales. Gradient Boosting often achieves good results, as successive models build on weakness of previous ones. Furthermore, combining lots of weak learners helps to reduce variance / overfitting.

## 8_Ada_Boost (classification / regression)
**Approach**: Ada Boost also builds a series of weak learners, with each weak learner trying to improve upon previous mistakes. Each data point is given a weight, with the misclassified data points given higher weights, and correctly classified data points given lower weights. The data points and weights are then used to build new weak learners. The weak learners are aggregated when a prediction needs to be made. Decision trees (or decision stumps) are commonly used as weak learners.

**Advantages/Disadvantages**: The advantages similar to decision trees (highly flexible model, limited preprocessing, very little assumptions), however we have reduced variance, reduced noise, and reduced the chance of over-fitting (whilst keeping bias the same). It is easy to implement, works well with a wide range of classifiers, and no parameters to adjust. Ada Boost is sensitive to noise and outliers because it works hard to correctly classify misclassified data points.

## 9_XGBoost (classification / regression)
**Approach**: XGBoost improves upon other boosting methods by adding regularization / pruning techniques. It is effectively a regularised form of gradient boosting, but with software engineering enhancements that meaningfully improve computation time. XGboost uses decisions trees as 'weak learners'. When constructing decision trees, splits are pruned if the 'gain in information' is below a threshold. The threshold, and the gain are regularization hyperparameters which can be specified in order to control the size of decision trees. The errors (residuals) from a weak leaner are used by the next weak leaner to improve the classifier.

**Advantages/Disadvantages**: The advantages are the same as gradient boost but XGBoost has the added advantage of enchanced regularization. System optimizations include parallelization, and algorithm choices that make efficient use of resources. 

## 10_Linear_Regression (Regression)
**Approach**: Multiple linear regression attempts to explain the relationship between dependent variables and two or more independent variables with a linear relationship. The coefficients for each independent variable indicate how much variability in that feature influence variability in the dependent variable. We can test whether these coefficients are significantly different from 0, if it is not, then we can remove it without a significant impact on the models predictive ability. We can use the coefficient of determination to look how well the model explains variation in the dependent variable.

**Advantages/Disadvantages**: Linear regression is straight forward to compute, and easy to understand. Features can be pruned if their coefficients are not significant. The disadvantages are based around the assumptions it makes around the underlying data (linearity, random sampling, no perfect multicollinearity, normality) and the residuals (constant variance, no autocorrelation).

## 9_Lasso_Regression (Regression)
**Approach**: Linear regression without regularization uses ordinary least squared (OLS), which is the squared sum of the residuals (actual values - predicted) as its cost to minimize. Lasso regression adds an extra penalty; the sum of the absolute values of the parameters. The optimisation processes tries to improve the predictive ability of the model, whilst also trying to keep coefficients as low as possible. A penalty parameter can be tuned to change how much high coefficients are penalized.

**Advantages/Disadvantages**: One feature of Lasso regression is that it has the ability to force coefficients towards 0. This means the Lasso regression performs feature selection which can be useful. The ability to tune the sensitivity to the regularization parameter means regualarization can be controlled. Lasso regression has the same advantages as linear regression (simplicity, understandability, complexity), and the same disadvantages (lots of assumptions).



















