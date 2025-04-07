"""デモアプリのメインウィンドウを定義するモジュール"""

import wx

from color_picker_panel import ColorPickerPanel
from memo_panel import MemoPanel


class MainFrame(wx.Frame):
    """メインウィンドウ"""

    def __init__(self, parent=None, title="デモアプリ by SurpassOne"):
        super().__init__(parent, title=title, size=(1200, 800))
        self.panel = wx.Panel(self)
        self.memo_panel = None
        self.color_panel = None  # カラーパネル用

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        self.SetMenuBar(self.create_menu_bar())
        self.Centre()

    def create_menu_bar(self):
        """メニューバーを作成する"""
        menu_bar = wx.MenuBar()

        # デモメニュー
        demo_menu = wx.Menu()
        memo_item = demo_menu.Append(wx.ID_ANY, "メモアプリ")
        color_picker_item = demo_menu.Append(wx.ID_ANY, "カラーピッカー")
        ui_library_item = demo_menu.Append(wx.ID_ANY, "UIライブラリ")  # 追加

        # Bind the menu items to their event handlers
        self.Bind(wx.EVT_MENU, self.on_open_memo, memo_item)
        self.Bind(wx.EVT_MENU, self.on_open_color_picker, color_picker_item)
        self.Bind(wx.EVT_MENU, self.on_open_ui_library, ui_library_item)

        menu_bar.Append(demo_menu, "デモメニュー")

        # ファイル操作メニュー
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
        if self.color_panel:
            self.color_panel.Hide()
        self.panel.Hide()
        self.Layout()

    def on_open_color_picker(self, event):
        """カラーピッカーを開く"""
        if not self.color_panel:
            self.color_panel = ColorPickerPanel(self)
            self.sizer.Add(self.color_panel, 1, wx.EXPAND)
        if self.memo_panel:
            self.memo_panel.Hide()
        self.panel.Hide()
        self.color_panel.Show()
        self.Layout()

    def on_open_ui_library(self, event):
        """UIライブラリを開く"""
        from ui_library import UILibraryPanel

        if not hasattr(self, "ui_library_panel") or self.ui_library_panel is None:
            self.ui_library_panel = UILibraryPanel(self)
            self.sizer.Add(self.ui_library_panel, 1, wx.EXPAND)
        if self.memo_panel:
            self.memo_panel.Hide()
        if self.color_panel:
            self.color_panel.Hide()
        self.panel.Hide()
        self.ui_library_panel.Show()
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
