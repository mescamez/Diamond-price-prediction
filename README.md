# Diamond-price-prediction

The goal of this project is to predict the diamond's price based on the data contain in the diamonds.csv file that it's divided in two parts, train and test.

The following steps have been carried out in order to set up the project.

### 1. Visualization and cleaning the dataset

First of all it was necessary to study the dataset, and look for some information about diamonds in order to clean properly the dataset.
Then, the following items are analyzed:
    
    - Size
    - Missing values
    - Type of variables
    - Correlation matrix
    - Summary of statistics information
    - Outliers

After that, it was necessary to transform the columns 'cut', 'color' and 'clarity', 
using two different techniques, in order to compare both results and to know which offers a better result:

    - Transform to categoric
    - Transform with get_dummies() function.

Moreover the outliers were eliminated using for it IQR method.

Finally the dataset was ready to be trained.

### 2. Training the dataset

To train a regression problem the most suitable models were chosen . RMSE is the metric selected to evaluate the models.
For the best model we use GridSearchCV in order to know which parameters are abble to improve the current result.

We have also used the H2o library with its autoML interface that trains the most appropriate models for the current data.

### 3. Kaggle competition

The results are uploaded to the kaggle competition.
