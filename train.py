import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import normalize

clf1 = Perceptron(penalty='elasticnet',alpha=1e-5,max_iter=10000)

# load data
all_data_dir = "./training_data"
with open(f'{all_data_dir}/train.npy', 'rb') as f:
    X = np.load(f, allow_pickle=True)
    Y = np.load(f, allow_pickle=True)

X_train, X_test, y_train, y_test = train_test_split(normalize(X), Y,
                                                        test_size=0.3, random_state=42)

if __name__ == "__main__":

    plt.figure(figsize=(10,5))
    clf1.fit(X_train,y_train)
    print('Training score : {}'.format(clf1.score(X_train,y_train)))

    y_predict = clf1.predict(X_train)
    conf_mat = confusion_matrix(y_train,y_predict)

    plt.subplot(1,2,1)
    plt.imshow(conf_mat)
    plt.colorbar()
    plt.title('Trainig confusion matrix')

    print('Testing score : {}'.format(clf1.score(X_test,y_test)))

    y_predict = clf1.predict(X_test)
    conf_mat = confusion_matrix(y_test,y_predict)

    plt.subplot(1,2,2)
    plt.imshow(conf_mat)
    plt.title('Testing confusion matrix')
    plt.colorbar()


    plt.show()