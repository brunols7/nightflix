import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import pandas as pd
import sqlite3
from functools import partial

#connection
conn = sqlite3.connect('nf.db')
cc = conn.cursor()

#Aparencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#janela do login
janela = ctk.CTk()
janela.resizable(0, 0)
janela.geometry("680x380")
janela.title("Sistema de login")
janela.iconbitmap("icon.ico")
janela.resizable(False, False)

#imagem da esquerda
img = PhotoImage(file="Net.png",)
label_img= ctk.CTkLabel(master= janela, image=img, text_color= "red")
label_img.place(x=-20, y=-3)

label_tt = ctk.CTkLabel(master= janela, text= "Entre em sua conta", font=("Roboto", 18), text_color= "#FF0000")

#frame da direita
Login_frame = ctk.CTkFrame(master= janela, width= 350, height= 396)
Login_frame.pack(side=RIGHT)

label = ctk.CTkLabel(master=Login_frame, text='Faça o Login', font = ('Roboto', 20, 'bold'), text_color= ("red") )
label.place(x=25, y=25)

#campo de usuario e senha
username_login  = ctk.CTkEntry(master =Login_frame, placeholder_text="Email", width= 300, font=("Roboto", 14)).place(x=25, y=105)
label1 = ctk.CTkLabel(master= Login_frame, text="*Este campo é obrigatorio.", text_color="green", font=("Roboto", 8)). place(x=25, y=135)

Password_login =ctk.CTkEntry(master =Login_frame, placeholder_text="Senha", width= 300, font=("Roboto", 14), show="*").place(x=25, y=175)
label2 = ctk.CTkLabel(master= Login_frame, text="*Este campo é obrigatorio.", text_color="green", font=("Roboto", 8)). place(x=25, y=205)

#caixa para manter conectado
chekbox = ctk.CTkCheckBox(master=Login_frame, text="Mantenha-me conectado",).place (x=25, y=235)

#filmes
def mostrar_filmes(tree, categoria_id=None):
    conn = sqlite3.connect('nf.db')
    if categoria_id is None:
        df = pd.read_sql('SELECT filme_id, titulo FROM filmes', conn)
    else:
        df = pd.read_sql(f'SELECT filme_id, titulo FROM filmes WHERE categoria_id = {categoria_id}', conn)

    # Limpa a tabela (remove todas as linhas)
    for item in tree.get_children():
        tree.delete(item)

    for index, row in df.iterrows():
        tree.insert("", "end", values=(row[0], row[1]))

#series
def mostrar_series(tree, categoria_id=None):
    conn = sqlite3.connect('nf.db')
    if categoria_id is None:
        df = pd.read_sql('SELECT serie_id, titulo FROM series', conn)
    else:
        df = pd.read_sql(f'SELECT serie_id, titulo FROM series WHERE categoria_id = {categoria_id}', conn)

    # Limpa a tabela (remove todas as linhas)
    for item in tree.get_children():
        tree.delete(item)

    for index, row in df.iterrows():
        tree.insert("", "end", values=(row[0], row[1]))

#janela 2
def nova_janela():
    nova_janela = tk.Toplevel(janela)
    nova_janela.resizable(0, 0)
    nova_janela.configure(bg="#212121")
    nova_janela.geometry("680x380")
    nova_janela.iconbitmap("icon.ico")
    nova_janela.title("Sistema de Escolha")

    # Crie uma tabela para exibir os dados
    tree = ttk.Treeview(nova_janela, columns=("ID", "Título"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Título", text="Título")
    tree.place(x=150, y=0)
    tree.pack()

    #font
    fonte = ("Arial", 10, "bold")

    #Botão "Filmes"
    filmes_button = tk.Button(nova_janela, text="Filmes", command=lambda: mostrar_filmes(tree), bg="#be2929", font=fonte, borderwidth=2)
    filmes_button.place(x=570, y=25)


    #Botão "Séries"
    series_button = tk.Button(nova_janela, text="Séries", command=lambda: mostrar_series(tree), bg="#be2929", font=fonte, borderwidth=2)
    series_button.place(x=50, y=25)


    #Botões de filtro por categoria
    categorias = {
        1: "Comédia",
        2: "Ação",
        3: "Drama",
        4: "Ficção Científica",
        5: "Terror",
        6: "Documentário",
        7: "Desenho Animado"
    }  # IDs das categorias
    #Botoes categoria
    for categoria_id, nome_categoria in categorias.items():
        categoria_button = tk.Button(nova_janela, text=f"{nome_categoria}",
                                     command=lambda cid=categoria_id: mostrar_filmes(tree, categoria_id=cid))
        categoria_button.pack(side=tk.LEFT, padx=10, expand=True)

#LOGIN

def login():
        msg= messagebox.showinfo(title= "Estado de login", message= "Parabéns! Login realizado com sucesso.")
        pass
login_button = ctk.CTkButton(master=Login_frame, text='ENTRAR', width =300, command= nova_janela).place(x=25, y=285)





#botão para cadastrar
def tela_register():
    Login_frame.pack_forget()

    rg_frame = ctk.CTkFrame(master=janela, width= 350, height= 396)
    rg_frame.pack(side= RIGHT)

    label= ctk.CTkLabel(master =rg_frame, text="Realize seu cadastro", font=("Roboto", 20)).place(x=25, y=5)
    
    span = ctk.CTkLabel(master= rg_frame, text="*Por favor preencha todos os campos", font=("Roboto", 12), text_color ="red").place(x=25, y= 45)

    user_login  = ctk.CTkEntry(master =rg_frame, placeholder_text="Nome completo", width= 300, font=("Roboto", 14)).place(x=25, y=85)

    email_login  = ctk.CTkEntry(master =rg_frame, placeholder_text="E-mail", width= 300, font=("Roboto", 14)).place(x=25, y=125)

    password_login  = ctk.CTkEntry(master =rg_frame, placeholder_text="Senha", width= 300, font=("Roboto", 14), show="*").place(x=25, y=165)

    cPassword_login  = ctk.CTkEntry(master =rg_frame, placeholder_text="Confirmar senha", width= 300, font=("Roboto", 14), show="*").place(x=25, y=205)

    chekbox = ctk.CTkCheckBox(master=rg_frame, text="Aceito os Termos e Politicas de uso",).place (x=25, y=245)
    
    ver_senha = ctk.CTkCheckBox(master= rg_frame, text="Revelar senha", font=("Century Gothic bold", 12), corner_radius =20 ).place (x=220, y=245)
    

    def back():
        rg_frame.pack_forget()

        Login_frame.pack(side=RIGHT)

    
    back_button = ctk.CTkButton(master=rg_frame, text='VOLTAR', width =145, fg_color="red", command= back).place(x=25, y=300)

    def save_user():
        msg = messagebox.showinfo(title= "Estado do cadastro", message = "Parbéns Usuario criado com sucesso")
        pass
    save_button = ctk.CTkButton(master=rg_frame, text='Criar Conta', width =145, fg_color="green").place(x=180, y=300)


    

register_span = ctk.CTkLabel(master= Login_frame, text= "Se não tiver uma conta" ).place(x=25, y=325)
register_button = ctk.CTkButton(master=Login_frame, text='CADASTRE-SE', width =150, fg_color="green", hover_color= "#2D9334", command= tela_register).place(x=175, y=325)

janela.mainloop()
