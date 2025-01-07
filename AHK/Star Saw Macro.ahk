Toggle := 0

GuiColorDefault := "Silver"
GuiColorRunning := "Red"
TextColorDefault := "Black"
TextColorRunning := "White"

Gui +AlwaysOnTop +ToolWindow +LastFound
Gui, Font, s10, Tahoma ; Set font to Tahoma, size 10
Gui, Color, Silver ; Set background color to white
Gui, Add, Text, x15 y10 w200 h20 vTitle, Star Saw Macro
Gui, Font, s10, Segoe UI Bold ; Set font to Segoe UI Bold for the button
Gui, Add, Button, x0 y40 w400 h30 gToggleScript +Border +0x2000 vToggleButton, Not Active (CTRL + P to Start)
Gui, Show, w400 h90, Star Saw

Gui, Add, Text, x0 y0 w250 h30 vDragHandle
GuiControl, +BackgroundTrans, DragHandle
GuiControl, Hide, DragHandle

GuiEscape:
GuiLButtonDown:
    PostMessage, 0xA1, 2,,, Star Saw Macro
Return

PressFour:
    Send, 4
Return

ToggleScript:
    If (Toggle)
    {
        SetTimer, PressFour, Off
        GuiControl,, ToggleButton, Not active (CTRL + P to Resume)
        GuiControl, +c%TextColorDefault%, Title
        Gui, Color, %GuiColorDefault%
        Toggle := 0
    }
    else
    {
        SetTimer, PressFour, 10000
        GoSub, PressFour
        GuiControl,, ToggleButton, Running (CTRL + Q to Pause)
        GuiControl, +c%TextColorRunning%, Title
        Gui, Color, %GuiColorRunning%
        Toggle := 1
    }
Return

^p::
    If (!Toggle)
        GoSub, ToggleScript
Return

^q::
    If (Toggle)
        GoSub, ToggleScript
Return

GuiClose:
    ExitApp
Return
