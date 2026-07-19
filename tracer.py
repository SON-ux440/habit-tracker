import time
from storage import load_habits, save_habits

habits = load_habits()
#date
t = time.localtime()
date = time.strftime(" %Y-%m-%d", t)
#menu
def print_menu():
    print("=====================================")    
    print("            HABIT TRACKER            ")
    print("=====================================") 
    print("➕ 1. Add habit")
    print("📋 2. Show habits")
    print("🗑️ 3. Delete habit")
    print("✅ 4. Mark completed")
    print("✒️ 5. Edit habit")
    print("📋 6.Statistics")
    print("🚪 7. Exit")
    print("=========================")
    print("Select option:")

# Add a new habit
def add_habit():
    
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

#A list of all habits 
def show_habits():

    if not habits:
        print("No habits yet.")

    else:
        
        for step, habit in enumerate(habits, start=1):

            if habit["completed"]:
                status = "✅"
            else:
                status = "❌"

            print(f"{step}.{status} {habit['name']}:{date}")
              
# Deleting hobbies 
def delete_habit():
    if not habits:
        print("No habits yet.")

    else:
        show_habits()
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
def mark_completed():

    if not habits:
        print("No habits yet.")
        return

    show_habits()

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
def edit_habit():
    if not habits:
        print("No habits yet.")
        return
    
    else:
        show_habits()

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

def statistics_habit():
    if not habits:
        print("No habits yet.")
        return
    else:
        completed = 0
        for habit in habits:
            if habit["completed"]:
                completed += 1
        total = len(habits)
        remaining = total - completed
        progress = completed / total * 100

    print("===== Statistics =====")
    print(f"Total habits: {total}")
    print(f"Completed: {completed}")
    print(f"Remaining: {remaining}")
    print(f"Progress: {progress:.1f}%")

while True:
    print_menu()
    
    choice = input('Select the option:')

    if choice == '1':
        print('=====Add Habit=====')
        add_habit()
        
    elif choice == '2':
        print('====Your Habits====')
        show_habits()
    
    elif choice == '3':
        print('===== Delete Habit =====')
        delete_habit()

    elif choice == '4':
        print('=====Mark completed=====')
        mark_completed()

    elif choice == '5':
        print('=====Edit habit=====')
        edit_habit()

    elif choice =="6":
        print('=====Statistics=====')
        statistics_habit()
        
    elif choice == '7':
        print('Exit')
        break
        
    else:
        print('Error: this option does not exist')
