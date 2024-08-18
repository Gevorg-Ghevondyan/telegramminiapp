const emojis = ["🍎", "🍌", "🍓", "🍉", "🍇", "🍑", "🍍", "🥝"];
let board = [];
let flippedCards = [];
let matchedPairs = 0;

// Initialize the game
function startGame() {
    board = [...emojis, ...emojis];
    board = board.sort(() => Math.random() - 0.5); // Shuffle
    const gameBoard = document.getElementById('game-board');
    gameBoard.innerHTML = '';
    
    board.forEach((emoji, index) => {
        const card = document.createElement('div');
        card.className = 'card';
        card.dataset.index = index;
        card.addEventListener('click', flipCard);
        gameBoard.appendChild(card);
    });
}

// Handle card flip
function flipCard(event) {
    const card = event.target;
    const index = card.dataset.index;
    if (flippedCards.length === 2 || card.classList.contains('flipped')) return;

    card.textContent = board[index];
    card.classList.add('flipped');
    flippedCards.push({ card, index });

    if (flippedCards.length === 2) {
        setTimeout(checkForMatch, 500);
    }
}

// Check for matching cards
function checkForMatch() {
    const [firstCard, secondCard] = flippedCards;
    if (board[firstCard.index] === board[secondCard.index]) {
        matchedPairs++;
        if (matchedPairs === emojis.length) {
            setTimeout(() => alert('You won!'), 100);
        }
    } else {
        firstCard.card.textContent = '';
        secondCard.card.textContent = '';
        firstCard.card.classList.remove('flipped');
        secondCard.card.classList.remove('flipped');
    }
    flippedCards = [];
}

// Restart the game
document.getElementById('restart-button').addEventListener('click', startGame);

// Start the game on page load
startGame();
