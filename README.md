# Diamond-price-prediction

The goal of this project is to predict the diamond's price based on the data contain in the file diamonds.csv that it's divided in two parts, train and test.

The steps followed to carry out this project have been the following.

### 1. Visualization and cleaning the dataset

First of all it was necessary tu study the dataset, and look for some information about diamonds in order to clean properly the dataset.
Then, the following points are analyzed:
    
    - Size
    - Missing values
    - Type of variables
    - Correlation matrix
    - Summary of statistics information
    - Outliers

After that, it was necessary to transform the columns 'cut', 'color' and 'clarity', 
using for this two different techniques, in order to compare both results and to know which offers a better result:

    - Transform to categoric
    - Transform with get_dummies() function.

After that, the outliers were eliminated using for it IQR method.

After these steps the dataset is ready to be trained.

### 2. Training the dataset

To train the most suitable models for a regression problem are chosen. The metric chosen to value the models is RMSE.
Once with the best models we use GridSearchCV to test with which parameters of that model we get a better result.

We have also used the H2o library with its autoML interface that trains the most appropriate models for the data we have.

### 3. Kaggle competition

The results are uploaded to the kaggle competition.
