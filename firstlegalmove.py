# Importa les llibreries necessàries
import chess  # Llibreria per gestionar les regles del joc d'escacs
import chess.svg  # Llibreria per crear imatges del tauler d'escacs en format SVG
import cairosvg  # Llibreria per convertir SVG a PNG
from PIL import Image, ImageTk  # Llibreria per mostrar imatges
import tkinter as tk  # Llibreria per a la interfície gràfica
from tkinter import simpledialog, messagebox  # Per a entrades de diàleg i missatges d'error
import io  # Llibreria per manejar fluxos de dades

# Funció per a la IA senzilla que tria el primer moviment legal disponible
def fer_moviment_simple(tauler):
    # Obtenim tots els moviments legals que la IA pot fer
    moviments_legals = list(tauler.legal_moves)
    # Triem el primer moviment legal disponible
    moviment = moviments_legals[0]
    # TAMBE PODEM TRIAR NO EL PRIMER LEGAL SINO UN ALEATORI ENTRE ELS LEGALS
     # Triem un moviment legal aleatori
    # moviment = random.choice(moviments_legals)
    # Fem el moviment triat al tauler
    tauler.push(moviment)

# Dibuixa el tauler i les peces
def dibuixar_tauler(tauler, label, tamany):
    # Creem una imatge del tauler en format SVG
    imatge_svg = chess.svg.board(tauler, size=tamany)
    # Convertim la imatge SVG a PNG
    cairosvg.svg2png(bytestring=imatge_svg, write_to="tauler.png")
    # Carreguem la imatge PNG
    imatge = Image.open("tauler.png")
    # Redimensionem la imatge
    imatge = imatge.resize((tamany, tamany), Image.LANCZOS)
    # Convertim la imatge a un format que tkinter pugui utilitzar
    imatge_tk = ImageTk.PhotoImage(imatge)
    # Actualitzem el label de tkinter amb la nova imatge
    label.config(image=imatge_tk)
    label.image = imatge_tk

# Funció per gestionar el moviment del jugador
def moviment_jugador(tauler, root, label, tamany):
    # Crea un diàleg per a l'entrada del moviment
    moviment = simpledialog.askstring("Moviment del jugador", "Introdueix el teu moviment (ex: e4). Escriu 'exit' per sortir:", parent=root)
    if moviment:
        if moviment.lower() == "exit":
            root.destroy()
            return False
        try:
            # Convertim la notació algebraica abreujada a un moviment legal
            moviment_san = tauler.parse_san(moviment)
            if moviment_san in tauler.legal_moves:
                tauler.push(moviment_san)
                return True
            else:
                messagebox.showerror("Error", "Moviment no vàlid. Prova de nou.")
                return False
        except ValueError:
            messagebox.showerror("Error", "Moviment no vàlid. Prova de nou.")
            return False

# Funció per mostrar la pantalla inicial
def pantalla_inicial():
    # Crea la finestra principal només per les instruccions
    root_instruccions = tk.Tk()
    root_instruccions.title("Instruccions i Configuració")

    # Afegir instruccions
    instruccions = """
    Benvingut al Joc d'Escacs!
    
    Instruccions per jugar:
    - Utilitza la notació algebraica per introduir els teus moviments (ex: e4, Nf3, O-O).
    - Les peces es mouen seguint les regles tradicionals dels escacs.
    - Per sortir del joc, escriu 'exit' a la finestra de moviment o prem la tecla ESC.

    Notació algebraica en escacs:
    - Peons: es mouen indicant només la casella de destí (ex: e4)
    - Cavalls (N): ex: Nf3 (Cavall a la casella f3)
    - Alfils (B): ex: Bb5 (Alfil a la casella b5)
    - Torres (R): ex: Rd1 (Torre a la casella d1)
    - Dames (Q): ex: Qh4 (Dama a la casella h4)
    - Reis (K): ex: Ke2 (Rei a la casella e2)
    - Enroc curt: O-O
    - Enroc llarg: O-O-O

    Introduïu el tamany del tauler (en píxels):
    """
    label_instruccions = tk.Label(root_instruccions, text=instruccions, justify="left")
    label_instruccions.pack(pady=10, padx=10)

    # Entrada per al tamany del tauler
    tamany_entry = tk.Entry(root_instruccions)
    tamany_entry.pack(pady=5)

    # Funció per començar el joc
    def comencar_joc():
        tamany = tamany_entry.get()
        try:
            tamany = int(tamany)
            root_instruccions.destroy()  # Tanca la finestra de configuració
            iniciar_joc(tamany)  # Inicia el joc amb el tamany especificat
        except ValueError:
            messagebox.showerror("Error", "Si us plau, introdueix un número vàlid per al tamany del tauler.")

    # Botó per començar el joc
    boto_comencar = tk.Button(root_instruccions, text="Començar Joc", command=comencar_joc)
    boto_comencar.pack(pady=10)

    root_instruccions.mainloop()

# Funció principal que gestionarà el joc
def iniciar_joc(tamany=400):
    # Inicialitza el tauler d'escacs
    tauler = chess.Board()
    
    # Configura la interfície gràfica de tkinter
    root = tk.Tk()
    root.title("Joc d'Escacs")
    
    label = tk.Label(root)
    label.pack()
    
    # Funció per tancar el joc amb ESC
    def tancar(event=None):
        root.destroy()
    
    root.bind("<Escape>", tancar)  # Assigna la tecla ESC per tancar el programa

    en_curs = True

    while en_curs:
        # Mostrem el tauler actualitzat
        dibuixar_tauler(tauler, label, tamany)
        root.update()

        # Comprovem si el joc ha acabat
        if tauler.is_game_over():
            # Si el joc ha acabat, mostrem un missatge indicant-ho
            resultat = tauler.result()
            messagebox.showinfo("Joc acabat!", f"Resultat: {resultat}")
            en_curs = False
            break

        # Si és el torn de les blanques (el jugador)
        if tauler.turn == chess.WHITE:
            valid = False
            while not valid:
                valid = moviment_jugador(tauler, root, label, tamany)
                if not valid:
                    en_curs = False
                    break
        else:
            # Moviment de la IA senzilla
            fer_moviment_simple(tauler)

        # Actualitza el tauler
        dibuixar_tauler(tauler, label, tamany)
        root.update()
    
    root.mainloop()

# Aquesta línia assegura que la funció pantalla_inicial s'executi quan el programa comenci
if __name__ == "__main__":
    pantalla_inicial()

