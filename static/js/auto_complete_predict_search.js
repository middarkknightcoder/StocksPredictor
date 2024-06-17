// script.js
document.addEventListener('DOMContentLoaded', () => {
    const searchBar = document.getElementById('search-bar');
    const resultsContainer = document.getElementById('results');
    const apiKey = '9RHLBC4JFIMH0O12';

    searchBar.addEventListener('input', (event) => {
        const query = event.target.value.trim().toLowerCase();

        if (query.length > 0) {
            fetchResults(query).then(results => {
                displayResults(results);
            });
        } else {
            clearResults();
        }
    });

    async function fetchResults(query) {
        const url = `https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=${query}&apikey=${apiKey}`;
        try {
            const response = await fetch(url);
            const data = await response.json();
            return data.bestMatches || [];
        } catch (error) {
            console.error('Error fetching data:', error);
            return [];
        }
    }

    function displayResults(results) {
        clearResults();
        results.forEach(result => {
            const li = document.createElement('li');
            li.textContent = `${result['1. symbol']} - ${result['2. name']}`;
            li.addEventListener('click', () => {
                searchBar.value = result['1. symbol'];
                clearResults();
                performSearch(result['1. symbol']);
            });
            resultsContainer.appendChild(li);
        });
    }

    function clearResults() {
        resultsContainer.innerHTML = '';
    }

    function performSearch(query) {
        // Perform the search action here. For now, we'll just log the query.
        console.log('Selected and searching for:', query);
        // You can also initiate another API call or update the UI based on the selected item.
    }

    // Hide suggestions container when clicking outside of it
    document.addEventListener('click', function (event) {
        if (!resultsContainer.contains(event.target) && event.target !== searchBar) {
            resultsContainer.innerHTML = '';
        }
    });
});