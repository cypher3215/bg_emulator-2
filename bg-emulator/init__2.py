from GameBoy import GameBoy

if __name__ == "__main__":
    rom_path = "b.gb"  # Ruta del archivo .gb
    gameboy = GameBoy(rom_path)
    gameboy.run()  # Inicia la ejecución del juego
