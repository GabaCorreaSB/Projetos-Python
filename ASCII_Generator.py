import PIL.Image

def abrir_imagem():

	caminho = input("Coloque o caminho da imagem que deseja converter: \n ")
	try:
		imagem = PIL.Image.open(caminho)
	except:
		print(f"Não foi possivel encontrar a imagem no caminho {caminho} ")

	imagem = redimensionar(imagem)

	imagem_cinza = cinza(imagem)

	str_ascii = pixel_para_ascii(cinza)

	largura_imagem = imagem_cinza.width

	str_ascii_len = len(str_ascii)
	ascii_imagem = ""

	for i in range(0, str_ascii_len, largura_imagem):
		ascii_imagem += str_ascii[i:i+largura_imagem] + "\n"

	with open("ascii_imagem.txt", "w") as nova_imagem:
		nova_imagem.write(ascii_imagem);


ASCII_CHARS = ["#", "@", "%", "&", "$", "*", "+", ";", ":", ",", "."]

def redimensionar(imagem, nova_largura = 100):
	largura, altura = imagem.size
	
	nova_altura = nova_largura * altura / largura

	return imagem.redimensionar((nova_largura, nova_altura))

def cinza():
	return imagem.convert("L")


def pixel_para_ascii(imagem):
	pixels = imagem.getdata()
	str_ascii = ""

	for pixel in pixels:
		str_ascii += ASCII_CHARS[pixel//25]
	return str_ascii


abrir_imagem()

