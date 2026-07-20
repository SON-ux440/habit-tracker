
def statistics_habit(habits):
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