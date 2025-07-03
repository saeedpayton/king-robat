import os
import time
import random

# ANSI escape codes for colors
# \033[92m is Bright Green, \033[32m is regular Green
GREEN = '\033[92m'  
ENDC = '\033[0m'    # Reset color
BOLD = '\033[1m'    # Bold text (optional)

# Character set for the "code"
CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+"

# Get terminal size (approximate for Termux)
# Using 'tput cols' and 'tput lines' is often more reliable than 'stty size'
def get_terminal_size():
    try:
        # Using tput to get actual terminal dimensions
        cols = int(os.popen('tput cols', 'r').read().strip())
        rows = int(os.popen('tput lines', 'r').read().strip())
        return rows, cols
    except:
        # Fallback to default if tput command fails
        return 24, 80 # Default if detection fails

def clear_screen():
    """Clears the terminal screen."""
    os.system('clear')

def main():
    rows, cols = get_terminal_size() # Get terminal size at the start of main
    
    clear_screen()
    print(f"{BOLD}{GREEN}Initializing the Matrix...{ENDC}")
    time.sleep(1) # Short delay before starting the animation
    clear_screen()

    # Data structure to manage individual "drops" of matrix code
    # Each drop is a dictionary: {'col': column_index, 'row': current_row, 'speed': how fast it moves, 'last_update': timestamp}
    drops = []
    
    try:
        while True:
            # Add new drops from the top of the screen
            # High chance to start a new drop from a random column
            if random.random() < 0.8: # Adjusted probability for more drops
                drops.append({
                    'col': random.randint(0, cols - 1), 
                    'row': 0, 
                    'speed': random.uniform(0.04, 0.15), # Faster and varied speeds
                    'last_update': time.time()
                })

            current_time = time.time()
            to_remove = [] # List to store indices of drops that go off-screen

            # Iterate through all active drops
            for i, drop in enumerate(drops):
                # Clear the character from its *previous* position (if it was visible)
                # We clear the character that was printed in the *previous* frame at (drop['row'] - 1, drop['col'])
                if drop['row'] > 0 and drop['row'] - 1 < rows:
                    # Move cursor to the previous position of the character and print a space to clear it
                    print(f"\033[{drop['row']};{drop['col'] + 1}H ", end='', flush=True) 
                
                # Update drop's position based on its speed
                if current_time - drop['last_update'] > drop['speed']:
                    drop['row'] += 1 # Move drop down one row
                    drop['last_update'] = current_time # Update last update time

                # If the drop is still within the screen boundaries, print a new character
                if drop['row'] < rows:
                    char_to_print = random.choice(CHARS) # Get a random character
                    # Move cursor to the *new* current position and print the character with green color
                    print(f"\033[{drop['row'] + 1};{drop['col'] + 1}H{GREEN}{char_to_print}{ENDC}", end='', flush=True)
                else:
                    # If the drop went off-screen, mark it for removal
                    to_remove.append(i)
            
            # Remove drops that are no longer on screen (iterate in reverse to avoid index issues)
            for i in reversed(to_remove):
                drops.pop(i)

            # A very small delay to control the overall animation speed (frame rate)
            time.sleep(0.02) # Adjusted for smoother animation

    except KeyboardInterrupt:
        # This block runs when Ctrl+C is pressed
        print(f"\n{ENDC}{BOLD}Matrix simulation ended.{ENDC}")
        # Clear the entire screen after the simulation ends
        clear_screen()
        # Move cursor to the bottom-left corner to ensure proper prompt display
        print(f"\033[{rows};{1}H", end='', flush=True) 
        pass # Allows the main assistant loop to resume if called from there

# This ensures main() is called only when the script is executed directly
if __name__ == '__main__':
    main()
