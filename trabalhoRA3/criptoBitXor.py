alfabeto = {'A': 24, 'B': 19, 'C': 14, 'D': 18, 'E': 16, 'F': 22, 'G': 11,
            'H': 5, 'I': 12, 'J': 26, 'K': 30, 'L': 9, 'M': 7, 'N': 6,
            'O': 3, 'P': 13, 'Q': 29, 'R': 10, 'S': 20, 'T': 1, 'U': 28,
            'V': 15, 'W': 25, 'X': 23, 'Y': 21, 'Z': 17, '9': 4, '8': 31,
            '+': 27, '4': 8, '3': 2, '/': 0}
pontuacao = {' ': '9', '?': '8', '.': '+', ',': '3', '!': '4', ';': '/'}
texto = 'RESOLUCAO DE PROBLEMAS DE NATUREZA DISCRETA; TRABALHO POR FELIPE TOMAZELLI'
criptografado = 'SJX9XFP8QCZXJML9POB/NKMYCCH88FLXVDMYDKPPCG+MJGL8PDR3QCC9SCYXXNCXJG//N+BCXN'
chave = 'KROM'


def rf01(text, key):
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


