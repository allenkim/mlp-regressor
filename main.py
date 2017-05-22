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


def rate(in_data: [[]]):
    num_samples = len(in_data) - 1
    train_x = []
    train_y = []
    test_x = []
    test_y = []

    for i in range(num_samples):
        rand_num = random()
        if rand_num < 0.67:
            train_x.append(in_data[i])
            train_y.append(in_data[i + 1])
        else:
            test_x.append(in_data[i])
            test_y.append(in_data[i + 1])
    print("Train X: {}, TEST X: {}".format(len(train_x), len(test_x)))

    reg = MLPRegressor(hidden_layer_sizes=(15, 15), max_iter=1000000)
    print("Start fit...")
    reg.fit(train_x, train_y)
    print("Finished...")
    return reg, reg.score(test_x, test_y)


def train(in_data: [[]]):
    num_samples = len(in_data) - 1
    train_x = []
    train_y = []

    for i in range(num_samples):
        train_x.append(in_data[i])
        train_y.append(in_data[i + 1])

    reg = MLPRegressor(hidden_layer_sizes=(15, 15), max_iter=1000000)
    reg.fit(np.array(train_x), np.array(train_y))
    return reg

def average_predict(num_of_runs: int, prices: [[]]):
    total = 0
    for i in range(num_of_runs):
        reg = train(prices)
        total += reg.predict(np.array(prices[-1]).reshape(1, -1))
        if i % 50 == 0:
            print(i)
    return total / num_of_runs


def main():
    # TODO: Neural network on the data
    at_t, t_mobile, sprint, verizon = pack_data()
    at_t_reg = train(at_t)
    t_mobile_reg = train(t_mobile)
    sprint_reg = train(sprint)
    verizon_reg = train(verizon)

    at_t_predict = average_predict(1000, at_t)
    print("at_t", at_t_predict)

    t_mobile_predict = average_predict(2000, t_mobile)
    print("tmobile", t_mobile_predict)

    sprint_predict = average_predict(2000, sprint)
    print("sprint", sprint_predict)

    verizon_predict = average_predict(2000, verizon)
    print("vz", verizon_predict)
    # [[ 38.01167605  38.06460258  38.06191534  38.05008283  38.09149562]]
    # [[ 38.04889345  38.02461876  38.02900608  38.07312175  38.06090416]]


if __name__ == "__main__":
    main()
