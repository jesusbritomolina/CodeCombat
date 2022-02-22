//https://codecombat.com/play/level/javascript-patrol-buster?&codeLanguage=javascript
// Remember that enemies may not yet exist.
while (true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        // Но когда он появится, атакуйте!
        hero.attack(enemy);
    }
}