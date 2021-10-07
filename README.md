## Classification Tasks
regergr

## Purpose
ergerger

## 1_Decision_Tree
**Preprocessing**: The dataset is split 75% training, and 25% test. There is no need to standardize or normalize the data because a decision tree is unaffected by the sizes of different features. There are no outliers, but if they were there would be limited advantage in removing them.

**Approach**: A decision tree recursively divides up the feature space. The algorithm chooses to split a feature at a certain threshold by calculating an 'impurity score' for every possible split for each feature. The split is chosen that creates the most 'information gain' (i.e. does the best job at splitting the classes). In this case we set a maximum depth of 5 which indicates a maximum of 5 splits (this is a hyperparameter to be tuned).

**Advantages/Disadvantages**: Decision trees are good at learning non-linear relationships, are relatively inexpensive to compute and easy to understand. It tends to be pretty accurate, and works well with simple datasets. Depending on the hyperparameters it is easy to overfit a decision tree so pruning techniques might be needed. Another drawback, is decision trees don't work well in high dimension / sparse spaces, which makes it difficult to divide up the feature space. Furthermore, as shown graphically below, the decision boundary is restricted to being parallel to attribute axes.

**Results**: Accuracy of 94% was achieved. As mentioned above, decision trees are easy to understand and each split can be shown below. It was interesting to see the first split (most informative) was 'age' = 44.5. As initially observed, older people appear more likely to buy SUV's. The decision tree boundary is shown graphically below (notice the boundary line is parallel to the axis).

## 2_Linear_Kernel_SVC
**Preprocessing**: The dataset is split 75% training, and 25% test. Data is standardized so varying scales don't impact the algorithm or the the optimisation process.

**Approach**: SVC finds the hyperplane (division in the feature space) that creates the biggest *margin* between the training points for the different classes. The margin effectively forms a band each side of the hyperplane. Incorrectly classified data points near the margin contribute to errors, which SVC tries to minimize. This forms a constrained optimisation problem, where the SVC is trying to make the margin as large as possible, whilst minimizing the errors from misclassified points. The optimisation problem is a and is solved using the Lagrange function.

**Advantages/disadvantages**: SVC is a convex optimisation problem, which means we can be sure a global solution is found, and there are well established methods to find it. It is accurate and can handle very many, or very few features (even where no. of features > no. samples). In addition, SVM only focuses on the 'margin', i.e. the interesting data points around the hyperplane (it focuses on the hard to classify data). Disadvantages include over-fitting (although regularisation parameters exist) and potentially slow computation speeds.

**Results (Linear)**: The accuracy achieved is 90%, with noticeably a lot of false positives. LinearSVC is as the name suggests... Linear, which means any non-linear relationships can't be represented. You can see the hyperplane (in this case a straight line) in the image below.

**Kernels**: If a dataset does not demonstrate a linear relationship, we can map this data to a higher dimension feature space, and then apply LinearSVC in that feature space. The idea is that after transforming our dataset to a higher dimension, the classes might not be linearly separable. It is easier to demonstrate this visually. As shown below data points which are inseparable in a lower dimension become separable in a higher dimension. This can be very computationally expensive (mapping data up and down dimensions). However, Kernels can provide a nice shortcut... they allows us to calculate the LinearSVC in a higher dimension without actually transforming the data.

**Results (Kernel)**: As you can see the accuracy increases to 93%, and we have significantly less false positives. The hyperplane in the lower dimension is non-linear and does a much better job at describing the relationships in the data.

## 3_K_Nearest_Neighbors
**Preprocessing**: The dataset is imbalanced. This can be problematic for KNN as predictions are made on nearby datapoints. We make the dataset balanced by 'upsampling' the small class (people who don't buy SUV's) and 'downsampling' the large class (people who buy SUV's). This creates 200 observations for each class. We then split the data set into 75% training, and 25% test.

**Approach**: KNN makes predictions by identifying the closest 'K' data points to a query point. 'Distance' is calculated in order to find the closest data points. Typically this is 'euclidean'. 'K' is a hyperparameter to be tuned. Low values of 'K' create very flexible models (with high variance) and high values of 'K' create stable / robust models (with high bias).

**Advantages/disadvantages**: KNN is very good at learning non-linear / complex functions as all that is considered is the local area around a query point. This makes it a poor classifier for sparse / high dimensional feature space. The main draw back is all computation is reserved until a query is made (no function is learnt). Computations can also become quite large because many distances need to be calculated before the closest neigbours can be found.

**Results**: Accuracy of 89%. 'K' is a hyperparameter to be tuned. By using GridSearch() we find K=6 produces the highest accuracy. It achieves 94% on the test dataset.

## 4_Logistic_Regression
**Preprocessing**: Limited preprocessing was made. The dataset was standardized to remove the impact from varying scales. Although the class sizes were imbalanced this can be rectified with the 'class_weight' parameter in the classification algorithm. The dataset was split into 75% training and 25% test. 

**Approach**: Logistic regression is used to predicted outcomes which fall into discrete categories. It is similar to linear regression, but involves fitting the data against an 'S' shaped logistic function. This 'S' curve is bounded by 0 and 1, and represents the probability of a prediction falling into one class vs. another class. 

**Advantages/disadvantages**: Logistic regression is much more suitable than linear regression for discrete classification problems (it can be used for multiple classes, the coefficients are easy to understand, won't get predictions outside of 0 or 1). Logistic regression does not work well for non-linear relationships, if the variables are highly correlated, or if there is a lot of noise of data (all of these apply to linear regression also).

**Results**: The accuracy of the model is 89%. The coefficients indicate that 'age' is a more important indicator that 'salary' when it comes to predicting SUV purchases.






























