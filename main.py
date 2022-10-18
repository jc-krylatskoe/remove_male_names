from typing import List


def create_male_names_list(filename: str) -> List:
    male_name_list = []
    with open(filename, "r", encoding="utf-8") as fp:
        for name in fp:
            male_name_list.append(name.rstrip("\n").lower())
    return male_name_list


def is_name_male(input_name: str, male_names_list: List) -> bool:
    res = False
    if input_name in male_names_list:
        res = True
    return res


def remove_male_contacts(filename_input: str, filename_output: str, male_list_filename: str) -> None:
    male_names_list = create_male_names_list(male_list_filename)

    with open(filename_input, "r", encoding="cp1251") as fin:
        with open(filename_output, "w", encoding="cp1251") as fout:
            counter = 0
            male_names_filtered = 0
            for line in fin:
                name = line.split(";")[1].split(" ")[0].rstrip("\n").lower()

                """
                if 97 <= ord(name[0]) <= 122:
                    print(line)
                """

                if is_name_male(name, male_names_list):
                    print(f"- {line}", end="")
                    male_names_filtered += 1
                else:
                    fout.write(line)

                counter += 1

        print(f'male contacts filtered: {male_names_filtered} of total {counter} '
              f'({male_names_filtered * 100 / counter :.1f}%)')


if __name__ == '__main__':
    # filename_input = "base_11000.csv"
    filename_input = "base_all.csv"
    filename_output = filename_input.split(".")[0] + "_output." + filename_input.split(".")[1]
    male_list_filename = "male_names_rus.txt"
    # male_list_filename = "all_names_rus.txt"
    remove_male_contacts(filename_input, filename_output, male_list_filename)

