'''
This will be our linear regression model, and here we will be splitting our dataset,
training the model and returning the accuracy and loss while writing everything to
our config file
'''
# import pickle5 as pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
# from sklearn.externals import joblib

f = 'fullycleaned.csv'

#Both the next functions are in case of a Linear Regression to compare the accuracy

#in our example, Gradient Boosting Regressor gives a 78% accuracy
def train_GBR(X, y):
  # f = "joblib_model.pkl"
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 150)
	reg = GradientBoostingRegressor()

	reg.fit(X_train, y_train)
  #code to save our model for it to be downloaded
  # f = 'GBR_model.sav'
  # pickle.dump(reg, open(f, 'wb'))
  
  # reg.save()
	print('The accuracy provided by the Gradien Boosting Algorithm is: ' + str(reg.score(X_test, y_test)))
  # joblib.dump(reg, f)

	return reg.score(X_test, y_test)

#in our example, Linear regression gives a 65% accuracy
def train_LR(X, y):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 150)

	reg = LinearRegression()

	reg.fit(X_train, y_train)

  #code to save our model for it to be downloaded
  # f = 'LR_model.sav'
  # pickle.dump(reg, open(f, 'wb'))

	print('The accuracy provided by the Linear Regression Algorithm is: ' + str(reg.score(X_test, y_test)))

	return reg.score(X_test, y_test)

def train_LogR(X, y):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 150)
  model = LogisticRegression(solver='liblinear', random_state=0)
  model.fit(X, y)

  #Model evaluation
  p_pred = model.predict_proba(X)
  y_pred = model.predict(X)
  score_ = model.score(X, y)
  conf_m = confusion_matrix(y, y_pred)
  report = classification_report(y, y_pred)


#this is our sigmoid function that will serve as an activation function for our NN
def Sigmoid(z):
  return (1 / (1 + np.exp(-z.astype(float))))

""" The main function calls the Train function to get the final values of the weights and bias. It then calculates the success rate of the model."""

def main(csv):
    W,B = Train(csv,2,0.001)
    print("Weights:\n",W)
    print("Bias: ",B)
    successRate = Test(csv,W,B)
    print("Success Rate: ",np.sum(successRate))

"""The Save Result function adds a new column to the test results file that represents the predictions. Everything is saved in a new file not to disturb the program the next time it runs."""

def SaveResult(file,result):
    df = pd.read_csv(file)
    df['Prediction'] = [int(i) for i in np.transpose(result)]
    df.to_csv('test-result.csv')

"""The Train function will read the file and make a call to the initialize function after transposing both X and Y. It will then make a call to the Gradient Descent function that will return the final W and B. """

def Train(file, epochs, alpha):
    X,Y = Read(file)
    X = np.transpose(X)
    
    Y = np.transpose(Y)
    nx,m = np.shape(X)
    W,B = Initialize(nx)
    W,B = GradientDescent(W,B,X,Y,epochs, alpha)
    
    return W,B

"""The Test function will execute the gradient descent for one epoch. It will then return the success rate that will be displayed at the end."""

def Test(file,W,B):
    X,Y = Read(file)
    X = np.transpose(X)
    # X = Normalize(X)
    Y = np.transpose(Y)
    Z = np.dot(W.T, X) + B
    A = Sigmoid(Z)
    A = np.round(A)
    diff = np.sum(np.abs(A-Y))
    successRate = (1 - (diff/np.size(A)))/X.shape[1]
    return successRate

"""The Read function reads data from the file and manages both the splitting and cleaning of the data."""

def Read(file):
    data = pd.read_csv(file, delimiter=';')
    data_train, data_test = splitting(data)
    
    Y_train = data_train.filter(['y'], axis=1)
    X_train = data_train.drop(['y'], axis=1)
    X_train = Clean_X(X_train)
    Y_train = Clean_Y(Y_train)

    Y_test = data_test.filter(['y'], axis=1)
    X_test = data_test.drop(['y'], axis=1)
    X_test = Clean_X(X_test)
    Y_test = Clean_Y(Y_test)

    # print(X)
    # print(Y)
    return X_train, Y_train

"""This function initializes the weights with random values and the bias with zero."""

def Initialize(nx):
    W = np.random.randn(nx, 1)* 0.01
    B = 0
    return W,B

"""The Gradient Descent function follows the algorithm seen in class. It uses the forward then backward propagation with a calculation of the cost and an update of the weights and bias."""

def GradientDescent(W,B,X,Y,epochs,learnRate):
    m,nx = np.shape(X)
    costs = []
    print("Working with learn rate",learnRate,"and",epochs,"iterations")
    for i in range (epochs):
        print("Epoch: ", i+1)
        Z = np.array(np.dot(W.T,X) + B, dtype=np.float32)
        A = Sigmoid(Z.astype(float))
        cost = 1/m * - np.sum(Y*np.log(A)+(1-Y)*np.log(1-A))
        print("Cost: ", np.sum(cost))
        if i==0 or i==epochs-1:
            costs.append(cost)
        dz = A-Y
        dw = (1/m) * np.dot(X,dz.T)
        db = (1/m) * np.sum(dz)
        W = W - learnRate*dw
        B = B - learnRate*np.mean(db)
        print("Accuracy: ", accuracy(classify(A), Y))
    print("Cost started with:",np.sum(costs[0]),"and ended with:",np.sum(costs[1]))
    return W,B


"""The Splitting function splits the data into a training and testing set."""

def splitting(data):
  train, test = train_test_split(data, test_size=0.2)
  return train, test

"""The Clean_X function helps cleaning the data into different categories (int, category, date)."""

def Clean_X(data):
  data.default.replace(('yes', 'no'), (1, 0), inplace=True)
  data.housing.replace(('yes', 'no'), (1, 0), inplace=True)
  data.loan.replace(('yes', 'no'), (1, 0), inplace=True)
  # Normalization techniques
  data.age = (data.age - min(data.age)) / (max(data.age) - min(data.age))
  data.balance = (data.balance - min(data.balance)) / (max(data.balance) - min(data.age))
  data.day = (data.day - min(data.day)) / (max(data.day)- min(data.age))
  data.duration = (data.duration - min(data.duration)) / (max(data.duration)- min(data.age))
  data.campaign = (data.campaign - min(data.campaign)) / (max(data.campaign)- min(data.age))
  data.pdays = (data.pdays - min(data.pdays)) / (max(data.pdays)- min(data.age))
  data.previous = (data.previous - min(data.previous)) / (max(data.previous)- min(data.age))

  data.job = pd.get_dummies(data, columns=["job"])
  data.marital = pd.get_dummies(data, columns=["marital"])
  data.education = pd.get_dummies(data, columns=["education"])
  data.contact = pd.get_dummies(data, columns=["contact"])
  data.poutcome = pd.get_dummies(data, columns=["poutcome"])
  data.month = pd.get_dummies(data, columns=["month"])

  return data

"""The Clean_Y performs the same actions as Clean_X on y only."""

def Clean_Y(data):
  data.y.replace(('yes', 'no'), (1, 0), inplace=True)
  return data

"""The Accuracy function calculates the accuracy of the model at each iteration."""

def accuracy(predicted, actual):
  diff = predicted - actual
  return 1.0 - (float(np.count_nonzero(diff)) / predicted.shape[0])

"""The Decision Boundary function returns 0 or 1 according to the probability gotten."""

def decision_boundary(prob):
  return 1 if prob >= .5 else 0

"""The Classify function will help in classifying the weights into 0s and 1s using the Decision Boundary Function."""

def classify(predictions):
  fun = np.vectorize(decision_boundary)
  return fun(predictions).flatten()