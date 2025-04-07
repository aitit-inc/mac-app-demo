import wx
import sys


class ColorPickerPanel(wx.Panel):
    """マウス位置の色を表示するカラーピッカーパネル"""

    def __init__(self, parent):
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.current_color_text = wx.StaticText(self, label="RGB: (---, ---, ---)")
        sizer.Add(self.current_color_text, 0, wx.ALL, 10)

        self.color_display = wx.Panel(self, size=(50, 50))
        sizer.Add(self.color_display, 0, wx.ALL, 10)

        self.SetSizer(sizer)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(200)

    def on_timer(self, event):
        pos = wx.GetMousePosition()

        # macOSのRetina対応：スクリーン座標スケールを考慮
        display_index = wx.Display.GetFromPoint(pos)
        if display_index != wx.NOT_FOUND:
            scale_factor = wx.Display(display_index).GetScaleFactor()
        else:
            scale_factor = 1.0
        x = int(pos.x * scale_factor)
        y = int(pos.y * scale_factor)

        screen_dc = wx.ScreenDC()
        pixel_color = screen_dc.GetPixel(x, y)

        # Fallback（GetPixelが失敗時、1ピクセルキャプチャ）
        if not pixel_color.IsOk():
            shot_bmp = wx.Bitmap(1, 1)
            mem_dc = wx.MemoryDC(shot_bmp)
            mem_dc.Blit(0, 0, 1, 1, screen_dc, x, y)
            mem_dc.SelectObject(wx.NullBitmap)
            img = shot_bmp.ConvertToImage()
            r = img.GetRed(0, 0)
            g = img.GetGreen(0, 0)
            b = img.GetBlue(0, 0)
        else:
            r = pixel_color.Red()
            g = pixel_color.Green()
            b = pixel_color.Blue()

        self.current_color_text.SetLabel(f"RGB: ({r}, {g}, {b})")
        self.color_display.SetBackgroundColour(wx.Colour(r, g, b))
        self.color_display.Refresh()
