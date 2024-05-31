from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import mysql.connector


def validar_registro(usernameR, senhaR):
         
         try:
            conexao = mysql.connector.connect(host= 'localhost',
                                            database= 'login',
                                            user= 'root',
                                            password= 'MassaCorrida123*')
            
            cursorR = conexao.cursor()
            tabelaR = "SELECT * FROM usuarios WHERE username=%s"
            cursorR.execute(tabelaR, (usernameR,))
            resultadoR = cursorR.fetchone()

            if resultadoR:
                messagebox.showerror("Erro", "Esse username ja existe!")
            else:
                comando = "INSERT INTO usuarios (username, senha) VALUES (%s,%s)"
                cursorR.execute(comando, (usernameR, senhaR))
                conexao.commit()

                messagebox.showinfo("Sucesso!", "Registro realizado com sucesso")
                cursorR.close()
                conexao.close()

                janela_register.destroy()

         except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")



def registrar():

    global janela_register
    janela_register = Tk()
    janela_register.title("Tela de Registro")
    janela_register.geometry("+700+450")

    Label(janela_register, text="REGISTRAR").grid(row=0, column=1)

    Label(janela_register,text="Username").grid(row=1,column=0)
    usernameR_entry = Entry(janela_register)
    usernameR_entry.grid(row=1,column=1)

    Label(janela_register, text="Senha").grid(row=2, column=0)
    senhaR_entry = Entry(janela_register, show="*")
    senhaR_entry.grid(row=2, column=1)

    botao_registrar = Button(janela_register, text="Registrar", command= lambda: validar_registro(usernameR_entry.get(), senhaR_entry.get())).grid(row=3, column=1)


def validar_login():

    username = username_entry.get()
    senha = senha_entry.get()

    try:
        conexao = mysql.connector.connect(host= 'localhost',
                                  database= 'login',
                                  user= 'root',
                                  password= 'MassaCorrida123*')
        
        cursor = conexao.cursor()
        tabela = "SELECT * FROM usuarios WHERE username=%s AND senha=%s"
        cursor.execute(tabela, (username,senha))
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Erro", "Usuario ou senha incorretos!")
        
        cursor.close()
        conexao.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Nao pode se estabelecer conexao com o banco de dados, erro: {err}")



janela_login = Tk()
janela_login.title("Tela de Login")
janela_login.geometry("+700+350")

Label(janela_login, text="LOGIN").grid(row=0, column=1)

Label(janela_login,text="Username").grid(row=1,column=0)
username_entry = Entry(janela_login)
username_entry.grid(row=1,column=1)

Label(text="Senha").grid(row=2, column=0)
senha_entry = Entry(janela_login, show="*")
senha_entry.grid(row=2, column=1)

botao_login = Button(janela_login, text="Login", command=validar_login).grid(row=3, column=1)

Label(janela_login, text="Nao possui Login?").grid(row=2, column=2)
botao_register = Button(text="Registrar", command=registrar).grid(row=3, column=2)



janela_login.mainloop()