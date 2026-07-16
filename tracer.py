print('===== Habit Tracker =====')

habits = []
#menu
def print_menu():
    print("=====================================")    
    print("            HABIT TRACKER            ")
    print("=====================================") 
    print("➕ 1. Add habit")
    print("📋 2. Show habits")
    print("🗑️ 3. Delete habit")
    print("✅ 4. Mark completed")
    print("🚪 5. Exit")
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
            "completed": False
            }) 
            print("Habit added successfully!")
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

            print(f"{step}.{status} {habit['name']}")
              
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

            print(f'"{habit["name"]}" marked as completed!')
            break

        except ValueError:
            print("Please enter a valid number.")


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
        print('Exit')
        break
        
    else:
        print('Error: this option does not exist')
