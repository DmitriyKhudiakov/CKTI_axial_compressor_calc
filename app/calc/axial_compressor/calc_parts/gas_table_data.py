import matplotlib.pyplot as plt
import pathlib


class TableData:
    def __init__(self, csv_data_names):
        self.data_gr_points = []
        self.read_data(csv_data_names)

    def read_data(self, csv_data_names):
        for csv_data_name in csv_data_names:
            # curr_path = str(pathlib.Path(__file__).parent.absolute())
            path = str(pathlib.Path().absolute()) + "\\app\\calc\\axial_compressor\\calc_parts\\data_files\\tables\\gas_dynamic_functions\\" + csv_data_name
            file = open(path, "r")
            file_lines = file.read()
            list_of_lines = file_lines.split("\n")
            data_points = []
            for curr_line in list_of_lines:
                if curr_line == "":
                    break
                data_points.append(float(curr_line))
            self.data_gr_points.append(data_points)

    @staticmethod
    def plot_graph_by_x_y_lists(x_list, y_list):
        plt.title("$y = f(x)$")
        plt.ylabel("$y$")
        plt.xlabel("$x$")
        plt.grid(True, linestyle='-', color='0.75')
        data_x = []
        data_y = []
        for curr_data_x, curr_data_y in zip(x_list, y_list):
            data_x.append(curr_data_x)
            data_y.append(curr_data_y)
        plt.plot(data_x, data_y)
        plt.show()

    def find_nearest_x_point_in_list(self, x_list_n, y_list_n, x):
        n_x = 0
        n_curr = -1
        min_diff = 99999999999.9
        for curr_x in self.data_gr_points[x_list_n]:
            n_curr += 1
            diff = abs(x - curr_x)
            if diff < min_diff:
                min_diff = diff
                n_x = n_curr
        return self.data_gr_points[y_list_n][n_x]


if __name__ == "__main__":
    pass
