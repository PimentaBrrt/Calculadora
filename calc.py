# Importação de Funções

from tkinter import *
from math import log

# Funções

def botao_clicar(n):
    atual = e.get()
    e.delete(0, END)
    e.insert(0, atual + str(n))

def botao_limpar():
    e.delete(0, END)

def botao_somar():
    n1 = e.get()
    global p_num
    global math
    math = "+"
    p_num = float(n1)
    e.delete(0, END)

def botao_igual():
    def exponencial(a, b):
        if b == 0: return 1
        return a * exponencial(a, b - 1)
    n2 = float(e.get())
    e.delete(0, END)
    try:
        if math == "+":
            e.insert(0, p_num + n2)
        elif math == "-":
            e.insert(0, p_num - n2)
        elif math == "*":
            e.insert(0, p_num * n2)
        elif math == "/":
            e.insert(0, p_num / n2)
        elif math == "^":
            e.insert(0, exponencial(p_num, n2))
        elif math == "log":
            e.insert(0, log(p_num, n2))
        else:
            e.insert(0, n2)
    except:
        e.insert(0, n2)
        
def botao_subtrair():
    n1 = e.get()
    global p_num
    global math
    math = "-"
    p_num = float(n1)
    e.delete(0, END)
    
def botao_multiplicar():
    n1 = e.get()
    global p_num
    global math
    math = "*"
    p_num = float(n1)
    e.delete(0, END)   

def botao_dividir():
    n1 = e.get()
    global p_num
    global math
    math = "/"
    p_num = float(n1)
    e.delete(0, END)

def botao_raiz():
    n1 = float(e.get())
    if n1 >= 0:
        num = n1 ** (1 / 2)
    else:
        num = "Números complexos não inclusos."
    e.delete(0, END)
    e.insert(0, num)

def botao_exponenciacao():
    n1 = e.get()
    global p_num
    global math
    math = "^"
    p_num = float(n1)
    e.delete(0, END)

def botao_fatorial():
    def fatorial(a):
        if a <= 1: return 1
        return a * fatorial(a - 1)
    n1 = float(e.get())
    if n1 >= 0 and n1.is_integer():
        num = int(fatorial(n1))
    else:
        num = "Número inválido. Deve ser positivo e inteiro."
    e.delete(0, END)
    e.insert(0, num)

def botao_log():
    n1 = e.get()
    global p_num
    global math
    math = "log"
    p_num = float(n1)
    e.delete(0, END)

# Layout

janela = Tk()
janela.title("Calculadora básica")

e = Entry(janela, width=55, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botao_1 = Button(janela, text="1", padx=40, pady=20, bg="#ADDFFF", command=lambda: botao_clicar(1))
botao_2 = Button(janela, text="2", padx=40, pady=20, bg="#ADDFFF", command=lambda: botao_clicar(2))
botao_3 = Button(janela, text="3", padx=40, pady=20, bg="#ADDFFF", command=lambda: botao_clicar(3))
botao_4 = Button(janela, text="4", padx=40, pady=20, bg="#ADDFFF", command=lambda: botao_clicar(4))
botao_5 = Button(janela, text="5", padx=40, pady=20, bg="#ADDFFF", command=lambda: botao_clicar(5))
botao_6 = Button(janela, text="6", padx=40, pady=20, bg="#ADDFFF", command=lambda: botao_clicar(6))
botao_7 = Button(janela, text="7", padx=40, pady=20, bg="#ADDFFF", command=lambda: botao_clicar(7))
botao_8 = Button(janela, text="8", padx=40, pady=20, bg="#ADDFFF", command=lambda: botao_clicar(8))
botao_9 = Button(janela, text="9", padx=40, pady=20, bg="#ADDFFF", command=lambda: botao_clicar(9))
botao_0 = Button(janela, text="0", padx=40, pady=20, bg="#ADDFFF", command=lambda: botao_clicar(0))

botao_somar = Button(janela, text="+", padx=39, pady=20, bg="#D1EAF0", command=botao_somar)
botao_igual = Button(janela, text="=", padx=90, pady=20, bg="#D1EAF0", command=botao_igual)
botao_limpar = Button(janela, text="Limpar", padx=76, pady=20, bg="#D1EAF0", command=botao_limpar)

botao_subtrair = Button(janela, text="-", padx=41, pady=20, bg="#D1EAF0", command=botao_subtrair)
botao_multiplicar = Button(janela, text="*", padx=40, pady=20, bg="#D1EAF0", command=botao_multiplicar)
botao_dividir = Button(janela, text="/", padx=41, pady=20, bg="#D1EAF0", command=botao_dividir)

botao_raiz = Button(janela, text="√", padx=41, pady=20, bg="#D1EAF0", command=botao_raiz)
botao_exponenciacao = Button(janela, text="^", padx=40, pady=20, bg="#D1EAF0", command=botao_exponenciacao)
botao_fatorial = Button(janela, text="!", padx=41, pady=20, bg="#D1EAF0", command=botao_fatorial)
botao_log = Button(janela, text="log", padx=34, pady=20, bg="#D1EAF0", command=botao_log)

botao_1.grid(row=3, column=0)
botao_2.grid(row=3, column=1)
botao_3.grid(row=3, column=2)

botao_4.grid(row=2, column=0)
botao_5.grid(row=2, column=1)
botao_6.grid(row=2, column=2)

botao_7.grid(row=1, column=0)
botao_8.grid(row=1, column=1)
botao_9.grid(row=1, column=2)

botao_0.grid(row=4, column=0)

botao_somar.grid(row=5, column=0)
botao_igual.grid(row=5, column=1, columnspan=2)
botao_limpar.grid(row=4, column=1, columnspan=2)

botao_subtrair.grid(row=6, column=0)
botao_multiplicar.grid(row=6, column=1)
botao_dividir.grid(row=6, column=2)

botao_raiz.grid(row=1, column=3)
botao_exponenciacao.grid(row=2, column=3)
botao_fatorial.grid(row=3, column=3)
botao_log.grid(row=4, column=3)

janela.mainloop()