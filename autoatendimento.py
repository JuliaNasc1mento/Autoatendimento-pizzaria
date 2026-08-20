#Disciplina: Programação estruturada e orientada a objetos
#Turma: INFO2V
#Discentes: Jamylli Santiago Falcão Silvestre
#           Julia da Silva Nascimento
#           Maria Eloisa de Lima Silva
#           Saul Vitório Batista Reis do Nascimento
#==============================================================================================================================================================#
#importações
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import tkinter as tk

#Janela_02 ("Solicitar dados dos usuarios não cadastrados.") ==================================================================================================#
def imagem_fundo():
    def janela_2():
        abrir_janela2 =tk.Toplevel()
        abrir_janela2.title('Cadastro de usuário.')
        abrir_janela2.geometry('1350x1230')
        abrir_janela2.configure(background = '#ffb90f')
        abrir_janela2.maxsize(width = 1350, height = 1230)
        abrir_janela2.minsize(width = 500, height = 500)

        #Alterando icone da janela 2
        icone_caminho = "Projeto_4°bim/logo.ico"
        abrir_janela2.wm_iconbitmap(icone_caminho)

        #Adicionando Frames a janela 2
        frame_2 = Frame(abrir_janela2, background = '#0D0D0D')
        frame_2.place(relx = 0.01, rely= 0.01, relwidth = 0.9785, relheight = 0.54)

        #Adicionado fundo
        fundo = Image.open('Projeto_4°bim/fundo2.png')
        tamanho_fundo = fundo.resize((1316, 661))
        fundo_tk = ImageTk.PhotoImage(tamanho_fundo)

        label_fundo = ttk.Label(frame_2, image = fundo_tk)
        label_fundo.image = fundo_tk
        label_fundo.place(x = 0, y = 0)

        #Fazendo os dados da janela 2 irem para um arquivo txt
        def salvar_dados():
            nome = entry_nome.get()
            login = entry_login.get()
            senha = entry_senha.get()
            telefone = entry_telefone.get()
            email = entry_email.get()

            if not nome or not login or not senha or not telefone:
                messagebox.showinfo('Campos incompletos', 'Por favor, preencha todos os campos antes de cadastrar.')
                
            else:
                messagebox.showinfo('Sucesso', f'Cadastro realizado!') 
                abrir_janela2.quit()

            # Dados a serem salvos
            dados = f"Nome: {nome}\nLogin: {login}\nSenha: {senha}\nTelefone: {telefone}\nEmail: {email}\n\n"

            # Salvar os dados em um arquivo txt
            with open('cadastro_usuarios.txt', 'a') as arquivo:
                arquivo.write(dados)

            abrir_janela2.destroy()

        #Adicionando widget-Label 'Digite seu nome'
        ttk.Label(frame_2, text = 'Digite seu nome:', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 50, y = 25)
        entry_nome = ttk.Entry(frame_2)
        entry_nome.place(x = 180, y = 27, width = 217)

        #Adicionando widget-labe 'Login'
        ttk.Label(frame_2, text = 'Crie seu login:', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 50, y = 65)
        entry_login = ttk.Entry(frame_2)
        entry_login.place(x = 165, y = 67, width = 232)

        #Adicionando widget-Label 'Digite sua senha'
        ttk.Label(frame_2, text = 'Crie sua senha:', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 50, y = 105)
        entry_senha = ttk.Entry(frame_2)
        entry_senha.place(x = 172, y = 107, width = 225)

        #Adicionando widget-label 'Digite seu telefone'
        ttk.Label(frame_2, text = 'Digite seu telefone:', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 50, y = 145)
        entry_telefone = ttk.Entry(frame_2)
        entry_telefone.place(x = 197, y = 147, width = 200)

        #Adicionando widget-label 'Digite seu email'
        ttk.Label(frame_2, text = 'Digite seu email:', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 50, y = 185)
        entry_email = ttk.Entry(frame_2)
        entry_email.place(x = 187, y = 187, width = 210)

        #Adicionando widget-botão 'cadastrar'
        ttk.Button(frame_2, text = 'Cadastrar', command = salvar_dados).place(x = 600, y = 210)

        #Adicionando botão 'cancelar'
        ttk.Button(frame_2, text = 'Cancelar', command = abrir_janela2.destroy).place(x = 700, y = 210)

        abrir_janela2.mainloop()

    janela_2()

#Janela_03 ("Área principal, fazer pedido.") ==================================================================================================================#
def janela3():
    abrir_janela3 = tk.Toplevel(abrir_janela1)
    abrir_janela3.title('Faça seu pedido!')
    abrir_janela3.geometry('1350x1230')
    abrir_janela3.configure(background = '#ffb90f')
    abrir_janela3.maxsize(width = 1350, height = 1230)
    abrir_janela3.minsize(width = 500, height = 500)

    #Alterando icone da janela 3
    icone_caminho = "Projeto_4°bim/logo.ico"
    abrir_janela3.wm_iconbitmap(icone_caminho)

    #Criando frame 3
    frame_3 = Frame(abrir_janela3, background = '#0D0D0D')
    frame_3.place(relx = 0.01, rely = 0.01, relwidth = 0.49, relheight = 0.539)

    ttk.Label(frame_3, text = 'Selecione o tamanho da pizza:', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 50, y = 50)
    tamanho = tk.StringVar()

    #função validar
    def validar_pedido():
        #Verifica se todos os campos estão vazios
        if not sabor_var.get() and not tamanho.get() and not quantidade.get() and not pagamento.get():
            messagebox.showinfo('Aviso', 'Selecione o tamanho, sabor, quantidade e forma de pagamento do seu pedido.', parent = frame_3)
            return
        
        #Verifica se quatro entradas estão vazias
        if not tamanho.get() and not quantidade.get() and not pagamento.get() and not receber1.get():
            messagebox.showinfo('Aviso', 'Selecione tamanho, quantidade, pagamento a forma de receber do seu pedido.', parent = frame_3)
            return
        
        if not sabor_var.get() and not quantidade.get() and not pagamento.get() and not receber1.get():
            messagebox.showinfo('Aviso', 'Selecione sabor, quantidade, forma de pagamento a forma de receber do seu pedido.', parent = frame_3)
            return
        
        if not tamanho.get() and not sabor_var.get() and not pagamento.get() and not receber1.get():
            messagebox.showinfo('Aviso', 'Selecione tamanho, sabor, forma de pagamento a forma de receber do seu pedido.', parent = frame_3)
            return
        
        if not tamanho.get() and not sabor_var.get() and not quantidade.get() and not receber1.get():
            messagebox.showinfo('Aviso', 'Selecione tamanho, sabor, quantidade a forma de receber do seu pedido.', parent = frame_3)
            return
        
        if not tamanho.get() and not sabor_var.get() and not quantidade.get() and not pagamento.get():
            messagebox.showinfo('Aviso', 'Selecione tamanho, sabor, quantidade e forma de pagamento do seu pedido.', parent = frame_3)
            return
        
        #Verifica se três campos estão vazios
        if not sabor_var.get() and not tamanho.get() and not quantidade.get():
            messagebox.showinfo('Aviso', 'Selecione o sabor, tamanho e quantidade do seu pedido.', parent = frame_3)
            return
        
        if not pagamento.get() and not tamanho.get() and not quantidade.get():
            messagebox.showinfo('Aviso', 'Selecione a forma de pagamento, tamanho e quantidade do seu pedido.', parent = frame_3)
            return
        
        if not pagamento.get() and not sabor_var.get() and not quantidade.get():
            messagebox.showinfo('Aviso', 'Selecione a forma de pagamento, sabor e quantidade do seu pedido.', parent = frame_3)
            return
        
        if not pagamento.get() and not sabor_var.get() and not tamanho.get():
            messagebox.showinfo('Aviso', 'Selecione a forma de pagamento, sabor e tamanho do seu pedido.', parent = frame_3)
            return
        
        if not quantidade.get() and not pagamento.get() and not receber1.get():
            messagebox.showinfo('Aviso', 'Selecione quantidade, forma de pagamento a forma de receber do seu pedido.', parent = frame_3)
            return
        
        if not sabor_var.get() and not pagamento.get() and not receber1.get():
            messagebox.showinfo('Aviso', 'Selecione o sabor, forma de pagamento e forma de receber seu pedido.', parent = frame_3)
            return
        
        if not sabor_var.get() and not quantidade.get() and not receber1.get():
            messagebox.showinfo('Aviso', 'Selecione sabor, quantidade e forma de receber seu pedido.', parent = frame_3)
            return
        
        if not tamanho.get() and not quantidade.get() and not receber1.get():
            messagebox.showinfo('Aviso', 'Selecione o tamanho, quantidade e forma de receber seu pedido.', parent = frame_3)
            return
        
        if not tamanho.get() and not sabor_var.get() and not receber1.get():
            messagebox.showinfo('Aviso', 'Selecione o tamanho, sabor e forma de receber seu pedido.', parent = frame_3)
            return

        #Verifica se dois dos campos estão vazios
        if not sabor_var.get() and not tamanho.get():
            messagebox.showinfo('Aviso', 'Selecione o sabor e o tamanho do seu pedido.', parent = frame_3)
            return
            
        if not sabor_var.get() and not quantidade.get():
            messagebox.showinfo('Aviso', 'Selecione o sabor e a quantidade do seu pedido.', parent = frame_3)
            return

        if not tamanho.get() and not quantidade.get():
            messagebox.showinfo('Aviso', 'Selecione o tamanho e a quantidade do seu pedido.', parent = frame_3)
            return
        
        if not pagamento.get() and not quantidade.get():
            messagebox.showinfo('Aviso', 'Selecione a forma de pagamento e quantidade do seu pedido.', parent = frame_3)
            return
        
        if not pagamento.get() and not tamanho.get():
            messagebox.showinfo('Aviso', 'Selecione a forma de pagamento e tamanho do seu pedido.', parent = frame_3)
            return
        
        if not pagamento.get() and not sabor_var.get():
            messagebox.showinfo('Aviso', 'Selecione a forma de pagamento e quantidade do seu pedido.', parent = frame_3)
            return
        
        if not pagamento.get() and not receber1.get():
            messagebox.showinfo('Aviso', 'Selecione a forma de receber e pagamento do seu pedido.', parent = frame_3)
            return
        
        if not receber1.get() and not quantidade.get():
            messagebox.showinfo('Aviso', 'Selecione a forma de receber e quantidade do seu pedido.', parent = frame_3)
            return
        
        if not receber1.get() and not sabor_var.get():
            messagebox.showinfo('Aviso', 'Selecione a forma de receber e sabor do seu pedido', parent = frame_3)
            return
        
        if not receber1.get() and not tamanho.get():
            messagebox.showinfo('Aviso', 'Selecione a forma de receber e tamanho do seu pedido', parent = frame_3)
            return
        
        #Verifica se cada campo individualmente está vazio
        if not tamanho.get():
            messagebox.showinfo('Aviso', 'Selecione o tamanho do seu pedido.', parent = frame_3)
            return
            
        if not sabor_var.get():
            messagebox.showinfo('Aviso', 'Selecione o sabor do seu pedido.', parent = frame_3)
            return
        
        if not quantidade.get():
            messagebox.showinfo('Aviso', 'Selecione a quantidade do seu pedido.', parent = frame_3)
            return
        
        if not pagamento.get():
            messagebox.showinfo('Aviso', 'Selecione a forma do seu pedido.', parent = frame_3)
            return
        
        if not receber1.get():
            messagebox.showinfo('Aviso', 'Selecione a forma de receber do seu pedido.', parent = frame_3)
            return
        
        # Se tudo estiver correto, exibe uma mensagem de sucesso
        messagebox.showinfo('Pedido Confirmado', f'Pedido de pizza {tamanho.get()} de sabor {sabor_var.get()} e quantidade {quantidade.get()} para {receber1.get()}, confirmado! ({especificação.get()})', parent = frame_3)
        abrir_janela3.quit()

    # Botões para confirmar e cancelar o pedido
    ttk.Button(frame_3, text = 'Confirmar', command = validar_pedido).place(x = 325, y = 575)
    ttk.Button(frame_3, text = 'Cancelar', command = abrir_janela3.destroy).place(x = 425, y = 575)

    #Criação dos radio buttons
    style = ttk.Style()
    style.configure('TRadiobutton', foreground='#F0FFFF', background='#0D0D0D', font = ('century', 12))

    radio_pequena = ttk.Radiobutton(frame_3, text = 'Pequena', variable = tamanho, value = 'Pequena', style = 'TRadiobutton')
    radio_media = ttk.Radiobutton(frame_3, text = 'Média', variable = tamanho, value = 'Média', style = 'TRadiobutton')
    radio_grande = ttk.Radiobutton(frame_3, text = 'Grande', variable = tamanho, value = 'Grande', style = 'TRadiobutton')

    #Posicionando os radio buttons na janela usando place()
    radio_pequena.place(x = 50, y = 70)
    radio_media.place(x = 50, y = 90)
    radio_grande.place(x = 50, y = 110)

    #Escolhendo o sabor da pizza
    ttk.Label(frame_3, text = 'Selecione o sabor da pizza:', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 50, y = 150)
    sabor_var = tk.StringVar()

    radio_frango = ttk.Radiobutton(frame_3, text = 'Frango', variable = sabor_var, value = 'Frango', style = 'TRadiobutton')
    radio_frango_catupiry = ttk.Radiobutton(frame_3, text = 'Frango com catupiry', variable = sabor_var, value = 'Frango com catupiry', style = 'TRadiobutton')
    radio_frango_especial = ttk.Radiobutton(frame_3, text = 'Frango especial', variable = sabor_var, value = 'Frango especial', style = 'TRadiobutton')
    radio_frango_crocante = ttk.Radiobutton(frame_3, text = 'Frango crocante', variable = sabor_var, value = 'Frango crocante', style = 'TRadiobutton')
    radio_frango_cremoso = ttk.Radiobutton(frame_3, text = 'Frango cremoso', variable = sabor_var, value = 'Frango cremoso', style = 'TRadiobutton')
    radio_carne_de_sol = ttk.Radiobutton(frame_3, text = 'Carne de sol', variable = sabor_var, value = 'Carne de sol', style = 'TRadiobutton')
    radio_carne_de_sol_com_cheddar = ttk.Radiobutton(frame_3, text = 'Carne de sol com cheddar', variable = sabor_var, value = 'Carne de sol com cheddar', style = 'TRadiobutton')
    radio_mussarela = ttk.Radiobutton(frame_3, text = 'Mussarela', variable = sabor_var, value = 'Mussarela', style = 'TRadiobutton')
    radio_marguerita = ttk.Radiobutton(frame_3, text = 'Marguerita', variable = sabor_var, value = 'Marguerita', style = 'TRadiobutton')
    radio_calabresa = ttk.Radiobutton(frame_3, text = 'Calabresa', variable = sabor_var, value = 'Calabresa', style = 'TRadiobutton')
    radio_portuguesa = ttk.Radiobutton(frame_3, text = 'Portuguesa', variable = sabor_var, value = 'Portuguesa', style = 'TRadiobutton')
    radio_alho_frito = ttk.Radiobutton(frame_3, text = 'Alho frito', variable = sabor_var, value = 'Alho frito', style = 'TRadiobutton')
    radio_quatro_queijos = ttk.Radiobutton(frame_3, text = 'Quatro queijos', variable = sabor_var, value = 'Quatro queijos', style = 'TRadiobutton')
    radio_camarao = ttk.Radiobutton(frame_3, text = 'Camarão', variable = sabor_var, value = 'Camarão', style = 'TRadiobutton')
    radio_chocolate = ttk.Radiobutton(frame_3, text = 'Chocolate', variable = sabor_var, value = 'Chocolate', style = 'TRadiobutton')

    # Posicionamento dos botões de sabor
    radio_frango.place(x = 50, y = 170)
    radio_frango_catupiry.place(x = 50, y = 190)
    radio_frango_especial.place(x = 50, y = 210)
    radio_frango_crocante.place(x = 50, y = 230)
    radio_frango_cremoso.place(x = 50, y = 250)
    radio_carne_de_sol.place(x = 50, y = 270)
    radio_carne_de_sol_com_cheddar.place(x = 50, y = 290)
    radio_mussarela.place(x = 50, y = 310)
    radio_marguerita.place(x = 50, y = 330)
    radio_calabresa.place(x = 50, y = 350)
    radio_portuguesa.place(x = 50, y = 370)
    radio_alho_frito.place(x = 50, y = 390)
    radio_quatro_queijos.place(x = 50, y = 410)
    radio_camarao.place(x = 50, y = 430)
    radio_chocolate.place(x = 50, y = 450)

    #Escolhendo quantidade de pizzas
    quantidade = tk.StringVar()
    ttk.Label(frame_3, text = 'Selecione a quantidade:', background = '#0D0D0D',foreground = '#F0FFFF', font = ('century', 12)).place(x = 50, y = 500)
    ttk.Spinbox(frame_3, from_ = 1, to = 100, text = quantidade).place(x = 230, y = 503, width = 50)

    #Alguma especificação
    especificação = tk.StringVar()
    ttk.Label(frame_3, text = 'Digite aqui alguma especificação:', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 350, y = 180)
    especificação = ttk.Entry(frame_3)
    especificação.place(x = 360, y = 210, width = 200)

    #Escolhendo forma de pagamento
    pagamento = tk.StringVar()
    ttk.Label(frame_3, text = 'Forma de pagamento:', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 350, y = 50)
    
    #Pagamento via pix
    radio_pix = ttk.Radiobutton(frame_3, text = 'PIX', variable = pagamento, value = 'PIX', style = 'TRadiobutton')
    radio_pix.place(x = 350, y = 70)

    #Pagamento cartão de credito
    radio_cartão_credito = ttk.Radiobutton(frame_3, text = 'Crédito', variable = pagamento, value = 'Crédito', style = 'TRadiobutton')
    radio_cartão_credito.place(x = 350, y = 90)

    #Pagamento cartão de débito
    radio_cartão_debito = ttk.Radiobutton(frame_3, text = 'Débito', variable = pagamento, value = 'Débito', style = 'TRadiobutton')
    radio_cartão_debito.place(x = 350, y = 110)

    #Pagamento em espécie
    radio_especie = ttk.Radiobutton(frame_3, text = 'Espécie', variable = pagamento, value = 'Espécie', style = 'TRadiobutton')
    radio_especie.place(x = 350, y = 130)

    #Adicionando a forma de receber o pedido 
    receber1 = tk.StringVar()
    lista_receber = ['comer aqui', 'retirada', 'entrega']
    receber = ttk.Label(frame_3, text = 'Selecione como vai receber seu pedido:', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12))
    receber.place(x = 350, y = 275)

    receber1 = ttk.Combobox(frame_3, value = lista_receber)
    receber1.place(x = 360, y = 303, width = 200)

    #Criando frame 4
    frame_4 = Frame(abrir_janela3, background = '#0D0D0D')
    frame_4.place(relx = 0.51, rely = 0.01, relwidth = 0.48, relheight = 0.539)

    #Adicionando cardapio
    cardapio = Image.open('Projeto_4°bim/cardapio.jpeg')
    tamanho_cardapio = cardapio.resize((450, 625)) 
    cardapio_tk = ImageTk.PhotoImage(tamanho_cardapio)

    label_cardapio = ttk.Label(frame_4, image = cardapio_tk)
    label_cardapio.place(x = 100, y = 20)

    abrir_janela3.mainloop()

#Janela-04 ("Confirmação das informações já repassadas. Botão fechar a tela.") ================================================================================#
    abrir_janela4 = tk.Toplevel(abrir_janela1)
    abrir_janela4.title('Confirme seu pedido.')
    abrir_janela4.geometry('1350x1230')
    abrir_janela4.configure(background = '#ffb90f')
    abrir_janela4.maxsize(width = 1350, height = 1230)
    abrir_janela4.minsize(width = 500, height = 500)

    #Alterando icone da janela 4
    icone_caminho = "Projeto_4°bim/logo.ico"
    abrir_janela4.wm_iconbitmap(icone_caminho)

    #criando frame 5
    frame_5 = Frame(abrir_janela4, background = '#0D0D0D')
    frame_5.place(relx = 0.01, rely = 0.01, relwidth = 0.9785, relheight = 0.54)

    ttk.Button(abrir_janela4, text = 'Confirmar', command = abrir_janela1.destroy).place(x = 580, y = 400)
    ttk.Button(abrir_janela4, text = 'Sair', command = abrir_janela1.destroy).place(x = 680, y = 400)

    #Adicionado fundo
    fundo = Image.open('Projeto_4°bim/fundo4.png')
    tamanho_fundo = fundo.resize((1316, 661))
    fundo_tk = ImageTk.PhotoImage(tamanho_fundo)

    label_fundo = ttk.Label(frame_5 , image = fundo_tk)
    label_fundo.place(x = 0, y = 0)

    #Confirmação de informações a partir do que o usuario forneceu
    ttk.Label(frame_5, text = f'Pizza Escolhida: {sabor_var.get()}', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 540, y = 25)
    ttk.Label(frame_5, text = f'Quantidade: {quantidade.get()} pizza(s)', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 540, y = 55)
    ttk.Label(frame_5, text = f'Especificação: {especificação.get()}', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 540, y = 85)
    ttk.Label(frame_5, text = f'Tamanho: {tamanho.get()}', background='#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 540, y = 115)
    ttk.Label(frame_5, text = f'Forma de pagamento: {pagamento.get()}', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 540, y = 145)
    ttk.Label(frame_5, text = f'Recebimento: {receber1.get()}', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 540, y = 175)

    abrir_janela4.mainloop()

#Verificando login e senha
def login_senha():
    # Verifica se login e senha foram preenchidos
    if not entry_login.get() and not entry_senha.get():
        messagebox.showinfo('Aviso', 'Por favor, digite login e senha.')
        return

    if not entry_login.get():
        messagebox.showinfo('Aviso', 'Por favor, digite seu login.')
        return

    if not entry_senha.get():
        messagebox.showinfo('Aviso', 'Por favor, digite sua senha.')
        return

    usuario_encontrado = False
    senha_encontrada = False
    login = entry_login.get().strip().lower()
    senha = entry_senha.get().strip()

    with open('cadastro_usuarios.txt', 'r') as arquivo:
        usuarios = arquivo.readlines()
        for i in range(len(usuarios)):
            linha = usuarios[i].strip()
            if linha.startswith("Login:"):
                login_arquivo = linha.split("Login: ")[1].strip().lower()
                if login == login_arquivo:
                    usuario_encontrado = True
                    if i + 1 < len(usuarios) and usuarios[i + 1].startswith("Senha:"):
                        senha_arquivo = usuarios[i + 1].strip().split("Senha: ")[1].strip()
                        if senha == senha_arquivo:
                            senha_encontrada = True
                            break

    if usuario_encontrado and senha_encontrada:
        messagebox.showinfo('Sucesso', 'Login e senha confirmados!')
        janela3()

    else:
        if not usuario_encontrado:
            messagebox.showinfo('Erro', 'Login não encontrado! Por favor, realize o cadastro.')

        elif not senha_encontrada:
            messagebox.showinfo('Erro', 'Senha incorreta! Tente novamente.')

#Janela_01 ("Solicitar dados como login e senha para acessar a área de pedidos.") =============================================================================#
abrir_janela1 = Tk()
abrir_janela1.title('Login de usuário')
abrir_janela1.geometry('1350x1230')
abrir_janela1.configure(background = '#ffb90f')
abrir_janela1.maxsize(width = 1350, height = 1230)
abrir_janela1.minsize(width =500, height = 500)

#Alterando icone da janela 1
icone_caminho = "Projeto_4°bim/logo.ico"
abrir_janela1.wm_iconbitmap(icone_caminho)

#Criando frame 1
frame_1 = Frame(abrir_janela1, background = '#0D0D0D')
frame_1.place(relx = 0.01, rely = 0.01, relwidth = 0.9785, relheight = 0.54)

#adicionando logo
cor_fundo = '#0D0D0D'
logo = Image.open('Projeto_4°bim/logo.png')
logo = logo.resize((1316, 661))
fundo = Image.new("RGB", logo.size, cor_fundo)
fundo.paste(logo, (0, 0), logo)
logo_tk = ImageTk.PhotoImage(fundo)

label_imagem = ttk.Label(frame_1, image = logo_tk)
label_imagem.place(x = 0, y = 0)

#Adicionando widget-Label 'Digite seu login'
ttk.Label(frame_1, text = 'Digite seu login:', background = '#0D0D0D', foreground ='#F0FFFF', font = ('century', 12)).place(x = 50, y = 25)
entry_login = ttk.Entry(frame_1)
entry_login.place(x = 180, y = 27, width = 205)

#Adicionando widget-Label 'Digite sua senha'
ttk.Label(frame_1, text = 'Digite sua senha:', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 50, y = 65)
entry_senha = ttk.Entry(frame_1, show = '*')
entry_senha.place(x = 185, y = 67, width = 200)

#Adicionando widget-Label 'Ainda não tem cadastro?
ttk.Label(frame_1, text = 'Ainda não tem cadastro em nossa pizzaria?, clique em cadastrar!', background = '#0D0D0D', foreground = '#F0FFFF', font = ('century', 12)).place(x = 50, y = 100)

#Adicionando widget-botão 'cadastrar'
botão = ttk.Button(frame_1, text = 'Cadastrar', command = imagem_fundo).place(x = 400, y = 150)

#Adicionando widget-botão 'Próximo'
ttk.Button(frame_1, text = 'Próximo', command = login_senha).place(x = 500, y = 150)

#Adicionando widget-botão 'Cancelar'
ttk.Button(frame_1, text = 'Cancelar', command = abrir_janela1.destroy).place(x = 600, y = 150)

abrir_janela1.mainloop()
