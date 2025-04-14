let currentQuestion = 0;
let score = 0;
let questions = [];

document.addEventListener('DOMContentLoaded', () => {
    startQuiz();
});

async function startQuiz() {
    try {
        const response = await fetch('/api/quiz');
        questions = await response.json();
        showQuestion();
    } catch (error) {
        console.error("Error loading quiz:", error);
        alert("Failed to load quiz. Please try again later.");
    }
}

function showQuestion() {
    if (currentQuestion >= questions.length) {
        showResults();
        return;
    }

    const question = questions[currentQuestion];
    const questionEl = document.getElementById('quiz-question');
    const optionsEl = document.getElementById('quiz-options');
    const progressEl = document.getElementById('quiz-progress');
    const categoryEl = document.getElementById('category-display');

    // Update progress
    progressEl.style.width = `${((currentQuestion + 1) / questions.length) * 100}%`;
    
    // Display category
    categoryEl.textContent = question.category.toUpperCase();
    categoryEl.className = `category-display category-${question.category}`;
    
    // Display question
    questionEl.textContent = question.question;
    
    // Clear previous options
    optionsEl.innerHTML = '';
    
    // Create new option buttons with better visibility
    question.options.forEach((option, index) => {
        const button = document.createElement('button');
        button.textContent = option;
        button.className = 'quiz-option';
        button.style.color = '#000000'; // Black text for better visibility
        button.style.fontWeight = 'bold'; // Bold text
        button.style.fontSize = '16px'; // Larger font size
        
        button.addEventListener('click', () => checkAnswer(index));
        optionsEl.appendChild(button);
    });
}

function checkAnswer(selectedIndex) {
    const question = questions[currentQuestion];
    const buttons = document.querySelectorAll('#quiz-options button');
    
    // Disable all buttons
    buttons.forEach(button => {
        button.disabled = true;
    });
    
    // Highlight correct answer (but don't show feedback text)
    buttons.forEach((button, index) => {
        if (index === question.answer) {
            button.classList.add('correct');
        }
    });
    
    // Update score if correct
    if (selectedIndex === question.answer) {
        score++;
    }
    
    // Move to next question after delay
    setTimeout(() => {
        currentQuestion++;
        showQuestion();
    }, 1000); // Reduced delay to 1 second
}

function showResults() {
    const quizContent = document.getElementById('quiz-content');
    const resultsEl = document.getElementById('quiz-results');
    
    quizContent.style.display = 'none';
    resultsEl.style.display = 'block';
    
    // Calculate score
    const percentage = Math.round((score / questions.length) * 100);
    document.getElementById('result-score').textContent = 
        `You scored ${score} out of ${questions.length} (${percentage}%)`;
    
    // Set result message
    const titleEl = document.getElementById('result-title');
    const badgeEl = document.getElementById('badge-earned');
    
    if (percentage >= 80) {
        titleEl.textContent = "🌠 Cosmic Genius!";
        badgeEl.textContent = "🏆";
    } else if (percentage >= 50) {
        titleEl.textContent = "🚀 Space Explorer!";
        badgeEl.textContent = "🛰️";
    } else {
        titleEl.textContent = "🌌 Keep Exploring!";
        badgeEl.textContent = "🔭";
    }
    
    // Reset button
    document.getElementById('try-again').onclick = () => {
        currentQuestion = 0;
        score = 0;
        quizContent.style.display = 'block';
        resultsEl.style.display = 'none';
        showQuestion();
    };
}