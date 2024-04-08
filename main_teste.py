import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


Q = ['q0', 'q1', 'q2']
Sigma = ['0', '1']
delta = { ('q0','0'): 'q0', ('q0','1'): 'q1', ('q1','0'): 'q1',
    ('q1','1'): 'q2', ('q2','0'): 'q2', ('q2','1'): 'q2'}
F = ['q2']
    
    
def AFD(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    q_atual = q0
    for simbolo in cadeia:
        q_atual = delta[(q_atual, simbolo)]
    return q_atual in F

email_exemplo1 = """Estamos oferecendo descontos incríveis em nossa loja online, 
especialmente para você! Aproveite para economizar em uma variedade de produtos, 
de moda eletrônicos. Além disso, frete grátis em compras acima de R$100. 
Não perca tempo, essas ofertas são por tempo limitado! Visite nosso site agora e faça suas 
compras com descontos exclusivos.
Atenciosamente,"""



email_exemplo2 = """Atualizamos nossos sistemas de segurança e solicitamos que você 
verifique e atualize suas informações de conta para garantir a continuidade do serviço. 
Acesse o link abaixo para concluir o processo"""


palavras_chaves = [
    "desconto", "descontos",
    "aproveite", "tempo limitado",
    "promoção", "promoções",
    "oferta", "ofertas",
    "exclusivo",    "exclusivos",
    "liquidação", "liquidações",
    "economizar", "Não perca tempo",
    "promo", "promos",
    "cupom", "cupons",
    "imperdível", "imperdíveis",
    "economize", "economia",
    "black friday",
    "cyber monday",
    "outlet", "outlets",
    "preço baixo", "preços baixos",
    "desconto especial", "descontos especiais",
    "frete grátis", "frete",
    "última chance", "últimas chances",
    "descontão", "exclusivos",
    "mega promoção", "mega promoções",
    "saldão", "saldões",
    "oportunidade única", "oportunidades únicas",
    "compre agora", "compre já"
]





# print(f"Conjunto de string: {conjunto_de_string}")


def verificar_promocao(texto, conjunto_de_string="", saida=""):
    
    frases = sent_tokenize(texto)
    i = 0
    for frase in frases:
        print(f'{i} - {frase}')
        i+=1
    
    for frase in frases :
        conjunto_de_string=""
        palavras = word_tokenize(frase.lower())
        for palavra in palavras:
            if palavra in palavras_chaves:
                conjunto_de_string += "1"
            else:
                conjunto_de_string +="0"
        if(AFD((Q, Sigma, delta, 'q0', F), conjunto_de_string )== True):
            saida+="1"
        else:
            saida+="0"
        print(conjunto_de_string, "-",  AFD((Q, Sigma, delta, 'q0', F), conjunto_de_string))    
    
    print(f"Saida :{AFD((Q, Sigma, delta, 'q0', F), saida)}")     
    return saida

resultado = verificar_promocao(email_exemplo1)
print(f"Resultado: {resultado}")


# print(verificar_promocao(email_exemplo1))



# if verificar_promocao(email_exemplo1):
#     print("Este é um email de promoção.")
# else:
#     print("Este não é um email de promoção.")
    
    
# if verificar_promocao(email_exemplo2):
#     print("Email 1 é um email de promoção.")
# else:
#     print("Email 2 não é um email de promoção.")
    


