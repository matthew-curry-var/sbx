import PySimpleGUI as psg


x = 0

pieceImages = [
                "chess-transparent/Chess_bdt60.png", "chess-transparent/Chess_blt60.png",
                "chess-transparent/Chess_kdt60.png", "chess-transparent/Chess_klt60.png",
                "chess-transparent/Chess_ndt60.png", "chess-transparent/Chess_nlt60.png",
                "chess-transparent/Chess_pdt60.png", "chess-transparent/Chess_plt60.png",
                "chess-transparent/Chess_qdt60.png", "chess-transparent/Chess_qlt60.png",
                "chess-transparent/Chess_rdt60.png", "chess-transparent/Chess_rlt60.png"
            ]

init_layout = [
                [psg.Image(pieceImages[x])],
                [psg.Button("click next pick")]
            ]

# Create the window
window = psg.Window('My Window', layout=init_layout, size=(400,400))

# Run the event loop
while True:
    event, values = window.read()

    print("event: ", event)
    print("values: ", values)

    if (event == psg.WIN_CLOSED):
        break
    """
    if (event == 'click next pick'):
        print("ive been clicKed!")
        x += 1
        window["-IMAGE-"].update(filename=pieceImages[x])
        if (x == 11):
            x = 0

    #if (...):
        # Update the text of the label
        #window.update_layout({'Text': 'This is the new text of the label.'})

    """



window.close()