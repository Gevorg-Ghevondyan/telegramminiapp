document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('game-container');
    const scoreElement = document.getElementById('score');
    const rows = 8;
    const cols = 8;
    const icons = ['gun', 'knife', 'rifle', 'swords', 'weapon'];
    const board = [];
    let selectedTile = null;
    let score = 0;

    function initBoard() {
        container.innerHTML = '';
        for (let i = 0; i < rows; i++) {
            board[i] = [];
            for (let j = 0; j < cols; j++) {
                const tile = document.createElement('div');
                tile.className = 'tile';
                tile.dataset.row = i;
                tile.dataset.col = j;
                tile.style.backgroundImage = `url('images/${getRandomIcon()}.png')`;
                tile.addEventListener('click', handleTileClick);
                container.appendChild(tile);
                board[i][j] = tile;
            }
        }
    }

    function getRandomIcon() {
        return icons[Math.floor(Math.random() * icons.length)];
    }

    function handleTileClick(event) {
        const tile = event.target;
        if (selectedTile) {
            if (areAdjacent(selectedTile, tile)) {
                swapTiles(selectedTile, tile);
                setTimeout(() => {
                    if (!checkMatches()) {
                        swapTiles(selectedTile, tile);
                    } else {
                        applyGravity();
                    }
                }, 500);
            } else {
                selectedTile.classList.remove('selected');
                selectedTile = tile;
                selectedTile.classList.add('selected');
            }
        } else {
            selectedTile = tile;
            selectedTile.classList.add('selected');
        }
    }

    function areAdjacent(tile1, tile2) {
        const row1 = parseInt(tile1.dataset.row);
        const col1 = parseInt(tile1.dataset.col);
        const row2 = parseInt(tile2.dataset.row);
        const col2 = parseInt(tile2.dataset.col);

        return (Math.abs(row1 - row2) === 1 && col1 === col2) ||
               (Math.abs(col1 - col2) === 1 && row1 === row2);
    }

    function swapTiles(tile1, tile2) {
        const img1 = tile1.style.backgroundImage;
        const img2 = tile2.style.backgroundImage;

        tile1.style.backgroundImage = img2;
        tile2.style.backgroundImage = img1;

        tile1.classList.remove('selected');
        tile2.classList.remove('selected');
    }

    function checkMatches() {
        let foundMatch = false;
        const tilesToRemove = [];
        
        function collectMatches(startRow, startCol, directionRow, directionCol) {
            let match = [];
            let i = startRow;
            let j = startCol;
            while (i >= 0 && i < rows && j >= 0 && j < cols) {
                const tile = board[i][j];
                const icon = tile.style.backgroundImage.split('/').pop().split('.')[0];
                if (match.length === 0 || icon === match[0].style.backgroundImage.split('/').pop().split('.')[0]) {
                    match.push(tile);
                } else {
                    break;
                }
                i += directionRow;
                j += directionCol;
            }
            if (match.length >= 3) {
                tilesToRemove.push(...match);
                foundMatch = true;
            }
        }

        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                collectMatches(i, j, 0, 1); // Horizontal
                collectMatches(i, j, 1, 0); // Vertical
            }
        }

        if (foundMatch) {
            tilesToRemove.forEach(tile => {
                tile.style.backgroundImage = `url('images/${getRandomIcon()}.png')`;
            });
            updateScore(tilesToRemove.length);
            setTimeout(() => {
                applyGravity();
                setTimeout(checkMatches, 500);
            }, 500);
        }

        return foundMatch;
    }

    function applyGravity() {
        for (let col = 0; col < cols; col++) {
            let emptySpaces = 0;
            for (let row = rows - 1; row >= 0; row--) {
                const tile = board[row][col];
                if (tile.style.backgroundImage === `url('images/${getRandomIcon()}.png')`) {
                    emptySpaces++;
                } else if (emptySpaces > 0) {
                    tile.style.transition = 'top 0.5s ease-out';
                    tile.style.top = `${(emptySpaces * 60) - 60}px`;
                    board[row + emptySpaces][col] = tile;
                    board[row][col] = null;
                }
            }
            for (let i = 0; i < emptySpaces; i++) {
                const newTile = board[i][col];
                newTile.style.top = `${i * 60}px`;
                newTile.style.backgroundImage = `url('images/${getRandomIcon()}.png')`;
                board[i][col] = newTile;
            }
        }
    }

    function updateScore(points) {
        score += points;
        scoreElement.textContent = score;
    }

    initBoard();
});
