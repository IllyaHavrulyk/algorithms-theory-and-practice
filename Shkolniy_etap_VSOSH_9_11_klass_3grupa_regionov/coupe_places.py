def main():
    max_place = 67
    coupe_number = int(input())
    fourth_place = coupe_number * 4
    coupe_places = [fourth_place - 3, fourth_place -
                    2, fourth_place - 1, fourth_place]
    for i in range(0, len(coupe_places)):
        print(coupe_places[i])
    print(str(max_place - (coupe_number * 2)))
    print(str(max_place - (coupe_number * 2) + 1))


main()
