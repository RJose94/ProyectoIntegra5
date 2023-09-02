import readchar
import os

class JuegoLaberinto:
    def __init__(self, start, end, laberinto_filename):
        self.start = start
        self.end = end
        self.laberinto = self.cargar_laberinto(laberinto_filename)

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_laberinto(self):
        self.limpiar_pantalla()
        for row in self.laberinto:
            print(''.join(row))

    def main_loop(self):
        px, py = self.start

        while (px, py) != self.end:
            self.laberinto[py][px] = "P"
            self.print_laberinto()
            self.laberinto[py][px] = '.'

            key = readchar.readkey()

            if key == readchar.key.UP:
                new_py = py - 1
                if new_py >= 0 and self.laberinto[new_py][px] != '#':
                    py = new_py
            elif key == readchar.key.DOWN:
                new_py = py + 1
                if new_py < len(self.laberinto) and self.laberinto[new_py][px] != '#':
                    py = new_py
            elif key == readchar.key.LEFT:
                new_px = px - 1
                if new_px >= 0 and self.laberinto[py][new_px] != '#':
                    px = new_px
            elif key == readchar.key.RIGHT:
                new_px = px + 1
                if new_px < len(self.laberinto[py]) and self.laberinto[py][new_px] != '#':
                    px = new_px

        self.laberinto[py][px] = "P"
        self.print_laberinto()
        print("¡Has llegado al final, FELICIDADES!")

    def cargar_laberinto(self, laberinto_filename):
        try:
            with open(laberinto_filename, 'r') as file:
                laberinto_str = file.read()
                return self.parse_laberinto(laberinto_str)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se pudo encontrar el archivo {laberinto_filename}")

    def parse_laberinto(self, laberinto_str):
        return [list(row) for row in laberinto_str.split("\n")]

    def jugar(self):
        self.main_loop()

if __name__ == "__main__":
    start = (0, 0)
    end = (20, 20)
    laberinto_filename = "mi_laberinto.txt"  # Cambia el nombre del archivo por el que quieras cargar
    juego = JuegoLaberinto(start, end, laberinto_filename)
    juego.jugar()
