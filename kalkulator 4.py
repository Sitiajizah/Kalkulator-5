from tkinter import *

window = Tk()

def tombol_klik(item):
    global ekspresi
    ekspresi += str(item)
    input_text.set(ekspresi)

def tombol_hapus():
    global ekspresi
    ekspresi = ""
    input_text.set("")

def tombol_samadengan():
    global ekspresi
    try:
        hasil = str(eval(ekspresi))
        input_text.set(hasil)
    except Exception:
        input_text.set("Error")
    ekspresi = ""

ekspresi = ""
input_text = StringVar()

frame = Frame(window, bg="cyan", width=500, height=300)
frame.pack()

frame2 = Frame(window, bg="black", width=500, height=300)
frame2.pack()

label = Label(frame, text="Kalkulator Siti PPLG1", anchor="w", width=50, font=("Arial", 15))
label.pack(padx=20, pady=20)

label2 = Label(frame, textvariable=input_text, font=("Arial", 20), anchor="e", width=30)
label2.pack(padx=20, pady=20)

Button(frame2, text="AC", width=5, height=3, command=tombol_hapus, fg="white", bg="red").grid(row=0, column=0)

Button(frame2, text="/", width=5, height=3, command=lambda: tombol_klik("/"), bg="gray").grid(row=0, column=3, padx=10, pady=10)
Button(frame2, text="+/-", width=5, height=3, command=lambda: tombol_klik("+/-"), bg="gray").grid(row=0, column=1, padx=10, pady=10)  # plus/minus
Button(frame2, text="%", width=5, height=3, command=lambda: tombol_klik("%"), bg="gray").grid(row=0, column=2, padx=10, pady=10) #persen
Button(frame2, text="*", width=5, height=3, command=lambda: tombol_klik("*"), bg="gray").grid(row=1, column=3, padx=10, pady=10)
Button(frame2, text="-", width=5, height=3, command=lambda: tombol_klik("-"), bg="gray").grid(row=2, column=3, padx=10, pady=10)
Button(frame2, text="+", width=5, height=3, command=lambda: tombol_klik("+"),bg="gray").grid(row=3, column=3,)

Button(frame2, text=".", width=5, height=3, command=lambda: tombol_klik(".")).grid(row=4, column=2, padx=10, pady=10)
Button(frame2, text="=", width=5, height=3, command=tombol_samadengan, bg="gray").grid(row=4, column=3,)

Button(frame2, text="0", width=14, height=3, command=lambda: tombol_klik("0")).grid(row=4, column=0, columnspan=2)

Button(frame2, text="1", width=5, height=3, command=lambda: tombol_klik("1")).grid(row=3, column=0, padx=10, pady=10)
Button(frame2, text="2", width=5, height=3, command=lambda: tombol_klik("2")).grid(row=3, column=1, padx=10, pady=10)
Button(frame2, text="3", width=5, height=3, command=lambda: tombol_klik("3")).grid(row=3, column=2, padx=10, pady=10)

Button(frame2, text="4", width=5, height=3, command=lambda: tombol_klik("4")).grid(row=2, column=0, padx=10, pady=10)
Button(frame2, text="5", width=5, height=3, command=lambda: tombol_klik("5")).grid(row=2, column=1, padx=10, pady=10)
Button(frame2, text="6", width=5, height=3, command=lambda: tombol_klik("6")).grid(row=2, column=2, padx=10, pady=10)

Button(frame2, text="7", width=5, height=3, command=lambda: tombol_klik("7")).grid(row=1, column=0, padx=10, pady=10)
Button(frame2, text="8", width=5, height=3, command=lambda: tombol_klik("8")).grid(row=1, column=1, padx=10, pady=10)
Button(frame2, text="9", width=5, height=3, command=lambda: tombol_klik("9")).grid(row=1, column=2, padx=10, pady=10)

window.mainloop()