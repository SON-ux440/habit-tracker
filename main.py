from storage import load_habits, save_habits
from habit_statistics import statistics_habit
from menu import print_menu
import habit_manager as manager

habits = load_habits()



while True:
    print_menu()
    
    choice = input('Select the option:')

    if choice == '1':
        print('=====Add Habit=====')
        manager.add_habit(habits)
        
    elif choice == '2':
        print('====Your Habits====')
        manager.show_habits(habits)
    
    elif choice == '3':
        print('===== Delete Habit =====')
        manager.delete_habit(habits)

    elif choice == '4':
        print('=====Mark completed=====')
        manager.mark_completed(habits)

    elif choice == '5':
        print('=====Edit habit=====')
        manager.edit_habit(habits)

    elif choice =="6":
        print('=====Statistics=====')
        statistics_habit(habits)
        
    elif choice == '7':
        print('Exit')
        break
        
    else:
        print('Error: this option does not exist')
