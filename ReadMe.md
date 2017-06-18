Projet : Modélisation du flux sanguin

I. Description des fichiers

La liste des fichiers présents dans le dépôt a été dans l'ensemble conçue et exploitée par l'équipe pilotant le projet.
Dans cette liste sont disponibles les fichiers suivants :
  - Projet.py : ce fichier est un script python permettant de lancer la simulation du mouvement du flux sanguin.
  - dataToTxt.py : il s'agit d'un script qui n'est utilisé qu'un faible nombre de fois. Il permet de transformer les données de modèle étudié en données textuelles importables dans l'API Tulip. C'est ce script qui permet de créer le graphe de modélisation du système circulatoire.
  - plusieurs versions PDF du rapport de projet : ceux-ci attestent du développement et du pilotage du projet. Une version condensée est écrite ci-dessous mais ne contient pas d'images. Il est recommandé de lire la dernière version pour comprendre tous nos choix et méthodes.



II. Rapport condensé

    Fonctionnement du système circulatoire

Il existe quatre types de vaisseaux sanguins dans le corps humain : les artères, les artérioles, les capillaires et les veines. Les premières apportent le sang depuis le cœur au reste du corps afin que les artérioles puissent approvisionner les muscles, tissus et organes en nutriments. Les capillaires font la jonction avec les veines qui ramènent le sang de ces parties au cœur.
De par la nature et les fonctions uniques de ces vaisseaux, le principe de la circulation du sang est différent pour chacune d’elles. 
Le flux sanguin est assuré dans les artères par l’activité cardiaque. Ce dernier s’effectue en quatre phases au cours desquelles les ventricules du cœur changent de volume et permettent une éjection effective du sang qu’ils contiennent. Dans les artères de la circulation systémique, c’est la pression sanguine qui permet de faire circuler le sang vers les autres parties du corps. Elle reste constante pendant toute l’activité cardiaque. Pour le cas des veines, la pression est faible et à peine suffisante pour que les contractions musculaires et les valvules présentes dans ces vaisseaux rapportent le sang vers le cœur.
Approximation : Pour le modèle que l’on crée, on considère que les mouvements de fluides dans les artères et dans les veines s’effectuent avec les mêmes propriétés (débit, vitesse, …)


    Circulation pulmonaire et circulation systémique

En plus des différences au niveau du flux sanguin dans les divers vaisseaux existants, il faut aussi distinguer la circulation pulmonaire de la circulation systémique. En effet, la composante principale à apporter aux autres parties du corps humain est le dioxygène. La première circulation est un cycle court entre le cœur et les poumons afin de réapprovisionner le sang. L’autre circulation envoie celui-ci au reste du corps.
De ce fait, les caractéristiques des vaisseaux sanguins dans ces deux systèmes sont aussi différentes.
La circulation pulmonaire représente un réseau aux caractéristiques uniques. Ici, les pressions artérielles ne dépassent jamais 25 mm/Hg et les vaisseaux sanguins suivent le réseau bronchique des poumons. L’hémodynamique garde cependant les mêmes formules que celles présentes dans la circulation systémique.
Approximation : On considère ainsi que le fluide sanguin s’écoule de la même manière que dans la circulation systémique. Une amélioration serait de prendre en compte les changements de pression et de résistance au sein de ce circuit pour réguler correctement la vitesse et le débit.

Le tableau suivant donne les caractéristiques moyennes de la circulation systémique recueillies sur diverses sources d’information avec un débit cardiaque moyen de 5L/min (repos systémique) et une viscosité de 0.006PA.s. (Calculs à revérifier en détail)
Approximation : Au vu du modèle que nous avons récupéré et des données du tableau ci-dessous, on concentre notre modélisation sur la simulation du flux dans les artères et les veines. Les artérioles, veinules et capillaires seront omis, et l’échange entre le système d’apport du sang et celui du retour se fait simplement dans des sommets représentant le circuit de transfert. Une amélioration serait de prendre en compte l’existence et les propriétés des autres types de vaisseau sanguin.
Approximation : Par manque de données statistiques et pour simplifier la modélisation, nos travaux prendront en compte les données moyennes récupérées pour un individu de taille, d’âge et de poids moyens. En effet, ces paramètres peuvent influencer les caractéristiques des vaisseaux sanguins.


Vaisseaux	Diamètre (mm)	Longueur (cm)	Pression (mm/Hg)	Résistance 	Vitesse (cm/s)
					
Aorte, grosses artères	~ 10	~ 40	~ 100	Faible	~ 40
Petites artères	~ 3	~ 20	~ 70	Faible	10 – 40
Artérioles	~ 0.02	~ 0.2	~ 35	Élevée	0.1 – 10
Capillaires	~ 0.008	~ 0.1	~ 21	Élevée	< 0.1
Veinules	~ 0.03	~ 0.2	~ 11	Élevée	< 0.3
Veines	~ 2 – 6	~ 5 – 20	~ 7 	Faible	0.3 – 5
Veine Cave	~ 12.5	~ 40	~ 3	Faible	5 - 20




Paramètres influençant le flux dans les vaisseaux sanguins


    Diamètre et épaisseur du vaisseau sanguin et viscosité du sang

Comme pour tout fluide parcourant un tube, le sang circulera plus ou moins rapidement en fonction de l’espace dans lequel il évolue. Plus la surface de section disponible est élevée, plus la vitesse maximale possible augmente, la résistance à l’écoulement étant moins important. De même, une paroi plus épaisse induit une résistance plus forte et donc un écoulement plus lent.
La viscosité du sang influe sur la résistance vasculaire dans la circulation systémique et donc directement sur le débit sanguin. Plusieurs modèles peuvent le caractériser dont le principe d’écoulement de Poiseuille.

L’écoulement laminaire est défini par une résistance faible. La vitesse de chaque particule de sang est homogène et basse. À l’inverse, lorsque la résistance est élevée, on passe en écoulement turbulent et la vitesse de chaque particule devient hétérogène et forte.
La viscosité est une propriété variable chez l’humain et peut dépendre de plusieurs paramètres : hématocrite (rapport du volume des globules rouges sur le volume sanguin total), structure des globules rouges, …
Ces deux régimes d’écoulement peuvent aussi être interprétés d’une autre manière via le nombre de Womersley.

Ce dernier permet de dresser des profils de vitesse et indique si les forces d’inertie prépondèrent sur les forces de frottements liés à la viscosité du fluide. C’est le cas notamment des artères et des veines de diamètre assez grand mais l’inverse pour les artérioles, capillaires et veinules qui sont eux très fins.
De plus, l’existence de forces de frottements implique qu’au sein même d’un vaisseau sanguin, la vitesse du flux n’est jamais homogène. Les profils sont paraboliques, montrant que le fluide s’écoule plus rapidement au centre des tubes et presque nullement sur les parois.
Approximation : Le but de la modélisation est d’observer les mouvements d’un fluide injecté dans le sang à partir d’un endroit du corps humain quelconque. Pour simplifier le modèle, nous négligeons l’influence de la viscosité et de la résistance des vaisseaux sanguins. Le débit et la vitesse du sang sont donc considérés maximaux et homogènes. Seule la nature du vaisseau sanguin influencera ces paramètres.


    Pression artérielle

La pression artérielle dépend directement de la nature des vaisseaux sanguins, de la phase de l’activité cardiaque (systole, diastole, …), de l’âge de l’individu, etc.
Les veines subissent une pression très faible, le sang y circulant les parcourt grâce à un autre procédé physiologique utilisant la contraction musculaire pour pousser le fluide et des valvules pour les empêcher le reflux. C’est le retour veineux.
Approximation : Étant donné que le retour veineux s’appuie sur un principe complexe mettant en avant d’autres parties de l’anatomie humaine, il devient compliqué de modéliser efficacement et simplement ce phénomène. Dans notre modèle, nous l’apparentons à l’écoulement laminaire dans le réseau artériel.




Récapitulatif des difficultés pour la simulation et solution d’approximation proposées


Retour veineux : Pour notre simulation, on considère que le retour veineux s’apparente en termes de mouvements de flux à celui de l’écoulement laminaire.
Circulation pulmonaire : L’approche de la circulation systémique est utilisée.
Existence de plusieurs types d’écoulement et donc de modèles : Écoulement laminaire dans les vaisseaux sanguins, abstraction de l’écoulement turbulent (on ne modélise pas les artérioles, veinules et capillaires)
Profils de vitesse parabolique  Approximer en considérant une vitesse homogène et maximale.
Disparité des données : On considère un être humain de taille et de poids moyens au repos pour utiliser les données moyennes.
Suivi de l’injection : Le code prend en entrée le sommet sur lequel on injecte la séquence et le nombre d’itérations à simuler pour observer la propagation.
Jonction entre artères et veines : Certains sommets auront pour but de transformer une artère en une veine. Ce principe sera fortement visuel. 
Simulation du flux sanguin


    Modélisation du système circulatoire

En se basant sur un modèle de réseau sanguin en 3D, nous extrayons des données visuelles et les adaptons pour créer un graphe orienté et cyclique représentant une simplification de la totalité du système circulatoire humain. Les vaisseaux sanguins seront modélisés par des ensembles de sommets et arêtes. La disposition de ceux-ci dans le logiciel Tulip sera représentative au mieux du réseau dans l’anatomie humaine.
Nous faisons en sorte de classer chacun de ces ensembles par natures de vaisseau sanguin : grosse artère, petite artère, petite veine, grosse veine. Les réseaux de transfert artérioles – capillaires – veinules seront représentés par un simple sommet dédié.
Afin d’améliorer la visualisation du modèle et de pouvoir le comparer virtuellement à un corps humain, nous pouvons rajouter quelques sommets et adapter les distances entre chacun de ces sommets ainsi que leurs connexions. Cela permet d’affiner la représentation visuelle de l’anatomie humaine.
Par souci d’encombrement et technique, les muscles et organes ne seront pas tous présentés. On ne garde que les parties importantes et permettant dans notre modèle de bien comprendre le processus de propagation du flux sanguin. De plus, dans la réalité, l’activité cardiaque implique que les organes, les muscles et les vaisseaux possèdent un volume variable en fonction de la pression appliquée par ce processus cyclique. Nous simplifions cette partie et ne considérons un mouvement homogène du flux sanguin dans un état d’écoulement laminaire stationnaire.

Étant donné que nous exécutons notre simulation avec une multitude d’approximations, le modèle est fortement améliorable. De nombreux changements peuvent être apportés afin de rendre une solution plus claire et plus précise du système circulatoire. Parmi eux, on peut citer les exemples suivants : prise en compte de tous les types de vaisseau sanguin, affinage des connexions entre les organes, les tissus, les muscles et les vaisseaux sanguins, approche dynamique, …


	  Propagation de l’injection dans le sang

Cette partie de la simulation comprend également son lot d’approximations. Le fluide s’écoule sans force de frottements induite par sa viscosité et la résistance des vaisseaux sanguins. Le mouvement est donc homogène et à vitesse maximale.
L’algorithme utilisé prend alors en entrée le sommet sur lequel nous injectons le fluide de propagation. Optionnellement, l’utilisateur peut spécifier le nombre d’itérations et le temps de repos entre chacune de celles-ci pour observer le phénomène. Visuellement, lorsque le flux atteint un sommet ou une arête représentant un vaisseau ou une autre partie du corps humain, ceux-ci se colorient.
Dans le cas présent, à chaque itération, l’algorithme coloriera les voisins directs des sommets qui viennent d’être atteints, ainsi que les arêtes faisant la liaison entre les deux. Une amélioration consisterait d’abord à prendre en compte la nature des vaisseaux afin de pouvoir considérer un facteur de distance et de vitesse et emprunter une approche plus dynamique du réseau. 




Liens utiles :

Modèles du système circulatoire avec noms des principales artères et veines.
http://www.lecorpshumain.fr/wp-content/uploads/2012/01/circulation_sang_1.jpg	
https://upload.wikimedia.org/wikipedia/commons/2/29/Circulatory_System_en.svg
http://biowiki.mbolduc1.profweb.ca/index.php/La_circulation_sanguine#Variation_du_d.C3.A9bit_sanguin_dans_les_lits_capillaires

Fonctionnement du système circulatoire et données/caractéristiques :
http://umvf.omsk-osma.ru/premannee/PEPIN_Jean_Louis/PEPIN_Jean_Louis_P02/PEPIN_Jean_Louis_P02.pdf
http://pro.bel.pagesperso-orange.fr/TPE/Productions/G9/ligne1.HTM
http://www.ifits.fr/IMG/pdf/Physiologie061010-3.pdf
http://coproweb.free.fr/pagphy/physioan/ch2s3.htm
http://medecineamiens.fr/Cours/L3/M1_PHEFI/UE_Regulation_Dysregulation/05_Circulation_pulmonaire.pdf

Méthodes de calculs de la vitesse et du débit sanguin.
http://www.biomecardio.com/pageshtm/download/lecture/GBM6107-chp8.pdf
http://biowiki.mbolduc1.profweb.ca/index.php/Le_coeur,_la_fr%C3%A9quence_cardiaque_et_le_d%C3%A9bit_cardiaque

Écoulement de Poiseuille (fluides visqueux).
https://fr.wikipedia.org/wiki/%C3%89coulement_de_Poiseuille
http://fms2.cerimes.fr/vod/media/canalu/documents/tele2sciences/.coulement.de.poiseuille.d.un.fluide.visqueux_18169/accessibilite.poiseuille.pdf

Quelques données de référence.
Viscosité des fluides : https://fr.wikipedia.org/wiki/Viscosit%C3%A9
Vitesses moyennes de flux sanguins dans le corps : https://fr.answers.yahoo.com/question/index?qid=20080328044259AAc5gLG


