import cv2#é importada para fornecer funcionalidades de processamento de imagens
import matplotlib.pyplot as mat#é importado para exibir as imagens resultantes

imagem = cv2.imread('formas.jpg')#lê a imagem 
borda_fraca = 50# determina o limiar de borda fraca 
borda_forte = 150# determina o limiar de borda forte
imagem_canny = cv2.Canny(imagem, borda_fraca, borda_forte)#recebe uma imagem e os limiares e a saida é uma imagem binaria.BRANCO(valor máximo), PRETO(valor mínimo) e a imagem é armazenada em "imagem_canny"

contornos, hierarquia = cv2.findContours(imagem_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)#recebe a imagem binarizada, o modo de recuperação de contornos, nesse caso apenas os contornos externos,e método de aproximação de contorno. Neste caso, não estamos fazendo nenhuma aproximação, ou seja, estamos mantendo todos os pontos do contorno.

for contorno in contornos:#percorre a lista de contornos
    area = cv2.contourArea(contorno)#verifica a area de cada contorno
    if area > 1000:
        epsilon = 0.02 * cv2.arcLength(contorno, True)#é usada para calcular o comprimento de um contorno fechado, é passado o contorno e um valor boolenao que representa se a curva é fechada ou não e dps multiplicamos o valor por 0.2, que é o fator que determina o nivel de aproximacao,quanto menor, mais pontos de contorno serão preservados.
        approx = cv2.approxPolyDP(contorno, epsilon, True)# usado para aproximar o contorno com base no valor(epsilon), é passado o contorno, o parametro de distancia maxima para controlar o nivel de aproximacao,e um valor boolean para verificar se o contorno é fechado.a funcao retorna uma lista de pontos de aproximacao;
        vertices = len(approx)#utilizamos para obter o numero de elementos da lista presentes 

        if vertices == 3:
            nome = "Triangulo"
        elif vertices == 4:
            nome = "Quadrado"
        elif vertices == 5:
            nome = "Pentagono"
        elif vertices == 6:
            nome = "Hexagono"

        retangulo = cv2.boundingRect(contorno)#cria um retangulo ao redor da forma e retorna as coordenadas dele mesmo;
        cv2.putText(
            imagem,
            f"{nome}: {vertices} Vertices",
            (retangulo[0] + retangulo[2] + 5, retangulo[1] + retangulo[3] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            (0, 255, 0),
            1
        )#funcao para colocar o texto ao lado da imagem,primeiro passa a imagem, segundo a string com o texto, terceiro as coordenadas de onde colocar a imagem,o tipo da fonte, size da fonte, cor e espessura
        
        cv2.drawContours(imagem, [contorno], -1, (0, 255, 0), 3)#desenha os contornos da imagem, primeiro passa a imagem, segundo a lista de contornos, terceiro é o indice que o cortorno deve ser desenhado e como queremos que todos os contornos sejam desenhados colocamos -1 para pintar todos,depois coloca a cor que ira ser desenhado, e por ultimo o número 3 representa a espessura de 3 pixels.

imagem_copia = cv2.imread('formas.jpg')# representa a copia das formas originais
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)# converte a imagem lida inicialmente em BRG(Blue-Green-Red) para RGB(Red-Green-Blue), primeiro passa a imagem e em segundo a constante que especifica a conversao de BRG para RGB.Isso é necessario pq  o matplotlib espera imagens RGB para exibição correta.
imagem_copia_rgb = cv2.cvtColor(imagem_copia, cv2.COLOR_BGR2RGB)# faz a mesma coisa que o imagem_rgb, mas agr é para imagem copia.

mat.figure(figsize=(12, 6))#uma nova figura é criada com as dimensões especificadas.
mat.subplot(121)#Um subplot é uma divisão de uma figura em regiões menores, permitindo a exibição de múltiplos gráficos ou imagens em uma única figura,No caso de 121, isso significa que a figura terá 1 linha, 2 colunas e o subplot atual é o primeiro da esquerda para a direita.
mat.imshow(imagem_copia_rgb)#é usada para exibir uma imagem em um subplot específico da figura.
mat.title("Imagem Original")#printar um titulo
mat.axis('off')#Essa linha é aplicada para o subplot atual (no exemplo, o subplot com índice 121) e tem como objetivo remover os eixos coordenados, como as linhas de grade e os rótulos dos eixos, para criar uma visualização mais limpa e focada apenas na imagem
mat
mat.subplot(122)
mat.imshow(imagem_rgb)
mat.title("Imagem Final")
mat.axis('off')
mat
mat.tight_layout()
mat.show()