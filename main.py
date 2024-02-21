from tkinter import Tk, ttk, Frame, FALSE, NSEW, LEFT, CENTER, NW, SOLID, Button, Entry, Label
from PIL import Image, ImageTk
import requests
import json

# CORES
cor0 = '#FFFFFF'
cor1 = '#333333'
cor2 = '#38576b'

# JANELA
janela = Tk()
janela.geometry('300x320')
janela.title('conversor')
janela.configure(bg=cor0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

# DIVISÃO DE JANELA
frame_cima = Frame(janela, width=300, height=60, padx=0, pady=0, bg=cor2, relief='flat')
frame_cima.grid(row=0, column=0, columnspan=2)

frame_baixo = Frame(janela, width=300, height=260, padx=0, pady=5, bg=cor0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# FUNÇÃO CONVERTER
def converter():
    global moeda_equivalente
    moeda_de = combo_de.get()
    moeda_para = combo_para.get()
    valor_entrada = valor.get()
    
    print("Moeda de origem:", moeda_de)
    print("Moeda de destino:", moeda_para)
    print("Valor de entrada:", valor_entrada)
    
    response = requests.get('https://api.exchangerate-api.com/v4/latest/{}'.format(moeda_de))
    dados = response.json()
    
    if moeda_para in dados['rates']:
        cambio = dados['rates'][moeda_para]
        resultado = float(valor_entrada) * float(cambio)

        print("Taxa de câmbio:", cambio)
        print("Resultado da conversão:", resultado)
        
        if moeda_para == 'EUR':
            simbolo = '€'
        elif moeda_para == 'JPY':
            simbolo = '¥'
        elif moeda_para == 'USD':
            simbolo = '$'
        elif moeda_para == 'KRW':
            simbolo = '₩'
        else:
            simbolo = 'R$'

        moeda_equivalente = simbolo + "{:,.2f}".format(resultado)
        
        app_resultado.config(text=moeda_equivalente) 
    
    # Configurando a label com o resultado da conversão
    else:
        app_resultado.config(text='Moeda de destino inválida!')

    print("Resultado exibido na interface:", moeda_equivalente)
    
# FRAME CIMA
icon = Image.open('image/icon.png')
icon = icon.resize((40, 40), Image.NEAREST)
icon = ImageTk.PhotoImage(icon)

app_nome = Label(frame_cima, image=icon, compound=LEFT, text='Conversor de Moedas', height=5, pady=30, padx=30,
                 relief="raised", anchor=CENTER, font="Arial 12 bold", bg=cor2, fg=cor0)
app_nome.place(x=0, y=0)

# FRAME BAIXO

app_resultado = Label(frame_baixo, text='', width=16, height=2, relief="solid", anchor=CENTER, font="Ivy 15 bold",
                      bg=cor0, fg=cor1)
app_resultado.place(x=50, y=10)

moedas = ['BRL', 'EUR', 'JPY', 'USD', 'KRW']

# DE

app_de = Label(frame_baixo, text='De', width=8, height=1, relief="flat", anchor=NW, font="Ivy 10 bold", bg=cor0,
               fg=cor1)
app_de.place(x=48, y=90)
combo_de = ttk.Combobox(frame_baixo, width=8, justify=CENTER, font='Ivy 12 bold')
combo_de.place(x=50, y=115)
combo_de['values'] = moedas

# PARA

app_para = Label(frame_baixo, text='Para', width=8, height=1, relief="flat", anchor=NW, font="Ivy 10 bold", bg=cor0,
                 fg=cor1)
app_para.place(x=158, y=90)
combo_para = ttk.Combobox(frame_baixo, width=8, justify=CENTER, font='Ivy 12 bold')
combo_para.place(x=160, y=115)
combo_para['values'] = moedas
  
# CAIXA PARA VALORES

valor = Entry(frame_baixo, width=22, justify=CENTER, font='Ivy 12 bold', relief=SOLID)
valor.place(x=50, y=155)

# BOTÃO

botao = Button(frame_baixo, command=converter, text='CONVERTER', width=19, padx=5, height=1, bg=cor2, fg=cor0,
               font='Ivy 12 bold',
               relief='raised', overrelief=SOLID)
botao.place(x=50, y=210)

janela.mainloop()

