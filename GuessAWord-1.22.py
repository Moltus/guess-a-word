from tkinter import *
from tkinter import ttk
from random import randint, shuffle


class Settings(object):
    def __init__(self, master, nb_letters=6, nb_tries=3, language='english',
                 font_size=12):

        self.master = master
        self.nb_letters = IntVar()
        self.nb_letters.set(nb_letters)
        self.nb_tries = IntVar()
        self.nb_tries.set(nb_tries)
        self.language = StringVar()
        self.language.set(language)
        self.font_size = IntVar()
        self.font_size.set(font_size)


        self.frame_lang = LabelFrame(
                self.master, text=" language ", bg='light grey', fg='black',
                font=f"Helvetica {self.font_size.get()}"
                )
        self.frame_lang.grid(row=0, column=0, padx=10, pady=10)


        self.uk_img = PhotoImage(file="uk.gif")
        self.english = Radiobutton(
                self.frame_lang, variable=self.language, bg='light grey',
                value='english', font=f"Helvetica {self.font_size.get()}",
                image=self.uk_img, text='english'
                )
        self.english.grid(padx=10, pady=5, row=0, column=0)

        self.fr_img = PhotoImage(file="france.gif")
        self.french = Radiobutton(
                self.frame_lang, variable=self.language, bg='light grey',
                value='french', font=f"Helvetica {self.font_size.get()}",
                image=self.fr_img
                )
        self.french.grid(padx=10, pady=5, row=0, column=1)

        self.frame_difficulty = LabelFrame(
                self.master, text=" difficulty ", bg='light grey', fg='black',
                font=f"Helvetica {self.font_size.get()}"
                )
        self.frame_difficulty.grid(row=1, column=0, padx=10, pady=10)

        self.three_tries = Radiobutton(
                self.frame_difficulty, value=3, bg='light grey',
                text="normal, 3 tries", variable=self.nb_tries, fg='black',
                font=f"Helvetica {self.font_size.get()}"
                )
        self.three_tries.grid(padx=10, pady=5, sticky='w')

        self.one_try = Radiobutton(
                self.frame_difficulty, text="hard, only 1 try!",
                bg='light grey', fg='black', value=1, variable=self.nb_tries,
                font=f"Helvetica {self.font_size.get()}"
                )
        self.one_try.grid(padx=10, pady=5, sticky='w')

        self.frame_nb_letters = LabelFrame(
                self.master, text=" letters ", bg='light grey', fg='black',
                font=f"Helvetica {self.font_size.get()}"
                )
        self.frame_nb_letters.grid(row=0, column=1, padx=10, pady=10)

        self.five_letter = Radiobutton(
                self.frame_nb_letters, text=5, bg='light grey', fg='black',
                variable=self.nb_letters, value=5,
                font=f"Helvetica {self.font_size.get()}"
                )
        self.five_letter.grid(padx=10, pady=5, row=0, column=0)

        self.six_letter = Radiobutton(
                self.frame_nb_letters, text=6, value=6,
                variable=self.nb_letters, bg='light grey', fg='black',
                font=f"Helvetica {self.font_size.get()}"
                )
        self.six_letter.grid(padx=10, pady=5, row=0, column=1)

        self.seven_letter = Radiobutton(
                self.frame_nb_letters, text=7, bg='light grey', fg='black',
                value=7, font=f"Helvetica {self.font_size.get()}",
                variable=self.nb_letters
                )
        self.seven_letter.grid(padx=10, pady=5, row=0, column=2)

        self.frame_fontsize = LabelFrame(
                self.master, text=" font size ", bg='light grey', fg='black',
                font=f"Helvetica {self.font_size.get()}"
                )
        self.frame_fontsize.grid(row=1, column=1, padx=10, pady=10)

        self.font12 = Radiobutton(
                self.frame_fontsize, text="Helvetica 12 / 20",
                bg='light grey', fg='black', variable=self.font_size, value=12,
                font=f"Helvetica {self.font_size.get()}",
                command=self.change_font
                )
        self.font12.grid(padx=10, pady=5, sticky='w')

        self.font15 = Radiobutton(
                self.frame_fontsize, text="Helvetica 15 / 25", bg='light grey',
                fg='black', font=f"Helvetica {self.font_size.get()}",
                variable=self.font_size, value=15, command=self.change_font
                )
        self.font15.grid(padx=10, pady=5, sticky='w')

        self.font18 = Radiobutton(
                self.frame_fontsize, text="Helvetica 18 / 30", bg='light grey',
                fg='black', font=f"Helvetica {self.font_size.get()}",
                variable=self.font_size, value=18, command=self.change_font
                )
        self.font18.grid(padx=10, pady=5, sticky='w')

        self.button = Button(self.master, text="confirm choices",
                             font=f"Helvetica {self.font_size.get()}",
                             command=self.confirm_choices)
        self.button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def confirm_choices(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        global app
        app = App(root, self.nb_letters.get(), self.nb_tries.get(),
                  self.language.get(), self.font_size.get())


    def change_font(self):
        for widget in self.master.winfo_children():
            widget.configure(font = f"Helvetica {self.font_size.get()}")
        for lang in self.frame_lang.winfo_children():
            lang.configure(font = f"Helvetica {self.font_size.get()}")
        for diff in self.frame_difficulty.winfo_children():
            diff.configure(font = f"Helvetica {self.font_size.get()}")
        for letters in self.frame_nb_letters.winfo_children():
            letters.configure(font = f"Helvetica {self.font_size.get()}")
        for size in self.frame_fontsize.winfo_children():
            size.configure(font = f"Helvetica {self.font_size.get()}")



class App(object):
    def __init__(self, master, nb_letters, nb_tries, language, font_size,
                 word_num=0):

        self.master = master
        self.nb_letters = nb_letters
        self.nb_tries = nb_tries
        self.language = language
        self.font_size = font_size
        self.canvas_size = (self.nb_letters*100, self.nb_letters*40)
        self.canvas_image = PhotoImage(file="image_bg.gif")

        self.word_num = word_num
        self.rem_tries = self.nb_tries
        self.total_score = 0
        self.word_score = 0

        self.guesses = []
        self.letters = None
        self.write_animation = None
        self.word_to_guess = None
        self.current_word = None
        self.pinfo_inc = 0

        self.word_txt = open(f"{self.nb_letters}letters_{self.language}.txt")
        self.word_list = self.word_txt.read().split()

        self.tries_label = Label(
                self.master, font=f"Helvetica {self.font_size}",
                bg='light grey', fg='black'
                )
        self.tries_label.grid(row=0, padx=10, pady=10, sticky=W)

        self.score_label = Label(
                self.master, font=f"Helvetica {self.font_size}",
                text=f"total score : {self.total_score}",
                bg='light grey', fg='black'
                )
        self.score_label.grid(row=0, padx=10, pady=10, sticky=E)

        self.player_info = Label(
                self.master, bg='light grey', fg='black', text='',
                justify=CENTER, font=f"Helvetica {self.font_size}"
                )
        self.player_info.grid(row=1)

        self.canvas_frame = LabelFrame(self.master, bg='light grey', fg='black')
        self.canvas_frame.grid(row=2, padx=30, pady=10)
        self.canvas = Canvas(self.canvas_frame, width=self.canvas_size[0],
                             height=self.canvas_size[1], bg='light grey',
                             highlightthickness=0)
        self.canvas.grid(padx=0, pady=0)
        self.canvas.create_image(0, 0, image=self.canvas_image, anchor=NW)
        self.canvas.update()

        self.current_guess = StringVar()
        self.info_word = Label(self.master, font=f"Helvetica {self.font_size}",
                               textvariable=self.current_guess,
                               bg='light grey', fg='black')
        self.info_word.grid(row=3, pady=10, sticky=N)

        self.settings_btn = Button(self.master, command=self.get_settings,
                            text="settings", font=f"Helvetica {self.font_size}")
        self.settings_btn.grid(row=3, padx=30, pady=10, sticky=W)
        self.confirm_btn = Button(self.master, text="verify word",
                                  font=f"Helvetica {self.font_size}",
                                  command=self.check_word)
        self.confirm_btn.grid(row=3, padx=30, pady=10, sticky=E)

        self.get_new_word(True)



    def write_word(self):
        self.letters.sort(key=lambda letter: letter.x0)
        self.current_word = ''
        for letter in self.letters:
            self.current_word += letter.character
        self.current_guess.set("your word : " + self.current_word)

    def check_word(self):

        def right_answer():
            self.word_score += self.rem_tries + 2
            self.total_score += self.rem_tries + 2
            self.score_label['text'] = f"total score : {self.total_score}"
            for l in self.letters:
                l.set_ball_color((105, 205, 105))
            for l in self.letters:
                l.set_outline_color('green2')
            self.write_info(" You found the correct word! You "
                            f"scored {self.word_score} points ")
            self.current_guess.set("Congratulations!")
            self.confirm_btn['text'] = "next word"
            self.confirm_btn['command'] = self.get_new_word

        def wrong_answer():
            self.rem_tries -= 1
            self.tries_label['text'] = (
                        f"word {self.word_num}  |  tries : {self.rem_tries}"
                        )

            def valid_word():
                self.write_info(f" This is a valid {self.nb_letters}"
                                " word, just not the one ")
                if self.rem_tries == 0:
                    self.word_score += 2
                    self.total_score += 2
                    self.score_label['text'] = ("total score : "
                                               f"{self.total_score}")
                    self.guesses = []
                    for l in self.letters:
                        l.set_ball_color((205, 205, 105))
                    for l in self.letters:
                        l.set_outline_color('yellow2')
                    self.write_info(" Not the one, but a valid word!"
                                    f" You scored {self.word_score} points ")
                    self.current_guess.set(
                                        f"the word was : {self.word_to_guess}"
                                        )
                    if self.word_num == 10:
                        self.confirm_btn['text'] = "your score"
                        self.confirm_btn['command'] = self.score_screen

                    else:
                        self.confirm_btn['text'] = "next word"
                        self.confirm_btn['command'] = self.get_new_word

                else:
                    self.word_score += 2
                    self.total_score += 2
                    self.score_label['text'] = ("total score : "
                                               f"{self.total_score}")
                    self.current_guess.set("+2 points! Keep searching!")
                    for l in self.letters:
                        l.fade_color((205, 205, 5), (255, 255, 255), 50,
                                     self.write_info)
                    self.guesses.append(self.current_word)

            def invalid_word():
                if self.rem_tries == 0:
                    self.guesses = []
                    for l in self.letters:
                        l.set_ball_color((205, 105, 105))
                    for l in self.letters:
                        l.set_outline_color('firebrick2')
                    self.write_info(" You failed to find the word!"
                                    f" You scored {self.word_score} points ")
                    self.current_guess.set(
                            f"the word was : {self.word_to_guess}"
                            )
                    if self.word_num == 10:
                        self.confirm_btn['text'] = "your score"
                        self.confirm_btn['command'] = self.score_screen
                    else:
                        self.confirm_btn['text'] = "next word"
                        self.confirm_btn['command'] = self.get_new_word
                else:
                    self.write_info(" Wrong! You still have "
                                    f"{self.rem_tries} {self.gram_tries()} ")
                    for l in self.letters:
                        l.fade_color((205, 105, 105), (255, 255, 255), 50,
                                     self.write_info)

            if (self.current_word.lower() in self.word_list and
                self.current_word not in self.guesses):
                valid_word()

            else:
                invalid_word()

        # found the word
        if self.current_word == self.word_to_guess:
            right_answer()
        # haven't found the word
        else:
            wrong_answer()


    def write_info(self, text=None):
        def add_letter():
            if self.pinfo_inc <= len(text):
                self.pinfo_inc += 1
                self.player_info['text'] = text[:self.pinfo_inc]
                self.write_animation = self.master.after(33, add_letter)
            else:
                self.write_animation = None


        if self.write_animation:
            self.master.after_cancel(self.write_animation)

        self.pinfo_inc = 0
        if not text:
            text = " Try to form the correct word "
        add_letter()

    def gram_tries(self):
        if self.rem_tries == 1:
            return 'try'
        else:
            return 'tries'

    def get_new_word(self, init=None):

        if not init:
            self.canvas.delete("balls")

        if self.word_num == 10:
            self.word_num = 0

        self.word_to_guess = (
                    self.word_list[randint(0, len(self.word_list)-1)].upper()
                    )
        self.disordered_word = list(self.word_to_guess)
        shuffle(self.disordered_word)
        self.current_word = ''.join(self.disordered_word)

        self.current_guess.set("your word : " + self.current_word)

        self.letters = []
        self.word_score = 0
        n = 0
        for l in self.disordered_word:
            letter = DragBall(self.master, self.canvas, self.canvas_size,
                            self.nb_letters, n, l, "letter")
            self.letters.append(letter)
            n += 1

        self.rem_tries = self.nb_tries
        self.word_num += 1
        self.confirm_btn['text'] = "verify word"
        self.confirm_btn['command'] = self.check_word
        self.write_info(" Try to form the correct word ")
        self.tries_label['text'] = (f"word {self.word_num}  |  "
                                    f"tries : {self.rem_tries}")



    def score_screen(self):

        self.canvas.delete("balls")


        line1_str = "SCORE:"
        line2_str = f"{self.total_score}"


        line1 = []

        n = 0
        for c in line1_str:
            if c == " ":
                pass
            else:
                l1 = CharBall(self.master, self.canvas, self.canvas_size,
                                len(line1_str), n, c, "score_l1", line=1)
                line1.append(l1)
            n += 1

        line2 = []
        n = 0
        for c in line2_str:
            if c == " ":
                pass
            else:
                l2 = CharBall(self.master, self.canvas, self.canvas_size,
                                len(line2_str), n, c, "score_l2", line=2)
                line2.append(l2)
            n += 1


        def gradient(balls):
            for b in balls:
                if b == balls[0]:
                    b.set_ball_color((205, 105, 105))
                    c = (205, 105, 105)
                else:
                    if c == (205, 105, 105):
                        b.set_ball_color((105, 205, 105))
                        c = (105, 205, 105)

                    elif c == (105, 205, 105):
                        b.set_ball_color((205, 205, 105))
                        c = (205, 205, 105)

                    elif c == (205, 205, 105):
                        b.set_ball_color((205, 105, 105))
                        c = (205, 105, 105)
                b.fade_rgb()



        gradient(line1+line2)

        self.current_guess.set("")
        self.write_info(" ")
        self.confirm_btn['text'] = "new words"
        self.confirm_btn['command'] = self.get_new_word


    def get_settings(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        settings.__init__(self.master, self.nb_letters, self.nb_tries,
                          self.language, self.font_size)



class CharBall(object):

    ball_diameter = 72
    ball_font_size = 25

    def __init__(self, master, canvas, canvas_size, nb_letters, index,
                 character, tag, line=0):

        self.master = master
        self.canvas = canvas
        self.canvas_size = canvas_size
        self.nb_letters = nb_letters
        self.index = index
        self.character = character
        self.tag = tag


        self.ball_color = [255, 255, 255]
        self.fade_animation = None

        self.x0 = ((self.canvas_size[0]-self.nb_letters*
                   CharBall.ball_diameter)/2 +
                   self.index*CharBall.ball_diameter)

        if line == 1:
            self.y0 = self.canvas_size[1]/2 - CharBall.ball_diameter
        elif line == 2:
            self.y0 = self.canvas_size[1]/2
        else:
            self.y0 = self.canvas_size[1]/2 - CharBall.ball_diameter/2
        self.x1 = self.x0 + CharBall.ball_diameter
        self.y1 = self.y0 + CharBall.ball_diameter

        self.create_ball()

    def create_ball(self):

        self.circle = self.canvas.create_oval(
                self.x0, self.y0, self.x1, self.y1,
                fill='white', tags=(f"{self.tag}_{self.index}",
                f"{self.tag}_balls", "balls"),
                width=5, outline='light slate grey'
                )
        self.txt = self.canvas.create_text(
                (self.x0+self.x1)/2, (self.y0+self.y1)/2, text=self.character,
                font=f'Helvetica {CharBall.ball_font_size} bold',
                tags=(f"{self.tag}_{self.index}", f"{self.tag}_balls", "balls")
                )


    def set_ball_color(self, in_color):

        self.ball_color[:] = in_color[:]

        if self.fade_animation:
            self.master.after_cancel(self.fade_animation)

        self.canvas.itemconfigure(self.circle, fill='#%02x%02x%02x' % (
                    self.ball_color[0], self.ball_color[1], self.ball_color[2]))

    def set_outline_color(self, color):

        self.canvas.itemconfigure(self.circle, outline=color)

    def fade_color(self, in_color, out_color, delay, end_func):
        def animation():
            self.ball_color[0] += fade_inc[0]
            self.ball_color[1] += fade_inc[1]
            self.ball_color[2] += fade_inc[2]
            self.set_ball_color(self.ball_color[:])

            if (self.ball_color[0] == out_color[0] and
                self.ball_color[1] == out_color[1] and
                self.ball_color[2] == out_color[2]):

                self.set_ball_color(out_color)
                self.fade_animation = None
                if end_func:
                    end_func()
            else:
                self.fade_animation = self.master.after(delay, animation)

        self.set_ball_color(in_color)
        fade_inc = (round((out_color[0]-in_color[0])/50),
                    round((out_color[1]-in_color[1])/50),
                    round((out_color[2]-in_color[2])/50))
        animation()

    def fade_rgb(self):
        if self.ball_color == [205, 105, 105]:
            self.fade_color((205, 105, 105), (205, 205, 105), 20, self.fade_rgb)
        elif self.ball_color == [205, 205, 105]:
            self.fade_color((205, 205, 105), (105, 205, 105), 20, self.fade_rgb)
        elif self.ball_color == [105, 205, 105]:
            self.fade_color((105, 205, 105), (205, 105, 105), 20, self.fade_rgb)





class DragBall(CharBall):

    def __init__(self, master, canvas, canvas_size, nb_letters, index, character, tag):
        self.master = master
        self.canvas = canvas
        self.canvas_size = canvas_size
        self.nb_letters = nb_letters
        self.index = index
        self.character = character
        self.tag = tag

        self.selected = False
        self.ball_color = [255, 255, 255]
        self.fade_animation = None

        self.column_width = self.canvas_size[0] / self.nb_letters
        self.x0 = randint(self.index*self.column_width+1,
                          ((self.index+1)*self.column_width -
                          CharBall.ball_diameter))

        self.x1 = self.x0 + CharBall.ball_diameter
        self.y0 = randint(1, self.canvas_size[1]-CharBall.ball_diameter-1)
        self.y1 = self.y0 + CharBall.ball_diameter

        self.create_ball()

        self.canvas.tag_bind(f"{self.tag}_{self.index}", '<Enter>',
                             self.on_enter)
        self.canvas.tag_bind(f"{self.tag}_{self.index}", '<Leave>',
                             self.on_leave)
        self.canvas.tag_bind(f"{self.tag}_{self.index}", '<1>',
                             self.on_click)
        self.canvas.tag_bind(f"{self.tag}_{self.index}", '<B1-Motion>',
                             self.on_drag)
        self.canvas.tag_bind(f"{self.tag}_{self.index}", '<ButtonRelease-1>',
                             self.on_release)

    def on_enter(self, event):
        self.canvas.itemconfigure(self.circle, outline='green2')


    def on_leave(self, event):
        if not self.selected:
            self.canvas.itemconfigure(self.circle, outline='light slate grey')
        else:
            self.canvas.itemconfigure(self.circle, outline='green2')

    def on_click(self, event):
        self.selected = True
        self.canvas.itemconfigure(self.circle, outline='green2')
        self.canvas.tag_raise(f"{self.tag}_{self.index}")
        self.lastx, self.lasty = event.x, event.y


    def on_drag(self, event):
        self.seleted = True
        x_move = event.x - self.lastx
        y_move = event.y - self.lasty
        if (self.canvas.coords(f"{self.tag}_{self.index}")[0] <= 0 and
                              x_move <=0):
            x_move = 0
        elif (self.canvas.coords(f"{self.tag}_{self.index}")[2] >=
              self.canvas_size[0] and x_move >= 0):
            x_move = 0

        if (self.canvas.coords(f"{self.tag}_{self.index}")[1] <= 0 and
                              y_move <= 0):
            y_move = 0
        elif (self.canvas.coords(f"{self.tag}_{self.index}")[3] >=
              self.canvas_size[1] and y_move >= 0):
            y_move = 0


        self.canvas.move(f"{self.tag}_{self.index}", x_move, y_move)
        self.lastx = event.x
        self.lasty = event.y

    def on_release(self, event):
        self.selected = False
        self.x0, self.x1, self.y0, self.y1 = self.canvas.coords(
                    f"{self.tag}_{self.index}")
        app.write_word()


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.configure(background='light grey')
root.title("Find a Word")

settings = Settings(root)

root.mainloop()
