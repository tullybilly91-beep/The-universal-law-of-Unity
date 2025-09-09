```javascript
    document.addEventListener('DOMContentLoaded', () => {
        const analyzeButton = document.getElementById('analyze-button');
        const resultsContainer = document.getElementById('results-container');
        const resultsOutput = document.getElementById('results-output');

        analyzeButton.addEventListener('click', async () => {
            // 1. Collect data from the form
            const systemData = {
                system_name: document.getElementById('system_name').value,
                natural: { core_principle: document.getElementById('natural_layer').value },
                symbolic: { stated_value: document.getElementById('symbolic_layer').value },
                numeric: { primary_goal: document.getElementById('numeric_layer').value },
                personal_catalyst: { observed_behavior: document.getElementById('personal_catalyst').value }
            };

            // 2. Show a loading message and send data to the backend API
            resultsOutput.textContent = 'Analyzing...';
            resultsContainer.classList.remove('hidden');

            try {
                const response = await fetch('/api', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(systemData)
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const results = await response.json();
                
                // 3. Display the results from the Python backend
                resultsOutput.textContent = JSON.stringify(results, null, 2);

            } catch (error) {
                resultsOutput.textContent = `An error occurred: ${error.message}`;
            }
        });
    });
    ```
