from view.main import GameInterface
from modelView.DisjointSets import Disjoint_Set as DisjointSets
from modelView.Rick import Rick

sets = DisjointSets(4)
sets.build()
GameScreen = GameInterface()
rick = Rick(GameScreen, sets)
GameScreen.set_rick(rick)
sets.setRicK(rick)
GameScreen.start_gui()

