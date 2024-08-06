import psutil

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    return cpu_usage, memory_usage

def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    return disk_usage
