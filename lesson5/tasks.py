import os
import re

def task1():
    DIGIT_NAME = "digit"
    DEGREE_NAME = "degree"
    OUT_FILENAME = "out.txt"

    def parse_polynomial(polynomial: str) -> list:
        pattern = r"(?P<digit>[+-]?\d+)(?:\*)?(?P<x>x)?(?:\^(?P<degree>[+-]?\d+)?)?"
        polynomial = str.replace(polynomial, " ", "")
        polynomial_iter = re.finditer(pattern, polynomial)
        result_list = []
        
        for entry in polynomial_iter:
            internal_dict = {}    
            if entry.group("x") is None:
                internal_dict[DEGREE_NAME] = 0
            else:
                if entry.group(DEGREE_NAME) is None:
                    internal_dict[DEGREE_NAME] = 1
                else:
                    internal_dict[DEGREE_NAME] = int(entry.group(DEGREE_NAME))
            internal_dict[DIGIT_NAME] = int(entry.group(DIGIT_NAME))
            result_list.append(internal_dict)

        return result_list
                

    path_input_1 = input("Enter a path to first file > ")
    path_input_2 = input("Enter a path to second file > ")
    if not os.path.isfile(path_input_1) or not os.path.isfile(path_input_2):
        print("Inputs were not files")
        return
    with open(path_input_1, 'r') as f:
        file_text_1 = f.readline()
    with open(path_input_2, 'r') as f:
        file_text_2 = f.readline()
    list_1 = parse_polynomial(file_text_1)
    list_2 = parse_polynomial(file_text_2)
    if len(list_1) > len(list_2):
        smaller_list = list_2
        bigger_list = list_1
    else:
        smaller_list = list_1
        bigger_list = list_2
    
    copy_of_smaller_list = smaller_list.copy()
    for element in smaller_list:
        for el in bigger_list:
            if element[DEGREE_NAME] == el[DEGREE_NAME]:
                el[DIGIT_NAME] += element[DIGIT_NAME]
                copy_of_smaller_list.remove(element)
                break
    if len(copy_of_smaller_list):
        bigger_list.extend(copy_of_smaller_list)
    bigger_list.sort(key=lambda x: x[DEGREE_NAME], reverse=True)
            
    with open(OUT_FILENAME, 'w') as f:
        for el in bigger_list:
            f.write(f"{el[DIGIT_NAME]:+}")
            if el[DEGREE_NAME] > 1:
                f.write(f"*x^{el[DEGREE_NAME]}")
            elif el[DEGREE_NAME] == 1:
                f.write("*x") 
    print(f"Result was written to {os.path.join(os.path.abspath(), OUT_FILENAME)}")    


def task2():
    pass
     


def task3():
    pass


def main():
    task_list = [task1, task2, task3]
    for task in task_list:
        print(f"{task.__name__}...")
        task()
        print("Done\n")


if __name__ == "__main__":
    main()
