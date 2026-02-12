import tkinter as tk
from tkinter import messagebox
import random

class ValentineAsker:
    def __init__(self, root):
        self.root = root
        self.root.title("❤️ A Special Question ❤️")
        self.root.geometry("500x400")
        self.root.configure(bg='#FFE5E5')
        
        # Counter for how many times she tries to click "No"
        self.no_count = 0
        
        # Question label
        self.question_label = tk.Label(
            root,
            text="Will you be my Valentine? 💕",
            font=('Arial', 24, 'bold'),
            bg='#FFE5E5',
            fg='#FF1493'
        )
        self.question_label.pack(pady=50)
        
        # Yes button (stays put and gets bigger each time)
        self.yes_button = tk.Button(
            root,
            text="Yes! 💖",
            font=('Arial', 16, 'bold'),
            bg='#FF69B4',
            fg='white',
            command=self.yes_clicked,
            padx=20,
            pady=10
        )
        self.yes_button.pack(pady=20)
        
        # No button (runs away!)
        self.no_button = tk.Button(
            root,
            text="No",
            font=('Arial', 12),
            bg='#FFB6C1',
            fg='#666',
            command=self.no_clicked,
            padx=15,
            pady=5
        )
        self.no_button.pack(pady=10)
        
        # Bind mouse motion to make the No button run away
        self.no_button.bind('<Enter>', self.run_away)
    
    def run_away(self, event):
        # Get window size
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        
        # Get button size
        button_width = self.no_button.winfo_width()
        button_height = self.no_button.winfo_height()
        
        # Random new position
        new_x = random.randint(0, max(0, window_width - button_width))
        new_y = random.randint(100, max(100, window_height - button_height))
        
        # Move the button
        self.no_button.place(x=new_x, y=new_y)
        
        # Make Yes button bigger and more tempting
        current_size = int(self.yes_button.cget('font').split()[1])
        new_size = min(current_size + 2, 32)
        self.yes_button.config(font=('Arial', new_size, 'bold'))
        
        # Update text on No button to make it funnier
        self.no_count += 1
        funny_texts = [
            "No",
            "Bunjie click yes",
            "Nana say yes",
            "Baby just click yes",
            "Are you sure?",
            "Really?",
            "Think again!",
            "Nope! 😏",
            "Not happening!",
            "Mageba just click yes would you",
            "Try the other one!",
            "Wrong button!",
            "Come on... 😊",
            "The YES button looks nice!"
        ]
        if self.no_count < len(funny_texts):
            self.no_button.config(text=funny_texts[self.no_count])
    
    def no_clicked(self):
        # This shouldn't happen, but if she manages to click it...
        messagebox.showinfo("Nice try!", "Oops! You were too fast! 😄\nBut we both know the answer is YES! 💕")
    
    def yes_clicked(self):
        # Celebration!
        self.root.destroy()
        
        # Create celebration window
        celebration = tk.Tk()
        celebration.title("💖 YES! 💖")
        celebration.geometry("500x400")
        celebration.configure(bg='#FFE5E5')
        
        # Hearts and celebration
        tk.Label(
            celebration,
            text="🎉 ❤️ 💕 ❤️ 🎉",
            font=('Arial', 32),
            bg='#FFE5E5'
        ).pack(pady=30)
        
        tk.Label(
            celebration,
            text="I knew you'd say yes!",
            font=('Arial', 24, 'bold'),
            bg='#FFE5E5',
            fg='#FF1493'
        ).pack(pady=20)
        
        tk.Label(
            celebration,
            text="I love you! ❤️\n\nHappy Valentine's Day!",
            font=('Arial', 18),
            bg='#FFE5E5',
            fg='#FF69B4'
        ).pack(pady=20)
        
        tk.Button(
            celebration,
            text="Close",
            font=('Arial', 14),
            bg='#FF69B4',
            fg='white',
            command=celebration.destroy,
            padx=20,
            pady=10
        ).pack(pady=20)
        
        celebration.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ValentineAsker(root)
    root.mainloop()