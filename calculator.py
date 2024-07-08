def read_input():
    result = 0
    with open('input.txt', 'r') as file:
        for line in file:
            first_digit = get_first_digit(line)
            last_digit = get_last_digit(line)

            combined_digit = addition(first_digit, last_digit)

            result = result + int(combined_digit)




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


def get_first_digit(full_line):
    # go through the line

    candidate = ""
    counter = 1

    for c in full_line:
        candidate = c

        if c.isdigit(): 
            return c
        else:
            reduced_line = full_line[counter:]
            # check partial match
            for d in reduced_line:
                candidate += d


                partial_match = False
                for number in number_dict:
                    if candidate in number:
                        partial_match = True
                
                if candidate in number_dict:
                    return number_dict[candidate]
                
                if partial_match == False:
                    break                    

            
        counter = counter + 1



def get_last_digit(full_line):

    candidate = ""
    counter = 1

    for c in full_line[::-1].strip():
        candidate = c
        if c.isdigit(): 
            return c    
        else:
            reduced_reversed_line = full_line[::-1].strip()[counter:]
            

            for d in reduced_reversed_line:
                candidate += d

                partial_match = False
                for number in number_dict:
                    if candidate in number[::-1].strip():
                        partial_match = True

                
                if candidate[::-1].strip() in number_dict:
                    return number_dict[candidate[::-1].strip()]

                
                if partial_match == False:
                    break
                
                           
    
        counter = counter + 1

           

def addition(first, last):
    return first + last





if __name__ == "__main__":
    print(read_input())

