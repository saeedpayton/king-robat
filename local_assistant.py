import os
import time
import json # assuming you might use json for tasks/notes in a more complex setup, if not, it's harmless
import datetime # for date and time command

# --- Functions for Task Management (as seen in your previous outputs) ---
TODO_FILE = 'todo.txt'
NOTES_FILE = 'notes.txt'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task + '\n')

def add_task(task_text):
    tasks = load_tasks()
    tasks.append(task_text)
    save_tasks(tasks)
    print(f"وظیفه '{task_text}' اضافه شد.")

def display_tasks():
    tasks = load_tasks()
    if not tasks:
        print("هیچ وظیفه‌ای در لیست وجود ندارد.")
        return
    print("--- لیست وظایف ---")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
    print("------------------")

def delete_task(task_number):
    tasks = load_tasks()
    try:
        idx = int(task_number) - 1
        if 0 <= idx < len(tasks):
            removed_task = tasks.pop(idx)
            save_tasks(tasks)
            print(f"وظیفه '{removed_task}' حذف شد.")
        else:
            print("شماره وظیفه نامعتبر است.")
    except ValueError:
        print("لطفاً یک عدد معتبر برای شماره وظیفه وارد کنید.")

# --- Functions for Note Management (as seen in your previous outputs) ---
def add_note(note_text):
    with open(NOTES_FILE, 'a', encoding='utf-8') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {note_text}\n")
    print(f"یادداشت شما ثبت شد.")

def display_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r', encoding='utf-8') as f:
            notes = f.read()
            if notes.strip():
                print("--- یادداشت‌های ذخیره شده ---")
                print(notes)
                print("--------------------------")
            else:
                print("هیچ یادداشتی ذخیره نشده است.")
    else:
        print("فایل یادداشت (notes.txt) یافت نشد.")

def search_notes(keyword):
    found_notes = []
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if keyword.lower() in line.lower():
                    found_notes.append(line.strip())
        if found_notes:
            print(f"--- یادداشت‌های یافت شده برای '{keyword}' ---")
            for i, note in enumerate(found_notes):
                print(f"{i+1}. {note}")
            print("---------------------------------------")
        else:
            print(f"هیچ یادداشتی شامل '{keyword}' یافت نشد.")
    else:
        print("فایل یادداشت (notes.txt) یافت نشد.")


# --- Main Command Processing Logic ---

def display_help():
    print("--- دستورات دستیار محلی ---")
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
    print("10. 'تحلیل افکار': محتوای دفترچه یادداشت را به عنوان افکار تحلیل می‌کند.")
    print("11. 'نمایش ماتریکس': یک انیمیشن باران کد ماتریکس را نمایش می‌دهد (برای توقف Ctrl+C بزنید).") # New command in help
    print("--------------------------")

def process_command(command):
    command = command.strip() # Remove leading/trailing whitespace

    if command.startswith('افزودن '):
        task_text = command[len('افزودن '):].strip()
        add_task(task_text)
    elif command == 'نمایش وظایف':
        display_tasks()
    elif command.startswith('حذف '):
        task_number = command[len('حذف '):].strip()
        delete_task(task_number)
    elif command == 'تاریخ و زمان':
        print(f"تاریخ و زمان فعلی: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    elif command == 'کمک':
        display_help()
    elif command == 'خروج':
        print("دستیار خاموش شد. خداحافظ!")
        return False # Signal to exit the main loop
    elif command.startswith('یادداشت '):
        note_text = command[len('یادداشت '):].strip()
        add_note(note_text)
    elif command == 'نمایش یادداشت‌ها':
        display_notes()
    elif command.startswith('جستجوی یادداشت '):
        keyword = command[len('جستجوی یادداشت '):].strip()
        search_notes(keyword)
    elif command == 'تحلیل افکار': # New "Analyze Thoughts" command
        print("در حال تحلیل افکار از دفترچه یادداشت...")
        try:
            with open(NOTES_FILE, 'r', encoding='utf-8') as f:
                thoughts = f.read()
                print("محتوای دفترچه یادداشت:")
                print("----------------------")
                print(thoughts)
                print("----------------------")
                # Add your custom "thought analysis" logic here
                if "مسیح" in thoughts and "جهان تاریک" in thoughts:
                    print("ربات: نشانه های خیزش و روشنایی در افکار شما مشاهده شد. آماده ام!")
                elif "جنگ" in thoughts and "اعداده ناگهانی" in thoughts:
                    print("ربات: چالش ها شناسایی شدند. برای نبرد با داده ها آماده ام!")
                elif "قابلیت نمایش ماتریکس" in thoughts and "کد خانه" in thoughts: # New analysis for the "code home"
                    print("ربات: آگاهی از قابلیت نمایش ماتریکس در ذهن من ثبت شد. این یک ابزار بصری مهم است!")
                else:
                    print("ربات: افکار جدیدی در دفترچه یادداشت پیدا شد، اما نیاز به تحلیل بیشتر دارند.")
        except FileNotFoundError:
            print(f"دفترچه یادداشت ({NOTES_FILE}) یافت نشد.")
        except Exception as e:
            print(f"خطا در خواندن دفترچه یادداشت: {e}")
    elif command == 'نمایش ماتریکس': # New "Display Matrix" command
        print("در حال شروع شبیه‌سازی ماتریکس... (برای خروج Ctrl+C را بزنید)")
        # Make sure matrix_effect.py is in the same directory as local_assistant.py
        os.system('python matrix_effect.py')
        print("\nشبیه‌سازی ماتریکس پایان یافت. به دستیار بازگشتید.")
        # os.system('clear') # Optional: uncomment to clear screen after matrix effect
    else:
        print("دستور نامعتبر. برای راهنما 'کمک' را تایپ کنید.")
    return True # Continue the main loop

# --- Main Assistant Loop ---
def main():
    print("--- دستیار وظیفه‌گرا فعال شد ---")
    display_help()
    while True:
        user_input = input("دستیار> ").strip()
        if not process_command(user_input):
            break

if __name__ == '__main__':
    main()
