from moviepy.editor import *

video = VideoFileClip('C:/Users/...Nome do Arquivo.extensão')
# local para pegar o caminho do vídeo 
# # necessário que inclua o nome com a extensão 
# (ex: nome.mkv ou nome.mp4)


def converte_horas_segundos():

    # inicio da conversão
    hora_inicio = int(input('Hora inicial: '))
    min_inicio = int(input('Minuto inicial: '))
    seg_inicial = int(input('Segundo inicial: '))
    converte_horas_inicio = (hora_inicio * 60) * 60
    converter_min_inicio = (min_inicio * 60)
    segundos_totais_iniciais = (converte_horas_inicio + converter_min_inicio) + seg_inicial

    # fim da conversão
    hora_fim = int(input('Hora Final: '))
    min_fim = int(input('Minuto Final: '))
    seg_fim = int(input('Segundo Final: '))
    converte_horas_fim = (hora_fim * 60) * 60
    converter_min_fim = (min_fim * 60)
    segundos_totais_fim = (converte_horas_fim + converter_min_fim) + seg_fim

    
    fstarted_time = segundos_totais_iniciais # segundos iniciais para corte
    fend_time = segundos_totais_fim # segundos finais para o corte

    trimed_video = video.subclip(fstarted_time, fend_time) 
    # variavel que armazenará os valores
    # tamamho do vídeo original 01:17:20
    # valor passado inicio: H: 0 / M: 0 / S: 0
    # valor passado fim: H:1 / M: 12 / S: 20
    # seu video ficará com tamanho total dse 01:12:20
   


    trimed_video.write_videofile('C:/Users/.../Nome do Arquivo.extensão', codec='libx264') 
    # local para salvar o video 
    # # necessário que inclua o nome com a extensão 
    # (ex: nome.mkv ou nome.mp4)


converte_horas_segundos()




