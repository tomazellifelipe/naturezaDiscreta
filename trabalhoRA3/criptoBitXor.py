alfabeto = {'A': 0b11000, 'B': 0b10011, 'C': 0b01110, 'D': 0b10010, 'E': 0b10000, 'F': 0b10110, 'G': 0b01011,
            'H': 0b00101, 'I': 0b01100, 'J': 0b11010, 'K': 0b11110, 'L': 0b01001, 'M': 0b00111, 'N': 0b00110,
            'O': 0b00011, 'P': 0b01101, 'Q': 0b11101, 'R': 0b01010, 'S': 0b10100, 'T': 0b00001, 'U': 0b11100,
            'V': 0b01111, 'W': 0b11001, 'X': 0b10111, 'Y': 0b10101, 'Z': 0b10001, '9': 0b00100, '8': 0b11111,
            '+': 0b11011, '4': 0b01000, '3': 0b00010, '/': 0b00000}
pontuacao = {' ': '9', '?': '8', '.': '+', ',': '3', '!': '4', ';': '/'}
texto = 'RESOLUCAO DE PROBLEMAS DE NATUREZA DISCRETA; TRABALHO POR FELIPE TOMAZELLI'
criptografado = 'SJX9XFP8QCZXJML9POB/NKMYCCH88FLXVDMYDKPPCG+MJGL8PDR3QCC9SCYXXNCXJG//N+BCXN'
chave = 'KROM'


def rf01(text, key):
    text = text.upper()
    ct = 0
    cripto = ''
    for char in text:
        if ct == len(key):
            ct = 0
        if char in pontuacao.keys():
            char = pontuacao[char]
        code = list(alfabeto.keys())[list(alfabeto.values()).index((alfabeto[char] ^ alfabeto[key[ct]]))]
        cripto += code
        ct += 1
    return cripto


def rf02(text, key):
    ct = 0
    uncripto = ''
    for char in text:
        if ct == len(key):
            ct = 0
        code = list(alfabeto.keys())[list(alfabeto.values()).index((alfabeto[char] ^ alfabeto[key[ct]]))]
        if code in pontuacao.values():
            code = list(pontuacao.keys())[list(pontuacao.values()).index(code)]
        uncripto += code
        ct += 1
    return uncripto


print(rf01(texto, chave))
print(rf02(rf01(texto, chave), chave))

