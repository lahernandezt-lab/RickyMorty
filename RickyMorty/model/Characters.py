# Ejemplo de conjuntos disyuntos
# Cada valor debe ser un objeto de tipo Character!

from modelView.Types import Code, NodeType
from modelView.Character import Character
from modelView.nodes.NodeSimple import NodeSimple

Characters = {
    # GRUPO 1: Ciudadela de Ricks (Indices 0-5)
    0: Character("Evil Morty",
                 "view/assets/characters/nodes/evil_morty.png",
                 "view/assets/characters/mini_alive/evil_morty-vivo.png",
                 "view/assets/characters/mini_dead/evil_morty-muerto.png",
                 (175,160),
                 NodeSimple(NodeType.STORY, '''"Me recuerdas a mí, pero con más defectos y menos éxito," dice Evil Morty con una sonrisa fría. "Pensaste que ibas a escapar de la Ciudadela tan fácilmente, ¿no? Pobre Rick."

Te pones tu Pistola de Portales en modo de combate y decides atacarlo con''', ['Tu Plumbus', 'Batería de Plasma'], [6, Code.DKTMU])
                 ),
    1: Character("Presidente Morty",
                 "view/assets/characters/nodes/presidente_morty.png",
                 "view/assets/characters/mini_alive/presidente_morty-vivo.png",
                 "view/assets/characters/mini_dead/presidente_morty-muerto.png",
                 (380,160),
                 NodeSimple(NodeType.STORY, '''"¡Esto es insensato, Rick! Estás desestabilizando toda la curva finita central," grita el Presidente Morty, visiblemente exasperado. "¡No me dejas otra opción que ordenar a la Guardia de la Ciudadela que te desintegre!"

Mientras la alarma suena y te rodea, tu instinto te dice que debes''', ['hackear la alarma', 'lanzar un Batarang'], [Code.DKTMU, 7])
                 ),
    2: Character("Rick Borracho",
                 "view/assets/characters/nodes/rick_borracho.png",
                 "view/assets/characters/mini_alive/rick_borracho-vivo.png",
                 "view/assets/characters/mini_dead/rick_borracho-muerto.png",
                 (275, 265),
                 NodeSimple(NodeType.STORY, '''"¡Eh, yo también soy Rick! ¿Por qué tienes que ser tan... *hic*... arrogante? Yo inventé el portal a ese planeta de globos." Un Rick patéticamente ebrio se abalanza sobre ti. "¡Dame tu petaca!"

Lo empujas y al caer, notas cerca de ti en el suelo''', ['un rayo reductor', 'un destornillador sónico'], [8, Code.DKTMU])
                 ),
    3: Character("Rick Granjero",
                 "view/assets/characters/nodes/rick_granjero.png",
                 "view/assets/characters/mini_alive/rick_granjero-vivo.png",
                 "view/assets/characters/mini_dead/rick_granjero-muerto.png",
                 (520,160),
                 NodeSimple(NodeType.STORY, '''"¡No pasarás por mi granja interdimensional sin pagar el peaje! ¡Mis tomates son orgánicos!" grita un Rick con sombrero de paja. "¡Ahora, entrégame el Chip de Estabilidad Portal que robaste!"

Comienza una pelea ridícula donde te lanza calabazas explosivas. Te las arreglas para inmovilizar su Portal Gun. Entonces le''', ['disparas un rayo aturdidor', 'usas un inversor de gravedad'], [Code.DKTMU, Code.DKTMU])
                 ),
    4: Character("Guardia de la Ciudadela",
                 "view/assets/characters/nodes/guardia_ciudadela.png",
                 "view/assets/characters/mini_alive/guardia_ciudadela-vivo.png",
                 "view/assets/characters/mini_dead/guardia_ciudadela-muerto.png",
                 (670,160),
                 NodeSimple(NodeType.STORY, '''"¡Alto ahí, Rick C-137! ¡Las reglas de la Ciudadela prohíben estrictamente el sarcasmo no autorizado!" Un Guardia de la Ciudadela se interpone entre tú y la salida, blandiendo un batón eléctrico.

"¡Oh, mira, Morty! Un robot con un complejo de superioridad." El guardia te aplasta contra el piso. Logras recuperar el aliento y decides''', ['activar tu campo de fuerza', 'sacar la Pistola de Portales'], [Code.DKTMU, Code.DKTMU])
                 ),
    5: Character("Morty Científico",
                 "view/assets/characters/nodes/morty_cientifico.png",
                 "view/assets/characters/mini_alive/morty_cientifico-vivo.png",
                 "view/assets/characters/mini_dead/morty_cientifico-muerto.png",
                 (1020, 160),
                 NodeSimple(NodeType.STORY, '''Un Morty con un mono de laboratorio te saluda. "Rick, no lo hagas. Este experimento podría colapsar la Dimensión K-47. Ya lo calculé."

"¿Calcular? ¿Ese es tu truco, Morty? La ciencia es un arte, no matemáticas aburridas." Te abres paso. El Morty científico saca un tubo de ensayo con un líquido verde hirviendo.''', ['Usar un Plumbus', 'Atravesar el Portal'], [59, Code.DKTMU])
                 ),
    # GRUPO 2: Federación Galáctica (Indices 6-11)
    6: Character("Agente Vancie",
                 "view/assets/characters/nodes/agente_vancie.png",
                 "view/assets/characters/mini_alive/agente_vancie-vivo.png",
                 "view/assets/characters/mini_dead/agente_vancie-muerto.png",
                 (810, 160),
                 NodeSimple(NodeType.STORY, '''El Agente Vancie de la Federación te apunta con un rifle de plasma. "¡Te sugiero que regreses, C-137! El espacio profundo no es un parque temático."

"Lo sé, Vancie. Es mucho más divertido. Ahora, ¿me vas a multar o a pelear?" Vancie dispara, pero el rayo rebota en tu campo de fuerza. Él exige''', ['"¿Quién te dio ese campo?"', '"¡Alto en nombre de la ley!"'], [Code.DKTMU, Code.DKTMU])
                 ),
    7: Character("Gromflomita Líder",
                 "view/assets/characters/nodes/gromflomita_lider.png",
                 "view/assets/characters/mini_alive/gromflomita_lider-vivo.png",
                 "view/assets/characters/mini_dead/gromflomita_lider-muerto.png",
                 (930, 260),
                 NodeSimple(NodeType.STORY, '''"¡Tu insolencia nos costó la Batalla de la Tierra C-137! ¡Morirás por eso!" grita el Gromflomita Líder. Sus tres ojos brillan con odio mientras sus pinzas se abren.

En un rápido movimiento, lanzas una Caja Meeseeks para distraerlo. Él se confunde. Es tu oportunidad para''', ['Disparar al ojo principal', 'Sacar la Batería'], [Code.DKTMU, Code.DKTMU])
                 ),
    8: Character("Krombopulos Michael",
                 "view/assets/characters/nodes/krombopulos_michael.png",
                 "view/assets/characters/mini_alive/krombopulos_michael-vivo.png",
                 "view/assets/characters/mini_dead/krombopulos_michael-muerto.png",
                 (810,370),
                 NodeSimple(NodeType.STORY, '''"Hola, Rick. ¿Vienes por mí? Lástima, tenía un contrato con un Zigerion para la próxima semana," dice Krombopulos Michael, un asesino amigable. "Esto es solo negocios."

Te lanza una granada sónica, pero la atrapas con un portal de bolsillo. "Michael, ¿alguna vez pensaste en ser artista en lugar de asesino?"''', ['"No lo creo"', '"Algún día"'], [Code.DKTMU, Code.DKTMU])
                 ),
    9: Character("Birdperson (Cyborg)",
                 "view/assets/characters/nodes/birdperson_cyborg.png",
                 "view/assets/characters/mini_alive/birdperson_cyborg-vivo.png",
                 "view/assets/characters/mini_dead/birdperson_cyborg-muerto.png",
                 (670,375),
                 NodeSimple(NodeType.STORY, '''"Tu amistad es un virus que debe ser erradicado, Rick," dice el cyborg Birdperson con voz metálica. Sus alas mecánicas giran peligrosamente.

Birdperson te embiste, pero te conviertes en una versión diminuta de ti mismo. Mientras él busca, tú le disparas con el''', ['rayo desintegrador', 'Cristal de Culillos'], [Code.DKTMU, Code.DKTMU])
                 ),
    10: Character("Tammy",
                  "view/assets/characters/nodes/tammy.png",
                  "view/assets/characters/mini_alive/tammy-vivo.png",
                  "view/assets/characters/mini_dead/tammy-muerto.png",
                  (560,515),
                  NodeSimple(NodeType.STORY, '''"Siempre supe que eras un peligro para la estabilidad galáctica, Rick," dice Tammy, con el traje de la Federación. "Ahora, vas a pagar por lo que le hiciste a Birdperson... y por arruinar mi fiesta de graduación."

Te lanza una red de energía que neutraliza tus gadgets. Te teletransportas justo a tiempo y gritas''', ['"¡Hora del baile!"', '"¡No hemos terminado!"'], [Code.DKTMU, Code.DKTMU])
                  ),
    11: Character("Dr. Wong (Psiquiatra)",
                  "view/assets/characters/nodes/dr_wong.png",
                  "view/assets/characters/mini_alive/dr_wong-vivo.png",
                  "view/assets/characters/mini_dead/dr_wong-muerto.png",
                  (1020,400),
                  NodeSimple(NodeType.STORY, '''"Rick, no podemos resolver esto con violencia. Necesitamos tener una conversación honesta sobre tus miedos de intimidad." La Dra. Wong intenta calmarte.

"¿Miedos? ¡Mi único miedo es convertirme en un Jerry!" le disparas, pero ella lo bloquea con un campo de fuerza mental. Ella te pide que uses''', ['el Plumbus', 'la Batería Microversal'], [Code.DKTMU, Code.DKTMU])
                  ),
    # GRUPO 3: Seres Interdimensionales (Indices 12-19)
    12: Character("Abradolf Lincler",
                  "view/assets/characters/nodes/abradolf_lincler.png",
                  "view/assets/characters/mini_alive/abradolf_lincler-vivo.png",
                  "view/assets/characters/mini_dead/abradolf_lincler-muerto.png",
                  (550,285),
                  NodeSimple(NodeType.STORY, '''"Debo destruir, ¡pero también debo unirme a ti! ¡El dilema de la paz!" grita Abradolf Lincler, mitad Abraham Lincoln, mitad Hitler. Su confusión te da tiempo para atacar.

Él lanza un discurso confuso sobre la democracia y el genocidio. Te acercas y le gritas al oído''', ['"¡Eres una paradoja andante!"', '"¡Llamen al director!"'], [Code.DKTMU, Code.DKTMU])
                  ),
    13: Character("Reina de las Serpientes",
                  "view/assets/characters/nodes/reina_serpiente.png",
                  "view/assets/characters/mini_alive/reina_serpiente-vivo.png",
                  "view/assets/characters/mini_dead/reina_serpiente-muerto.png",
                  (440,420),
                  NodeSimple(NodeType.STORY, '''La Reina Serpiente te mira con ojos fríos. "Los humanos son una plaga temporal, Rick. Mi especie gobernará este segmento del tiempo."

"¡Oh, mira, Morty! ¡Un 'Snake-Terminator' pretencioso!" La Reina intenta morderte, pero activas un escudo de energía. Decides''', ['usar tu Plasma Verde', 'cortar su cola'], [Code.DKTMU, Code.DKTMU])
                  ),
    14: Character("Mister Nimbus",
                  "view/assets/characters/nodes/mister_nimbus.png",
                  "view/assets/characters/mini_alive/mister_nimbus-vivo.png",
                  "view/assets/characters/mini_dead/mister_nimbus-muerto.png",
                  (170,375),
                  NodeSimple(NodeType.STORY, '''"Rick, ¿no te cansas de insultar a la gente?" pregunta Mister Nimbus, el rey del océano, mientras flota sobre un chorro de agua. "Yo soy la ley y el orden aquí."

"¡Tú eres solo un viejo desnudo con superpoderes!" Nimbus te ataca con un chorro de agua a presión. Te proteges y gritas''', ['"¡Calma, viejo!"', '"¡Te voy a secar!"'], [Code.DKTMU, Code.DKTMU])
                  ),
    15: Character("Beth Clon",
                  "view/assets/characters/nodes/beth_clon.png",
                  "view/assets/characters/mini_alive/beth_clon-vivo.png",
                  "view/assets/characters/mini_dead/beth_clon-muerto.png",
                  (310,375),
                  NodeSimple(NodeType.STORY, '''Una de las Beth (la clon o la original, nunca lo sabrás) aparece con un rifle de caza. "¡Tú eres el que está arruinando mi vida, papá! ¡Deja de meterte con mis sentimientos!"

"¡Oh, drama! ¡Justo lo que necesitaba en un apocalipsis multiversal!" Beth te dispara. Te aburres de la situación y decides dispararle con''', ['un rayo reductor', 'el Cargador de Plasma'], [Code.DKTMU, Code.DKTMU])
                  ),
    16: Character("Reina Alienígena",
                  "view/assets/characters/nodes/reina_alienigena.png",
                  "view/assets/characters/mini_alive/reina_alienigena-vivo.png",
                  "view/assets/characters/mini_dead/reina_alienigena-muerto.png",
                  (170,515),
                  NodeSimple(NodeType.STORY, '''"¡Tu especie ha contaminado 12 galaxias, C-137! ¡Serás juzgado por el Consejo Intergaláctico!" grita una reina alienígena.

"¡Consejo! ¡Yo soy el consejo, cariño!" Ella te lanza un parásito de control mental. Lo evitas y sacas un Mega Seed. Es tu oportunidad de''', ['Cortar su cabeza', 'Usar el Portal Inestable'], [Code.DKTMU, Code.DKTMU])
                  ),
    17: Character("Armothy",
                  "view/assets/characters/nodes/armothy.png",
                  "view/assets/characters/mini_alive/armothy-vivo.png",
                  "view/assets/characters/mini_dead/armothy-muerto.png",
                  (310,515),
                  NodeSimple(NodeType.STORY, '''"¡La venganza es un plato que se sirve frío, Rick!" grita Armothy, el hombre-brazo que tomó el control del brazo de Rick. Te ataca con fuerza bruta.

Te burlas de su tamaño muscular. "Eres todo brazo y cero cerebro, ¿no?" Armothy te golpea. Sientes que es hora de usar''', ['la Caja de Meeseeks', 'el Chip de Estabilidad'], [Code.DKTMU, Code.DKTMU])
                  ),
    18: Character("Mr. Poopybutthole",
                  "view/assets/characters/nodes/mr_poopybutthole.png",
                  "view/assets/characters/mini_alive/mr_poopybutthole-vivo.png",
                  "view/assets/characters/mini_dead/mr_poopybutthole-muerto.png",
                  (755,515),
                  NodeSimple(NodeType.STORY, '''"Ooooweeeee, Rick! ¿Por qué tienes que pelear con todos? ¡Podríamos ser amigos!" grita Mr. Poopybutthole.

"¡Tú eres un parásito o un amigo falso! ¡No puedo distinguirte, y eso me irrita!" Poopybutthole te dispara. Lo ignoras y decides''', ['"¡Robin Hood!"', 'Dispararle en la cabeza'], [Code.DKTMU, Code.DKTMU])
                  ),
    19: Character("Doofus Rick",
                  "view/assets/characters/nodes/doofus_rick.png",
                  "view/assets/characters/mini_alive/doofus_rick-vivo.png",
                  "view/assets/characters/mini_dead/doofus_rick-muerto.png",
                  (920,515),
                  NodeSimple(NodeType.STORY, '''"¡Oh, disculpa! ¡No te vi! Solo estaba comiendo un poco de caca de mi propio tarro," dice Doofus Rick.

"¡Eres la prueba de que hay dimensiones que deberían ser destruidas, no salvadas!" Sacas tu Pistola de Portales y decides teletransportarlo a la dimensión de''', ['los gatos gigantes', 'los hombres pájaro'], [Code.DKTMU, Code.DKTMU])
                  )
}
