from modelView.nodes.NodeSimple import NodeSimple, NodeType
from modelView.nodes.NodeCharacter import NodeCharacter

# --- NODO SIMPLE (HISTORIA) ---
Root_test_tree = NodeSimple()

Root_test_tree.setType(NodeType.STORY)
Root_test_tree.setContent("¡Wubba lubba dub dub! Bienvenido a la aventura multiversal, Rick.")
Root_test_tree.setOptions(["Buscar Petaca", "Insultar a Summer"])

# --- NODO DE DIÁLOGO (PERSONAJE) ---
Dialogue_test_node = NodeCharacter()

Dialogue_test_node.setType(NodeType.DIALOGUE)
Dialogue_test_node.setContent("Rick, eres la versión más patética que he encontrado. Todo lo que haces es predecible, incluyendo este test. Deja de intentar ser especial. El universo es vasto y tú eres irrelevante.")
Dialogue_test_node.setOptions(["¡Cállate, Morty!", "Dime dónde está la Ciudadela"])

Dialogue_test_node.setCharacterPictureRoute("view/assets/characters/evil_morty.png") 
Dialogue_test_node.setCharacterName("Evil Morty")

# --- NODO DE LUCHA (PERSONAJE) ---
Fight_test_node = NodeCharacter()

Fight_test_node.setType(NodeType.FIGHT)
Fight_test_node.setContent("¡Hora de un duelo dimensional, Rick! ¿Crees que tu pistola de portales es rival para mi campo de fuerza mental?")
Fight_test_node.setOptions(["Usar el Cristal de Culillos", "Activar autodestrucción"])

Fight_test_node.setCharacterPictureRoute("view/assets/characters/evil_morty.png")
Fight_test_node.setCharacterName("Evil Morty")
