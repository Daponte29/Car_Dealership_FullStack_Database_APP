import tkinter as tk
from tkinter import ttk


class LoginView(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = None

        self.top = tk.Toplevel(parent)
        self.top.title('Login')

        # Username label
        self.username_label = ttk.Label(self.top, text="Username")
        self.username_label.grid(row=1, column=0)

        # Username field
        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(self.top, textvariable=self.username_var, width=30)
        self.username_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # Password label
        self.password_label = ttk.Label(self.top, text="Password")
        self.password_label.grid(row=2, column=0)

        # Password field
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self.top, textvariable=self.password_var, show="*", width=30)
        self.password_entry.grid(row=2, column=1, sticky=tk.NSEW)

        # login button
        self.login_button = ttk.Button(self.top, text='Login', command=self.validate_button_clicked)
        self.login_button.grid(row=3, column=3, padx=10)

        # Message label
        self.message_label = ttk.Label(self.top, text='', foreground='red')
        self.message_label.grid(row=4, column=0, columnspan=2, sticky=tk.W)

    def set_controller(self, controller):
        self.controller = controller

    def validate_button_clicked(self):
        if self.controller:
            self.controller.validate_credentials(self.username_var.get(),
                                                 self.password_var.get())

    def show_error(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(4000, self.hide_message)

    def show_success(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'blue'
        self.message_label.after(2000, self.hide_message)
        self.username_var.set('')
        self.password_var.set('')

    def hide_message(self):
        self.message_label['text'] = ''
        self.top.withdraw()
