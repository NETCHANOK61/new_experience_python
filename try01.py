# library create GUI Desktop App
import tkinter as tk
def calcualtor():
    number = int(text_input.get()) #ดึงข้อความที่กรอกเข้ามาใน text_input มาใช้งาน
    if number == 0:
        result_area.configure(text='Am I Wrong?')
        return
    output = ''
    for i in range(1, 13):
        output += str(number) + 'X' + str(i) + '=' + str(number*i) + '\n'
    result_area.configure(text=output)

window = tk.Tk()
window.title('MyTest')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='Number')
title_label.pack(pady=20) #pady = ระยะห่างแกนตั้ง padx = ระยะห่างแกนนอน

text_input = tk.Entry(master=window, width=15)
text_input.pack()

button_submit = tk.Button(master=window, text='Okay', command=calcualtor, width=10, height=1)
# when click button function set_message will process = command
button_submit.pack(pady=20)

result_area = tk.Label(master=window)
result_area.pack(pady=20)

#click run code = open window app
window.mainloop()
