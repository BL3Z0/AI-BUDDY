// static/js/space_shooter.js
class SpaceShooter {
    constructor(canvasId) {
      this.canvas = document.getElementById(canvasId);
      this.ctx = this.canvas.getContext('2d');
      this.width = 800;
      this.height = 600;
      this.canvas.width = this.width;
      this.canvas.height = this.height;
      
      // Game state
      this.player = {
        x: this.width/2 - 25,
        y: this.height - 70,
        width: 50,
        height: 50,
        speed: 5
      };
      
      this.bullets = [];
      this.meteors = [];
      this.score = 0;
      this.lives = 3;
      this.spawnRate = 60;
      this.meteorSpeed = 2;
      this.keys = {};
      this.gameOver = false;
      
      // Event listeners
      window.addEventListener('keydown', (e) => this.keys[e.key] = true);
      window.addEventListener('keyup', (e) => this.keys[e.key] = false);
      this.canvas.addEventListener('click', () => {
        if(this.gameOver) this.resetGame();
      });
      
      // Start game loop
      this.gameLoop();
    }
  
    gameLoop() {
      if(this.gameOver) return;
      
      this.update();
      this.draw();
      
      requestAnimationFrame(() => this.gameLoop());
    }
  
    update() {
      // Player movement
      if(this.keys['ArrowLeft'] || this.keys['a']) {
        this.player.x = Math.max(0, this.player.x - this.player.speed);
      }
      if(this.keys['ArrowRight'] || this.keys['d']) {
        this.player.x = Math.min(this.width - this.player.width, 
                                this.player.x + this.player.speed);
      }
      
      // Shoot with spacebar
      if(this.keys[' ']) {
        this.keys[' '] = false; // Prevent auto-repeat
        this.bullets.push({
          x: this.player.x + this.player.width/2 - 2.5,
          y: this.player.y,
          width: 5,
          height: 10,
          speed: 10
        });
      }
      
      // Spawn meteors
      if(Math.random() * this.spawnRate < 1) {
        this.meteors.push({
          x: Math.random() * (this.width - 40),
          y: -40,
          width: 40,
          height: 40,
          speed: this.meteorSpeed
        });
        this.spawnRate *= 0.995; // Gradually increase difficulty
      }
      
      // Update bullets
      for(let i = this.bullets.length-1; i >= 0; i--) {
        this.bullets[i].y -= this.bullets[i].speed;
        if(this.bullets[i].y < 0) {
          this.bullets.splice(i, 1);
        }
      }
      
      // Update meteors and check collisions
      for(let i = this.meteors.length-1; i >= 0; i--) {
        this.meteors[i].y += this.meteors[i].speed;
        
        // Bullet collision
        for(let j = this.bullets.length-1; j >= 0; j--) {
          if(this.checkCollision(this.bullets[j], this.meteors[i])) {
            this.meteors.splice(i, 1);
            this.bullets.splice(j, 1);
            this.score += 10;
            break;
          }
        }
        
        // Player collision
        if(this.checkCollision(this.player, this.meteors[i])) {
          this.meteors.splice(i, 1);
          this.lives--;
          if(this.lives <= 0) {
            this.gameOver = true;
          }
        }
        
        // Meteor out of screen
        if(this.meteors[i].y > this.height) {
          this.meteors.splice(i, 1);
        }
      }
    }
  
    draw() {
      // Clear canvas
      this.ctx.fillStyle = 'black';
      this.ctx.fillRect(0, 0, this.width, this.height);
      
      // Draw stars (background)
      for(let i = 0; i < 100; i++) {
        this.ctx.fillStyle = 'white';
        this.ctx.fillRect(
          Math.random() * this.width,
          Math.random() * this.height,
          1, 1
        );
      }
      
      // Draw player (spacecraft)
      this.ctx.fillStyle = '#4361ee';
      this.ctx.fillRect(
        this.player.x, 
        this.player.y, 
        this.player.width, 
        this.player.height
      );
      
      // Draw bullets
      this.ctx.fillStyle = 'white';
      this.bullets.forEach(bullet => {
        this.ctx.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
      });
      
      // Draw meteors
      this.ctx.fillStyle = '#f72585';
      this.meteors.forEach(meteor => {
        this.ctx.fillRect(meteor.x, meteor.y, meteor.width, meteor.height);
      });
      
      // Draw score and lives
      this.ctx.fillStyle = 'white';
      this.ctx.font = '24px Arial';
      this.ctx.fillText(`Score: ${this.score}`, 20, 30);
      this.ctx.fillText(`Lives: ${this.lives}`, 20, 60);
      
      // Game over screen
      if(this.gameOver) {
        this.ctx.fillStyle = 'rgba(0,0,0,0.7)';
        this.ctx.fillRect(0, 0, this.width, this.height);
        this.ctx.fillStyle = 'white';
        this.ctx.font = '48px Arial';
        this.ctx.textAlign = 'center';
        this.ctx.fillText('GAME OVER', this.width/2, this.height/2 - 40);
        this.ctx.font = '24px Arial';
        this.ctx.fillText(`Final Score: ${this.score}`, this.width/2, this.height/2);
        this.ctx.fillText('Click to play again', this.width/2, this.height/2 + 40);
        this.ctx.textAlign = 'left';
      }
    }
  
    checkCollision(obj1, obj2) {
      return obj1.x < obj2.x + obj2.width &&
             obj1.x + obj1.width > obj2.x &&
             obj1.y < obj2.y + obj2.height &&
             obj1.y + obj1.height > obj2.y;
    }
  
    resetGame() {
      this.player.x = this.width/2 - 25;
      this.player.y = this.height - 70;
      this.bullets = [];
      this.meteors = [];
      this.score = 0;
      this.lives = 3;
      this.spawnRate = 60;
      this.meteorSpeed = 2;
      this.gameOver = false;
      this.gameLoop();
    }
  }