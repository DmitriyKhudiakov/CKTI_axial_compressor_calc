#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import app.gui.launch as ln


def get_ready_calc_list():
    calc_list = []
    with open("app\\ready_calc.csv", newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            calc_list.append(row)
    return calc_list


def main():
    calc_list = get_ready_calc_list()
    ln.launch(calc_list)


if __name__ == "__main__":
    main()
