import lab04
import sys

# This function tests your lab 01 code, ensuring that it prints the correct output
def test_main(capsys):
    lab04.main() # run the student's code
    captured = capsys.readouterr()
    sys.stderr.write('actual output:\n')
    sys.stderr.write(captured.out + '\n')
    correct_student_data_output = "[{'first_name': 'Lucie', 'last_name': 'Manette', 'test1': 34.0, 'test2': 47.5}, {'first_name': 'Charles', 'last_name': 'Darnay', 'test1': 75.5, 'test2': 82.0}]\nGrimbor (level 9 Dwarf Warrior) - HP: 58\n"

    sys.stderr.write('correct output:\n')
    sys.stderr.write(correct_student_data_output + '\n')
    assert captured.out == correct_student_data_output # verify that the output is a match
