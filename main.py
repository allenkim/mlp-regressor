from yielder import FileManager, DataYielder


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
    sprint_data = DataYielder.get_stock_data(sprint_path)
    sprint_structured_data = DataYielder.get_structured_data(sprint_data)
    file_manager.close_file()

    file_manager.open_file(verizon_path)
    verizon_data = DataYielder.get_stock_data(file_manager.managed_file)
    verizon_structured_data = DataYielder.get_structured_data(verizon_data)
    file_manager.close_file()

    return at_t_structured_data, t_mobile_structured_data, sprint_structured_data, verizon_structured_data


def main():
    # TODO: Neural network on the data
    at_t, t_mobile, sprint, verizon = pack_data()


if __name__ == "__main__":
    main()
