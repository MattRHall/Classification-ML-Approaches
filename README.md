## Supervised Tasks
In supervised tasks models are created to establish a relationship between a number of independent variables (often called features), and a dependent variable. If the dependent variable is continuous, then it is defines a regression problem. If the dependent variable is categorical, then it is defined as a classification problem.

## Purpose
The purpose is to provide a brief demonstration of common machine learning models. The purpose is not on complex feature engineering, data preprocessing, or hyperparameter tuning. To that end a very simple data set was chosen, and models are only lightly tuned.

## 1_Decision_Tree
**Approach**: A decision tree recursively divides up the feature space. The algorithm chooses to split a feature at a certain threshold by calculating an 'impurity score' for every possible split for each feature. The split is chosen that creates the most 'information gain' (i.e. does the best job at splitting the classes). In this case we set a maximum depth of 5 which indicates a maximum of 5 splits (this is a hyperparameter to be tuned).

**Advantages/Disadvantages**: Decision trees are good at learning non-linear relationships, are relatively inexpensive to compute and easy to understand. It tends to be pretty accurate, and works well with simple datasets. Depending on the hyperparameters it is easy to overfit a decision tree so pruning techniques might be needed. Another drawback, is decision trees don't work well in high dimension / sparse spaces, which makes it difficult to divide up the feature space. Furthermore, as shown graphically below, the decision boundary is restricted to being parallel to attribute axes.

## 2_Linear_Kernel_SVC
**Approach**: SVC finds the hyperplane (division in the feature space) that creates the biggest *margin* between the training points for the different classes. The margin effectively forms a band each side of the hyperplane. Incorrectly classified data points near the margin contribute to errors, which SVC tries to minimize. This forms a constrained optimisation problem, where the SVC is trying to make the margin as large as possible, whilst minimizing the errors from misclassified points. The optimisation problem is a and is solved using the Lagrange function.

**Advantages/disadvantages**: SVC is a convex optimisation problem, which means we can be sure a global solution is found, and there are well established methods to find it. It is accurate and can handle very many, or very few features (even where no. of features > no. samples). In addition, SVM only focuses on the 'margin', i.e. the interesting data points around the hyperplane (it focuses on the hard to classify data). Disadvantages include over-fitting (although regularisation parameters exist) and potentially slow computation speeds.

**Kernels**: If a dataset does not demonstrate a linear relationship, we can map this data to a higher dimension feature space, and then apply LinearSVC in that feature space. The idea is that after transforming our dataset to a higher dimension, the classes might not be linearly separable. It is easier to demonstrate this visually. As shown below data points which are inseparable in a lower dimension become separable in a higher dimension. This can be very computationally expensive (mapping data up and down dimensions). However, Kernels can provide a nice shortcut... they allows us to calculate the LinearSVC in a higher dimension without actually transforming the data.

## 3_K_Nearest_Neighbors
**Approach**: KNN makes predictions by identifying the closest 'K' data points to a query point. 'Distance' is calculated in order to find the closest data points. Typically this is 'euclidean'. 'K' is a hyperparameter to be tuned. Low values of 'K' create very flexible models (with high variance) and high values of 'K' create stable / robust models (with high bias).

**Advantages/disadvantages**: KNN is very good at learning non-linear / complex functions as all that is considered is the local area around a query point. This makes it a poor classifier for sparse / high dimensional feature space. The main draw back is all computation is reserved until a query is made (no function is learnt). Computations can also become quite large because many distances need to be calculated before the closest neigbours can be found.

## 4_Logistic_Regression
**Approach**: Logistic regression is used to predicted outcomes which fall into discrete categories. It is similar to linear regression, but involves fitting the data against an 'S' shaped logistic function. This 'S' curve is bounded by 0 and 1, and represents the probability of a prediction falling into one class vs. another class. 

**Advantages/disadvantages**: Logistic regression is much more suitable than linear regression for discrete classification problems (it can be used for multiple classes, the coefficients are easy to understand, won't get predictions outside of 0 or 1). Logistic regression does not work well for non-linear relationships, if the variables are highly correlated, or if there is a lot of noise of data (all of these apply to linear regression also).

## 5_Gaussian_Naive_Bayes
**Approach**: Bayes classification is based around Bayes theory. In classification problems the probability of a data point 'd' being in class 'c' is a function of the the probability of generating 'd' given 'c' and the probability of occurance of class 'c'. GaussianNB assumes that the underlying features are normally distributed, and conditionally independent. At prediction time, the closer a data point is to the mean of the features for a specific class, the more likely it belongs to that class.

**Advantages/disadvantages**: Bayes approaches are simple and powerful. They perform very well with multiple classes and high dimensions. They don't rely on complex algorithms to solve, and computations increase linearly. In my experience it often performs as well as much more complex classification models. There are no hyperparameters that need adjusting which need tuning. However, the underlying assumptions are often not satisfied (especially conditionally independence), and the quality of input data needs to be good (given no hyperparameters to tune).

## 6_Random_Forrest
**Approach**: Random Forrest involves create multiple decision trees, and selecting the most common predictions from each tree. It is called 'random' because each tree is built around a sample of data with replacement, and at each node a limited number of features are randomly selected as potential splits. The general principle is to build a large number of small trees, which are likely over-fitted, but given the trees are built on different data, the errors are relatively independent and therefore will cancel out. This is referred to as an *ensemble* method.

**Advantages/Disadvantages**: The advantages are the same as a decision tree (highly flexible model, limited preprocessing, very little assumptions), however we have reduced variance, reduced noise, and reduced the chance of over-fitting (whilst keeping bias the same). The disadvantages are that random forrests can still overfit data, the model becomes less interpretable, and it can be computationally intensive.




























