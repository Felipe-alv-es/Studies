from datetime import date, time, datetime

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_srt = data_atual.strftime('%d/%m/%y')
    print(data_atual_srt)

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_srt = horario.strftime('%H:%M:%S')
    print(horario_srt)

def trabalhando_com_datetime():
    data_atual = datetime.now()
    data_atual_str = data_atual.strftime('%d/%m/%y %H:%M:%S')
    print(data_atual_str)

if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()