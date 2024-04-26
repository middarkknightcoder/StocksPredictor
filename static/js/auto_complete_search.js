// const searchInput = document.getElementById('searchInput');
// const suggestionsContainer = document.getElementById('suggestionsContainer');

// searchInput.addEventListener('input', function () {
//     const query = searchInput.value.trim();

//     // Clear previous suggestions
//     suggestionsContainer.innerHTML = '';

//     // Fetch suggestions from Alpha Vantage API
//     fetch(`https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=${query}&apikey=6V8HYZYHGF4V86E6`)
//         .then(response => response.json())
//         .then(data => {
//             // Display suggestions
//             data.bestMatches.forEach(match => {
//                 const symbol = match['1. symbol'];
//                 const name = match['2. name'];

//                 const suggestionElement = document.createElement('li');
//                 suggestionElement.classList.add('suggestion');
//                 suggestionElement.textContent = `${symbol} - ${name}`;

//                 suggestionElement.addEventListener('click', function () {
//                     // Populate search input with selected symbol
//                     searchInput.value = symbol;
//                     suggestionsContainer.innerHTML = ''; // Clear suggestions
//                 });

//                 suggestionsContainer.appendChild(suggestionElement);
//             });
//         })
//         .catch(error => console.error('Error fetching suggestions:', error));
// });

// // Hide suggestions container when clicking outside of it
// document.addEventListener('click', function (event) {
//     if (!suggestionsContainer.contains(event.target)) {
//         suggestionsContainer.innerHTML = ''; // Clear suggestions
//     }
// });


// const searchInput = document.getElementById('searchInput');
// const suggestionsContainer = document.getElementById('suggestionsContainer');
// let companyData = [];

// // Fetch data from CSV file
// fetch('All_Indian_Stocks_listed_in_nifty500.csv')
//     .then(response => response.text())
//     .then(csvText => {
//         // Parse CSV data
//         const rows = csvText.split('\n');
//         rows.forEach(row => {
//             const columns = row.split(',');
//             if (columns.length >= 5) {
//                 const company = {
//                     companyName: columns[0].trim(),
//                     industry: columns[1].trim(),
//                     symbol: columns[2].trim(),
//                     series: columns[3].trim(),
//                     isinCode: columns[4].trim()
//                 };
//                 companyData.push(company);
//             }
//         });
//     })
//     .catch(error => console.error('Error fetching CSV data:', error));

// searchInput.addEventListener('input', function () {
//     const query = searchInput.value.trim().toLowerCase();

//     // Clear previous suggestions
//     suggestionsContainer.innerHTML = '';

//     // Filter companyData based on query
//     const filteredCompanies = companyData.filter(company =>
//         company.companyName.toLowerCase().includes(query) ||
//         company.symbol.toLowerCase().includes(query) ||
//         company.industry.toLowerCase().includes(query) ||
//         company.series.toLowerCase().includes(query) ||
//         company.isinCode.toLowerCase().includes(query)
//     );

//     // Display suggestions
//     filteredCompanies.forEach(company => {
//         const suggestionElement = document.createElement('li');
//         suggestionElement.classList.add('suggestion');
//         suggestionElement.textContent = `${company.companyName} - ${company.symbol}`;

//         suggestionElement.addEventListener('click', function () {
//             // Populate search input with selected company
//             searchInput.value = company.companyName;
//             suggestionsContainer.innerHTML = ''; // Clear suggestions
//         });

//         suggestionsContainer.appendChild(suggestionElement);
//     });
// });

// // Hide suggestions container when clicking outside of it
// document.addEventListener('click', function (event) {
//     if (!suggestionsContainer.contains(event.target)) {
//         suggestionsContainer.innerHTML = ''; // Clear suggestions
//     }
// });



// *************** Below code is write based on the rapid api call const url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/search?search=AA';

// For searchbar-1s

const searchInput = document.getElementById('searchInput');
const suggestionsContainer = document.getElementById('suggestionsContainer');

searchInput.addEventListener('input', async function () {
    const inputValue = this.value.trim();
    if (!inputValue) {
        suggestionsContainer.innerHTML = '';
        return;
    }

    const url = `https://yahoo-finance15.p.rapidapi.com/api/v1/markets/search?search=${inputValue}`;
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '08f1541678msh2a4747804150020p1237efjsn27b025299ffd',
            'X-RapidAPI-Host': 'yahoo-finance15.p.rapidapi.com'
        }
    };

    try {
        const response = await fetch(url, options);
        const data = await response.json();
        displaySuggestions(data.body);
    } catch (error) {
        console.error(error);
    }
});

function displaySuggestions(suggestions) {
    suggestionsContainer.innerHTML = '';
    suggestions.forEach(item => {
        const suggestionElement = document.createElement('option');
        suggestionElement.classList.add('suggestion');
        suggestionElement.style = "color:white;"
        suggestionElement.textContent = `${item.symbol}`;
        suggestionElement.addEventListener('click', function () {
            searchInput.value = item.symbol;
            suggestionsContainer.innerHTML = '';
        });
        suggestionsContainer.appendChild(suggestionElement);
    });
}

// Hide suggestions container when clicking outside of it
document.addEventListener('click', function (event) {
    if (!suggestionsContainer.contains(event.target) && event.target !== searchInput) {
        suggestionsContainer.innerHTML = '';
    }
});

// You can see if not run any api form of autocomplete then used


// For SeacrhBar-2


