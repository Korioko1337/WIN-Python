import time
import os
import random

# --- Konstanten auf Modulebene (für einfachen Zugriff) ---

# Nur die Baumstruktur mit Platzhaltern
TREE_STRUCTURE = [
    "         *         ",
    "        ***        ",
    "       *****       ",
    "      *******      ",
    "     *********     ",
    "    ***********    ",
    "   *************   ",
    "  ***************  ",
    " ***************** ",
    "        |||        ",
    "        |||        "
]

# Farben für die Lichter und den Baum
COLORS = {
    "R": "\033[31m",  # Red
    "G": "\033[32m",  # Green
    "B": "\033[33m",  # Blue
    "Y": "\033[34m",  # Yellow
    "W": "\033[35m"   # White
}

RESET_COLOR = "\033[0m" # Zurücksetzen der Farbe

# Positionen für die Lichter (●)
LIGHT_POSITIONS = [
    (2, 9), (3, 7), (3, 11), (4, 5), (4, 13),
    (5, 3), (5, 15), (6, 1), (6, 17), (7, 4),
    (7, 14), (8, 6), (8, 12)
]
# --- Ende Konstanten ---

def clear_console():
    """Löscht die Konsole. Korrigiert 'comsole' zu 'console'."""
    os.system('cls' if os.name == 'nt' else 'clear')

def decorate_tree(light_colors, tree_color_mode=False):
    """
    Dekoriert den Baum.
    light_colors: Die Farben der Lichter (Liste von Farbschlüsseln)
    tree_color_mode: Wenn True, werden auch die * des Baumes gefärbt.
    """
    decorated_tree = []
    light_index = 0
    
    # Verfügbare Farben für Baumsternchen
    available_colors = list(COLORS.keys())
    
    for i, line in enumerate(TREE_STRUCTURE):
        line_list = list(line)
        
        # 1. Baumsterne färben (wenn im Modus)
        if tree_color_mode:
            temp_line = ""
            for char in line:
                if char == '*':
                    # Zufällige Farbe für das Sternchen
                    color_key = random.choice(available_colors)
                    temp_line += COLORS[color_key] + '*' + RESET_COLOR
                else:
                    temp_line += char
            line_list = list(temp_line)
        else:
            # Wenn kein Baumfärbemodus, behalten wir die Sternchen als '*'
            pass

       
        
        # Fügt die Zeile zur Ausgabe hinzu
        decorated_tree.append("".join(line_list))
    
    return decorated_tree

def main():
    # Farben für die Lichterkette
    light_colors = [random.choice(list(COLORS.keys())) for _ in range(len(LIGHT_POSITIONS))]
    
    # Steuern Sie, ob der Baum selbst blinkt (abwechselnd an/aus)
    blink_state = False
    
    while True:
        clear_console()
        
        # Wechselt den Zustand zum Blinken des Baumes (alle 2 Iterationen)
        blink_state = not blink_state
        
        # Ruft decorate_tree auf. Wenn blink_state True ist, wird der Baum gefärbt.
        decorated_tree = decorate_tree(light_colors, tree_color_mode=blink_state)
        
        for line in decorated_tree:
            print(line)
            
        time.sleep(0.5)
        
    

if __name__ == "__main__":
    main()