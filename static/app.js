const faqForm = document.getElementById('faqForm');
const questionInput = document.getElementById('questionInput');
const questionError = document.getElementById('questionError');
const answerBox = document.getElementById('answerBox');
const sourceBox = document.getElementById('sourceBox');
const submitBtn = document.getElementById('submitBtn');

function clearValidationState() {
  questionInput.classList.remove('is-invalid');
  questionError.textContent = '';
}

faqForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const question = questionInput.value.trim();

  if (!question) {
    questionInput.classList.add('is-invalid');
    questionError.textContent = 'Please enter a question before submitting.';
    questionInput.focus();
    return;
  }

  clearValidationState();
  submitBtn.disabled = true;
  submitBtn.textContent = 'Asking...';
  answerBox.classList.remove('error', 'empty');
  answerBox.textContent = 'Looking for an answer...';

  try {
    const response = await fetch('/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question })
    });

    let data;
    try {
      data = await response.json();
    } catch {
      throw new Error('The server returned an unreadable response. Please try again.');
    }

    if (!response.ok) {
      throw new Error(data.error || 'We could not answer that right now. Please try again.');
    }
    if (!data.answer || !data.source) {
      throw new Error('The server response was missing the answer or source. Please try again.');
    }

    answerBox.textContent = data.answer;
    sourceBox.textContent = data.source;
    sourceBox.classList.remove('empty');
  } catch (error) {
    answerBox.classList.add('error');
    answerBox.textContent = error.message || 'Something went wrong. Please try again.';
    sourceBox.textContent = 'No source snippet available.';
    sourceBox.classList.add('empty');
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = 'Ask';
  }
});
