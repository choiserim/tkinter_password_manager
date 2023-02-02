# import module
from tkinter import *
import random
from tkinter import messagebox
import pyperclip

# ---------------------------- INSTRUCTOR PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# LIST Comprehension
password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
pasword_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

password_list = password_letters + password_symbols + pasword_numbers
random.shuffle(password_list)

password = "".join(password_list)
# password = ""
# for char in password_list:
#   password += char

print(f"Your password is: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    website_add = website_address_entry.get()
    email_user = email_user_name_entry.get()
    pass_word = made_pw_entry.get()

    # check enough entry box
    if len(website_add) == 0 or len(pass_word) == 0:
        messagebox.showinfo(title="Entry Checking", message="entry doesn't enough")
    else:
        # output new password
        # 입력된 문자열 가져오기
        global password
        password = website_add + " " + email_user + " " + pass_word
        print(f"가져온 물자열1{password}")


        # 가져온 문자열 리스트로 변환
        pw_list = []
        for i in password:
            if i == " " or i == ".":
                pass
            else:
                pw_list.append(i)
        print(pw_list)
        random.shuffle(pw_list)
        print(f"섞인 리스트{pw_list}")

        new_pw = ""
        for char in pw_list:
            print(f"{char}")
            new_pw += char
            print(new_pw)
        made_pw_entry.delete(0, END)
        made_pw_entry.insert(END, string=new_pw)

    # made clipboard
    pyperclip.copy(new_pw)
    pyperclip.paste()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    website_add = website_address_entry.get()
    email_user = email_user_name_entry.get()
    pass_word = made_pw_entry.get()

    # check enough entry box
    if len(website_add) == 0 or len(pass_word) == 0:
        messagebox.showinfo(title="Entry Checking", message="entry doesn't enough")
    else:
        is_ok = messagebox.askokcancel(title=website_add,
                                       message=f" 입력한 이메일: {email_user}\n 암호는: {pass_word} 입니다. \n 저장하시겠습니까?")

        if is_ok:
            password = website_add + " " + email_user + " " + pass_word
            test = password.replace(" ", " | ")
            print(test)
            website_address_entry.delete(0, END)
            made_pw_entry.delete(0, END)
            with open("password.txt", "a") as save:
                print("succeed save")
                save.write(test + "\n")



# ---------------------------- UI SETUP ------------------------------- #
# first make window
window = Tk()
# window.minsize(width=350, height=400)
window.title(string="Password Manager")
window.config(padx=50, pady=50)


# second import logo.png
canvas = Canvas(width=200, height=200)
key_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_img)
canvas.grid(row=0, column=1)


# third make website text label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)


# fourth make input website address entry
website_address_entry = Entry(width=35)
# input_website_address.insert(END, string="input Website address")
website_address_entry.focus()
website_address_entry.grid(row=1, column=1, columnspan=2)


# fifth make Email/Username text label
email_user_name = Label(text="Email/Username:")
email_user_name.grid(row=2, column=0)


# sixth make input  Email/Username input entry
email_user_name_entry = Entry(width=35)
# insert(index - 처음시작할거면 0, 글자가 입력된 경우 글자 끝에서 시작할거면 END, string)
address = email_user_name_entry.insert(0, string="aws@email.com")
email_user_name_entry.grid(row=2, column=1, columnspan=2)


# seventh make password text label
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)


# eighth made password entry
made_pw_entry = Entry(width=21)
# made_pw_label.insert(END, string="made pw")
made_pw_entry.grid(row=3, column=1)


# ninth make generate password button
pw_generate_button =Button(text="Generate Password", command=generate_pw)
pw_generate_button.grid(row=3, column=2)


# tenth writing make txt file button
save_button = Button(text="add", width=36, command=save_file)
save_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
