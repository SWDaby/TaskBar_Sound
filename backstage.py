import wx
import wx.adv
import sys


class MyTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = "res/sound-waves.ico"  # 图标地址

    ID_ABOUT = wx.ID_ABOUT  # 菜单选项“关于”的ID
    ID_EXIT = wx.ID_EXIT  # 菜单选项“退出”的ID
    ID_SHOW_WEB = wx.ID_NEW  # 菜单选项“显示页面”的ID
    TITLE = "任务栏音量"  # 鼠标移动到图标上显示的文字

    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)  # 设置图标和标题
        self.Bind(wx.EVT_MENU, self.onAbout, id=self.ID_ABOUT)  # 绑定“关于”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onExit, id=self.ID_EXIT)  # 绑定“退出”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onShowWeb, id=self.ID_SHOW_WEB)  # 绑定“显示页面”选项的点击事件

    # “关于”选项的事件处理器
    def onAbout(self, event):

        info = wx.adv.AboutDialogInfo()
        info.SetIcon(wx.Icon('res/sound-waves.ico', wx.BITMAP_TYPE_ICO,))
        info.SetVersion('1.0')

        info.SetCopyright('(C) 2022-03-10 Daby')

        wx.adv.AboutBox(info)
       #wx.MessageBox('程序作者：Daby\n最后更新日期：2022-03-09', "关于")

    # “退出”选项的事件处理器
    def onExit(self, event):
        wx.Exit()


    # “显示页面”选项的事件处理器
    def onShowWeb(self, event):
        pass

    # 创建菜单选项
    def CreatePopupMenu(self):
        menu = wx.Menu()
        for menuAttr in self.getMenuAttrs():
            menu.Append(menuAttr[1], menuAttr[0])
        return menu

    # 获取菜单的属性元组
    def getMenuAttrs(self):
        return [
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


'''
if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

'''
