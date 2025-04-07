import wx


class UILibraryPanel(wx.Panel):
    """UIライブラリのパネル"""

    def __init__(self, parent):
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # テキスト表示
        self.static_text = wx.StaticText(self, label="UIライブラリへようこそ")
        sizer.Add(self.static_text, 0, wx.ALL, 5)

        # ボタン
        self.button = wx.Button(self, label="ボタン")
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)
        sizer.Add(self.button, 0, wx.ALL, 5)

        # トグルボタン
        self.toggle_button = wx.ToggleButton(self, label="トグル")
        self.toggle_button.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle)
        sizer.Add(self.toggle_button, 0, wx.ALL, 5)

        # チェックボックス
        self.checkbox = wx.CheckBox(self, label="チェックボックス")
        self.checkbox.Bind(wx.EVT_CHECKBOX, self.on_checkbox)
        sizer.Add(self.checkbox, 0, wx.ALL, 5)

        # ラジオボタン
        self.radio1 = wx.RadioButton(self, label="ラジオ1", style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(self, label="ラジオ2")
        sizer.Add(self.radio1, 0, wx.ALL, 5)
        sizer.Add(self.radio2, 0, wx.ALL, 5)

        self.SetSizer(sizer)

    def on_button_click(self, event):
        wx.MessageBox("ボタンがクリックされました", "情報", wx.OK | wx.ICON_INFORMATION)

    def on_toggle(self, event):
        state = "ON" if self.toggle_button.GetValue() else "OFF"
        wx.MessageBox(f"トグルは {state} です", "情報", wx.OK | wx.ICON_INFORMATION)

    def on_checkbox(self, event):
        is_checked = self.checkbox.GetValue()
        wx.MessageBox(
            f"チェックは {'オン' if is_checked else 'オフ'} です",
            "情報",
            wx.OK | wx.ICON_INFORMATION,
        )
