import wx 
class Frame1(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title)
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1= wx.TextCtrl(panel, value = "おっはよう~", size = (200,180), style = wx.TE_MULTILINE)
        sizer.Add(self.text1, 0, wx.ALIGN_TOP | wx.EXPAND)
        button1 = wx.Button(panel, label = "一番可愛い子は誰?")
        button2 = wx.Button(panel, label = "あやねる!")
        sizer.Add(button1)
        sizer.Add(button2)
        panel.SetSizerAndFit(sizer)        
        panel.Layout()
        self.Bind(wx.EVT_BUTTON,self.OnClick1,button1)
        self.Bind(wx.EVT_BUTTON,self.OnClick2,button2)
        self.Show(True)
        
    def OnClick1(self, text1):
        self.text1.AppendText("\n戸山香澄に決まってるんでしょう!!")
    
    def OnClick2(self, text1):
        self.text1.AppendText("\n大好き!!")
        
if __name__ == '__main__': 
    app =wx.App()
    frame = Frame1(None, "今日もういい天気~")
    app.MainLoop()
