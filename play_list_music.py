from tkinter import *
import pygame
from tkinter import filedialog, ttk
import time
from mutagen.mp3 import MP3
from PIL import Image, ImageTk
from tkinter import messagebox


#colors
fundo_comum = "#34343a"

# Tela
tocador = Tk()
tocador.title('Player MPG V.3')
# tocador.iconbitmap(r'logozin.ico')
tocador.geometry("360x530")
tocador.configure(bg=fundo_comum)


# Criação do Menu Frame
Menu_frame = Frame()
Menu_frame.pack(pady=20)





# Back-End ////////////////////////////////////////////////////////////////////////

# iniciador do pygame
pygame.mixer.init()

linksMusicas = []
nomesMusicas = []



def adicionar_musica():
    musica = filedialog.askopenfilename(initialdir='C:/', title='Escolha a música', filetypes=(('Arquivos mp3', '*.mp3'),))
    # minha_label.config(text=musica)

    linksMusicas.append(musica)

    # tirar coisas do nome
    musica = musica.replace('C:/Users/', '')
    musica = musica.replace('.mp3', '')

    nome = musica.split('/')

    print(len(nome)-1)

    x = len(nome)-1

    while len(nome)-1 > 0:
        del nome[x-1]
        x -= 1

    print(nome)

    # adicionar a musica na playlist
    caixa_musicas.insert(END, nome[0])
    nomesMusicas.append(nome)


def adicionar_musicaPlay(linkNome):

    linkNome = linkNome.replace('.mp3', '')
    nome = linkNome.split('/')

    print(len(nome)-1)

    x = len(nome)-1

    while len(nome)-1 > 0:
        del nome[x-1]
        x -= 1

    print(nome)

    # adicionar a musica na playlist
    caixa_musicas.insert(END, nome[0])
    nomesMusicas.append(nome)

    return nome


# Função de adicionar várias músicas
def adicionar_varias_musicas():
    musicas = filedialog.askopenfilenames(initialdir='C:/' or '/storage/emulated/0' or '/Meu aparelho',
                                          title='Escolha as músicas', filetypes=(('Arquivos mp3', '*.mp3'),))

    # Loops
    for musica in musicas:
        linksMusicas.append(musica)

        # tirar coisas do nome
        musica = musica.replace('C:/Users/', '')
        musica = musica.replace('.mp3', '')


        nome = musica.split('/')

        print(len(nome) - 1)

        x = len(nome) - 1

        while len(nome) - 1 > 0:
            del nome[x - 1]
            x -= 1


        print(nome[0])

        # adicionar as musicas na playlist
        caixa_musicas.insert(END, nome[0])
        nomesMusicas.append(nome)

        print(nome)




# Função de deletar música
def deletar_musica():
    caixa_musicas.delete(ANCHOR)
    nomesMusicas.pop(caixa_musicas.select_anchor)
    linksMusicas.pop(caixa_musicas.select_anchor)
    #reset()


# Função de deletar todas as músicas
def deletar_musicas():
    caixa_musicas.delete(0, END)
    nomesMusicas.clear()
    linksMusicas.clear()
    #reset()




def salvar_playlist():
    savecon = messagebox.askquestion(
        'Save Confirmation', 'save your progress?')
    if savecon.upper() == "YES":
        with open("SaveFile.txt", "w") as filehandle:
            for musicas in linksMusicas:
                filehandle.write('%s\n' % musicas)
    else:
        pass


# def update_tasks():
#     deletar_musicas()
#     for musica in caixa_musicas:
#         caixa_musicas.insert("end", task)
#     numtask = len(tasks)
#     label_dsp_count['text'] = numtask
#
def carregar_playlist():
     loadcon = messagebox.askquestion(
         'Save Confirmation', 'save your progress?')
     if loadcon.upper() == "YES":
         deletar_musicas()

         with open('SaveFile.txt', 'r') as filereader:
             for line in filereader:
                 musica = line
                 adicionar_musicaPlay(musica)



     else:
         pass


def contagem():

    # formatação do tempo
    contar_tempo = pygame.mixer.music.get_pos() / 1000

    # conversão
    conversao_contar_tempo = time.strftime('%H:%M:%S', time.gmtime(contar_tempo))

    # Pegar a música
    # ver a música pelo número
    som_recorrente = caixa_musicas.curselection()

    # ver o nome da musica na playlist
    musica = caixa_musicas.get(som_recorrente)

    # acionar o diretório

    def selected_item():
        for i in caixa_musicas.curselection():
            return (caixa_musicas.getint(i))

    music = selected_item()


    musica = f'{linksMusicas[music]}'

    # Pegar a música pela Mutagen
    musica_mut = MP3(musica)

    # Ter uma extensão da mùsica
    extensao_musica = musica_mut.info.length

    # converter o tempo
    conversao_extensao_musica = time.strftime('%M:%S', time.gmtime(extensao_musica))


    # # contagem na barra
    # if contar_tempo > 0:
    #     barra_status.config(text=f'Tempo da Música  :  {conversao_contar_tempo}  /  {conversao_extensao_musica} ',
    #                     fg='DarkSlateGray')
    #
    # # subir tempo
    # barra_status.after(1000, contagem)


def selected_item():
    for i in caixa_musicas.curselection():
        a = (caixa_musicas.getint(i))
        return a

global janelaAberta
janelaAberta = False

def TrocarEstadoBotao():

    if janelaAberta == False:
        if caixa_musicas.curselection():

            abrirJanelaPlayer()
    else:
        pass



# Variável paused
    global paused
    paused = False

def abrirJanelaPlayer():
    global janelaAberta

    def play():
        # Fazer a variável mudar pra tocar o som
        global stopped
        stopped = False

        # musica = caixa_musicas.get(curselection)

        def selected_item():
            for i in caixa_musicas.curselection():
                return (caixa_musicas.getint(i))

        music = selected_item()
        print(music)
        print(linksMusicas)

        musica = f'{linksMusicas[music]}'

        pygame.mixer.music.load(musica)
        pygame.mixer.music.play()

    # Função de pause
    def pause(is_paused):
        global paused
        paused = is_paused

        if paused:
            # Unpause
            pygame.mixer.music.unpause()
            paused = False
        else:
            # Pause
            pygame.mixer.music.pause()
            paused = True

    def mudarBotao():
        if pause_button['image'] == "pyimage3":#pause
            pause(False)
            print(pause_button['image'])
            pause_button.config(image="pyimage1")
        elif pause_button['image'] == "pyimage1":#play
            play()
            print(pause_button['image'])
            pause_button['image'] = "pyimage3"
        else:
            print(pause_button['image'])

    print(nomesMusicas)

    janelaPlayer = Toplevel()

    janelaPlayer.title('Player')
    janelaPlayer.geometry("360x430")
    janelaPlayer.configure(bg=fundo_comum)

    labelExample = Label(janelaPlayer, text=nomesMusicas[selected_item()][0], bg=fundo_comum, font="Arial, 13", fg="#fff")
    labelExample.pack(ipady=5)

    # Read the Image
    image = Image.open("music-logo.jpg")

    # Resize the image using resize() method
    resize_image = image.resize((270, 230))

    img = ImageTk.PhotoImage(resize_image)

    # create label and add resize image
    label1 = Label(janelaPlayer, image=img)
    label1.image = img
    label1.pack()

    # Botões capas
    pause = Image.open("botao-pause.png").resize((50, 50))
    pause_btn_img = ImageTk.PhotoImage(pause)

    # Criação do Frame dos btns
    Btn_frame = Frame(janelaPlayer)
    Btn_frame.pack(pady=20)

    # Frames
    controle_frame = Frame(Btn_frame)
    controle_frame.grid(row=0, column=0)

    # Botões comandos
    pause_button = Button(controle_frame, image=play_btn_img, bg=fundo_comum, fg=fundo_comum, borderwidth=0,
                          command=mudarBotao)

    pause_button.pack()

    janelaPlayer.mainloop()
    janelaPlayer.quit()


# /////////////////////////////////////////////////////////////////////////////////






# Menu
meu_menu = Menu(tocador)
tocador.config(menu=meu_menu)

# adicionar playlists
colocar_msc_menu = Menu(meu_menu, tearoff=0)
meu_menu.add_cascade(label='Playlists', menu=colocar_msc_menu)

# carregar uma playlist
colocar_msc_menu.add_command(label='Carregar uma playlist', command=carregar_playlist)#

# salvar uma playlist
colocar_msc_menu.add_command(label='Salvar essa playlist', command=salvar_playlist)#

# adicionar músicas ao menu
colocar_msc_menu = Menu(meu_menu, tearoff=0)
meu_menu.add_cascade(label='Adicionar Músicas', menu=colocar_msc_menu)

# colocar um áudio na playlist
colocar_msc_menu.add_command(label='Adicionar uma música', command=adicionar_musica)#

# colocar vários áudios na playlist
colocar_msc_menu.add_command(label='Adicionar várias músicas', command=adicionar_varias_musicas)#

# Deletar um áudio da Playlist
remover_msc_menu = Menu(meu_menu, tearoff=0)
meu_menu.add_cascade(label='Remover músicas', menu=remover_msc_menu)
remover_msc_menu.add_command(label='Remover a música selecionada', command=deletar_musica)#
remover_msc_menu.add_command(label='Remover todas as músicas', command=deletar_musicas)#


# Playlist
caixa_musicas = Listbox(Menu_frame, font='Candara', bg="#114242", fg="#FFFAFA",
                        width=35,
                        height=22,
                        selectbackground='MintCream',
                        selectforeground='grey11')
caixa_musicas.grid(row=0, column=0)

play = Image.open("play-image.png").resize((40, 40))
play_btn_img = ImageTk.PhotoImage(play)


# Frames
controle_frame = Frame(Menu_frame)
controle_frame.grid(row=1, column=0, pady=2)

# Botões comandos
play_button = Button(controle_frame, borderwidth=0, image=play_btn_img, bg="red", command=TrocarEstadoBotao)
play_button.grid(row=0, column=1, padx=0)

tocador.mainloop()

