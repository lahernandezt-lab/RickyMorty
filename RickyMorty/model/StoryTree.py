from modelView.Types import NodeType, RickStacks

StoryTree = {
    1: {
        'type': NodeType.BLANK,
        'content': '''"¡Morty! *Burp* ¡Despierta, Morty! Mira dónde estamos. Esto no es la Dimensión 35-C, esto es mucho peor... estamos en una universidad pública del tercer mundo, Morty.

Estamos en la Universidad Nacional de Colombia. Algún idiota derramó jugo de lulo sobre mi Pistola de Portales y ahora los componentes vitales están esparcidos por todo el campus."''',
        'children': [2]
    },
    2: {
        'type': NodeType.BLANK,
        'content': '''"Escúchame bien, Morty. Necesitamos recuperar 6 componentes específicos para largarnos de aquí antes de que nos atrape la burocracia académica o nos vendan brownies mágicos.

El radar indica que el primer componente lo tiene un sujeto inestable cerca del edificio de Artes. Vamos a tener que 'socializar' a mi manera."''',
        'children': [3]
    },
    3: {
        'type': NodeType.BLANK,
        'content': '''"¿Listo para traumatizar estudiantes de artes, Morty?

Mira, ahí está ese borracho bloqueando el camino hacia la Facultad. Parece una versión patética de mí mismo."''',
        'children': [4]
    },
    4: {
        'type': NodeType.STORY,
        'content': '''Te acercas a "La Playita" y ves a un Rick completamente ebrio (Rick Borracho) balbuceando sobre filosofía barata.

"¡Eh! ¡Ustedes! *Hic* ¿Tienen monedas para el bus? ¡Yo inventé la educación gratuita!" grita mientras se tambalea.

Rick C-137 rueda los ojos. "Dios, odio ver mi futuro alternativo. Morty, encárgate, yo preparo el arma."''',
        'options': ['Patearle la botella', 'Ofrecerle un trago'],
        'children': [5, 5]
    },

    # ENCUENTRO 1: RICK BORRACHO (ID 2)
    5: {
        'type': NodeType.FIGHT,
        'content': '"¡Nadie toca mi aguardiente, hipócrita de bata blanca!"',
        'options': ['Pelear por tu dignidad'],
        'children':[9],
        'character': 2, # Rick Borracho
        'set': 0
    },
    6: {
        'type': NodeType.BLANK,
        'content': '''Intentaste razonar con el borracho, pero te vomitó encima. Fue asqueroso. Los estudiantes de artes te hicieron un performance interpretativo sobre tu fracaso.

Rick te arrastró fuera de la zona, humillado. "Buen trabajo, Morty. Ahora hueles a fracaso y alcohol barato."''',
        'children': [10]
    },
    7: {
        'type': NodeType.BLANK,
        'content': '''Le ofreciste un trago, pero él quería toda la botella. Se lanzó sobre ti y te golpeó con una guitarra acústica desafinada.

Terminaste inconsciente en el pasto. Rick te despertó con una cachetada. "Levántate, inútil. Tenemos trabajo que hacer."''',
        'children': [10]
    },
    8: {
        'type': NodeType.BLANK,
        'content': '''Intentaste esquivarlo, pero el Rick Borracho tiene un estilo de pelea impredecible (el estilo del mono ebrio). Te tropezaste con una mochila artesanal.

Rick suspira. "Eres una vergüenza para el apellido Smith."''',
        'children': [10]
    },
    9: {
        'type': NodeType.BLANK,
        'content': '''Le diste una patada giratoria al Rick Borracho que lo envió directo a dormir la mona en los arbustos.

Entre sus ropas sucias, encuentras algo brillando. "¡Bingo, Morty! ¡Mira esto!"''',
        'children': [11]
    },
    10: {
        'type': NodeType.BLANK,
        'content': '''Mientras el Rick Borracho se desmayaba solo por el exceso de alcohol, aprovechaste para registrar sus bolsillos.

"Al fin algo útil en este basurero," dice Rick limpiando el objeto.''',
        'children': [11]
    },
    11: {
        'type': NodeType.BLANK,
        'content': '''Rick sostiene el objeto triunfante. Luego, revisa su tablet. "El siguiente componente está en el Edificio de Ciencia y Tecnología (CyT). Al parecer un nerd pretencioso lo está usando para un proyecto de tesis."

Caminan hacia el CyT. Allí, bloqueando la entrada de los laboratorios, está un Morty con bata (Morty Científico).''',
        'children': [12]
    },
    12: {
        'type': NodeType.DIALOGUE,
        'content': '''"Alto ahí. El acceso a los laboratorios está restringido a personal con IQ superior a 200," dice el Morty Científico ajustándose las gafas.''',
        'options': ['"¡Yo soy Rick Sánchez!"', '"Cállate, nerd"'],
        'children': [13,13],
        'character': 5 # Morty Científico
    },
    13: {
        'type': NodeType.FIGHT,
        'content': '"Mis cálculos indican una probabilidad del 99% de que voy a patear tu trasero anciano."',
        'options': ['Demostrarle la mala matemática'],
        'children':[14],
        'character': 5,
        'set': 1
    },
    14: {
        'type': NodeType.BLANK,
        'content': '''"¿La ciencia es un arte, recuerdas?" Rick sobrecarga el calculadora del Morty Científico haciendo que explote en su cara.

Mientras el Morty nerd llora por sus datos perdidos, Rick entra al laboratorio y encuentra un cristal azul brillante conectado a una protoboard.''',
        'children': [16]
    },
    # RECOMPENSA 1: CRISTAL DE CULILLOS (Mapping to CRISTAL_DE_CULILLOS)
    16: {
        'type': NodeType.SPECIAL,
        'content': '''Tomas el objeto. Es el 'Cristal de Culillos'.

"Perfecto, Morty. Este cristal permite saltos espaciales de corto alcance. Ideal para evitar las filas de la cafetería... o para escapar de este infierno."

Usando el cristal, deciden teletransportarse a:''',
        'options': ['La Plaza Che','La Biblioteca Central'],
        'children': [18,17], # Swapped logic slightly to fit map
        'stack': RickStacks.CRISTAL_DE_CULILLOS
    },


    
    17: {
        'type': NodeType.BLANK,
        'content': '''Se teletransportan a la Biblioteca Central. Está llena de estudiantes durmiendo.

"Silencio, Morty. Huelo burocracia y maldad pura aquí."''',
        'children': [19]
    },
    18: {
        'type': NodeType.BLANK,
        'content': '''Aparecen en medio de la Plaza Che. Hay una asamblea estudiantil ocurriendo.

"¡Abajo el sistema!" gritan. En la tarima, liderando la revuelta, está nada menos que Evil Morty con un parche en el ojo.''',
        'children': [29]
    },
    
    # ENCUENTRO: EVIL MORTY (ID 0) 
    19: {
        'type': NodeType.DIALOGUE,
        'content': '''Encuentras a Evil Morty sentado en el escritorio de préstamo de libros.

"Te estaba esperando, Rick. Sabía que vendrías por el componente."''',
        'options': ['"¿Evil Morty?"', '"Dame eso"'],
        'children': [20,21],
        'character': 0 
    },
    20: {
        'type': NodeType.BLANK,
        'content': '''"El mismo. Y no, no te daré el chip. Planeo usarlo para hackear el sistema de notas de la universidad."''',
        'children': [22]
    },
    21: {
        'type': NodeType.BLANK,
        'content': '''"Siempre tan directo, Rick. Pero me temo que tu intelecto no es rival para mi astucia política."''',
        'children': [22]
    },
    22: {
        'type': NodeType.FIGHT,
        'content': '''"Veamos si puedes aprobar este examen final, Rick."''',
        'options': ['"¡Reprobado!"'],
        'children':[23],
        'character': 0,
        'set': 2
    },
    23: {
        'type': NodeType.BLANK,
        'content': '''Tras una batalla mental y física, Evil Morty escapa por un portal de emergencia, dejando caer un dispositivo verde.

Rick lo recoge. "Ja. Novato."''',
        'children': [24]
    },
    
    # RECOMPENSA 2: CARGADOR DE PLASMA VERDE (Mapping to CARGADOR_DE_PLASMA)
    24: {
        'type': NodeType.SPECIAL,
        'content': '''Tienes el 'Cargador de Plasma Verde'.

"Con esto podemos manipular la carga de nuestros escudos, Morty. O recargar mi teléfono, lo que es más importante ahora mismo."

¿Qué hacemos ahora?''',
        'options': ['Ver las noticias','Ir a la Asamblea'],
        'children': [26,28],
        'stack': RickStacks.CARGADOR_DE_PLASMA
    },
    25: {
        'type': NodeType.BLANK, # Unused logic path fix
        'content': '''Rick revisa su teléfono. "Aburrido. Vamos a buscar acción."''',
        'children': [28]
    },
    26: {
        'type': NodeType.BLANK,
        'content': '''Revisas las noticias universitarias en el celular. "¡Protesta masiva en la Plaza Che! Se reporta uso de tecnología alienígena".

"Suena a que alguien más tiene una pieza de mi pistola, Morty. Vamos."''',
        'children': [28]
    },
    27: { # Unused
        'type': NodeType.BLANK,
        'content': '''...''',
        'children': [28]
    },
    28: {
        'type': NodeType.BLANK,
        'content': '''Llegan a la Plaza Che. El ambiente está tenso. Hay humo y capuchos.

En el centro, un Rick Granjero está cultivando plantas extrañas en el concreto.''',
        'children': [29]
    },
    
    # ENCUENTRO: RICK GRANJERO (ID 3)
    29: {
        'type': NodeType.DIALOGUE,
        'content': '''"¡Lárguense de mis cultivos hidropónicos!" grita el Rick Granjero agitando una horca láser.''',
        'options': ['"¿Tomates?"', '"Danos la pieza"'],
        'children': [30,30],
        'character': 3
    },
    30: {
        'type': NodeType.DIALOGUE,
        'content': '''"¡No son tomates, ignorante! Son Mega-Semillas. Y necesito la energía de esta Batería para que crezcan." Señala un objeto morado brillante.''',
        'options': ['Reírse', 'Negociar'],
        'children': [31,32],
        'character': 3
    },
    31: {
        'type': NodeType.BLANK,
        'content': '''Rick se ríe. "Eres la versión más aburrida de mí. ¿Rick Granjero? ¿En serio?"''',
        'children': [33]
    },
    32: {
        'type': NodeType.BLANK,
        'content': '''"Mira, te cambio esas semillas por un cupón para la cafetería," miente Rick.''',
        'children': [33]
    },
    33: {
        'type': NodeType.FIGHT,
        'content': '''"¡Cosecharás lo que siembras!"''',
        'options': ['Desmalezar'],
        'children':[34],
        'character': 3,
        'set': 3
    },
    34: {
        'type': NodeType.BLANK,
        'content': '''Usas un herbicida experimental. El Rick Granjero sale corriendo protegiendo sus overoles.

"Nadie se mete con la agricultura sostenible," murmura mientras huye. Dejas el lugar hecho un desastre.''',
        'children': [39]
    },
    # --- NODO 35: Rick Obliga a ir a fem ---
    35: {
        'type': NodeType.STORY,
        'content': '''"¡Pero por favoooor, Morty! ¡Ese FEM tiene una tecnología tan estúpida que sería criminal no robarla! ¡Además, el guion dice que tenemos que ir allí! ¡No puedes simplemente saltarte el capítulo, jugador!" exige Rick, sujetando tu brazo para abrir un portal.
        
        "¡Wubba lubba dub dub! ¡Vámonos de aquí!"''',
        'options': ['"Agt, está bien, vamos a Wakanda"', '"No puedo discutir contigo, Rick"'],
        'children': [70] # Conecta con la llegada a FEM (Nodo 70)
    },
    # --- NODOS 36-38: Interrogatorio al Rick Granjero y transición ---
    36: {
        'type': NodeType.BLANK,
        'content': '''El Rick Granjero se retuerce en el suelo, abrazando una de sus plantas mutantes. "¡Mis bebés! ¡Iban a ganar el concurso de botánica interespecie!"

Rick le pone el pie encima. "¿Dondé está la Batería Microversal, hippie? ¿Y no me digas que la fumaste?"''',
        'children': [37]
    },
    37: {
        'type': NodeType.BLANK,
        'content': '''"Está ahí... alimentando el sistema de riego," gimotea el granjero. "Pero ya no importa, la Federación Galáctica está aterrizando en el Estadio. ¡Van a expropiarlo todo!"

"Gracias por el dato. Ahora vuelve a tu comuna," dice Rick.''',
        'children': [38]
    },
    38: {
        'type': NodeType.BLANK,
        'content': '''Caminas hacia el sistema de riego improvisado. En el centro, brillando con una luz violeta ominosa, está la pieza que buscaban.

"La gente usa esto para cultivar lechugas... Dios, qué desperdicio de tecnología nivel omega," se queja Rick.''',
        'children': [39] # Lleva a encontrar la pieza visualmente
    },
    39: {
        'type': NodeType.BLANK,
        'content': '''En medio de la huerta destruida, ves el objeto que alimentaba las plantas. Una batería con un universo en miniatura dentro.''',
        'children': [40]
    },
    
    # RECOMPENSA 3: BATERIA_MICROVERSAL (Mapping to BATERIA_MICROVERSAL)
    40: {
        'type': NodeType.SPECIAL,
        'content': '''Recuperas la 'Batería Microversal'.

"Esclavitud con pasos extra, Morty. Pero genera una cantidad absurda de energía. Cuidado, no la agites o destruirás una civilización entera."

Rick mira hacia el Estadio Alfonso López. "Siguiente parada: El Estadio. Detecto una señal de la Federación Galáctica."''',
        'options': ['Ir al Estadio','Destruir algo antes'],
        'children': [43,42],
        'stack': RickStacks.BATERIA_MICROVERSAL
    },
    # --- NODO 41: Uso destructivo de la Batería Microversal ---
    41: {
        'type': NodeType.BLANK,
        'content': '''Decides probar el poder de la Batería Microversal. Conectas los cables a un generador cercano y sobrecargas la red eléctrica de la plaza.
        
¡BOOM! Una explosión morada destruye la estatua del Che y varios puestos de empanadas.

"¡Jajaja! ¡Eso es lo que llamo una reforma estructural, Morty!" grita Rick. "Vámonos antes de que nos cobren los daños."''',
        'children': [43] # Lleva al Estadio
    },
    42: {
        'type': NodeType.BLANK,
        'content': '''Disparas un rayo de energía al edificio de Sociología. "Ups. Bueno, nadie notará la diferencia," dice Rick. Ahora sí, van al Estadio.''',
        'children': [43]
    },
    43: {
        'type': NodeType.BLANK,
        'content': '''En el Estadio, Birdperson (versión Cyborg) y Tammy están instalando una antena de transmisión.''',
        'children': [44]
    },
    
    # ENCUENTRO: BIRDPERSON CYBORG (ID 9) y TAMMY (ID 10) 
    44: {
        'type': NodeType.DIALOGUE,
        'content': '''"Rick Sanchez. Tu presencia viola 400 leyes galácticas," dice Birdperson con voz robótica.''',
        'options': ['"¡Hombre Pájaro!"', '"Maldita Tammy"'],
        'children': [45,45],
        'character': 9
    },
    45: {
        'type': NodeType.BLANK,
        'content': '''"Él ya no es tu amigo, Rick. Es propiedad de la Federación," dice Tammy con una sonrisa cínica.''',
        'options': ['"Voy a disfrutar desplumándolo,"',' "respondes sacando tu arma."'],
        'children': [47]
    },
    46: { # Skipped
        'type': NodeType.DIALOGUE,
        'content': '''...''',
        'children': [47],
        'character': 9
    },
    47: {
        'type': NodeType.DIALOGUE,
        'content': '''"Birdperson, elimínalo. Tengo una boda que planear," ordena Tammy.''',
        'options': ['"¡La boda roja!"', '"¡Traidora!"'],
        'children': [48,49],
        'character': 10
    },
    48: {
        'type': NodeType.BLANK,
        'content': '''"¡Nadie invita a Rick Sánchez a una boda y vive para contarlo!" gritas.''',
        'children': [50]
    },
    49: {
        'type': NodeType.BLANK,
        'content': '''"Tammy, eres lo peor que le ha pasado a la galaxia, y eso incluye a los Jerry," dice Rick.''',
        'children': [50]
    },
    50: {
        'type': NodeType.DIALOGUE,
        'content': '''Birdperson despliega sus alas metálicas.''',
        'options': ['Llorar', 'Pelear'],
        'children': [51,51],
        'character': 9
    },
    51: {
        'type': NodeType.FIGHT,
        'content': '''"Protocolo de eliminación activado."''',
        'options': ['¡Wubba Lubba Dub Dub!'],
        'children':[52],
        'character': 9,
        'set': 4
    },
    52: {
        'type': NodeType.BLANK,
        'content': '''Usando la Batería Microversal, sobrecargas los circuitos de Birdperson. Cae al suelo, echando chispas. Tammy huye cobardemente hacia la Rectoría.

Entre los restos de tu amigo cyborg, encuentras un extraño dispositivo naranja.''',
        'children': [53]
    },
    53: {
        'type': NodeType.BLANK,
        'content': '''"Lo siento, amigo," dice Rick bebiendo de su petaca.

Caminan hacia el edificio Uriel Gutiérrez (Administrativo). En la entrada, custodiando el paso, está el Agente Vancie.''',
        'children': [54]
    },
    
    # ENCUENTRO: AGENTE VANCIE (ID 6) 
    54: {
        'type': NodeType.DIALOGUE,
        'content': '''"Alto ahí. Tienen que llenar el formulario 34-B para pasar," dice el burócrata de la Federación.''',
        'options': ['"¿Formulario?"', '"Cómete esto"'],
        'children': [55,55],
        'character': 6
    },
    55: {
        'type': NodeType.DIALOGUE,
        'content': '''"Para obtener el 'Portal Inestable', debes sacrificar lo que más amas... Tu tiempo. Toma un turno y espera 4 horas."''',
        'options': ['"¡Jamás!"', '"¡Mátenme!"'],
        'children': [56,56],
        'character': 6
    },
    56: {
        'type': NodeType.DIALOGUE,
        'content': '''Rick se impacienta. "Mira, insecto, no tengo tiempo para trámites."''',
        'options': ['Disparar', 'Ignorar'],
        'children': [57,57], # Skip sacrifice logic, go straight to fight
        'character': 6
    },

    57: {
        'type': NodeType.FIGHT,
        'content': '''"¡Seguridad! ¡Tenemos un código C-137!"''',
        'options': ['Atacar'],
        'children':[58], # Loop back to getting the stack
        'character': 6,
        'set': 5
    },
    58: {
        'type': NodeType.SPECIAL,
        'content': '''Recoges el 'Portal Inestable' del cadáver del burócrata.

            "Es irónico, Morty. La burocracia universitaria casi nos mata de aburrimiento, pero conseguimos la pieza."

            De repente, escuchas un ruido en el Auditorio León de Greiff.''',
        'options': ['Ir al Auditorio'],
        'children': [60],
        'stack': RickStacks.PORTAL_INESTABLE
    },
    59: { # Logic check item
        'type': NodeType.BLANK,
        'content': '''...''',
        'children': [60]
    },
    60: {
        'type': NodeType.BLANK,
        'content': '''Dejas al Agente Vancie enterrado bajo una montaña de formularios sellados.

"La burocracia es lenta, pero mi láser es instantáneo," sentencia Rick.

Con el 'Portal Inestable' en mano, deciden cruzar el campus hacia el Auditorio León de Greiff, donde se detecta la siguiente señal. En el camino, alguien conocido los intercepta.''',
        'children': [61]
    },

    # Encuentro sorpresa con Mr. Poopybutthole (ID 18)
    61: {
        'type': NodeType.DIALOGUE,
        'content': '''"¡Oooooweeee! ¡Rick! ¡Morty! ¡Qué sorpresa verlos en la universidad!"
        
Un pequeño Mr. Poopybutthole con un carnet estudiantil colgado al cuello aparece saltando.''',
        'options': ['"¿Qué haces aquí?"', '"¡Aléjate!"'],
        'children': [62, 62],
        'character': 18
    },
    62: {
        'type': NodeType.FIGHT,
        'content': '''"Solo estoy terminando mi maestría en Artes Escénicas, ooooweee. Pero dicen que ustedes están causando problemas. ¡El Consejo Superior me pidió que los detuviera!"
        
Saca un bastón de karate. "¡Lo siento, Rick!"''',
        'options': ['Golpear al pequeño'],
        'children':[63],
        'character': 18,
        'set': 8
    },
    63: {
        'type': NodeType.BLANK,
        'content': '''Empujas a Mr. Poopybutthole y cae rodando por el césped. 
        
"¡Ay! ¡Ooooweee! ¡Eso me va a dejar un morado para el semestre que viene!"

"Vámonos, Morty. Nunca sé si ese tipo es real o un parásito de la memoria," dice Rick acelerando el paso.''',
        'children': [64]
    },
    64: {
        'type': NodeType.BLANK,
        'content': '''Finalmente llegan al Auditorio León de Greiff. Es un edificio imponente y oscuro. La entrada está abierta, como una boca esperando tragárselos.

"El chip de realidad está ahí dentro," susurra Rick. "Prepara tu arma. Esto huele a una trampa de asesinos profesionales."''',
        'children': [65] # Conecta con Krombopulos Michael
    },
    
    # ENCUENTRO: KROMBOPULOS MICHAEL (ID 8) 
    65: {
        'type': NodeType.DIALOGUE,
        'content': '''Entran al auditorio. Está oscuro. De las sombras emerge Krombopulos Michael.

"Oh, hola Rick. Aquí voy a matar de nuevo."''',
        'options': ['"¿Michael?"', '"¿Tú otra vez?"'],
        'children': [66,66],
        'character': 8
    },
    66: {
        'type': NodeType.DIALOGUE,
        'content': '''"Tengo un contrato para evitar que salgas de la universidad. Nada personal, solo negocios. Ah, y tengo este chip rojo que parece que quieres."''',
        'options': ['"Dámelo"', '"Peleemos"'],
        'children': [67,67],
        'character': 8
    },
    67: {
        'type': NodeType.FIGHT,
        'content': '''"Me encanta matar, Rick. ¡Me encanta!"''',
        'options': ['Defenderse'],
        'children':[68],
        'character': 8,
        'set': 6
    },
    68: {
        'type': NodeType.BLANK,
        'content': '''Krombopulos es rápido, pero tú eres más tramposo. Usas un portal para que se dispare a sí mismo.

"Profesionalismo mis bolas," dice Rick escupiendo al suelo.''',
        'children': [69]
    },
    
    # RECOMPENSA 5: CHIP DE ESTABILIDAD (Mapping to )
    69: {
        'type': NodeType.SPECIAL,
        'content': '''Recuperas el 'Chip de Estabilidad Portal'.

"¡Sí! ¡Con esto los portales dejarán de enviarnos a dimensiones donde todos son sillas!"

"Solo nos falta una pieza, Morty. La más difícil. Está en la Rectoría... Y parece que el Presidente Morty la tiene."''',
        'options': ['Vamos por todo','Tengo miedo'],
        'children': [70,35],
        'stack': RickStacks.CHIP_ESTABILIDAD
    },

    70: {
        'type': NodeType.BLANK,
        'content': '''Entran a la Rectoría. Es un edificio lujoso, muy diferente al resto de la universidad.

Al final del pasillo, ven al Presidente Morty y a sus guardias.''',
        'children': [71]
    },
    
    # ENCUENTRO FINAL: PRESIDENTE MORTY (ID 1)
    71: {
        'type': NodeType.DIALOGUE,
        'content': '''"Bienvenidos a mi despacho, caballeros. Veo que han causado destrozos en mi campus." El Presidente Morty acaricia una caja azul.''',
        'options': ['"Devuélvenos la caja"', '"Cállate"'],
        'children': [72,72],
        'character': 1
    },
    72: {
        'type': NodeType.DIALOGUE,
        'content': '''"¿Buscan la 'Caja de Meeseeks'? Es fascinante. Le pedí que arreglara el presupuesto de la nación y casi explota."''',
        'options': ['"Es peligrosa"', '"Dámela"'],
        'children': [73,73],
        'character': 1
    },
    73: {
        'type': NodeType.BLANK,
        'content': '''Aparecen Guardias de la Ciudadela (ID 4) rodeándolos.

"Rick, creo que estamos en problemas," dice Morty.''',
        'children': [74]
    },
    74: {
        'type': NodeType.DIALOGUE,
        'content': '''"Entréguenme las otras piezas y quizás los deje vivir como conserjes," ofrece el Presidente.''',
        'options': ['"¡Jamás!"', '"Chúpate esa"'],
        'children': [75,75],
        'character': 4 # Guardias
    },
    75: {
        'type': NodeType.DIALOGUE,
        'content': '''"Entonces, mueran."''',
        'options': ['¡A pelear!'],
        'children': [85],
        'character': 1
    },
    
# CONTINUACIÓN DEL DIÁLOGO EN RECTORÍA (Pre-Pelea)
    
    # Respuesta a "¡Jamás!"
    76: {
        'type': NodeType.BLANK,
        'content': '''"¡Jamás! Mi intelecto no se subordina a una administración que se demora tres semestres en aprobar una materia," escupe Rick con desprecio. "Prefiero lamer el suelo de la dimensión de las nalgas."''',
        'children': [79]
    },
    
    # Respuesta a "Chúpate esa"
    77: {
        'type': NodeType.BLANK,
        'content': '''Haces un gesto obsceno con ambas manos. "Chúpate esa, presi. Y arréglame el horario mientras estás ahí abajo." 
        
        Rick suelta una carcajada. "Ese es mi Morty. Aprendes rápido."''',
        'children': [79]
    },

    # El Presidente Morty reacciona
    79: {
        'type': NodeType.DIALOGUE,
        'content': '''El Presidente Morty suspira y ajusta su corbata. "Qué decepción, Rick C-137. Esperaba que entendieras la importancia del orden. Con la Caja de Meeseeks, he logrado reducir el tiempo de trámites de 5 años a 4 años y medio."''',
        'options': ['"¿Solo eso?"', '"¡Esclavista!"'],
        'children': [80,81],
        'character': 1
    },

    # Opción: Burlarse de la eficiencia
    80: {
        'type': NodeType.BLANK,
        'content': '''"¿Usas una caja capaz de alterar la realidad para mejorar la burocracia un 10%? Eres patético," dice Rick. "Yo uso esa caja para que me abran los frascos de pepinillos."''',
        'children': [82]
    },

    # Opción: Acusarlo de esclavista
    81: {
        'type': NodeType.BLANK,
        'content': '''"¡Estás esclavizando a los Meeseeks para hacer papeleo administrativo, monstruo!" grita Morty.

        "La existencia es dolor para un Meeseeks, Morty. Y llenar formularios de la universidad es el dolor máximo. Es poético," responde el Presidente.''',
        'children': [82]
    },

    # Escalada del conflicto
    82: {
        'type': NodeType.DIALOGUE,
        'content': '''"Suficiente charla," dice el Presidente, mientras los ojos de sus guardias brillan en rojo. "Si no van a ser parte de mi comité académico, serán parte de los cimientos del nuevo edificio de posgrados."''',
        'options': ['"Inténtalo"', '"Espera, ¿qué?"'],
        'children': [83,83],
        'character': 1
    },

    # Última provocación
    83: {
        'type': NodeType.BLANK,
        'content': '''Rick carga su arma recién ensamblada (parcialmente). "Lo único que vas a inaugurar hoy es tu propio funeral. Morty, ponte detrás de algo que no sea inflamable. O sea, no detrás de ti mismo."''',
        'children': [84]
    },

    # Transición a la pelea (Node 85)
    84: {
        'type': NodeType.BLANK,
        'content': '''La tensión en la oficina del rector es palpable. El Presidente Morty presiona un botón en su escritorio y las persianas se cierran de golpe.

        "Hora de la cancelación de matrícula definitiva."''',
        'children': [85] 
    },
    # PELEA FINAL: PRESIDENTE MORTY (ID 1)


    85: {
        'type': NodeType.FIGHT,
        'content': '''El Presidente Morty saca un rifle de plasma. "¡Este campus es mío!"''',
        'options': ['Disparar a matar'],
        'children':[86],
        'character': 1,
        'set': 7
    },
    
    # RECOMPENSA 6: CAJA DE MEESEEKS (Mapping to CAJA_DE_MEESEEKS)
    86: {
        'type': NodeType.SPECIAL,
        'content': '''Derrotas al Presidente Morty. Su cuerpo robótico chispea. Tomas la 'Caja de Meeseeks'.

"¡Lo tenemos todo, Morty! ¡La Caja de Meeseeks era la fuente de poder del procesador mental!"

Rick ensambla rápidamente la Pistola de Portales con las 6 piezas: Cristal, Cargador, Batería, Portal, Chip y Caja.''',
        'options': ['Abrir portal a casa','Invocar un Meeseeks'],
        'children': [87,88],
        'stack': RickStacks.CAJA_DE_MEESEEKS
    },
    87: {
        'type': NodeType.BLANK,
        'content': '''Rick abre un portal verde brillante.

"¡Adiós, universidad pública! ¡Adiós, paros! ¡Adiós, almuerzos de 2000 pesos!"

Saltan a través del portal, dejando atrás el caos.''',
        'children': [90]
    },
    88: {
        'type': NodeType.BLANK,
        'content': '''Rick presiona el botón de la caja. "¡Soy Mr. Meeseeks! ¡Mírenme!"

"Mr. Meeseeks, destruya toda evidencia de que estuvimos aquí."
"¡Caaaan do!"

Mientras el caos se desata, ustedes saltan al portal.''',
        'children': [90]
    },
    89: { # Unused
        'type': NodeType.BLANK,
        'content': '''...''',
        'children': [90]
    },
    90: {
        'type': NodeType.BLANK,
        'content': '''Aparecen en el garaje de la casa Smith.

"Hogar, dulce hogar, Morty. Pásame una cerveza. Esa aventura fue demasiado... educativa."

FIN.''',
        'children': [101]
    },
        # ESCENA POST-CRÉDITOS: Jerry (Ending)
    91: { 
        'type': NodeType.BLANK,
        'content': '''De repente, la puerta del garaje se abre. Jerry entra con una bata de dormir.

        "Oigan, ¿ustedes saben por qué hay un Meeseeks en la cocina intentando ayudarme a bajar mi handicap de golf a las 3 de la mañana?"

        Rick saca su arma y dispara al techo. Jerry sale corriendo y gritando.
        Rick y Morty se miran y se ríen.

        FIN DE LA PARTIDA.''',
        'children': [101]
    },
    101: {
        'type': NodeType.UNDEFINED,
        'content': "",
        'options': [],
        'children': []
    },
}
