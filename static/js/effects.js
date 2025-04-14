document.addEventListener('DOMContentLoaded', () => {
    // Create twinkling stars
    const starCount = 100;
    const container = document.body;
    
    for (let i = 0; i < starCount; i++) {
      const star = document.createElement('div');
      star.className = 'star';
      
      // Random position
      const x = Math.random() * 100;
      const y = Math.random() * 100;
      
      // Random size (1-3px)
      const size = Math.random() * 2 + 1;
      
      // Random animation delay
      const delay = Math.random() * 5;
      
      star.style.left = `${x}%`;
      star.style.top = `${y}%`;
      star.style.width = `${size}px`;
      star.style.height = `${size}px`;
      star.style.animationDelay = `${delay}s`;
      
      container.appendChild(star);
    }
  });