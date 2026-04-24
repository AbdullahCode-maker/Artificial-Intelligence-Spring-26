document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const resultValue = document.getElementById('result-value');
    const resultContainer = document.getElementById('result-container');

    const response = await fetch('/predict', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();

    if (data.result !== undefined) {
        // Result display karna
        resultValue.innerText = `$${data.result}`;
        resultContainer.classList.remove('hidden');
    } else {
        alert("Error: " + data.error);
    }
});