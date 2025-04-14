document.addEventListener('DOMContentLoaded', function() {
    // Handle course card clicks
    document.querySelectorAll('.course-card').forEach(card => {
        card.addEventListener('click', function(e) {
            // Only proceed if not clicking the enroll button
            if (!e.target.classList.contains('enroll-btn')) {
                const link = this.querySelector('a.enroll-btn');
                if (link) {
                    window.location.href = link.href;
                }
            }
        });
    });

    // Add visual feedback for taps
    document.querySelectorAll('.enroll-btn').forEach(btn => {
        btn.addEventListener('touchstart', function() {
            this.style.transform = 'scale(0.95)';
        });
        btn.addEventListener('touchend', function() {
            this.style.transform = 'scale(1)';
        });
    });
});