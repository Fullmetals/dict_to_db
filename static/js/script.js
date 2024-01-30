document.addEventListener("DOMContentLoaded", function() {
    const searchForm = document.getElementById('searchForm');
    searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const word = document.getElementById('searchInput').value;
        fetchResults(word);
    });
});

function fetchResults(word) {
    // Replace with the correct URL to your backend server
    const apiURL = `http://localhost:5000/search/${word}`;

    fetch(apiURL)
        .then(response => response.json())
        .then(data => {
            displayResults(data);
        })
        .catch(error => {
            console.error('Error fetching data: ', error);
            displayResults({ error: "An error occurred while fetching data." });
        });
}

function displayResults(data) {
    const resultSection = document.getElementById('resultSection');
    resultSection.innerHTML = ''; // Clear previous results

    if (data.error) {
        resultSection.innerHTML = `<p>${data.error}</p>`;
    } else {
        // Assuming `data` is an array of dictionary entries
        data.forEach(entry => {
            const div = document.createElement('div');
            div.innerHTML = `<h2>${entry.word}</h2><p>${entry.definition}</p>`;
            resultSection.appendChild(div);
        });
    }
}
