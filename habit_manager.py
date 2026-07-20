import time
from storage import load_habits, save_habits

t = time.localtime()
date = time.strftime(" %Y-%m-%d", t)

def check_habits(habits):
    if not habits:
        print("No habits yet.")
        return True

    return False

#A list of all habits 
def show_habits(habits):

    if check_habits(habits):
        return
    
    else:
        
        for step, habit in enumerate(habits, start=1):

            if habit["completed"]:
                status = "✅"
            else:
                status = "❌"

            print(f"{step}.{status} {habit['name']}:{date}")

# Add a new habit
def add_habit(habits):
    
    while True:
        habit = input("Enter habit: ").strip()

        if not habit:
            print ("Please make a habit of it")
            continue
        
        exists = False

        for habit_item in habits:
            if habit_item["name"] == habit:
                exists = True
                print("This habit already exists.")
                break

        if exists:              
            continue

        else:
            habits.append({
            "name": habit,
            "completed": False,
            "date_created": date
            }) 
            print("Habit added successfully!")
            save_habits(habits)
            break
              
# Deleting hobbies 
def delete_habit(habits):
    if check_habits(habits):
        return

    else:
        show_habits(habits)
        while True:
            try:
                number_delete_habit = int(input("Which habit do you want to delete?: "))
                if number_delete_habit < 1 or number_delete_habit > len(habits):
                    print("Invalid habit number.")
                else:
                    habits.pop(number_delete_habit - 1)
                    save_habits(habits)
                    print("Habit deleted successfully!")
                    break
            except ValueError:
                print('Please enter a valid number.:')

#Completion mark
def mark_completed(habits):

    if check_habits(habits):
        return

    show_habits(habits)

    while True:
        try:
            number = int(input("Which habit did you complete?: "))

            if number < 1 or number > len(habits):
                print("Invalid habit number.")
                continue

            habit = habits[number - 1]
            habit["completed"] = True
            save_habits(habits)

            print(f'"{habit["name"]}" marked as completed!')
            break

        except ValueError:
            print("Please enter a valid number.")

#Edit name habit
def edit_habit(habits):
    if check_habits(habits):
        return
    
    else:
        show_habits(habits)

        while True:
            try:
                number = int(input("Which habit do you want to edit?: "))

                if number < 1 or number > len(habits):
                    print("Invalid habit number.")
                    continue

                habit = habits[number - 1]

                while True:
                    new_name = input("Enter new habit name: ").strip()

                    if not new_name:
                        print("Habit name cannot be empty.")
                        continue

                    exists = False

                    for habit_item in habits:
                        if habit_item["name"] == new_name and habit_item != habit:
                            exists = True
                            break

                    if exists:
                        print("This habit already exists.")
                        continue

                    habit["name"] = new_name
                    save_habits(habits)

                    print("Habit updated successfully!")
                    return

            except ValueError:
                print("Please enter a valid number.")