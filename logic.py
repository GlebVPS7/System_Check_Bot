import psutil, datetime
psutil.boot_time()


def disk_info():
    disk = psutil.disk_usage("/")
    f"Информация о диске: Изпользовано: {disk.used}, Общий объем диска: {disk.total}, Процентов диска использовано: {disk.percent}"
    return f"Информация о диске: Изпользовано: {disk.used}, Общий объем диска: {disk.total}, Процентов диска использовано: {disk.percent}%"

def virt_mem_info():
    mem = psutil.virtual_memory()
    f"Количество иcпользуемой памяти: {mem.percent}%"
    THRESHOLD = 75  
    if  THRESHOLD <= mem.percent:
        print("Слишком много памяти изпользуеться в данный момент")
    else:
        print("Всё ок")
    return f"Количество иcпользуемой памяти: {mem.percent}%"

def cpu_load_info():
    f'Загрузка CPU: {psutil.cpu_percent(interval=1)}%'
    return f'Загрузка CPU: {psutil.cpu_percent(interval=1)}%'

def cpu_count():
    f"Количество логических и физических процессоров: {psutil.cpu_count()}"
    return f"Количество логических и физических процессоров: {psutil.cpu_count()}"