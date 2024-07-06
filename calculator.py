def read_input():
    result = 0
    with open('test.txt', 'r') as file:
        for line in file:
            first_digit = get_first_digit(line)
            last_digit = get_last_digit(line)

            combined_digit = addition(first_digit, last_digit)

            result = result + int(combined_digit)

            print(combined_digit)


    return result



number_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def get_first_digit(line):
    # go through the line

    candidate = ""

    for c in line:
        if c.isdigit(): 
            return c
        else:
            # store the character
            candidate += c
            # check partial match
            partial_match = False
            for number in number_dict:
                if candidate in number:
                    partial_match = True
            if partial_match == False:
                candidate = c
            
            if candidate in number_dict:
                return number_dict[candidate]



def get_last_digit(line):
    candidate = ""

    for c in reversed(line):
        if c.isdigit(): 
            return c    
        else:
            # store the character
            candidate += c
            reversed_candidate = candidate[::-1].strip()

            # check partial match
            partial_match = False
            for number in number_dict:
                if candidate in number[::-1]:
                    partial_match = True
            if partial_match == False:
                candidate = c
            


            if reversed_candidate in number_dict:
                return number_dict[reversed_candidate]
            

def addition(first, last):
    return first + last





if __name__ == "__main__":
    print(read_input())

