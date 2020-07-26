from sys import version as pythonV;
appV = "1.0";
from tkinter import *;
root = Tk(className = "MilkCmd");
root.geometry("620x400");
cnt = Frame(root);
cnt.grid(row = 0, column = 0);
cn2 = Frame(root);
cn2.grid(row = 1, column = 0);
inf = Entry(cnt, width = 70);
inf.grid(row = 0, column = 0);
txt = Text(cn2, width = 70, height = 400);
txt.grid(row = 0, column = 0);
srl = Scrollbar(cn2, command = txt.yview);
srl.grid(row = 0, column = 1);
txt.insert(1.0, "Made by MilkCool. Python v. " + pythonV + "\nApp v. " + appV + "\nDo not use \";\" symbol in the end of line! (Nothing will happen.)\nmc_print(string) - print something\nmc_clear() - clear the console\nmc_title(string) - set the title\n");
txt.config(state = DISABLED, yscrollcommand = srl.set);
def mc_print(text):
    global txt;
    txt.insert(END, text + "\n");
def mc_clear():
    global txt;
    txt.delete(1.0, END);
def mc_title(text):
    global root;
    root.title(text);
def exec():
    global txt, inf;
    txt.config(state = NORMAL);
    txt.insert(END, " > " + inf.get() + "\n");
    label = Label(text = str(eval(inf.get())), bg = "white", fg = "green");
    txt.insert(END, " < ");
    txt.window_create(INSERT, window = label);
    txt.insert(END, "\n");
    txt.config(state = DISABLED);
    inf.delete(0, END);
def exec_a(a):
    exec();
but = Button(cnt, text = " OK ", command = exec);
but.grid(row = 0, column = 1);
root.bind("<Return>", exec_a);
root.mainloop();
