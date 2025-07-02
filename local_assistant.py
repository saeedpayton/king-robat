import os
import datetime

# لیست وظایف ما (به صورت یک فایل متنی ذخیره می‌شود)
TODO_FILE = "todo.txt"
# فایل برای ذخیره یادداشت‌ها
NOTES_FILE = "notes.txt"

def load_todos():
    """وظایف را از فایل todo.txt بارگذاری می‌کند."""
    todos = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            for line in f:
                todos.append(line.strip())
    return todos

def save_todos(todos):
    """وظایف را در فایل todo.txt ذخیره می‌کند."""
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        for todo in todos:
            f.write(todo + "\n")

def load_notes():
    """یادداشت‌ها را از فایل notes.txt بارگذاری می‌کند."""
    notes = []
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            for line in f:
                notes.append(line.strip())
    return notes

def save_notes(notes):
    """یادداشت‌ها را در فایل notes.txt ذخیره می‌کند."""
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")

def display_help():
    """راهنمای دستورات را نمایش می‌دهد."""
    print("\n--- دستورات دستیار محلی ---")
    print("1. 'افزودن [وظیفه]': یک وظیفه جدید به لیست اضافه می‌کند.")
    print("   مثال: افزودن خرید شیر")
    print("2. 'نمایش وظایف': لیست تمام وظایف را نمایش می‌دهد.")
    print("3. 'حذف [شماره وظیفه]': یک وظیفه را از لیست حذف می‌کند. (شماره وظیفه از 'نمایش وظایف' بدست می‌آید)")
    print("   مثال: حذف 1")
    print("4. 'تاریخ و زمان': تاریخ و زمان فعلی را نمایش می‌دهد.")
    print("5. 'کمک': این راهنما را نمایش می‌دهد.")
    print("6. 'خروج': از دستیار خارج می‌شود.")
    print("7. 'یادداشت [متن یادداشت]': یک یادداشت جدید ثبت می‌کند.")
    print("   مثال: یادداشت جلسه با مشتری ساعت ۱۰ صبح")
    print("8. 'نمایش یادداشت‌ها': تمام یادداشت‌های ذخیره شده را نمایش می‌دهد.")
    print("9. 'جستجوی یادداشت [کلمه کلیدی]': در یادداشت‌ها جستجو می‌کند.")
    print("   مثال: جستجوی یادداشت جلسه")
    print("--------------------------")

def main():
    todos = load_todos()
    notes = load_notes() # خط اضافه شده
    print("--- دستیار وظیفه‌گرا فعال شد ---")
    display_help()

    while True:
        command = input("\nدستیار> ").strip().lower()

        if command.startswith("افزودن "):
            task = command[len("افزودن "):].strip()
            if task:
                todos.append(task)
                save_todos(todos)
                print(f"وظیفه '{task}' اضافه شد.")
            else:
                print("لطفاً وظیفه‌ای برای افزودن مشخص کنید.")
        
        elif command == "نمایش وظایف":
            if not todos:
                print("لیست وظایف خالی است.")
            else:
                print("\n--- وظایف شما ---")
                for i, task in enumerate(todos):
                    print(f"{i + 1}. {task}")
                print("----------------")
        
        elif command.startswith("حذف "):
            try:
                task_index = int(command[len("حذف "):].strip()) - 1
                if 0 <= task_index < len(todos):
                    removed_task = todos.pop(task_index)
                    save_todos(todos)
                    print(f"وظیفه '{removed_task}' حذف شد.")
                else:
                    print("شماره وظیفه نامعتبر است.")
            except ValueError:
                print("لطفاً یک عدد برای حذف وظیفه وارد کنید. مثال: حذف 1")
        
        elif command == "تاریخ و زمان":
            now = datetime.datetime.now()
            print(f"تاریخ امروز: {now.strftime('%Y-%m-%d')}")
            print(f"ساعت فعلی: {now.strftime('%H:%M:%S')}")
            
        elif command == "کمک":
            display_help()
            
        elif command == "خروج":
            print("دستیار خاموش شد. خدانگهدار!")
            break
            
        # --- قابلیت‌های یادداشت‌برداری جدید ---
        elif command.startswith("یادداشت "):
            note_content = command[len("یادداشت "):].strip()
            if note_content:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                full_note = f"[{timestamp}] {note_content}"
                notes.append(full_note)
                save_notes(notes)
                print(f"یادداشت شما ثبت شد: '{note_content}'")
            else:
                print("لطفاً متنی برای یادداشت وارد کنید.")

        elif command == "نمایش یادداشت‌ها":
            if not notes:
                print("لیست یادداشت‌ها خالی است.")
            else:
                print("\n--- یادداشت‌های شما ---")
                for i, note in enumerate(notes):
                    print(f"{i + 1}. {note}")
                print("---------------------")

        elif command.startswith("جستجوی یادداشت "):
            keyword = command[len("جستجوی یادداشت "):].strip().lower()
            if keyword:
                found_notes = [note for note in notes if keyword in note.lower()]
                if found_notes:
                    print(f"\n--- نتایج جستجو برای '{keyword}' ---")
                    for i, note in enumerate(found_notes):
                        print(f"{i + 1}. {note}")
                    print("-----------------------------------")
                else:
                    print(f"یادداشتی با کلمه '{keyword}' یافت نشد.")
            else:
                print("لطفاً کلمه کلیدی برای جستجو وارد کنید. مثال: جستجوی یادداشت جلسه")
        # --- پایان قابلیت‌های یادداشت‌برداری جدید ---
            
        else:
            print("دستور نامعتبر. برای راهنما 'کمک' را تایپ کنید.")

if __name__ == "__main__":
    main()
