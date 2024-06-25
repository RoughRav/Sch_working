import csv


def get_data(us_list: str):
    with open('data_base.csv', 'r', encoding="UTF-8") as file:
        data_base = csv.reader(file)
        res_list = []
        us_list = list(us_list.split())
        for line in data_base:
            count = 0
            if us_list[count] in line:
                for el in line:
                    if us_list[count] == el:
                        count += 1
                        if len(us_list) > count:
                            for it in line:
                                if us_list[count] == it:
                                    count += 1
                                    if len(us_list) > count:
                                        for it_1 in line:
                                            if us_list[count] == it_1:
                                                res_list.append(line)
                                    else:
                                        res_list.append(line)
                                    count -= 1
                        else:
                            res_list.append(line)
                        count -= 1
                    count = 0


        return res_list
