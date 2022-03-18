import logging
import wx
import wx.adv
import win32com.client as client
import os
import sys
import winshell

# 生成文件快捷方式的完整路径
# 如:运行main.py 则生成C:..\Startup\main.py.lnk
# 运行main.exe 则生成C:..\Startup\main.exe.lnk
lnkname = os.getenv(
    'USERPROFILE') + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\' + os.path.basename(
    sys.argv[0]) + '.lnk'  # 'main.py.lnk'

# 配置日志
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename="taskbar.log", level=logging.ERROR, format=LOG_FORMAT, datefmt=DATE_FORMAT)


# 定义在自启目录下创建快捷方式的方法
def createShortCut():
    """filename should be abspath, or there will be some strange errors"""
    try:
        # 获取当前运行的文件名
        filename = os.path.basename(sys.argv[0])  # 如:filename=main.exe 或者 main.py
        # print('lnkname:'+lnkname)

        # 获取当前运行文件(main.py 或者 main.exe)的目录  如:C:\..\
        foldpath = os.path.dirname(os.path.realpath(sys.argv[0]))
        # print('foldpath:'+foldpath)

        # 获取当前运行文件的绝对路径 如:C:\..\main.exe
        filename = foldpath + '\\' + filename
        # print('filename:'+ filename)

        shortcut = client.Dispatch("WScript.Shell").CreateShortCut(lnkname)
        shortcut.TargetPath = filename
        shortcut.save()

        # 设置快捷方式的起始位置 不设置可能不能自启
        with winshell.shortcut(lnkname) as link:
            # link.path = filename  # 目标文件
            link.working_directory = foldpath  # 'C:\\Users\\Daby\\PycharmProjects\\TaskBar_Sound\\dist\\'  # 起始位置
        # print('配置开机自启')
    except Exception as e:
        # print(e.args)
        logging.error(e)


class Setting_Frame(wx.Frame):

    def __init__(self, parent, title):
        super(Setting_Frame, self).__init__(parent, title=title, size=(300, 100))

        self.InitUI()
        self.Centre()
        # self.Show()

    def InitUI(self):
        option_panel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.onclose)
        self.box = wx.CheckBox(option_panel, -1, "开机自启", pos=(100, 12), size=(80, 30))
        self.SetIcon(wx.Icon('res/sound-waves.ico', wx.BITMAP_TYPE_ICO, ))
        self.SetMaxSize((300,100))
        self.SetMinSize((300,100))
        self.EnableMaximizeButton(False)
        self.Bind(wx.EVT_CHECKBOX, self.onChecked)
        if os.path.isfile(lnkname):
            self.box.SetValue(True)

    def onChecked(self, event):
        checkbox = event.GetEventObject()
        # print(checkbox.GetLabel(), ' is clicked', checkbox.GetValue())
        try:
            if checkbox.GetValue():
                createShortCut()
            else:
                os.remove(lnkname)
        except Exception as e:
            logging.error(e)

    def onclose(self,event):
        self.Hide()

class MyTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = "res/sound-waves.ico"  # 图标地址

    ID_ABOUT = wx.ID_ABOUT  # 菜单选项“关于”的ID
    ID_EXIT = wx.ID_EXIT  # 菜单选项“退出”的ID
    ID_SHOW_SETTING = wx.ID_NEW  # 菜单选项“显示页面”的ID

    # ID_TWO = wx.ID_NEW  # 菜单选项“显示页面”的ID
    TITLE = "任务栏音量"  # 鼠标移动到图标上显示的文字

    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)  # 设置图标和标题
        self.Bind(wx.EVT_MENU, self.onAbout, id=self.ID_ABOUT)  # 绑定“关于”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onExit, id=self.ID_EXIT)  # 绑定“退出”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onShowSetting, id=self.ID_SHOW_SETTING)  # 绑定“显示页面”选项的点击事件
        self.asetting = Setting_Frame(None, title='设置')

        # “关于”选项的事件处理器

    def onAbout(self, event):
        info = wx.adv.AboutDialogInfo()
        info.SetIcon(wx.Icon('res/sound-waves.ico', wx.BITMAP_TYPE_ICO, ))
        info.SetVersion('1.0')

        info.SetCopyright('(C) 2022-03-10 Daby')

        wx.adv.AboutBox(info)

    # wx.MessageBox('程序作者：Daby\n最后更新日期：2022-03-09', "关于")

    # “退出”选项的事件处理器
    def onExit(self, event):
        wx.Exit()

    # “显示页面”选项的事件处理器
    def onShowSetting(self, event):
        self.asetting.Show()

    def ontwo(self, event):
        pass

    # 创建菜单选项
    def CreatePopupMenu(self):
        menu = wx.Menu()
        for menuAttr in self.getMenuAttrs():
            menu.Append(menuAttr[1], menuAttr[0])
        return menu

    # 获取菜单的属性元组
    def getMenuAttrs(self):
        return [('设置', self.ID_SHOW_SETTING),
                ('关于', self.ID_ABOUT),
                ('退出', self.ID_EXIT)]


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self)
        MyTaskBarIcon()  # 显示系统托盘图标


class MyApp(wx.App):
    def OnInit(self):
        MyFrame()
        return True

#
# if __name__ == "__main__":
#     t = os.path.dirname(os.path.realpath(sys.argv[0])) + '\\' + 'main.py'
#     a = os.path.basename(os.path.realpath())
#     print(a)
