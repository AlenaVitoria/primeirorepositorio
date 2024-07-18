//Inserir valor de xp atual do personagem
const XP = 500; 

let nivel; //variavel.

if (XP < 1000) {
    nivel = "Bronze";
} else if (XP >= 1001 && XP <= 2000) {
    nivel = "Prata";
} else if (XP >= 2001 && XP <= 5000) {
    nivel = "Ouro";
} else if (XP >= 5001 && XP <= 7000) {
    nivel = "Platina";
} else if (XP >= 7001 && XP <= 8000) {
    nivel = "Diamante";
} else if (XP >= 8001 && XP <= 9000) {
    nivel = "Radiante";
} else if (XP >= 9001 && XP <= 10000) {
    nivel = "Imortal";
} else {
    nivel = "God";
}

// Digite o nome do Heroi.
const nomeHeroi = "MonkSlay"; 

console.log(O Herói de nome ${nomeHeroi} está no nível de ${nivel}.);