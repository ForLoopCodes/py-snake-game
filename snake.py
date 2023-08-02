import tkinter as tk, random as r
class SnakeGame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self, width=600, height=400, bg="black")
        self.canvas.pack()
        self.score = 0
        self.direction = "Right"
        self.head_x = 100
        self.head_y = 100
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.target = self.place_target()
        self.bind("<Key>", self.change_direction)
        self.timer = self.after(100, self.move)
    def place_target(self):
        x = r.randint(1, 29) * 20
        y = r.randint(1, 19) * 20
        self.canvas.create_oval(x, y, x+20, y+20, fill="red", tags="target")
        return (x, y)
    def change_direction(self, event):
        if event.keysym == "Up" and self.direction != "Down": self.direction = "Up"
        elif event.keysym == "Down" and self.direction != "Up": self.direction = "Down"
        elif event.keysym == "Left" and self.direction != "Right": self.direction = "Left"
        elif event.keysym == "Right" and self.direction != "Left": self.direction = "Right"
    def move(self):
        if self.direction == "Up": self.head_y -= 20
        elif self.direction == "Down": self.head_y += 20
        elif self.direction == "Left": self.head_x -= 20
        elif self.direction == "Right": self.head_x += 20
        self.body.insert(0, (self.head_x, self.head_y))
        if (self.head_x, self.head_y) == self.target:
            self.score += 10
            self.canvas.delete("target")
            self.target = self.place_target()
        else: self.body.pop()
        c=self.canvas
        c.delete("all")
        c.create_text(50, 10, text=f"Score: {self.score}", fill="white")
        for x, y in self.body:
            c.create_rectangle(x, y, x+20, y+20, fill="green")
        c.create_oval(self.target[0],self.target[1],self.target[0]+20,self.target[1]+20,fill="red", tags="target")
        if (self.head_x,self.head_y) in self.body[1:] or not(0<=self.head_x<600 and 0<=self.head_y<400):
            c.delete("all")
            c.create_text(300,200,text=f"Game Over!\nYour score: {self.score}", fill="white", font=("Arial", 20), justify=tk.CENTER)
        else: self.timer = c.after(100,self.move)
if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()
