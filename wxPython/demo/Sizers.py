# 11/26/2003 - Jeff Grimmett (grimmtooth@softhome.net)
#
# o Had to do a bit of rework for the demo; there was no panel attached
#   to the demo window, so all buttons were showing as dark gray on
#   dark gray. I have no idea why this didn't break before. Robin,
#   please examine my changes to ensure you approve. It's rather
#   hackish looking.
#

#----------------------------------------------------------------------
# sizer test code
#----------------------------------------------------------------------

import  wx

#----------------------------------------------------------------------

def makeSimpleBox1(win):
    box = wx.BoxSizer(wx.HORIZONTAL)
    box.Add(wx.Button(win, -1, "one"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "two"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "three"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "four"), 0, wx.EXPAND)

    return box

#----------------------------------------------------------------------

def makeSimpleBox2(win):
    box = wx.BoxSizer(wx.VERTICAL)
    box.Add(wx.Button(win, -1, "one"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "two"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "three"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "four"), 0, wx.EXPAND)

    return box

#----------------------------------------------------------------------

def makeSimpleBox3(win):
    box = wx.BoxSizer(wx.HORIZONTAL)
    box.Add(wx.Button(win, -1, "one"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "two"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "three"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "four"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "five"), 1, wx.EXPAND)

    return box

#----------------------------------------------------------------------

def makeSimpleBox4(win):
    box = wx.BoxSizer(wx.HORIZONTAL)
    box.Add(wx.Button(win, -1, "one"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "two"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "three"), 1, wx.EXPAND)
    box.Add(wx.Button(win, -1, "four"), 1, wx.EXPAND)
    box.Add(wx.Button(win, -1, "five"), 1, wx.EXPAND)

    return box

#----------------------------------------------------------------------

def makeSimpleBox5(win):
    box = wx.BoxSizer(wx.HORIZONTAL)
    box.Add(wx.Button(win, -1, "one"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "two"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "three"), 3, wx.EXPAND)
    box.Add(wx.Button(win, -1, "four"), 1, wx.EXPAND)
    box.Add(wx.Button(win, -1, "five"), 1, wx.EXPAND)

    return box

#----------------------------------------------------------------------

def makeSimpleBox6(win):
    box = wx.BoxSizer(wx.HORIZONTAL)
    box.Add(wx.Button(win, -1, "one"), 1, wx.ALIGN_TOP)
    box.Add(wx.Button(win, -1, "two"), 1, wx.EXPAND)
    box.Add(wx.Button(win, -1, "three"), 1, wx.ALIGN_CENTER)
    box.Add(wx.Button(win, -1, "four"), 1, wx.EXPAND)
    box.Add(wx.Button(win, -1, "five"), 1, wx.ALIGN_BOTTOM)

    return box

#----------------------------------------------------------------------

def makeSimpleBox7(win):
    box = wx.BoxSizer(wx.HORIZONTAL)
    box.Add(wx.Button(win, 1010, "one"), 0, wx.EXPAND)
    box.Add(wx.Button(win, 1010, "two"), 0, wx.EXPAND)
    box.Add(wx.Button(win, 1010, "three"), 0, wx.EXPAND)
    box.Add((60, 20), 0, wx.EXPAND)
    box.Add(wx.Button(win, 1010, "five"), 1, wx.EXPAND)

    return box

#----------------------------------------------------------------------

def makeSimpleBox8(win):
    box = wxBoxSizer(wx.VERTICAL)
    box.Add(wxButton(win, 1010, "one"), 0, wx.EXPAND)
    box.Add((0,0), 1)
    box.Add(wx.Button(win, 1010, "two"), 0, wx.ALIGN_CENTER)
    box.Add((0,0), 1)
    box.Add(wx.Button(win, 1010, "three"), 0, wx.EXPAND)
    box.Add(wx.Button(win, 1010, "four"), 0, wx.EXPAND)
#    box.Add(wx.Button(win, 1010, "five"), 1, wx.EXPAND)

    return box

#----------------------------------------------------------------------
#----------------------------------------------------------------------

def makeSimpleBorder1(win):
    bdr = wx.BoxSizer(wx.HORIZONTAL)
    btn = wx.Button(win, -1, "border")
    btn.SetSize((80, 80))
    bdr.Add(btn, 1, wx.EXPAND|wx.ALL, 15)

    return bdr

#----------------------------------------------------------------------

def makeSimpleBorder2(win):
    bdr = wx.BoxSizer(wx.HORIZONTAL)
    btn = wx.Button(win, -1, "border")
    btn.SetSize((80, 80))
    bdr.Add(btn, 1, wx.EXPAND | wx.EAST | wx.WEST, 15)

    return bdr

#----------------------------------------------------------------------

def makeSimpleBorder3(win):
    bdr = wx.BoxSizer(wx.HORIZONTAL)
    btn = wx.Button(win, -1, "border")
    btn.SetSize((80, 80))
    bdr.Add(btn, 1, wx.EXPAND | wx.NORTH | wx.WEST, 15)

    return bdr

#----------------------------------------------------------------------
#----------------------------------------------------------------------

def makeBoxInBox(win):
    box = wx.BoxSizer(wx.VERTICAL)

    box.Add(wx.Button(win, -1, "one"), 0, wx.EXPAND)

    box2 = wx.BoxSizer(wx.HORIZONTAL)
    box2.Add(wx.Button(win, -1, "two"), 0, wx.EXPAND)
    btn3 = wx.Button(win, -1, "three")
    box2.Add(btn3, 0, wx.EXPAND)
    box2.Add(wx.Button(win, -1, "four"), 0, wx.EXPAND)
    box2.Add(wx.Button(win, -1, "five"), 0, wx.EXPAND)

    box3 = wx.BoxSizer(wx.VERTICAL)
    box3.AddMany([ (wx.Button(win, -1, "six"),   0, wx.EXPAND),
                   (wx.Button(win, -1, "seven"), 2, wx.EXPAND),
                   (wx.Button(win, -1, "eight"), 1, wx.EXPAND),
                   (wx.Button(win, -1, "nine"),  1, wx.EXPAND),
                   ])

    box2.Add(box3, 1, wx.EXPAND)
    box.Add(box2, 1, wx.EXPAND)

    box.Add(wx.Button(win, -1, "ten"), 0, wx.EXPAND)

    ##box.Hide(btn3)

    return box

#----------------------------------------------------------------------

def makeBoxInBorder(win):
    bdr = wx.BoxSizer(wx.HORIZONTAL)
    box = makeSimpleBox3(win)
    bdr.Add(box, 1, wx.EXPAND | wx.ALL, 15)

    return bdr

#----------------------------------------------------------------------

def makeBorderInBox(win):
    insideBox = wx.BoxSizer(wx.HORIZONTAL)

    box2 = wx.BoxSizer(wx.HORIZONTAL)
    box2.AddMany([ (wx.Button(win, -1, "one"), 0, wx.EXPAND),
                   (wx.Button(win, -1, "two"), 0, wx.EXPAND),
                   (wx.Button(win, -1, "three"), 0, wx.EXPAND),
                   (wx.Button(win, -1, "four"), 0, wx.EXPAND),
                   (wx.Button(win, -1, "five"), 0, wx.EXPAND),
                 ])

    insideBox.Add(box2, 0, wx.EXPAND)

    bdr = wx.BoxSizer(wx.HORIZONTAL)
    bdr.Add(wx.Button(win, -1, "border"), 1, wx.EXPAND | wx.ALL)
    insideBox.Add(bdr, 1, wx.EXPAND | wx.ALL, 20)

    box3 = wx.BoxSizer(wx.VERTICAL)
    box3.AddMany([ (wx.Button(win, -1, "six"),   0, wx.EXPAND),
                   (wx.Button(win, -1, "seven"), 2, wx.EXPAND),
                   (wx.Button(win, -1, "eight"), 1, wx.EXPAND),
                   (wx.Button(win, -1, "nine"),  1, wx.EXPAND),
                 ])
    insideBox.Add(box3, 1, wx.EXPAND)

    outsideBox = wx.BoxSizer(wx.VERTICAL)
    outsideBox.Add(wx.Button(win, -1, "top"), 0, wx.EXPAND)
    outsideBox.Add(insideBox, 1, wx.EXPAND)
    outsideBox.Add(wx.Button(win, -1, "bottom"), 0, wx.EXPAND)

    return outsideBox


#----------------------------------------------------------------------

def makeGrid1(win):
    gs = wx.GridSizer(3, 3, 2, 2)  # rows, cols, hgap, vgap

    gs.AddMany([ (wx.Button(win, -1, 'one'),   0, wx.EXPAND),
                 (wx.Button(win, -1, 'two'),   0, wx.EXPAND),
                 (wx.Button(win, -1, 'three'), 0, wx.EXPAND),
                 (wx.Button(win, -1, 'four'),  0, wx.EXPAND),
                 (wx.Button(win, -1, 'five'),  0, wx.EXPAND),
                 #(75, 50),
                 (wx.Button(win, -1, 'six'),   0, wx.EXPAND),
                 (wx.Button(win, -1, 'seven'), 0, wx.EXPAND),
                 (wx.Button(win, -1, 'eight'), 0, wx.EXPAND),
                 (wx.Button(win, -1, 'nine'),  0, wx.EXPAND),
                 ])

    return gs

#----------------------------------------------------------------------

def makeGrid2(win):
    gs = wx.GridSizer(3, 3)  # rows, cols, hgap, vgap

    box = wx.BoxSizer(wx.VERTICAL)
    box.Add(wx.Button(win, -1, 'A'), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, 'B'), 1, wx.EXPAND)

    gs2 = wx.GridSizer(2,2, 4, 4)
    gs2.AddMany([ (wx.Button(win, -1, 'C'), 0, wx.EXPAND),
                  (wx.Button(win, -1, 'E'), 0, wx.EXPAND),
                  (wx.Button(win, -1, 'F'), 0, wx.EXPAND),
                  (wx.Button(win, -1, 'G'), 0, wx.EXPAND)])

    gs.AddMany([ (wx.Button(win, -1, 'one'),   0, wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM),
                 (wx.Button(win, -1, 'two'),   0, wx.EXPAND),
                 (wx.Button(win, -1, 'three'), 0, wx.ALIGN_LEFT | wx.ALIGN_BOTTOM),
                 (wx.Button(win, -1, 'four'),  0, wx.EXPAND),
                 (wx.Button(win, -1, 'five'),  0, wx.ALIGN_CENTER),
                 (wx.Button(win, -1, 'six'),   0, wx.EXPAND),
                 (box,                          0, wx.EXPAND | wx.ALL, 10),
                 (wx.Button(win, -1, 'eight'), 0, wx.EXPAND),
                 (gs2,                          0, wx.EXPAND | wx.ALL, 4),
                 ])

    return gs

#----------------------------------------------------------------------

def makeGrid3(win):
    gs = wx.FlexGridSizer(3, 3, 2, 2)  # rows, cols, hgap, vgap

    gs.AddMany([ (wx.Button(win, -1, 'one'),   0, wx.EXPAND),
                 (wx.Button(win, -1, 'two'),   0, wx.EXPAND),
                 (wx.Button(win, -1, 'three'), 0, wx.EXPAND),
                 (wx.Button(win, -1, 'four'),  0, wx.EXPAND),
                 #(wxButton(win, 1010, 'five'),  0, wxEXPAND),
                 ((175, 50)),
                 (wx.Button(win, -1, 'six'),   0, wx.EXPAND),
                 (wx.Button(win, -1, 'seven'), 0, wx.EXPAND),
                 (wx.Button(win, -1, 'eight'), 0, wx.EXPAND),
                 (wx.Button(win, -1, 'nine'),  0, wx.EXPAND),
                 ])

    gs.AddGrowableRow(0)
    gs.AddGrowableRow(2)
    gs.AddGrowableCol(1)
    return gs

#----------------------------------------------------------------------

def makeGrid4(win):
    bpos = wx.DefaultPosition
    bsize = wx.Size(100, 50)
    gs = wx.GridSizer(3, 3, 2, 2)  # rows, cols, hgap, vgap

    gs.AddMany([ (wx.Button(win, -1, 'one', bpos, bsize),
                  0, wx.ALIGN_TOP | wx.ALIGN_LEFT ),
                 (wx.Button(win, -1, 'two', bpos, bsize),
                  0, wx.ALIGN_TOP | wx.ALIGN_CENTER_HORIZONTAL ),
                 (wx.Button(win, -1, 'three', bpos, bsize),
                  0, wx.ALIGN_TOP | wx.ALIGN_RIGHT ),
                 (wx.Button(win, -1, 'four', bpos, bsize),
                  0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT ),
                 (wx.Button(win, -1, 'five', bpos, bsize),
                  0, wx.ALIGN_CENTER ),
                 (wx.Button(win, -1, 'six', bpos, bsize),
                  0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT ),
                 (wx.Button(win, -1, 'seven', bpos, bsize),
                  0, wx.ALIGN_BOTTOM | wx.ALIGN_LEFT ),
                 (wx.Button(win, -1, 'eight', bpos, bsize),
                  0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL ),
                 (wx.Button(win, -1, 'nine', bpos, bsize),
                  0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT ),
                 ])

    return gs

#----------------------------------------------------------------------

def makeShapes(win):
    bpos = wx.DefaultPosition
    bsize = wx.Size(100, 50)
    gs = wx.GridSizer(3, 3, 2, 2)  # rows, cols, hgap, vgap

    gs.AddMany([ (wx.Button(win, -1, 'one', bpos, bsize),
                  0, wx.SHAPED | wx.ALIGN_TOP | wx.ALIGN_LEFT ),
                 (wx.Button(win, -1, 'two', bpos, bsize),
                  0, wx.SHAPED | wx.ALIGN_TOP | wx.ALIGN_CENTER_HORIZONTAL ),
                 (wx.Button(win, -1, 'three', bpos, bsize),
                  0, wx.SHAPED | wx.ALIGN_TOP | wx.ALIGN_RIGHT ),
                 (wx.Button(win, -1, 'four', bpos, bsize),
                  0, wx.SHAPED | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT ),
                 (wx.Button(win, -1, 'five', bpos, bsize),
                  0, wx.SHAPED | wx.ALIGN_CENTER ),
                 (wx.Button(win, -1, 'six', bpos, bsize),
                  0, wx.SHAPED | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT ),
                 (wx.Button(win, -1, 'seven', bpos, bsize),
                  0, wx.SHAPED |  wx.ALIGN_BOTTOM | wx.ALIGN_LEFT ),
                 (wx.Button(win, -1, 'eight', bpos, bsize),
                  0, wx.SHAPED | wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL ),
                 (wx.Button(win, -1, 'nine', bpos, bsize),
                  0, wx.SHAPED | wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT ),
                 ])

    return gs

#----------------------------------------------------------------------

def makeSimpleBoxShaped(win):
    box = wx.BoxSizer(wx.HORIZONTAL)
    box.Add(wx.Button(win, -1, "one"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "two"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "three"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "four"), 0, wx.EXPAND)
    box.Add(wx.Button(win, -1, "five"), 1, wx.SHAPED)

    return box

#----------------------------------------------------------------------

theTests = [
    ("Simple horizontal boxes", makeSimpleBox1,
     "This is a HORIZONTAL box sizer with four non-stretchable buttons held "
     "within it.  Notice that the buttons are added and aligned in the horizontal "
     "dimension.  Also notice that they are fixed size in the horizontal dimension, "
     "but will stretch vertically."
     ),

    ("Simple vertical boxes", makeSimpleBox2,
     "Exactly the same as the previous sample but using a VERTICAL box sizer "
     "instead of a HORIZONTAL one."
     ),

    ("Add a stretchable", makeSimpleBox3,
     "We've added one more button with the stretchable flag turned on.  Notice "
     "how it grows to fill the extra space in the otherwise fixed dimension."
     ),

    ("More than one stretchable", makeSimpleBox4,
     "Here there are several items that are stretchable, they all divide up the "
     "extra space evenly."
     ),

    ("Weighting factor", makeSimpleBox5,
     "This one shows more than one stretchable, but one of them has a weighting "
     "factor so it gets more of the free space."
     ),

    ("Edge Affinity", makeSimpleBox6,
     "For items that don't completly fill their allotted space, and don't "
     "stretch, you can specify which side (or the center) they should stay "
     "attached to."
     ),

    ("Spacer", makeSimpleBox7,
     "You can add empty space to be managed by a Sizer just as if it were a "
     "window or another Sizer."
     ),

    ("Centering in available space", makeSimpleBox8,
     "This one shows an item that does not expand to fill it's space, but rather"
     "stays centered within it."
     ),

#    ("Percent Sizer", makeSimpleBox6,
#     "You can use the wx.BoxSizer like a Percent Sizer.  Just make sure that all "
#     "the weighting factors add up to 100!"
#     ),

    ("", None, ""),

    ("Simple border sizer", makeSimpleBorder1,
     "The wx.BoxSizer can leave empty space around its contents.  This one "
     "gives a border all the way around."
     ),

    ("East and West border", makeSimpleBorder2,
     "You can pick and choose which sides have borders."
     ),

    ("North and West border", makeSimpleBorder3,
     "You can pick and choose which sides have borders."
     ),

    ("", None, ""),

    ("Boxes inside of boxes", makeBoxInBox,
     "This one shows nesting of boxes within boxes within boxes, using both "
     "orientations.  Notice also that button seven has a greater weighting "
     "factor than its siblings."
     ),

    ("Boxes inside a Border", makeBoxInBorder,
     "Sizers of different types can be nested within each other as well. "
     "Here is a box sizer with several buttons embedded within a border sizer."
     ),

    ("Border in a Box", makeBorderInBox,
     "Another nesting example.  This one has Boxes and a Border inside another Box."
     ),

    ("", None, ""),

    ("Simple Grid", makeGrid1,
     "This is an example of the wxGridSizer.  In this case all row heights "
     "and column widths are kept the same as all the others and all items "
     "fill their available space.  The horizontal and vertical gaps are set to "
     "2 pixels each."
     ),

    ("More Grid Features", makeGrid2,
     "This is another example of the wxGridSizer.  This one has no gaps in the grid, "
     "but various cells are given different alignment options and some of them "
     "hold nested sizers."
     ),

    ("Flexible Grid", makeGrid3,
     "This grid allows the rows to have different heights and the columns to have "
     "different widths.  You can also specify rows and columns that are growable, "
     "which we have done for the first and last row and the middle column for "
     "this example.\n"
     "\nThere is also a spacer in the middle cell instead of an actual window."
     ),

    ("Grid with Alignment", makeGrid4,
     "New alignment flags allow for the positioning of items in any corner or centered "
     "position."
     ),

    ("", None, ""),

    ("Proportional resize", makeSimpleBoxShaped,
     "Managed items can preserve their original aspect ratio.  The last item has the "
     "wxSHAPED flag set and will resize proportional to its original size."
     ),

    ("Proportional resize with Alignments", makeShapes,
     "This one shows various alignments as well as proportional resizing for all items."
     ),

    ]
#----------------------------------------------------------------------

class TestFrame(wx.Frame):
    def __init__(self, parent, title, sizerFunc):
        wx.Frame.__init__(self, parent, -1, title)
        self.Bind(wx.EVT_BUTTON, self.OnButton)

        p = wx.Panel(self, -1)

        self.sizer = sizerFunc(p)
        self.CreateStatusBar()
        self.SetStatusText("Resize this frame to see how the sizers respond...")
        self.sizer.Fit(p)

        p.SetAutoLayout(True)
        p.SetSizer(self.sizer)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Fit()

    def OnCloseWindow(self, event):
        self.MakeModal(False)
        self.Destroy()

    def OnButton(self, event):
        self.Close(True)

#----------------------------------------------------------------------



class TestSelectionPanel(wx.Panel):
    def __init__(self, parent, frame):
        wx.Panel.__init__(self, parent, -1)
        self.frame = frame

        self.list = wx.ListBox(self, -1,
                              wx.DLG_PNT(self, 10, 10), wx.DLG_SZE(self, 100, 100),
                              [])
        self.Bind(wx.EVT_LISTBOX, self.OnSelect, id=self.list.GetId())
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnDClick, id=self.list.GetId())

        self.btn = wx.Button(self, -1, "Try it!", wx.DLG_PNT(self, 120, 10)).SetDefault()
        self.Bind(wx.EVT_BUTTON, self.OnDClick)

        self.text = wx.TextCtrl(self, -1, "",
                               wx.DLG_PNT(self, 10, 115),
                               wx.DLG_SZE(self, 200, 50),
                               wx.TE_MULTILINE | wx.TE_READONLY)

        for item in theTests:
            self.list.Append(item[0])


    def OnSelect(self, event):
        pos = self.list.GetSelection()
        self.text.SetValue(theTests[pos][2])


    def OnDClick(self, event):
        pos = self.list.GetSelection()
        title = theTests[pos][0]
        func = theTests[pos][1]

        if func:
            win = TestFrame(self, title, func)
            win.CentreOnParent(wx.BOTH)
            win.Show(True)
            win.MakeModal(True)

#----------------------------------------------------------------------

def runTest(frame, nb, log):
    win = TestSelectionPanel(nb, frame)
    return win

overview = ""
#wxSizer.__doc__        + '\n' + '-' * 80 + '\n' + \
#wxBoxSizer.__doc__     + '\n' + '-' * 80 + '\n' + \
#wxBorderSizer.__doc__

#----------------------------------------------------------------------

if __name__ == '__main__':

    class MainFrame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None, -1, "Testing...")

            self.CreateStatusBar()
            mainmenu = wx.MenuBar()
            menu = wx.Menu()
            menu.Append(200, 'E&xit', 'Get the heck outta here!')
            mainmenu.Append(menu, "&File")
            self.SetMenuBar(mainmenu)
            self.Bind(wx.EVT_MENU, self.OnExit, id=200)
            self.panel = TestSelectionPanel(self, self)
            self.SetSize((400, 380))
            self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        def OnCloseWindow(self, event):
            self.Destroy()

        def OnExit(self, event):
            self.Close(True)


    class TestApp(wx.App):
        def OnInit(self):
            frame = MainFrame()
            frame.Show(True)
            self.SetTopWindow(frame)
            return True

    app = TestApp(False)
    app.MainLoop()


#----------------------------------------------------------------------
