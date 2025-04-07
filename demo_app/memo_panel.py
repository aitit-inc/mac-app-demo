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
