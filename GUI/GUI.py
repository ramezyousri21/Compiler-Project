from audioop import add
from cProfile import label
from distutils import text_file
from re import sub
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Compiler')
root.iconbitmap("c.ico")
root.geometry("900x660")
output = StringVar()
output.set("Waiting")
# Set for open file name
global open_status_name
open_status_name = False


# Create New File Function
def new_file():
    # Delete Previous
    app_text.delete("1.0", END)
    # Update status bar
    root.title('New File - Compiler')
    status_bar.config(text="New File         ")
    global open_status_name
    open_status_name = False

# Open File


def openfile():
    # Delete previous text
    app_text.delete("1.0", END)
    # Grab Filename
    text_file = filedialog.askopenfilename(title="Open File")

    # Check to see if there is a file name
    if text_file:
        # Make filename global to access it
        global open_status_name
        open_status_name = text_file

    # Update Status Bar
    name = text_file
    status_bar.config(text=f'{name}       ')
    name = name.replace("", "")
    root.title(f'{name} - Compiler')
    # Open The File Itself
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # Add File To TextBox
    app_text.insert(END, stuff)
    # Close The Opened File
    text_file.close()

# Save As File


def save_as_file():
    text_file = filedialog.asksaveasfilename(
        defaultextension=".*", title="Save File")
    if text_file:
        # Update Status Bar
        name = text_file
        status_bar.config(text=f'Saved: {name}       ')
        name = name.replace("", "")
        root.title(f'{name} - Compiler')
        # Save The File
        text_file = open(text_file, 'w')
        text_file.write(app_text.get(1.0, END))
        # Close File
        text_file.close()

# Save File


def save_file():
    global open_status_name
    if open_status_name:
        # Save The File
        text_file = open(open_status_name, 'w')
        text_file.write(app_text.get(1.0, END))
        # Close File
        text_file.close()
        # Put status or update or popup code
        status_bar.config(text=f'Saved: {open_status_name}       ')
    else:
        save_as_file()

def gettext():
    inp = app_text.get(1.0 , 'end-1c')
    return inp
# Start Debugging
def Start_Debugging():
    import subprocess
    proc = subprocess.Popen('projectfinal' , shell=True , stdin=subprocess.PIPE , stdout=subprocess.PIPE , encoding='utf8')
    code = gettext()
    out = proc.communicate(input=code)[0]
    rc = proc.returncode
    if(rc == 0):
        print('yaay')
        output.set("No Syntax Errors , yaaaaaaaaaaaay :)")
    else:
        print("Sad")
        output.set("Syntax error")
        print("Directed By Robert B.Wiede")

    

# Start Without Debugging
#def Start_Without_Debugging():
    # write the code


# Create Main Frame
app_frame = Frame(root)
app_frame.pack(pady=5)

# Create Our Scroll Bar For The Text Box
text_scroll = Scrollbar(app_frame)
text_scroll.pack(side=RIGHT, fill=Y)


# Create Text Box
app_text = Text(app_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow",
                selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
app_text.pack()



#Create a label
label = Label(app_frame , textvariable=output)
label.pack()

# Configure Our Scroll Bar
text_scroll.config(command=app_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open",  command=openfile)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Run Menu
run_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Run", menu=run_menu)
run_menu.add_command(label="Start Debugging" , command=Start_Debugging)
run_menu.add_command(label="Start Without Debugging")


# Add Status Bar To Bottom Of App
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()

