from yielder import FileManager, DataYielder
from sklearn.neural_network import MLPRegressor
from random import random
import numpy as np


def pack_data():
    at_t_path = "at&t.csv"
    tmobile_path = "tmobile.csv"
    sprint_path = "sprint.csv"
    verizon_path = "verizon.csv"

    file_manager = FileManager()

    # For now try the AT&T path
    file_manager.open_file(at_t_path)
    at_t_data = DataYielder.get_stock_data(file_manager.managed_file)
    at_t_structured_data = DataYielder.get_structured_data(at_t_data)
    file_manager.close_file()

    file_manager.open_file(tmobile_path)
    t_mobile_data = DataYielder.get_stock_data(file_manager.managed_file)
    t_mobile_structured_data = DataYielder.get_structured_data(t_mobile_data)
    file_manager.close_file()

    file_manager.open_file(sprint_path)
    sprint_data = DataYielder.get_stock_data(file_manager.managed_file)
    sprint_structured_data = DataYielder.get_structured_data(sprint_data)
    file_manager.close_file()

    file_manager.open_file(verizon_path)
    verizon_data = DataYielder.get_stock_data(file_manager.managed_file)
    verizon_structured_data = DataYielder.get_structured_data(verizon_data)
    file_manager.close_file()

    return at_t_structured_data, t_mobile_structured_data, sprint_structured_data, verizon_structured_data


def rate(in_data: [[]], num_hidden: int):
    num_samples = len(in_data) - 1
    train_x = []
    train_y = []
    test_x = []
    test_y = []

    for i in range(num_samples):
        if i < 19 * num_samples / 20:
            train_x.append(in_data[i])
            train_y.append(in_data[i + 1])
        else:
            test_x.append(in_data[i])
            test_y.append(in_data[i + 1])
    #print("Train X: {}, TEST X: {}".format(len(train_x), len(test_x)))

    reg = MLPRegressor(hidden_layer_sizes=(num_hidden, num_hidden), max_iter=1000000)
    #print("Start fit...")
    reg.fit(train_x, train_y)
    #print("Finished...")
    return reg.score(test_x, test_y)


def train(in_data: [[]], num_hidden: int):
    num_samples = len(in_data) - 1
    train_x = []
    train_y = []

    for i in range(num_samples):
        train_x.append(in_data[i])
        train_y.append(in_data[i + 1])

    reg = MLPRegressor(hidden_layer_sizes=(num_hidden, num_hidden), max_iter=1000000)
    reg.fit(np.array(train_x), np.array(train_y))
    return reg

def average_predict(num_of_runs: int, prices: [[]], num_hidden: int):
    total = 0
    for i in range(num_of_runs):
        reg = train(prices, num_hidden)
        total += reg.predict(np.array(prices[-1]).reshape(1, -1))
        if i % 10 == 0:
            print("Number of runs: {}".format(i))
    return total / num_of_runs

def best_hidden_number(prices: [[]], num_avg: int):
    best_h = 2
    best_score = 0
    for _ in range(num_avg):
        best_score += rate(prices,best_h)
    best_score /= num_avg
    current_h = 3
    print("Best Hidden Number So Far: {}".format(best_h))
    print(best_score)
    while current_h < 60:
        print("Testing {}".format(current_h))
        current_score = 0
        for _ in range(num_avg):
            current_score += rate(prices,best_h)
        current_score /= num_avg
        print(current_score)
        if current_score > best_score:
            best_score = current_score
            best_h = current_h
            print("Best Hidden Number So Far: {}".format(best_h))
        current_h += 1

def main():
    # TODO: Neural network on the data
    at_t, t_mobile, sprint, verizon = pack_data()
    at_t_score = rate(at_t, 100)
    t_mobile_score = rate(t_mobile, 16)
    sprint_score = rate(sprint, 25)
    verizon_score = rate(verizon, 11)
    print("AT&T: {}\nT-Mobile: {}\nSprint: {}\nVerizon: {}".format(at_t_score, 
                                                                   t_mobile_score, 
                                                                   sprint_score, 
                                                                   verizon_score))
    """
    at_t_reg = train(at_t,100)
    t_mobile_reg = train(t_mobile,16)
    sprint_reg = train(sprint,25)
    verizon_reg = train(verizon,11)

    at_t_predict = average_predict(100, at_t, 100)
    print("at_t", at_t_predict)

    t_mobile_predict = average_predict(100, t_mobile, 16)
    print("tmobile", t_mobile_predict)

    sprint_predict = average_predict(100, sprint, 25)
    print("sprint", sprint_predict)

    verizon_predict = average_predict(100, verizon, 11)
    print("vz", verizon_predict)
    """

if __name__ == "__main__":
    main()
