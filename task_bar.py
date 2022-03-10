import ctypes

from win32api import GetMonitorInfo, MonitorFromPoint


# 此方法获取任务栏的坐标的最大最小值
def get_Taskbar_dim():
    user32 = ctypes.windll.user32
    gdi32 = ctypes.windll.gdi32
    dc = user32.GetDC(None)
    height_scale = gdi32.GetDeviceCaps(dc, 10)  # 分辨率缩放后的高度
    y_max = gdi32.GetDeviceCaps(dc, 117)  # 原始分辨率的高度
    scale = y_max / height_scale

    monitor_info = GetMonitorInfo(MonitorFromPoint((384, 0)))
    monitor = monitor_info.get('Monitor')  # 屏幕分辨率
    work = monitor_info.get('Work')  # 工作区间
    task_height = (monitor[3] - work[3]) * scale
    y_min = y_max - task_height
    #print(y_min, y_max)

    return y_max, y_min
