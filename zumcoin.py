import tkinter as tk
import webbrowser as wb

mouse1 = 1
mouse2 = 2
mouse3 = 5
mouse4 = 10
mouse5 = 15
mouse6 = 25
mouse7 = 45
mouse8 = 60
mouse9 = 85
mouse10 = 100

file_s = open(r"logs\window\packages\pack.txt", "r+")
progress = file_s.read()
score = int(progress)

file_m = open(r"logs\window\packages\packs.txt", "r+")
progress_m = file_m.read()
mouse = int(progress_m)


def plus():
    global score
    global mouse

    score += mouse

    label_score["text"] = f"""Ваш счёт {score} коинов
за клик: {mouse}"""


def error():
    err = tk.Tk()
    err.title("Недостаточно средств")
    err.geometry("400x200")
    err.resizable(False, False)
    err.config(bg="#00FF00")

    def destroy():
        err.destroy()

    label_error = tk.Label(err, text=f"""Недостаточно
коинов!""",
                          bg="#00FF00",
                          font=("Arial", "20", "bold"),
                          width=50
                          )

    button_error = tk.Button(err, text="Ну, окей",
                             command=destroy,
                             font=("Arial", "20", "bold")
                             )

    label_error.pack()
    button_error.place(x=130, y=100)
    err.mainloop()


def ms1():
    global mouse
    global mouse1
    global score
    if score < 250:
        error()
    score -= 250
    mouse += mouse1
    label_score["text"] = f"""Ваш счёт {score} коинов
за клик: {mouse}"""


def ms2():
    global mouse
    global mouse2
    global score
    if score < 500:
        error()
    score -= 500
    mouse += mouse2
    label_score["text"] = f"""Ваш счёт {score} коинов
за клик: {mouse}"""


def ms3():
    global mouse
    global mouse3
    global score
    if score < 1500:
        error()
    score -= 1500
    mouse += mouse3
    label_score["text"] = f"""Ваш счёт {score} коинов
за клик: {mouse}"""


def ms4():
    global mouse
    global mouse4
    global score
    if score < 3000:
        error()
    score -= 3000
    mouse += mouse4
    label_score["text"] = f"""Ваш счёт {score} коинов
за клик: {mouse}"""


def ms5():
    global mouse
    global mouse5
    global score
    if score < 4500:
        error()
    score -= 4500
    mouse += mouse5
    label_score["text"] = f"""Ваш счёт {score} коинов
за клик: {mouse}"""


def ms6():
    global mouse
    global mouse6
    global score
    if score < 10000:
        error()
    score -= 10000
    mouse += mouse6
    label_score["text"] = f"""Ваш счёт {score} коинов
за клик: {mouse}"""


def ms7():
    global mouse
    global mouse7
    global score
    if score < 15000:
        error()
    score -= 15000
    mouse += mouse7
    label_score["text"] = f"""Ваш счёт {score} коинов
за клик: {mouse}"""


def ms8():
    global mouse
    global mouse8
    global score
    if score < 20000:
        error()
    score -= 20000
    mouse += mouse8
    label_score["text"] = f"""Ваш счёт {score} коинов
за клик: {mouse}"""


def ms9():
    global mouse
    global mouse9
    global score
    if score < 30000:
        error()
    score -= 30000
    mouse += mouse9
    label_score["text"] = f"""Ваш счёт {score} коинов
за клик: {mouse}"""


def ms10():
    global mouse
    global mouse10
    global score
    if score < 50000:
        error()
    score -= 50000
    mouse += mouse10
    label_score["text"] = f"""Ваш счёт {score} коинов
за клик: {mouse}"""


def save():
    global file_s
    global file_m

    file_ss = open(r"logs\window\packages\pack.txt", "w")
    file_ss.write(str(score))
    file_mm = open(r"logs\window\packages\packs.txt", "w")
    file_mm.write(str(mouse))

    file_s.close()
    file_m.close()
    file_ss.close()
    file_mm.close()
    win.destroy()


win = tk.Tk()
win.title("zumcoin")
win.geometry("600x700")
win.resizable(False, False)
win.config(bg="#00FF00")
win.iconphoto(True, tk.PhotoImage(file="icon.png"))


def shop():
    global label_shop
    shop = tk.Tk()
    shop.title("Магазин")
    shop.geometry("600x700")
    shop.resizable(False, False)
    shop.config(bg="#00FF00")

    label_shop = tk.Label(shop, text=f"""Добро пожаловать в магазин!""",
                          bg="#00FF00",
                          font=("Arial", "15", "bold"),
                          width=50,
                          height=2
                          )

    btn_mouse1 = tk.Button(shop, text=f"Мышка 1-го уровня (+1)                               Стоимость: 250",
                           command=ms1,
                           font=("Arial", "10", "bold"),
                           bg="#b784a7",
                           activebackground="#ee9086",
                           height=3
                           )

    btn_mouse2 = tk.Button(shop, text=f"Мышка 2-го уровня (+2)                               Стоимость: 500",
                           command=ms2,
                           font=("Arial", "10", "bold"),
                           bg="#b784a7",
                           activebackground="#ee9086",
                           height=3
                           )

    btn_mouse3 = tk.Button(shop, text=f"Мышка 3-го уровня (+5)                              Стоимость: 1.500",
                           command=ms3,
                           font=("Arial", "10", "bold"),
                           bg="#b784a7",
                           activebackground="#ee9086",
                           height=3
                           )

    btn_mouse4 = tk.Button(shop, text=f"Мышка 4-го уровня (+10)                              Стоимость: 3.000",
                           command=ms4,
                           font=("Arial", "10", "bold"),
                           bg="#b784a7",
                           activebackground="#ee9086",
                           height=3
                           )

    btn_mouse5 = tk.Button(shop, text=f"Мышка 5-го уровня (+15)                              Стоимость: 4.500",
                           command=ms5,
                           font=("Arial", "10", "bold"),
                           bg="#b784a7",
                           activebackground="#ee9086",
                           height=3
                           )

    btn_mouse6 = tk.Button(shop, text=f"Мышка 6-го уровня (+25)                              Стоимость: 10.000",
                           command=ms6,
                           font=("Arial", "10", "bold"),
                           bg="#b784a7",
                           activebackground="#ee9086",
                           height=3
                           )

    btn_mouse7 = tk.Button(shop, text=f"Мышка 7-го уровня (+45)                              Стоимость: 15.000",
                           command=ms7,
                           font=("Arial", "10", "bold"),
                           bg="#b784a7",
                           activebackground="#ee9086",
                           height=3
                           )

    btn_mouse8 = tk.Button(shop, text=f"Мышка 8-го уровня (+60)                               Стоимость: 20.000",
                           command=ms8,
                           font=("Arial", "10", "bold"),
                           bg="#b784a7",
                           activebackground="#ee9086",
                           height=3
                           )

    btn_mouse9 = tk.Button(shop, text=f"Мышка 9-го уровня (+85)                              Стоимость: 30.000",
                           command=ms9,
                           font=("Arial", "10", "bold"),
                           bg="#b784a7",
                           activebackground="#ee9086",
                           height=3
                           )

    btn_mouse10 = tk.Button(shop, text=f"Мышка 10-го уровня (+100)                             Стоимость: 50.000",
                           command=ms10,
                           font=("Arial", "10", "bold"),
                           bg="#b784a7",
                           activebackground="#ee9086",
                           height=3
                           )

    label_shop.grid(row=0, column=0)
    btn_mouse1.grid(row=1, stick="we")
    btn_mouse2.grid(row=2, stick="we")
    btn_mouse3.grid(row=3, stick="we")
    btn_mouse4.grid(row=4, stick="we")
    btn_mouse5.grid(row=5, stick="we")
    btn_mouse6.grid(row=6, stick="we")
    btn_mouse7.grid(row=7, stick="we")
    btn_mouse8.grid(row=8, stick="we")
    btn_mouse9.grid(row=9, stick="we")
    btn_mouse10.grid(row=10, stick="we")

    shop.mainloop()


def falling():
    global score
    global mouse
    score = 0
    mouse = 1
    label_score["text"] = f"""Ваш счёт {score} коинов
за клик: {mouse}"""


def win_3():
    win3 = tk.Tk()
    win3.title("О проекте")
    win3.geometry("600x700")
    win3.resizable(False, False)
    win3.config(bg="#00FF00")

    def web():
        wb.open("https://vk.com/little_script_kiddie")

    label_1 = tk.Label(win3, text="О проекте: ",
                       bg="#00FF00",
                       font=("Arial", "15"),
                       width=55,
                       height=2
                       )

    label_alert = tk.Label(win3, text="""При закрытии чёрного окна cmd прогресс
    не сохраняется, будь осторожей!""",
                           bg="#00FF00",
                           font=("Arial", "15", "bold"),
                           width=45,
                           height=4,
                           anchor="s"
                           )

    label_3 = tk.Label(win3, text="Библиотека: Tkinter (Python)",
                       bg="#00FF00",
                       font=("Arial", "15"),
                       width=45,
                       height=4,
                       anchor="s"
                       )

    label_2 = tk.Label(win3, text="""Чтобы узнать о других проектах,
    напиши мне)""",
                       bg="#00FF00",
                       font=("Arial", "15"),
                       width=45,
                       height=4,
                       anchor="s"
                       )

    label_info = tk.Label(win3, text="Наслаждайся :)",
                          bg="#00FF00",
                          font=("Arial", "15"),
                          width=55
                          )

    label_info2 = tk.Label(win3, text="Стартовал: 20 января 2023",
                           bg="#00FF00",
                           font=("Arial", "15"),
                           width=45,
                           height=4,
                           anchor="s"
                           )

    btn_web = tk.Button(win3, text="Перейти на страницу разработчика",
                        command=web,
                        bg="#b784a7",
                        activebackground="#ee9086",
                        font=("Arial", "15"),
                        width=45
                        )

    btn_info1 = tk.Button(win3, text="Сбросить прогресс",
                          command=falling,
                          bg="#b784a7",
                          activebackground="#ee9086",
                          font=("Arial", "15"),
                          width=45
                          )

    btn_info2 = tk.Button(win3, text="Пустая кнопка",
                          font=("Arial", "15"),
                          width=55
                          )

    label_1.grid()
    btn_web.grid()
    btn_info1.grid()
    label_info2.grid()
    label_3.grid()
    label_alert.grid()
    label_2.grid()
    label_info.place(x=0, y=600)
    win3.mainloop()


label_score = tk.Label(win, text=f"""Ваш счёт {score} коинов
за клик: {mouse}""",
                     #image=photo,
                     bg="#00FF00",
                     font=("Arial", "15", "bold"),
                     height=5,
                     anchor="s",
                     )


btn_main = tk.Button(win, text="Жмякай",
                     command=plus,
                     bg="#b784a7",
                     activebackground="#ee9086",
                     font=("Arial", "15", "bold"),
                     width=30,
                     height=15
                     )


btn_mouse = tk.Button(win, text="Магазин",
                     command=shop,
                     bg="#b784a7",
                     activebackground="#ee9086",
                     font=("Arial", "15", "bold"),
                     width=38,
                     height=1
                     )


btn_help = tk.Button(win, text="info",
                     command=win_3,
                     bg="#b784a7",
                     activebackground="#ee9086",
                     font=("Arial", "15", "bold"),
                     width=10,
                     height=1
                     )


label_score.pack()
btn_main.place(x=115, y=175)
btn_mouse.place(x=1, y=657)
btn_help.place(x=468, y=657)
win.protocol("WM_DELETE_WINDOW", save)

win.mainloop()
