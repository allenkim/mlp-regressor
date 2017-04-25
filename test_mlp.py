from sklearn.neural_network import MLPRegressor 
from random import randint
 
def dist(x,y):
    return (x*x + y*y) ** 0.5

def avg(x,y):
    return (x+y)/2

num_training_samples = 10000
num_test_samples = 1000

# Create training set
train_x= []
train_y = []
for n in range(num_training_samples):
    pair = [randint(0,1000),randint(0,1000)]
    train_x.append(pair)
    train_y.append([dist(*pair),avg(*pair)])
 
reg = MLPRegressor(hidden_layer_sizes=(200,), max_iter=100000)
reg.fit(train_x,train_y)
 
test_x = []
test_y = []
for n in range(num_test_samples):
    pair = [randint(1000,2000),randint(1000,2000)]
    test_x.append(pair)
    test_y.append([dist(*pair),avg(*pair)])

 
predict = reg.predict(test_x)

for idx in range(len(predict)):
    print("{} -> {}".format(test_x[idx],predict[idx]))

print(reg.score(test_x,test_y))
