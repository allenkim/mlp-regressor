from yielder import FileManager, DataYielder
from sklearn.neural_network import MLPRegressor
from random import random


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
    return reg.score(test_x, test_y)


def test():
    pass


def main():
    # TODO: Neural network on the data
    at_t, t_mobile, sprint, verizon = pack_data()
    at_t_score = rate(at_t)
    t_mobile_score = rate(t_mobile)
    sprint_score = rate(sprint)
    verizon_score = rate(verizon)

    print("AT&T: {}, T Mobile: {}, Sprint: {}, Verizon: {}".format(at_t_score,
                                                                   t_mobile_score,
                                                                   sprint_score,
                                                                   verizon_score))


if __name__ == "__main__":
    main()
