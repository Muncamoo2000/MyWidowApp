import tkinter as tk

class MyWindow:
    def __init__(self, title, backgound, text_color):
           
        self.window = tk.Tk()
        
        self.window.title(title)
        self.window.configure(bg = backgound)
        
        #Name Imput Prompt
        self.prompt = tk.Label(
            self.window,
            text="What is your name: ",
            fg=text_color,
            bg=backgound
            )
        self.prompt.pack(pady=5)
        
        #user input field
        self.name_input = tk.Entry(self.window)
        self.name_input.pack(pady=5)
        
        #submit button
        self.submit_button = tk.Button(
            self.window,
            text="Submit",
            command=self.greet
            )
        self.submit_button.pack(pady=5)
        
        #greeting lable
        self.greeting = tk.Label(
            self.window, 
            text="", 
            fg=text_color,
            bg=backgound
            )
        self.greeting.pack(pady=10)
        
    #Method to process the input
    def greet(self): 
        name = self.name_input.get().strip()
            
        if name:
                self.greeting.config(text=f"Hello, {name}!")
        else:
                self.greeting.config(text="Please enter your name. ")
                
                
    def run(self):
         self.window.mainloop()
                
                
app1 = MyWindow(
    "Monica's first python app",
    "yellow",
    "blue"
    )

app1.run()
