
def create_filled_array(N):
    arr = []
    for i in range(0, N):
        arr.append(i + 1)
    return arr


def is_even(number):
    if number == 1:
        return False
    return number % 2 == 0


def reshuffle_array(deleting_method, arr, given_number):
    new_arr = []
    for i in range(0, len(arr)):
        if(is_even(i + 1) is True and deleting_method == "even" and arr[i] != given_number):
            new_arr.append(arr[i])

        elif(not is_even(i + 1) and deleting_method == "odd" and arr[i] != given_number):
            new_arr.append(arr[i])

        elif(arr[i] == given_number):
            new_arr.append(arr[i])
    if deleting_method == "odd":
        print(2)
    else:
        print(1)
    return new_arr


def remove_number(arr, given_number):
    if(len(arr) != 1 and is_even(arr.index(given_number))):
        arr = reshuffle_array("odd", arr, given_number)
        remove_number(arr, given_number)
    elif(len(arr) != 1 and not is_even(arr.index(given_number))):
        arr = reshuffle_array("even", arr, given_number)
        remove_number(arr, given_number)


def main():
    N = int(input())
    arr = create_filled_array(N)
    given_number = int(input())
    if(N != 1 or N != 2):
        remove_number(arr, given_number)
    else:
        if given_number == 1:
            print(2)
        elif given_number == 2:
            print(1)


main()
