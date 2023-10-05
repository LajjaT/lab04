# Lab 04 - Dictionaries, Strings, and Lists

In this lab, we'll learn how to use three of the most important data structures available in Python:  dictionaries, strings, and lists.

## Getting Started

Be sure that you have accepted the assignment invitation within GitHub Classroom (by clicking on the link provided in the lab assignment on Canvas), before you proceed.  You want to clone your own copy of the repository (not the original, since you can't write to that repository).  The command to do so will look something like this:

```
git clone https://github.com/CSCI1030U/lab04-rana-muniz
```

Be sure to change directory to a place where the rest of your CSCI1030U labs are stored, first, so that this command copies your lab assignment starter code into the proper place.

## Instructions

In this lab, you will edit the `lab04.py` file so that it meets the requirements described in the following sections.


### Part 1

The `lab03.py` file declares three list variables called `names`, `test1_marks`, and `test2_marks`.  These list variables have been set to some test values, for now, but you'll likely need to test various values to ensure that your code works correctly.  There is also another list variable declared, called `student_data`, which is currently empty.

Write a single loop that will combine `names`, `test1_marks`, and `test2_marks` into a list of dictionaries, putting the result into `student_data`.  The variable `names` has a list of full names (which consist of a first name and a last name separated by a space, such as `Sydney Carton`), but the list of dictionaries should have the first name and last name separated.  You are not expected to handle the case when the string in `names` does not contain exactly two names.  Example output is given below:

```python
[
    {'first_name': 'Lucie', 'last_name': 'Manette', 'test1': 34.0, 'test2': 47.5}, {'first_name': 'Charles', 'last_name': 'Darnay', 'test1': 75.5, 'test2': 82.0}, {'first_name': 'Sydney', 'last_name': 'Carton', 'test1': 58.0, 'test2': 63.5}
]
```

Finally, once the loop has finished, delete the dictionary in the last position within the list.  Code is already present which prints the resulting list of dictionaries.  The output for the sample data should look like this:

```python
[{'first_name': 'Lucie', 'last_name': 'Manette', 'test1': 34.0, 'test2': 47.5}, {'first_name': 'Charles', 'last_name': 'Darnay', 'test1': 75.5, 'test2': 82.0}]
```

### Part 2

The `lab04.py` file declares a variable called `character`, which contains sample values for a subset of the stats for a role-playing game character.  Your job will be to use the f-string syntax to print a summary of that character which will have the format `<NAME> (level <LEVEL> <RACE> <CLASS>) HP: <HP>`.  Finally, print out just the last letter of the character's name.

Sample output has been given, below:

```
Grimbor (level 9 Dwarf Warrior) - HP: 58
```

_**Note:** The output has to match exactly, so be sure to compare character by character if your test does not pass.  There will also be a newline after each variable output (as is the default for `print()`)._



## Verifying Correctness

Run the pre-written tests that verify that your lab assignment code passes, using the following command:

```
pytest --capture=sys
```

Examine the output closely.  There should be hints about what went wrong, if any of the tests fail.  If you are struggling to figure it out, you can always ask for help (see __Getting Help__ for details).


## Getting Help

If your code does not work, there is always a lab instructor present during your lab period for assistance.  Them not having to mark lab assignment submissions means that they should have plenty of time to ensure that you are able to get your lab assignment submission working by the end of the lab period.

_**Note:** The lab instructor is likely to help you figure out what is wrong with your code, rather than tell you how to fix it directly.  The goal is for you to learn how to diagnose and fix your bugs on your own._



## How to Submit

First, ensure that your code passes the tests (see the section __Verifying Correctness__ for details).  If you are certain that your code passes all of the tests, then you can submit your work using the following commands:

```
git add --all
git commit -m "Lab 04 completed code"
git push origin main
```

Once you have submitted your work, you can also double check that your auto-grading was successful by clicking on the `Actions` tab in your repository page on GitHub.  Sometimes, this takes a few minutes to complete, so please be patient.
