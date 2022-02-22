//https://codecombat.com/play/level/javascript-stillness-in-motion?&codeLanguage=javascript
// You can put one if-statement within another if-statement.
// Be careful how the if statements interact with each other.
// Make sure the indentation is correct!
// It's helpful to start with one outer if/else,
// using comments as placeholders for the inner if/else:

while(true) {
    var enemy = hero.findNearestEnemy();
    // If there is an enemy, then...
    if(enemy) {
        // Create a distance variable with distanceTo.
        var distance = hero.distanceTo(enemy);
        // If the distance is less than 5 meters, then attack.
        if(distance&&distance < 5){
            hero.attack(enemy);
        }
        // Else (the enemy is far away), then shield.
        else{
            hero.shield();
        }
    // Else (there is no enemy)...
    } else {
        // ... then move back to the X.
        hero.moveXY(40, 34);
    }
}