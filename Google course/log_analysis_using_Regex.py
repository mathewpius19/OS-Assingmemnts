#!/usr/bin/env python3

import re
import operator
import csv


def read_file():
        with open("syslog.log") as log_file:
                log_entries = log_file.readlines()
                log_file.close()
        return log_entries


def generate_local_lists(log_entries):
        error = []
        for entry in log_entries:
                if " ERROR " in entry:
                        error.append(entry)
        return error, log_entries


def generate_error_dictionary(error):
        error_final = {}
        pre_sort = {}
        post_sort = {}
        for entry in error:
                pattern = r'ERROR (.*) '
                result = re.search(pattern, entry)
                error_message = result.group(1).strip()+""
                if error_message in pre_sort:
                        pre_sort[error_message] += 1
                else:
                        pre_sort[error_message] = 1

        to_dict = sorted(pre_sort.items(), key=operator.itemgetter(1), reverse=True)
        for elem in to_dict:
                post_sort[elem[0]] = str(elem[1])
        error_final.update(post_sort)
        print(error_final)
        return error_final


def generate_user_dictionary(all_entries):
        per_user = {}
        pre_sort = {}
        post_sort = {}
        pattern = r"\(.*\)"

        for entry in all_entries:
                result = re.search(pattern, entry)
                username = (result.group(0).strip())[1:-1] + ""
                if username in pre_sort.keys():
                        if "INFO" in entry:
                                pre_sort[username][0] += 1
                        else:
                                pre_sort[username][1] += 1
                else:
                        if "INFO" in entry:
                                pre_sort[username] = [1, 0]
                        else:
                                pre_sort[username] = [0, 1]

        to_dict = sorted(pre_sort.keys())
        for elem in to_dict:
                post_sort[elem] = ''.join(str(e) for e in pre_sort[elem])
        per_user.update(post_sort)
        return per_user


def dict_to_csv(dict, header, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for key, value in dict.items():
            if filename == "error_message.csv":
                writer.writerow([key, value])
            else:
                writer.writerow([key, value[0], value[1]])


def main():
    split_entries = generate_local_lists(read_file())
    error = generate_error_dictionary(split_entries[0])
    user = generate_user_dictionary(split_entries[1])
    dict_to_csv(error, ["Error", "Count"], "error_message.csv")
    dict_to_csv(user, ["Username", "INFO", "ERROR"], "user_statistics.csv")


if __name__ == '__main__':
    main()

