import tkinter as tk

class DesktopHeader(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(side="top", fill="x")

        # Howard University blue hex color
        header_color = "#00416A"
        # White color for the text
        text_color = "white"

        #back button with Howard University blue background
        back_arrow = "\u2190"  # Left arrow Unicode character
        self.back_button = tk.Button(self, text=back_arrow, bg=header_color, fg=text_color, font=("Helvetica", 12),
                                     command=self.back_button_click)
        self.back_button.pack(side="left", padx=0)

        # Create header label
        self.app_name_label = tk.Label(self, text="Bison Advisor", bg=header_color, fg=text_color, font=("cursive", 14))
        self.app_name_label.pack(side="left", padx=0, fill="x", expand=True)

        # Create settings button 
        self.settings_button = tk.Button(self, text="⚙", bg=header_color, fg=text_color, font=("Helvetica", 12),
                                         command=self.settings_button_click)
        self.settings_button.pack(side="right", padx=0)

    def back_button_click(self):
        # Override method in your application to handle the back button click
        print("Back button clicked")

    def settings_button_click(self):
        # Override method in your application to handle the settings button click
        print("Settings button clicked")



class MyApp:
    def __init__(self, root):
        self.root = root
        self.header = DesktopHeader(root)

        # Add pages dynamically by attaching functions to header click event
        self.header.app_name_label.bind("<Button-1>", self.on_header_click)

    def on_header_click(self, event):
        # Handle header click event and add your page logic here
        print("Header clicked")


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
