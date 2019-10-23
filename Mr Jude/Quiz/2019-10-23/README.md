# II. Analysis and Programming

## Number 1

### Questions
1. What are the parent and child classes here?
    - The Spell class is the parent, and the Accio part is the child
2. What does the code print out? (Try figuring it out without running it in Python)
    - `spell.execute()` will print "Summoning Charm"
    - `study_spell(spell)` will print "Accio Summoning Charm\n No description"
    - `study_spell(Confundo())` will print "Confundo Confundus Charm\nCauses the victim to become confused and befuddled."
3. Which get description method is called when `study_spell(Confundo())` is executed? Why?
    - `study_spell(Confundo())` going to call `Confundo.get_description` because the parent's function is Overriden in the Confundo class
4. What do we need to do so that `print(Accio())` will print the appropriate description (This charm summons an object to the caster, potentially over a significant distance)?
    - Override the the parent's `get_description` function and create inside the Accio class:
    ```python
        class Accio(Spell):
            def __init__(self):
                Spell.__init__(self, "Accio", "Summoning Charm")

            def get_description(self):
                return "This charm summons an object to the caster, potentially over a significant distance."
    ```

## Number 2
### Tasks
####  You are required to create an application to manage staff salary data (use classes)
1. Program will read file data.txt
2. Program will display records(sorted by name) of data.txt to the screen. 
3. The program will display a menu which contains the following:
    - New Staff
    - Delete Staff
    - View Summary Data
    - Save and Exit
4. If user choose menu 1 “New Staff”
    - Ask user to input Staff ID, with the following requirements:
        - The length must be 5 characters.
        - The first character must be ‘S’.
        - The second until fifth character must be numeric.
        - Staff ID must be unique
    - Ask user to input name with length of name should not be more than 20 characters
    - Ask user to input position which must be ‘Staff’ or ‘Officer’ or ‘Manager’
    - Ask user to input salary, with following requirements:
    - User can choose menu “Delete Staff”
        - Ask user to input staff id.
        - Validate the staff whether in the list or not.
        - If the ID exists, then delete the record from the list. 
    - If user choose menu 3 “View Summary Data”, the program will show the minimum, maximum, and average salary for each position
    - If user choose menu 4 “Save & Exit”, the program will write staff salary data into data.txt and the application will be closed.