import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


Q = ['q0', 'q1', 'q2']
Sigma = ['0', '1']
delta = { ('q0','0'): 'q0', ('q0','1'): 'q1', ('q1','0'): 'q1',
    ('q1','1'): 'q2', ('q2','0'): 'q2', ('q2','1'): 'q2'}
F = ['q2']
    
    
def AFD(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    qA = q0
    for x in cadeia:
        qA = delta[(qA, x)]
    return qA in F


## Email promocional
email_exemplo1 = """Estamos oferecendo descontos incríveis em nossa loja online, 
especialmente para você! Aproveite para economizar em uma variedade de produtos, 
de moda eletrônicos. Além disso, frete grátis em compras acima de R$100. 
Não perca tempo, essas ofertas são por tempo limitado! Visite nosso site agora e faça suas 
compras com descontos exclusivos.
Atenciosamente,"""

## Email não promocional
email_exemplo2 = """ Esperamos que este email o encontre bem. Estamos escrevendo para informar
sobre uma atualização importante em nossa política de privacidade. Como parte de nossos esforços
contínuos para proteger seus dados e garantir sua segurança online, fizemos algumas alterações em
nossa política de privacidade para estar em conformidade com as regulamentações atuais e para 
oferecer maior transparência sobre como seus dados são coletados, usados e protegidos. As principais
mudanças incluem uma explicação mais clara de seus direitos em relação aos seus dados pessoais,
detalhes sobre como usamos cookies e tecnologias semelhantes em nosso site, e informações sobre 
como você pode controlar suas preferências de privacidade. Queremos garantir que você
esteja ciente dessas atualizações e que se sinta confortável com a maneira como suas informações
são tratadas por nós. Por favor, tome um momento para revisar nossa nova política de privacidade,
que pode ser encontrada em nosso site. Se você tiver alguma dúvida ou preocupação sobre essas 
mudanças ou sobre como seus dados são tratados, não hesite em entrar em contato conosco.
Estamos aqui para ajudar e garantir que sua experiência conosco seja sempre positiva e segura."""


## Email não promocional
email_exemplo3 = """É com grande entusiasmo que compartilhamos com você as incríveis ofertas que
preparamos especialmente para nossos clientes mais valiosos, como você! Por tempo limitado,
estamos oferecendo descontos imperdíveis em uma ampla variedade de produtos em nossa loja
online. De roupas elegantes a eletrônicos de última geração, de produtos de beleza de alta qualidade
a artigos para casa que vão transformar o seu lar, temos tudo o que você deseja com preços que vão 
além das suas expectativas! Além dos descontos incríveis, também estamos oferecendo frete grátis 
em todas as compras acima de um determinado valor. É a nossa maneira de agradecer pela sua lealdade
e confiança em nós. Mas espere, ainda há mais! Como um bônus especial, todos os clientes que 
fizerem uma compra durante esta promoção serão automaticamente inscritos em um sorteio exclusivo,
onde terão a chance de ganhar prêmios incríveis! Corra para o nosso site agora mesmo e descubra 
todas as ofertas e promoções que preparamos para você. Não perca tempo, pois essas ofertas são por
tempo limitado e podem acabar a qualquer momento. Agradecemos por ser um cliente tão valioso e 
esperamos que você aproveite ao máximo essas promoções especiais."""

## Email não promocional
email_exemplo4 = """Atualizamos nossos sistemas de segurança e solicitamos que você 
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


def verificar_promocao(texto, conjunto_de_string="", saida=""):
    
    frases = sent_tokenize(texto)
    
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
    
    print(f"Email de promoção :{AFD((Q, Sigma, delta, 'q0', F), saida)}")     
    return saida

resultado1 = verificar_promocao(email_exemplo1)
print(f"Saida 1: {resultado1}")

resultado2 = verificar_promocao(email_exemplo2)
print(f"Saida 2: {resultado2}")

resultado3 = verificar_promocao(email_exemplo3)
print(f"Saida 3: {resultado3}")

resultado4 = verificar_promocao(email_exemplo4)
print(f"Saida 4: {resultado4}")

