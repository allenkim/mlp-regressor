from yielder import FileManager, DataYielder


def main():
    at_t_path = "at&t.csv"
    tmobile_path = "tmobile.csv"
    sprint_path = "sprint.csv"
    verizon_path = "verizon.csv"

    file_manager = FileManager()

    # For now try the AT&T path
    file_manager.open_file(at_t_path)

    at_t_data = DataYielder.get_stock_data(file_manager.managed_file)


if __name__ == "__main__":
    pass
