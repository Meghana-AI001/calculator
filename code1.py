import customtkinter as ctk

# Set the appearance and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Secure Login")
        self.geometry("400x450")

        # Create a centered frame
        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(pady=40, padx=40, fill="both", expand=True)

        # Title Label
        self.label = ctk.CTkLabel(master=self.frame, text="Welcome Back", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)

        # Username Input
        self.username_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=12, padx=10)

        # Password Input (show="*" hides the characters)
        self.password_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=12, padx=10)

        # Login Button
        self.button = ctk.CTkButton(master=self.frame, text="Login", command=self.login_event)
        self.button.pack(pady=12, padx=10)

        # Checkbox for 'Remember Me'
        self.checkbox = ctk.CTkCheckBox(master=self.frame, text="Remember Me")
        self.checkbox.pack(pady=12, padx=10)

    def login_event(self):
        # This is where you would normally verify credentials
        user = self.username_entry.get()
        password = self.password_entry.get()
        
        if user == "admin" and password == "1234":
            print("Login Successful!")
        else:
            print("Invalid credentials.")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()