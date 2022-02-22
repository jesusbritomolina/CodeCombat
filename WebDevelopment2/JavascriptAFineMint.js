//https://codecombat.com/play/level/javascript-a-fine-mint?&codeLanguage=javascript
// ¡Los peones están tratando de robar tus monedas!
// Escribe una función para aplastarlos antes de que puedan llevarse tus monedas.

function pickUpCoin() {
    var coin = hero.findNearestItem();
    if(coin) {
        hero.moveXY(coin.pos.x, coin.pos.y);
    }
}

// Escriba la función attackEnemy a continuación
// ¡Encuentra el enemigo más cercano y atácalo si existe!
function attackEnemy(){
    var enemy = hero.findNearestEnemy();
    if(enemy){
        hero.say(enemy);
        hero.attack(enemy);
    }
}

while(true) {
    attackEnemy(); // ∆ Descomente esta línea después de que escriba la función attackEnemy.
    pickUpCoin();
}