import os
import shutil
import curses
import glob
import sys
import time
import pyfiglet

def input_bin_name(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Nama bin:")
    stdscr.refresh()

    curses.echo()
    bin_name = stdscr.getstr(0, 10).decode('utf-8')
    curses.noecho()

    return bin_name

def input_main_file(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Main file:")
    stdscr.refresh()

    curses.echo()
    data_to_copy = stdscr.getstr(0, 11).decode('utf-8')
    curses.noecho()

    return data_to_copy

def setup(stdscr):
    curses.curs_set(1)  # Show the cursor
    bin_name = input_bin_name(stdscr)

    try:
        # Salin direktori resources ke output dengan nama sesuai input bin
        shutil.copytree(os.path.join(main_folder, 'resources'), os.path.join('Awang-Installer-OutPut', bin_name))
        
        # Edit file /output/ input bin/install_to_bin.sh
        file_path = os.path.join('Awang-Installer-OutPut', bin_name, 'install_to_bin.sh')
        with open(file_path, 'r') as file:
            file_contents = file.read()
            # Replace semua teks "example" sesuai input bin
            file_contents = file_contents.replace('example', bin_name)
        with open(file_path, 'w') as file:
            file.write(file_contents)
        
        data_to_copy = input_main_file(stdscr)
        
        module_path = os.path.join('Awang-Installer-OutPut', bin_name, 'module') 
        if not os.path.exists(module_path):
            os.mkdir(module_path)
        # Salin data ke output/bin_name/module/
        if data_to_copy.strip() == '.':
            # Salin semua file dan folder di direktori saat ini
            all_files = glob.glob("*")
            for file in all_files:
                if os.path.isdir(file):
                    shutil.copytree(file, os.path.join(module_path, file))
                else:
                    shutil.copy(file, os.path.join(module_path, file))
        else:
            if os.path.isdir(data_to_copy):
                shutil.copytree(data_to_copy, os.path.join(module_path, os.path.basename(data_to_copy)))
            else:
                shutil.copy(data_to_copy, os.path.join(module_path, 'module'))
        
        stdscr.clear()
        stdscr.addstr(0, 0, "Setup selesai!")
        stdscr.refresh()
        time.sleep(3)  # Tampilkan pesan Setup selesai selama 3 detik
    except Exception as e:
        # Tangkap kesalahan dan tampilkan pesan error
        stdscr.clear()
        stdscr.addstr(0, 0, "Terjadi kesalahan: " + str(e))
        stdscr.refresh()
        time.sleep(3)  # Tampilkan pesan kesalahan selama 3 detik
    
    stdscr.clear()
    stdscr.addstr(0, 0, "Kembali ke menu utama...")
    stdscr.refresh()
    time.sleep(2)  # Tampilkan pesan Kembali ke menu utama selama 2 detik

def about(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Penulis: Dx4")
    stdscr.addstr(1, 0, "Support: F4Z, Allah")
    stdscr.refresh()
    stdscr.getch()
    
def display_figlet(stdscr, text):
    title = pyfiglet.figlet_format(text)
    lines = title.split('\n')
    height, width = stdscr.getmaxyx()
    y = height // 2 - len(lines) // 2
    x = width // 2 - max(len(line) for line in lines) // 2

    for line in lines:
        stdscr.addstr(y, x, line, curses.A_BOLD)
        y += 1
        
def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    # Daftar pilihan menu
    menu_items = ['Setup', 'About', 'Exit']
    
    # Indeks pilihan saat ini
    current_item = 0
    
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        # Menampilkan judul setup menggunakan figlet di atas menu
        display_figlet(stdscr, "Setup")
        
        for i, item in enumerate(menu_items):
            x = width//2 - len(item)//2 - 11
            y = height//2 - len(menu_items)//2 + i + len(pyfiglet.figlet_format("Setup").split('\n')) - 3
            if i == current_item:
                stdscr.addstr(y, x, item, curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, item)
        
        stdscr.refresh()
        
        # Menerima input dari arrow keys
        key = stdscr.getch()
        
        if key == curses.KEY_UP:
            current_item = (current_item - 1) % len(menu_items)
        elif key == curses.KEY_DOWN:
            current_item = (current_item + 1) % len(menu_items)
        elif key == ord('\n'):
            # Pilihan yang dipilih
            if current_item == 0:  # Setup
                setup(stdscr)
            elif current_item == 1:  # About
                about(stdscr)
            elif current_item == 2:  # Exit
                break
        elif key == 27:  # ASCII code for 'Esc' key
            break
if __name__ == "__main__":
    main_folder = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(main_folder)
    folder_path = os.path.join('Awang-Installer-OutPut') 

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        
    curses.wrapper(main)