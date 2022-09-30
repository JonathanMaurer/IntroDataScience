# Databricks notebook source
# MAGIC %md
# MAGIC ## One-class SVM 
# MAGIC 
# MAGIC One-class SVM is abbreviation of one-class support vector machines. It is an unsupervised algorithm that learns a decision function for novelty detection: classifying new data as similar or different to the training set (sklearn documentation). It basically means that this algorithm is trained only on the ‘normal’ data. It learns the boundaries of these normal points and is therefore able to classify any points that lie outside the boundary as, which in another name, outliers.
# MAGIC 
# MAGIC You can take a look at the parameters of the model down below, for more information regarding the model, please check out the [OneClassSVM documentation](
# MAGIC https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM
# MAGIC ):

# COMMAND ----------

# MAGIC %md
# MAGIC class sklearn.svm.OneClassSVM(*, kernel='rbf', degree=3, gamma='scale', coef0=0.0, tol=0.001, nu=0.5, shrinking=True, cache_size=200, verbose=False, max_iter=-1

# COMMAND ----------

# MAGIC %md
# MAGIC #### Explanation of important parameters:
# MAGIC 
# MAGIC - `kernel`: specifies the kernel type to be used in the algorithm.
# MAGIC - `nu` :the proportion of outliers you expect to observe 
# MAGIC - `gamma`: determines the smoothing of the contour lines.

# COMMAND ----------

# MAGIC %md
# MAGIC ### One-class SVM Exercises
# MAGIC 
# MAGIC First we will import OneClassSVM from sklearn.svm, make_blobs, numpy, and matplotlib.pyplot

# COMMAND ----------

from sklearn.svm import OneClassSVM
from sklearn.datasets import make_blobs
import numpy as np  # You will use np.quantile, np.where and np.random
import matplotlib.pyplot as plt

# COMMAND ----------

# MAGIC %md
# MAGIC We have created a random sample dataset below by using the `make_blobs()` function.

# COMMAND ----------

np.random.seed(13)
x, _ = make_blobs(n_samples=200, centers=1, cluster_std=.3, center_box=(8, 8))

plt.scatter(x[:,0], x[:,1])
plt.show()


# COMMAND ----------

# MAGIC %md
# MAGIC **TO DO:** We will use the rbf kernel type for our model, please set the kernel type to rbf, which stands for [`radial basis function`](https://en.wikipedia.org/wiki/Radial_basis_function_kernel)

# COMMAND ----------

# Task

svm = OneClassSVM(kernel='rbf', gamma=0.001, nu=0.03)
print(svm)

# COMMAND ----------

# MAGIC %md
# MAGIC **TO DO:** Please fit the model with the dataset `x` that we created at the beginning and get the prediction data by using the fit() and predict() method.

# COMMAND ----------

# Task

svm.fit(x)
pred = svm.predict(x)

# COMMAND ----------

# MAGIC %md
# MAGIC **TO DO:** If everything is done correctly before, please extract the negative outputs (where the prediction of the data is equal to -1) as the outliers.

# COMMAND ----------

# Task

anom_index = np.where(pred == -1)
values = x[anom_index]

# COMMAND ----------

# MAGIC %md
# MAGIC Now we will visualize what we have done by using plt.

# COMMAND ----------

plt.scatter(x[:,0], x[:,1])
plt.scatter(values[:,0], values[:,1], color='r')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Local Outlier Factor
# MAGIC 
# MAGIC The Local Outlier Factor (LOF) algorithm is an unsupervised anomaly detection method which computes the local density deviation of a given data point with respect to its neighbors. It considers as outliers the samples that have a substantially lower density than their neighbors. Note that when LOF is used for outlier detection it has no predict, decision_function and score_samples methods. 
# MAGIC 
# MAGIC Local Outlier Factor (LOF) is a score that describes how likely a certain data point is an outlier/anomaly.
# MAGIC 
# MAGIC - When LOF is around 1, it is most likely that the data point is normal.
# MAGIC - When LOF scores over 1, it is most likely that the data point is an outlier.
# MAGIC 
# MAGIC In general, the LOF of a point tells the density of this point compared to the density of its neighbors. If the density of a point is much smaller than the densities of its neighbors (LOF ≫1), the point is far from dense areas and, hence, an outlier.
# MAGIC 
# MAGIC #### Explanation of important parameters
# MAGIC - `n_neighbors`: the number of neighbors considered
# MAGIC     - it should be greater than the minimum number of samples a cluster has to contain, so that other samples can be local outliers relative to this cluster
# MAGIC     - and smaller than the maximum number of close by samples that can potentially be local outliers. 
# MAGIC     - In practice, such informations are generally not available, and taking n_neighbors=20 appears to work well in general.
# MAGIC - `contamination`: the amount of contamination of the data set, i.e. the proportion of outliers in the data set. When fitting this is used to define the threshold on the scores of the samples.
# MAGIC 
# MAGIC #### Explanation of attributes
# MAGIC - `negative_outlier_factor_`: the opposite LOF of the training samples. The higher, the more normal. Inliers tend to have a LOF score close to 1 (negative_outlier_factor_ close to -1), while outliers tend to have a larger LOF score. The local outlier factor (LOF) of a sample captures its supposed ‘degree of abnormality’. It is the average of the ratio of the local reachability density of a sample and those of its k-nearest neighbors.
# MAGIC - `n_neighbors_`:the actual number of neighbors used for kneighbors queries.
# MAGIC - `offset_`: offset used to obtain binary labels from the raw scores. Observations having a `negative_outlier_factor` smaller than `offset_` are detected as **abnormal**. 
# MAGIC 
# MAGIC See more information here: [LocalOutlierFactor Documentation](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html#:~:text=The%20Local%20Outlier%20Factor%20)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Local outlier factor exercises

# COMMAND ----------

# MAGIC %md
# MAGIC Firstly, we will important all necessary packages.

# COMMAND ----------

from sklearn.neighbors import LocalOutlierFactor
from sklearn.datasets import make_blobs

# COMMAND ----------

# MAGIC %md
# MAGIC We have created a random sample dataset below again by using the `make_blobs()` function.

# COMMAND ----------

np.random.seed(1)
x, _ = make_blobs(n_samples=200, centers=1, cluster_std=.3, center_box=(10,10))

# COMMAND ----------

# MAGIC %md
# MAGIC **TO DO:** please visualize the dataset in a plot

# COMMAND ----------

plt.scatter(x[:,0], x[:,1])
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC **TO DO:** we will then construct a LocalOutlierFactor model with n_neighbors set to 20 and contamination set to 0.03.

# COMMAND ----------

# Task

model = LocalOutlierFactor(n_neighbors=20, contamination=.03)

# COMMAND ----------

# MAGIC %md
# MAGIC **TO DO:** please fit the dataset that we generated in the beginning to the model and make prediction using the `fit_predict()` method.

# COMMAND ----------

# Task

y_pred = model.fit_predict(x)

# COMMAND ----------

# MAGIC %md
# MAGIC **TO DO:** please output the negative_outlier_factor_ from the model

# COMMAND ----------

# Task

lof = model.negative_outlier_factor_

print(lof)

# COMMAND ----------

# MAGIC %md
# MAGIC **TO DO:** find out the number of neighbors used for kneighbors queries in the model for practice

# COMMAND ----------

# MAGIC %md
# MAGIC **TO DO**: please assign the attribute `offset_` from the model to a variable called `threshold`

# COMMAND ----------

threshold = np.quantile(lof, .03)
print(threshold)

# COMMAND ----------

# MAGIC %md
# MAGIC There are two ways that we can find out the outliers.
# MAGIC 1. using the fit_predict() method and extract negative outputs as the outliers
# MAGIC 2. obtain the threshold value and extract the anomalies by comparing the threshold value and identify the values of elements

# COMMAND ----------

# MAGIC %md
# MAGIC #### Mehod 1
# MAGIC **TO DO:** please extract the negative outputs as the outliers

# COMMAND ----------

# Task

lofs_index = np.where(y_pred==-1)
values_1 = x[lofs_index]

values_1

# COMMAND ----------

plt.scatter(x[:,0], x[:,1])
plt.scatter(values_1[:,0],values_1[:,1], color='r')
plt.title ("Method 1")
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Method 2
# MAGIC **TO DO:** extract the anomalies by comparing the threshold value, when the threshold value bigger or equal to the local outlier factor score

# COMMAND ----------

# Task

index = np.where(lof<=threshold)
values_2 = x[index]

# COMMAND ----------

# MAGIC %md
# MAGIC If everything is done correctly before, we can visualize the outliers in the plot below.

# COMMAND ----------

plt.scatter(x[:,0], x[:,1])
plt.scatter(values_2[:,0],values_2[:,1], color='r')
plt.title ("Method 2")
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Some material adapted for RBI internal purposes with full permissions from original authors. [Source](https://github.com/zatkopatrik/authentic-data-science)
