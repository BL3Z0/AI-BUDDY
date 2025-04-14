document.addEventListener('DOMContentLoaded', () => {
    // Start button functionality
    document.getElementById("start-btn")?.addEventListener("click", () => {
        alert("Starting your AI journey!");
        fetchQuiz();
    });

    // Fetch quiz from Flask API
    function fetchQuiz() {
        fetch("/api/quiz")
            .then(response => response.json())
            .then(data => {
                if(data.length > 0) {
                    showQuestion(data[0]);
                }
            })
            .catch(error => {
                console.error("Error fetching quiz:", error);
                alert("Failed to load quiz. Please try again.");
            });
    }

    function showQuestion(question) {
        const container = document.getElementById("quiz-container");
        const questionEl = document.getElementById("quiz-question");
        const optionsEl = document.getElementById("quiz-options");
        
        container.style.display = "block";
        questionEl.textContent = question.question;
        optionsEl.innerHTML = "";
        
        question.options.forEach((option, index) => {
            const button = document.createElement("button");
            button.textContent = option;
            button.onclick = () => checkAnswer(index, question.answer);
            optionsEl.appendChild(button);
        });
    }

    function checkAnswer(selectedIndex, correctIndex) {
        if(selectedIndex === correctIndex) {
            alert("Correct!");
        } else {
            alert("Incorrect! Try again.");
        }
    }
});
document.addEventListener('DOMContentLoaded', function() {
    // Make all enroll buttons clickable
    document.querySelectorAll('.enroll-btn').forEach(button => {
        button.addEventListener('click', function() {
            const courseId = this.getAttribute('data-course-id');
            enrollCourse(courseId);
        });
    });
    
    function enrollCourse(courseId) {
        console.log(`Enrolling in course ${courseId}`);
        // Add your actual enrollment logic here
        // Example: window.location.href = `/enroll/${courseId}`;
    }
});