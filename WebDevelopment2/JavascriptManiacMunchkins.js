//https://codecombat.com/play/level/javascript-maniac-munchkins?&codeLanguage=javascript
// Attack the chest to break it open.
// Defend yourself when a munchkin gets too close.

while(true) {
    var enemy = hero.findNearestEnemy();
    var distance = hero.distanceTo(enemy);
    if(hero.isReady("cleave")) {
        // First priority is to cleave if it's ready:
        hero.cleave(enemy);
    } else if(distance < 5) {
        // Attack the nearest munchkin that gets too close:
        hero.attack(enemy);
    } else {
        // Otherwise, try to break open the chest:
        hero.attack("Chest");
    }
}