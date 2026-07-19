from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def accueil():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    print("Visiteur IP :", ip)

    return """
    <h1>Aimar développeur</h1>
    <p>Bienvenue sur mon site</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    return r"""
<!DOCTYPE html>
<html lang="fr">

<head>

<meta charset="UTF-8">
<title>AIMAR SYSTEM</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
}

body{

background:black;
color:#00ff99;
font-family:Consolas,monospace;
height:100vh;
overflow:hidden;

}


/* effet écran */

.glitch{

position:absolute;
inset:0;

background:

repeating-linear-gradient(
0deg,
transparent 0px,
transparent 3px,
rgba(0,255,120,.15) 4px
);

animation:bug .2s infinite;

pointer-events:none;

}


@keyframes bug{

0%{
transform:translate(0);
}

50%{
transform:translate(-5px,3px);
}

100%{
transform:translate(0);
}

}



/* pages */

.page{

height:100vh;
width:100%;

display:flex;

justify-content:center;
align-items:center;

flex-direction:column;

text-align:center;

}


.cache{

display:none;

}



/* textes */


h1{

font-size:75px;

letter-spacing:12px;

text-shadow:

0 0 20px #00ff99,
0 0 70px #00ff99;

animation:lum 2s infinite;

}



@keyframes lum{

50%{

opacity:.5;

}

}



p{

font-size:25px;

margin:30px;

color:white;

}



/* boutons */


button{

padding:20px 60px;

font-size:25px;

background:black;

color:#00ff99;

border:3px solid #00ff99;

cursor:pointer;

box-shadow:

0 0 30px #00ff99;

}


button:hover{

background:#00ff99;

color:black;

transform:scale(1.1);

}



/* terminal */

#texte{

font-size:25px;

line-height:2;

}



/* personnage final */


.personnage{

display:none;

margin-top:40px;

}


.tete{

width:150px;

height:150px;

background:#111;

border-radius:50%;

border:5px solid #00ff99;

box-shadow:

0 0 50px #00ff99;

animation:rigole .8s infinite;

margin:auto;

}


@keyframes rigole{

0%{
transform:rotate(0deg);
}

25%{
transform:rotate(10deg);
}

50%{
transform:rotate(-10deg);
}

100%{
transform:rotate(0deg);
}

}



.oeil{

display:inline-block;

width:20px;

height:20px;

background:#00ff99;

border-radius:50%;

margin:50px 20px 0;

box-shadow:0 0 20px #00ff99;

}



.bouche{

width:60px;

height:30px;

border-bottom:6px solid #00ff99;

border-radius:0 0 60px 60px;

margin:20px auto;

}



.fin{

font-size:35px;

margin-top:30px;

animation:apparaitre 3s;

}



@keyframes apparaitre{

from{

opacity:0;

transform:translateY(50px);

}

to{

opacity:1;

transform:translateY(0);

}

}


</style>


<script>


function acceder(){


document.getElementById("accueil").style.display="none";


document.getElementById("question").style.display="flex";


}



function lancer(){


document.getElementById("question").style.display="none";


document.getElementById("systeme").style.display="flex";


animationSysteme();


}



function animationSysteme(){


let messages=[

"> Connexion au système...",

"> Chargement Python...",

"> Analyse du code en cours...",

"> Vérification des modules...",

"> Création de l'interface...",

"> Développeur trouvé : AIMAR",

"> Phase de test du codage activée",

"> Projet terminé avec succès..."

];


let i=0;


let zone=document.getElementById("texte");



let timer=setInterval(function(){


zone.innerHTML += messages[i]+"<br>";


i++;


if(i>=messages.length){


clearInterval(timer);



setTimeout(function(){


document.getElementById("fin").style.display="block";


},3000);



}


},1500);



}



</script>


</head>



<body>


<div class="glitch"></div>




<!-- ACCUEIL -->


<div id="accueil" class="page">


<h1>

AIMAR

</h1>


<p>

Système développeur expérimental

</p>


<button onclick="acceder()">

ACCÉDER

</button>


</div>





<!-- QUESTION -->


<div id="question" class="page cache">


<h1>

CONTINUER ?

</h1>


<p>

Voulez-vous lancer la phase de test du codage ?

</p>


<button onclick="lancer()">

OUI

</button>


</div>






<!-- SYSTEME -->


<div id="systeme" class="page cache">


<h1>

BOOT SYSTEM

</h1>


<div id="texte"></div>



<div id="fin" class="personnage">


<div class="tete">


<div class="oeil"></div>

<div class="oeil"></div>


<div class="bouche"></div>


</div>



<div class="fin">


😂 Hahaha...


<br><br>


Au revoir...


<br><br>


⚡ C'était Aimar ⚡


</div>


</div>



</div>



</body>

</html>
"""


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)