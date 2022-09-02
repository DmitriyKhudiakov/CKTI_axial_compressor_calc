import csv
import pathlib


class GraphData:
    def __init__(self, csv_description_name):
        info = self.read_description(csv_description_name)
        self.image_name = info[0]
        self.p1_x = (int(info[1]), int(info[2]), float(info[3]))
        self.p2_x = (int(info[4]), int(info[5]), float(info[6]))
        self.p1_y = (int(info[7]), int(info[8]), float(info[9]))
        self.p2_y = (int(info[10]), int(info[11]), float(info[12]))
        self.range_x = (float(info[13]), float(info[14]))
        self.step_x = float(info[15])
        self.range_y = (float(info[16]), float(info[17]))
        self.step_y = float(info[18])
        self.color_find = (int(info[21]), int(info[20]), int(info[19]))
        self.data_file_name = info[22]
        self.data_points = []

    @staticmethod
    def read_description(csv_description_name):
        info_list = []
        # curr_path = str(pathlib.Path(__file__).parent.absolute())
        path = str(pathlib.Path().absolute()) + "\\app\\calc\\axial_compressor\\calc_parts\\data_files\\graphs\\csv_description\\" + csv_description_name
        with open(path, newline="") as File:
            reader = csv.reader(File)
            for row in reader:
                info_list.append(row)
        return info_list[0]

    def from_window_to_real_cycle(self, xw, yw, dx_cycle, dy_cycle):
        delta_x_window = xw - self.p1_x[0]
        delta_x_real = float(delta_x_window) / float(dx_cycle) * self.step_x
        x_coor = self.p1_x[2] + delta_x_real
        delta_y_window = yw - self.p1_y[1]
        delta_y_real = float(delta_y_window) / float(dy_cycle) * self.step_y
        y_coor = self.p1_y[2] + delta_y_real
        return x_coor, y_coor

    def write_data(self, data_points):
        # curr_path = str(pathlib.Path(__file__).parent.absolute())
        path = str(pathlib.Path().absolute()) + "\\app\\calc\\axial_compressor\\calc_parts\\data_files\\graphs\\csv_data\\" + self.data_file_name
        file = open(path, "w+")
        for curr_point in data_points:
            file.write(str(curr_point[0]) + "\n")
            file.write(str(curr_point[1]) + "\n")
        file.close()

    def read_data(self):
        # curr_path = str(pathlib.Path(__file__).parent.absolute())
        path = str(pathlib.Path().absolute()) + "\\app\\calc\\axial_compressor\\calc_parts\\data_files\\graphs\\csv_data\\" + self.data_file_name
        file = open(path, "r")
        file_lines = file.read()
        list_of_lines = file_lines.split("\n")
        data_points = []
        i = 0
        point_write = []
        for curr_line in list_of_lines:
            if i == 0:
                if curr_line == "":
                    break
                point_write = []
                point_write.append(float(curr_line))
                i += 1
            elif i == 1:
                if curr_line == "":
                    break
                point_write.append(float(curr_line))
                data_points.append(point_write)
                i = 0
        return data_points

    def get_data(self, is_read, is_write, is_show):
        data_points = []
        dxw = self.p2_x[0] - self.p1_x[0]
        dxr = self.p2_x[2] - self.p1_x[2]
        dyw = self.p2_y[1] - self.p1_y[1]
        dyr = self.p2_y[2] - self.p1_y[2]
        dx_cycle = self.step_x * dxw / dxr
        dy_cycle = self.step_y * dyw / dyr
        start_x_win = self.p1_x[0] + int((self.range_x[0] - self.p1_x[2]) / self.step_x * dx_cycle)
        nx_parts = int((self.range_x[1] - self.range_x[0]) / self.step_x)
        if is_read is True:
            data_points = self.read_data()
        else:
            image = self.load_image()
            delta_color = 10
            for i in range(nx_parts + 2):
                win_x = start_x_win + int(i * dx_cycle)
                for j in range(image.shape[0]):
                    if win_x > image.shape[1] or win_x < 0:
                        break
                    else:
                        pixel = image[j, win_x]
                        if abs(pixel[0] - self.color_find[0]) < delta_color:
                            if abs(pixel[1] - self.color_find[1]) < delta_color:
                                if abs(pixel[2] - self.color_find[2]) < delta_color:
                                    x_cor, y_cor = self.from_window_to_real_cycle(win_x, j, dx_cycle, dy_cycle)
                                    data_points.append([x_cor, y_cor])
                                    break
        if is_write is True:
            self.write_data(data_points)
        if is_show is True:
            image = self.load_image()
            self.show_image("window_show", image)
            self.plot_graph_by_points([data_points])
        self.data_points = data_points
        return data_points

    def find_max_y_point(self):
        save_point = [0.0, 0.0]
        max_y = -99999999999.9
        for curr_point in self.data_points:
            if curr_point[1] > max_y:
                max_y = curr_point[1]
                save_point = curr_point
        return save_point

    def find_nearest_x_point(self, x):
        save_point = [0.0, 0.0]
        min_diff = 99999999999.9
        for curr_point in self.data_points:
            diff = abs(x - curr_point[0])
            if diff < min_diff:
                min_diff = diff
                save_point = curr_point
        return save_point

    @staticmethod
    def create_average_list(data_1, val1, data_2, val2, val3):
        save_point = [0.0, 0.0]
        data_aver = []
        if val2 > val1:
            val_max = val2
            data_max = data_2
            val_min = val1
            data_min = data_1
        else:
            val_max = val1
            data_max = data_1
            val_min = val2
            data_min = data_2
        val_aver_relative = (val3 - val_min) / (val_max - val_min)
        max_x = data_max[-1][0]
        for curr_min in data_min:
            if curr_min[0] > max_x:
                break
            min_diff = 99999999999.9
            for curr_max in data_max:
                diff_x = curr_min[0] - curr_max[0]
                if abs(diff_x) < min_diff:
                    min_diff = abs(diff_x)
                    save_point = curr_max
            delta_x = save_point[0] - curr_min[0]
            delta_y = save_point[1] - curr_min[1]
            curr_aver = [curr_min[0] + delta_x * val_aver_relative, curr_min[1] + delta_y * val_aver_relative]
            data_aver.append(curr_aver)
        return data_aver

    @staticmethod
    def find_nearest_x_point_in_list(find_list, x):
        save_point = [0.0, 0.0]
        min_diff = 99999999999.9
        for curr_point in find_list:
            diff = abs(x - curr_point[0])
            if diff < min_diff:
                min_diff = diff
                save_point = curr_point
        return save_point

    @staticmethod
    def find_max_y_point_in_list(find_list):
        save_point = [0.0, 0.0]
        max_y = -99999999999.9
        for curr_point in find_list:
            if curr_point[1] > max_y:
                max_y = curr_point[1]
                save_point = curr_point
        return save_point


def example(): 
    my_graph = GraphData("example_description.csv")
    # get_data(is_read, is_write, is_show)
    data_list = my_graph.get_data(True, True, True)


if __name__ == "__main__":
    example()