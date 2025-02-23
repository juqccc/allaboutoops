import customtkinter as ctk
import tkinter.messagebox as tkmb

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

app = ctk.CTk() 
app.geometry("400x400") 
app.title("Juvenson project") 

# Entry widgets for username and password
user_entry = ctk.CTkEntry(app)
user_pass = ctk.CTkEntry(app, show="*")  # Assuming password should be hidden

# Place the Entry widgets on the window
user_entry.pack()
user_pass.pack()

# Define the login function 
# defining the login function 
def login(): 
	# pre-defined username 
	username = "Geeks"
	# pre-defined password 
	password = "12345"
	new_window = ctk.CTkToplevel(app) 

	new_window.title("New Window") 

	new_window.geometry("350x150") 
	
	
"""If user provides the above username and password 
then a success window will be shown 
and a new window will open with a simple message"""
if user_entry.get() == username and user_pass.get() == password: 
    tkmb.showinfo(title="Login Successful", 
                  message="You have logged in Successfully") 
    new_window = ctk.CTkToplevel(app)  # Define the new_window variable
    new_window.title("New Window") 
    new_window.geometry("350x150") 
    ctk.CTkLabel(new_window, 
                 text="GeeksforGeeks is best for learning ANYTHING !!").pack()  # Close the parentheses

"""If the user provides the correct username but 
the password is wrong then an warning window 
will be shown"""
elif user_entry.get() == username and user_pass.get() != password: 
    tkmb.showwarning(title='Wrong password', 
                     message='Please check your password') 
		
"""If the user provides the wrong username but 
the password is correct then an warning window 
will be shown"""
	elif user_entry.get() != username and user_pass.get() == password: 
		tkmb.showwarning(title='Wrong username', 
			message='Please check your username') 
		
"""If the user provides wrong username and password 
both then an error window will be shown"""
	else: 
		tkmb.showerror(title="Login Failed", 
		message="Invalid Username and password")

app.mainloop()
