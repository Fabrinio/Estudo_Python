def segundos(horas, min, seg):
    horas_seg = horas * 3600
    min_seg = min * 60
    segundos_totais = (horas_seg + min_seg) + seg
    print(f"{horas} horas, {min} minutos e {seg} segundos, dão um total de {segundos_totais} segundos")

horas = int(input("Digite as horas: "))
min = int(input("Digite os minutos: "))
seg = int(input("Digite os segundos: "))

segundos(horas, min, seg)