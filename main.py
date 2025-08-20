import time


def main():
    i_wana = """I wanna da-, I wanna dance in the lights                        \n"""
    i_wana_ro = """I wanna ro-, I wanna rock your body     \n"""
    i_wana_go = """I wanna go, I wanna go for a ride      \n"""
    hope = """Hop in the music and rock your body right"""

    recorrer_cancion(i_wana, 0.06)
    recorrer_cancion(i_wana_ro, 0.09)
    recorrer_cancion(i_wana_go, 0.09)
    recorrer_cancion(hope, 0.09)



def recorrer_cancion(text, retardo=0.1):
    for letra in text:
        print(letra, end="", flush=True)
        time.sleep(retardo)
    print

if __name__ == "__main__":
    main()