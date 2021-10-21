import mysql.connector
from tkinter import *

# Realiza a conexão com o banco de dados
banco = mysql.connector.connect (
        host = 'localhost',
        database = 'Agenda',
        user = 'root',
        password = 'ADD YOUR PASSWORD'
        )
cursor = banco.cursor()

root = Tk()
cor = '#00FF7F'
fonte = 'Courier 12'
root.title('Agenda telefônica')
root.configure(bg = cor)
root.geometry('500x400')
root.resizable(False, False)
largura = 400
altura = 300

# Centralizar a janela
largura_ecra = root.winfo_screenwidth()
altura_ecra = root.winfo_screenheight()
posx = largura_ecra / 2 - largura / 2
posy = altura_ecra / 2 - altura / 2
root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

# Desenvolvimento da GUI
class Aplicação:
    def __init__(self, master=None):
    
        self.label_Nome = Label(
        root, 
        text = 'Digite o nome: ', 
        font = f'{fonte}',
        bg = f'{cor}'
    ).pack()

        tb_Nome = StringVar()
        tb_Nome = Entry(root, textvariable = tb_Nome)
        tb_Nome.pack()

        self.label_Número = Label(
            root, 
            text = 'Digite o telefone: ',
            font = f'{fonte}',
            bg = f'{cor}'
        ).pack()

        tb_Num = StringVar()
        tb_Num = Entry(root, textvariable = tb_Num)
        tb_Num.pack()

        self.bt_salvar = Button(
        root,
        text = 'Salvar',
        bg = f'{cor}',
        borderwidth = 4,
        relief = 'groove',
        font = f'{fonte}',
        command = lambda: salvar()
    )
        self.bt_salvar.pack()

        self.bt_Limpar = Button(
            root,
            text = 'Limpar',
            bg = f'{cor}',
            borderwidth = 4,
            relief = 'groove',
            font = f'{fonte}',
            command = lambda: limpar()
        )
        self.bt_Limpar.pack()

    def salvar():    
        cursor = banco.cursor()
        comando_sql_insert = "INSERT INTO contatos (nome, telefone) VALUES (%s, %s)"
        nome = str(tb_Nome.get())
        telefone = str(tb_Num.get())
        dados = (nome, telefone)
        cursor.execute(comando_sql, dados)
        banco.commit()

    def limpar():
        tb_Nome.delete(0, END)
        tb_Num.delete(0, END)
            
Aplicação(root)
root.mainloop()
