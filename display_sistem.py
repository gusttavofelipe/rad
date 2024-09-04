import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Monitoring school system")
app.geometry("800x600")

top_frame = ctk.CTkFrame(app, height=50, corner_radius=0, fg_color="#d0d0d0")
top_frame.pack(fill="x", side="top")

extra_bar = ctk.CTkFrame(app, height=50, corner_radius=0, fg_color="#e0e0e0")
extra_bar.pack(fill="x", side="top")

slogan_label = ctk.CTkLabel(
    extra_bar,
    text="Empowering Educational Excellence with Advanced Monitoring and Analytics",
    font=("Arial", 18, "bold"),
    fg_color="#e0e0e0"
)
slogan_label.pack(pady=10, padx=20)

home_button = ctk.CTkButton(
    top_frame,
    text="Home", corner_radius=20, width=100, height=40, font=("Arial", 18, "bold")
)
home_button.pack(pady=5, padx=5, side="left")

settings_button = ctk.CTkButton(
    top_frame,
    text="Settings",
    corner_radius=20,
    width=100,
    height=40,
    font=("Arial", 18, "bold"), fg_color="#333333", border_width=0, text_color="white"
)
settings_button.pack(pady=5, padx=5, side="left")

login_button = ctk.CTkButton(
    top_frame,
    text="Log in", corner_radius=20, width=100, height=40, font=("Arial", 18, "bold")
)
login_button.pack(pady=5, padx=10, side="right")

central_frame = ctk.CTkFrame(app, corner_radius=0, fg_color="transparent")
central_frame.pack(expand=True, pady=(0, 250))

title_label = ctk.CTkLabel(
    central_frame, text="Monitoring school system", font=("Arial", 30, "bold")
)
title_label.pack(pady=(0, 100))

buttons_frame = ctk.CTkFrame(central_frame, corner_radius=0, fg_color="transparent")
buttons_frame.pack()

button_font = ("Arial", 18, "bold")

button1 = ctk.CTkButton(
    buttons_frame,
    text="Students' grades",
    corner_radius=20, width=200, height=50, font=button_font
)
button1.grid(row=0, column=0, padx=20)

button2 = ctk.CTkButton(
    buttons_frame,
    text="Exams", corner_radius=20, width=200, height=50, font=button_font
)
button2.grid(row=0, column=1, padx=20)

button3 = ctk.CTkButton(
    buttons_frame,
    text="Frequency", corner_radius=20, width=200, height=50, font=button_font
)
button3.grid(row=0, column=2, padx=20)

bottom_frame = ctk.CTkFrame(app, height=100, corner_radius=20, fg_color="#d0d0d0")
bottom_frame.pack(fill="x", side="bottom")

carousel_label = ctk.CTkLabel(
    bottom_frame,
    text="Warning: Meeting at 3 p.m. in the teachers' lounge", font=("Arial", 18, "bold")
)
carousel_label.pack(pady=10)

app.mainloop()
