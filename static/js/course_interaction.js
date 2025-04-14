document.addEventListener('DOMContentLoaded', () => {
    // Make lesson cards interactive
    const lessonCards = document.querySelectorAll('.lesson-card');
    
    lessonCards.forEach(card => {
        card.addEventListener('click', function() {
            this.classList.toggle('expanded');
            
            // Toggle emoji animation
            const emoji = this.querySelector('.lesson-emoji');
            emoji.style.animation = this.classList.contains('expanded') ? 
                'spin 1s ease-in-out' : 'float 3s ease-in-out infinite';
        });
    });

    // Start learning button
    document.querySelector('.start-learning').addEventListener('click', function() {
        this.textContent = "3... 2... 1... Launch! 🚀";
        setTimeout(() => {
            alert("Course started! Let's begin our AI adventure!");
            // In a real app, this would load the first lesson
        }, 1500);
    });

    // Add floating effect to question bubbles
    const bubbles = document.querySelectorAll('.bubble');
    bubbles.forEach((bubble, index) => {
        bubble.style.animation = `float ${3 + index*0.2}s ease-in-out infinite`;
    });
});

// Add to your CSS:
// @keyframes spin { 
//     from { transform: rotate(0deg); }
//     to { transform: rotate(360deg); }
// }
document.addEventListener('DOMContentLoaded', function() {
    // Make all course cards clickable
    document.querySelectorAll('.course-card').forEach(card => {
        card.addEventListener('click', function(e) {
            // Don't redirect if clicking on buttons/links inside
            if (!e.target.closest('a, button')) {
                window.location.href = this.querySelector('a').href;
            }
        });
    });

    // Add cosmic hover effects
    document.querySelectorAll('.cosmic-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
            this.style.boxShadow = '0 15px 30px rgba(114, 9, 183, 0.4)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 5px 15px rgba(114, 9, 183, 0.2)';
        });
    });
});