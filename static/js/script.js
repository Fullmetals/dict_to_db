document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const wordToSearch = document.getElementById('searchInput').value;
    // Fetch the dictionary data
    fetch('https://api.dictionaryapi.dev/api/v2/entries/en/' + wordToSearch)
        .then(response => response.json())
        .then(data => {
            // Process and display data in resultsContainer
            const resultsContainer = document.getElementById('resultsContainer');
            resultsContainer.innerHTML = ''; // Clear previous results
            data.forEach(result => {
                const resultItem = document.createElement('div');
                resultItem.classList.add('result-item');
                resultItem.innerHTML = `
                    <h3 class="word">${result.word}</h3>
                    <p class="partOfSpeech">${result.partOfSpeech}</p>
                    <p class="definition">${result.definition}</p>
                `;
                resultsContainer.appendChild(resultItem);
            });
        })
        .catch(error => {
            console.error('Error fetching data: ', error);
            // Handle errors here
        });
});