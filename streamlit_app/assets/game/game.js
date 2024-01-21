// Your enhanced JavaScript game logic goes here
const gameContainer = document.getElementById('game-container');

// Create a canvas element and append it to the game container
const canvas = document.createElement('canvas');
canvas.width = gameContainer.clientWidth;
canvas.height = gameContainer.clientHeight;
gameContainer.appendChild(canvas);

const image = new Image();
image.src = './assets/images/Eco_bot-1.png';

// Wait for the image to load
image.onload = function() {
  // Image is now loaded and can be used in the game
};
// Get the 2D rendering context
const ctx = canvas.getContext('2d');

// Define the game loop function
function gameLoop() {
  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Render the game objects and update their positions
  ctx.drawImage(image, x, y, width, height);

  // Call the game loop function recursively
  requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();