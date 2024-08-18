let score = 0;
let activeTile = null;
let gameInterval = null;

function startGame() {
    score = 0;
    updateScore();
    gameInterval = setInterval(highlightRandomTile, 1000);
}

function highlightRandomTile() {
    if (activeTile) {
        activeTile.classList.remove('highlighted');
    }
    const tiles = document.querySelectorAll('.tile');
    const randomIndex = Math.floor(Math.random() * tiles.length);
    activeTile = tiles[randomIndex];
    activeTile.classList.add('highlighted');
}

function clickTile(event) {
    if (event.target === activeTile) {
        score++;
        updateScore();
    }
}

function updateScore() {
    document.getElementById('score').textContent = `Score: ${score}`;
}

document.getElementById('start-button').addEventListener('click', startGame);

const gameBoard = document.getElementById('game-board');
for (let i = 0; i < 9; i++) {
    const tile = document.createElement('div');
    tile.className = 'tile';
    tile.addEventListener('click', clickTile);
    gameBoard.appendChild(tile);
}
