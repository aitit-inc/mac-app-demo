"""デモアプリのメインウィンドウを定義するモジュール"""

import wx


class MemoPanel(wx.Panel):
    """メモアプリのパネル"""

    def __init__(self, parent):
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text_ctrl = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        sizer.Add(self.text_ctrl, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sizer)

        # ファイルパスの保存用
        self.file_path = None

    def new_file(self):
        """新規ファイル作成"""
        self.file_path = None
        self.text_ctrl.SetValue("")

    def open_file(self):
        """ファイルを開く"""
        with wx.FileDialog(
            self,
            "ファイルを開く",
            wildcard="Text files (*.txt)|*.txt",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                self.file_path = dlg.GetPath()
                with open(self.file_path, "r", encoding="utf-8") as f:
                    self.text_ctrl.SetValue(f.read())

    def save_file(self):
        """ファイルを保存"""
        if not self.file_path:
            with wx.FileDialog(
                self,
                "ファイルを保存",
                wildcard="Text files (*.txt)|*.txt",
                style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
            ) as dlg:
                if dlg.ShowModal() == wx.ID_OK:
                    self.file_path = dlg.GetPath()

        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write(self.text_ctrl.GetValue())


class MainFrame(wx.Frame):
    """メインウィンドウ"""

    def __init__(self, parent=None, title="デモアプリ by SurpassOne"):
        super().__init__(parent, title=title, size=(400, 300))
        self.panel = wx.Panel(self)
        self.memo_panel = None

        # フレーム用のSizerを定義
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        self.SetMenuBar(self.create_menu_bar())
        self.Centre()

    def create_menu_bar(self):
        """メニューバーを作成する"""
        menu_bar = wx.MenuBar()

        # 既存のデモメニュー
        demo_menu = wx.Menu()
        memo_item = demo_menu.Append(wx.ID_ANY, "メモアプリ")
        self.Bind(wx.EVT_MENU, self.on_open_memo, memo_item)
        menu_bar.Append(demo_menu, "デモメニュー")

        # 新しいファイル操作メニュー
        file_menu = wx.Menu()
        new_item = file_menu.Append(wx.ID_NEW, "新規作成")
        open_item = file_menu.Append(wx.ID_OPEN, "開く")
        save_item = file_menu.Append(wx.ID_SAVE, "保存")

        self.Bind(wx.EVT_MENU, self.on_new_file, new_item)
        self.Bind(wx.EVT_MENU, self.on_open_file, open_item)
        self.Bind(wx.EVT_MENU, self.on_save_file, save_item)

        menu_bar.Append(file_menu, "ファイル")

        return menu_bar

    def on_open_memo(self, event):
        """メモアプリを開く"""
        if self.memo_panel is None:
            self.memo_panel = MemoPanel(self)
            self.sizer.Add(self.memo_panel, 1, wx.EXPAND)
        self.memo_panel.Show()
        self.panel.Hide()
        self.Layout()

    def on_new_file(self, event):
        """新規ファイル作成"""
        if self.memo_panel:
            self.memo_panel.new_file()

    def on_open_file(self, event):
        """ファイルを開く"""
        if self.memo_panel:
            self.memo_panel.open_file()

    def on_save_file(self, event):
        """ファイルを保存"""
        if self.memo_panel:
            self.memo_panel.save_file()
