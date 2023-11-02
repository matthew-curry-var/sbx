"""

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



layout = [
    [psg.Graph(canvas_size=(100,100), graph_bottom_left=(0,0), graph_top_right=(100,100), enable_events=True, key="-GRAPH-")],
    [psg.Image(filename="chess-transparent/Chess_bdt60.png", enable_events=True, key='bdt')],
    [psg.Image(filename="chess-transparent/Chess_blt60.png", enable_events=True, key='blt')],
    [psg.Image(filename="chess-transparent/Chess_kdt60.png", enable_events=True, key='kdt')],
    [psg.Button('Exit')]
]

window = psg.Window('Draggable Image Example', layout, finalize=True, size=(400,400))



while True:
    event, values = window.read()

    print("event: ", event)
    print("values: ", values)

    if event in (psg.WIN_CLOSED, 'Exit'):
        break
    


window.close()

"""
