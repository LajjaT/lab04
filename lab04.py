def main():
    # part 1

    names = ['Lucie Manette', 'Charles Darnay', 'Sydney Carton']
    test1_marks = [34.0, 75.5, 58.0]
    test2_marks = [47.5, 82.0, 63.5]
    
    student_data = []

    for i in range(len(names)):
        student_dictionary = {}
        full_names = names[i].split()
        student_dictionary = {'first_name': full_names[0],'last_name': full_names[1],'test1': test1_marks[i],'test2': test2_marks[i]}
        student_data.append(student_dictionary)
    
    # TODO: YOUR CODE TO DELETE THE LAST CHARACTER GOES HERE

    student_data.pop(-1)

    print(student_data)

    # part 2

    character = {
        'name': 'Grimbor',
        'race': 'Dwarf',
        'class': 'Warrior',
        'hp': 58,
        'level': 9,
    }

    name = ""
    name = character['name']

    race = ""
    race = character['race']

    clss = ""
    clss = character['class']

    hp = ""
    hp = character['hp']

    level = ""
    level = character['level']

    # TODO: YOUR CODE TO OUTPUT A SUMMARY FOR THIS CHARACTER GOES HERE
    print(f'{name} (level {level} {race} {clss}) - HP: {hp}')

if __name__ == "__main__":
    main()