import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

root = tk.Tk()
root.title("Bàn phím ảo")

entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['0', 'X']
]

for r in range(len(keys)):
    for c in range(len(keys[r])):
        btn = tk.Button(
            frame,
            text=keys[r][c],
            width=5,
            height=2,
            command=lambda k=keys[r][c]: press(k)
        )
        btn.grid(row=r, column=c, padx=5, pady=5)

root.mainloop()
