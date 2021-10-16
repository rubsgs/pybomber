import os
import re
import json
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--origem', help='Caminho da pasta de origem das imagens', required=True)
parser.add_argument('-d', '--destino', help='Caminho da pasta de destino da imagem', required=True)
parser.add_argument('-e', '--extensao', help='Extensao da imagem a ser utilizada sem o . no começo', required=False, default='png')

args = parser.parse_args()
origem = os.path.expanduser(args.origem)
destino = os.path.expanduser(args.destino)
extensao = args.extensao

if(not os.path.isdir(origem)):
  print('É necessário informar um caminho de origem válido')
  exit(1)
if(not os.path.isdir(destino)):
  print('É necessário informar um caminho de destino válido')
  exit(1)

#print(os.listdir(origem))
#print(os.listdir(destino))

lista_arquivos = os.listdir(origem)
spritesheet_meta = {}

regex_nome = f'^([a-zA-Z0-9]+[a-zA-Z0-9\s]*)\s\((\d+)*\)\.{extensao}$'
for arquivo in lista_arquivos:
  arquivo_valido = re.search(regex_nome, arquivo)
  if(not arquivo_valido):
    continue
  
  nome_sprite = arquivo_valido.group(1)
  nome_lower = nome_sprite.lower()
  if(nome_lower not in spritesheet_meta):
    spritesheet_meta[nome_lower] = {'total_imagens':0, 'nome': nome_sprite, 'sprite_rects':[]}
  
  spritesheet_meta[nome_lower]['total_imagens'] += 1

spritesheet_altura = 0
spritesheet_largura = 0
spritesheet_final = Image.new("RGBA", (0,0))
for sprite_key in spritesheet_meta:
  sprite = spritesheet_meta[sprite_key]

  spritesheet_animacao = spritesheet_animacao = Image.new('RGBA', (0, 0))
  max_altura = 0
  total_largura = 0
  for i in range(sprite['total_imagens']):
    inicio_x = total_largura
    imagem = Image.open(f'{origem}\\{sprite["nome"]} ({i+1}).{extensao}')

    largura, altura = imagem.size
    max_altura = altura if altura > max_altura else max_altura
    total_largura += largura
    spritesheet_largura = total_largura if total_largura > spritesheet_largura else spritesheet_largura    
    sprite['sprite_rects'].append({'inicio': [inicio_x, spritesheet_altura], 'rect': [largura, altura]})
    
    temp = Image.new("RGBA", (total_largura, max_altura))
    temp.paste(spritesheet_animacao, (0,0))
    temp.paste(imagem, (total_largura-largura, 0))
    
    spritesheet_animacao.close()
    spritesheet_animacao = temp
  temp_spritesheet = Image.new("RGBA", (spritesheet_largura, spritesheet_altura + max_altura))
  temp_spritesheet.paste(spritesheet_final, (0,0))
  temp_spritesheet.paste(spritesheet_animacao, (0, spritesheet_altura))
  spritesheet_final.close()
  spritesheet_final = temp_spritesheet
  spritesheet_altura += max_altura

spritesheet_final.save(f'{destino}\\spritesheet.png')
with open(f'{destino}\\spritesheet_meta.json', 'w') as f:
  json.dump(spritesheet_meta,f)