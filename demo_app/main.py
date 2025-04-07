"""
デモアプリケーションのエントリーポイント
"""

import wx
from .views import MainFrame


class MyApp(wx.App):
    """メインアプリケーションクラス"""

    def OnInit(self):
        """アプリケーションの初期化"""
        frame = MainFrame()
        frame.Show()
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
