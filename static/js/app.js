const api = "https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo";

fetch(api)
    .then((res) => res.json())
    .then((data) => {
        // console.log(data.most_actively_traded);

        const mostActivelyTraded = document.querySelector("#most-actively-traded");

        for (let i = 0; i < 8; i++) {

            const col = document.createElement("div");
            col.classList.add("col-lg-3", "col-12");
            mostActivelyTraded.appendChild(col);

            const col2 = document.createElement("div");
            col2.classList.add("services-thumb");
            col.appendChild(col2);

            const col3 = document.createElement("div");
            col3.classList.add("border-bottom", "mb-4", "pb-3");
            col2.appendChild(col3);

            const tickerName = document.createElement("h3");
            tickerName.classList.add("mb-0");
            tickerName.innerText = data.most_actively_traded[i].ticker;
            col3.appendChild(tickerName);

            const p1 = document.createElement("p");
            p1.classList.add("mb-0", "mt-1");
            p1.innerText = "price";
            col2.appendChild(p1);

            const colP1 = document.createElement("div");
            colP1.classList.add("services-price-wrap", "ms-auto");
            col2.appendChild(colP1);

            const colp1p = document.createElement("p");
            colp1p.classList.add("services-price-text", "mb-0");
            colp1p.innerText = `$${data.most_actively_traded[i].price}`;
            colP1.appendChild(colp1p);

            const colp1div = document.createElement("div");
            colp1div.classList.add("services-price-overlay");
            colP1.appendChild(colp1div);

            const p2 = document.createElement("p");
            p2.classList.add("mb-0", "mt-1");
            p2.innerText = "change amount";
            col2.appendChild(p2);

            const colP2 = document.createElement("div");
            colP2.classList.add("services-price-wrap", "ms-auto");
            col2.appendChild(colP2);

            const colp2p = document.createElement("p");
            colp2p.classList.add("services-price-text", "mb-0");
            colp2p.innerText = `$${data.most_actively_traded[i].change_amount}`;
            colP2.appendChild(colp2p);

            const colp2div = document.createElement("div");
            colp2div.classList.add("services-price-overlay");
            colP2.appendChild(colp2div);

            const p3 = document.createElement("p");
            p3.classList.add("mb-0", "mt-1");
            p3.innerText = "change percentage";
            col2.appendChild(p3);

            const colP3 = document.createElement("div");
            colP3.classList.add("services-price-wrap", "ms-auto");
            col2.appendChild(colP3);

            const colp3p = document.createElement("p");
            colp3p.classList.add("services-price-text", "mb-0");
            colp3p.innerText = `${data.most_actively_traded[i].change_percentage}`;
            colP3.appendChild(colp3p);

            const colp3div = document.createElement("div");
            colp3div.classList.add("services-price-overlay");
            colP3.appendChild(colp3div);

            const p4 = document.createElement("p");
            p4.classList.add("mb-0", "mt-1");
            p4.innerText = "volume";
            col2.appendChild(p4);

            const colP4 = document.createElement("div");
            colP4.classList.add("services-price-wrap", "ms-auto");
            col2.appendChild(colP4);

            const colp4p = document.createElement("p");
            colp4p.classList.add("services-price-text", "mb-0");
            colp4p.innerText = `${data.most_actively_traded[i].volume}`;
            colP4.appendChild(colp4p);

            // const colp4div = document.createElement("div");
            // colp4div.classList.add("services-price-overlay");
            // colP4.appendChild(colp4div);

            const discovermore = document.createElement("a");
            discovermore.href = "/companyinfo/" + data.most_actively_traded[i].ticker;
            discovermore.classList.add("custom-btn", "custom-border-btn", "btn", "mt-3", "p-3");
            discovermore.innerText = "Discover More";
            col2.appendChild(discovermore);
        }
    });


const key = "7aa4e3af189146c7abccadd68c0e3841";
const query = "business";
const url = `https://newsapi.org/v2/everything?q=${query}&apiKey=${key}`;

const req = new Request(url);

fetch(req)
    .then((res) => res.json())
    .then((data) => {
        console.log(data.articles);

        const front_news = document.querySelector("#front_news");

        for (let i = 0; i < 6; i++) {

            const col = document.createElement("div");
            col.classList.add("col-lg-4", "col-md-6", "col-12");
            front_news.appendChild(col);

            const newsPage = document.createElement("a");
            newsPage.href = data.articles[i].url;
            newsPage.target = "_blank"
            col.appendChild(newsPage);

            const col2 = document.createElement("div");
            col2.classList.add("projects-thumb");
            newsPage.appendChild(col2);

            const col3 = document.createElement("div");
            col3.classList.add("projects-info");
            col2.appendChild(col3);

            const source = document.createElement("small");
            source.classList.add("projects-tag");
            source.innerText = data.articles[i].source.name;
            col3.appendChild(source);

            const time = document.createElement("small");
            time.innerText = ` ${data.articles[i].publishedAt}`;
            col3.appendChild(time);

            const title = document.createElement("h3");
            title.classList.add("projects-title");
            title.innerText = data.articles[i].title;
            col3.appendChild(title);

            const description = document.createElement("p");
            description.innerText = data.articles[i].description;
            col2.appendChild(description);

            const newsimgZoom = document.createElement("a");
            newsimgZoom.classList.add("popup-image");
            newsimgZoom.href = data.articles[i].urlToImage;
            col2.appendChild(newsimgZoom);

            const newsimg = document.createElement("img");
            newsimg.classList.add("projects-image", "img-fluid");
            newsimg.src = data.articles[i].urlToImage;
            newsimgZoom.appendChild(newsimg);

        }
    });


fetch(req)
    .then((res) => res.json())
    .then((data) => {
        console.log(data.articles);

        const news = document.querySelector("#news");

        for (let i = 0; i < 50; i++) {

            const col = document.createElement("div");
            col.classList.add("col-lg-4", "col-md-6", "col-12");
            news.appendChild(col);

            const newsPage = document.createElement("a");
            newsPage.href = data.articles[i].url;
            newsPage.target = "_blank"
            col.appendChild(newsPage);

            const col2 = document.createElement("div");
            col2.classList.add("projects-thumb");
            newsPage.appendChild(col2);

            const col3 = document.createElement("div");
            col3.classList.add("projects-info");
            col2.appendChild(col3);

            const source = document.createElement("small");
            source.classList.add("projects-tag");
            source.innerText = data.articles[i].source.name;
            col3.appendChild(source);

            const time = document.createElement("small");
            time.innerText = ` ${data.articles[i].publishedAt}`;
            col3.appendChild(time);

            const title = document.createElement("h3");
            title.classList.add("projects-title");
            title.innerText = data.articles[i].title;
            col3.appendChild(title);

            const description = document.createElement("p");
            description.innerText = data.articles[i].description;
            col2.appendChild(description);

            const newsimgZoom = document.createElement("a");
            newsimgZoom.classList.add("popup-image");
            newsimgZoom.href = data.articles[i].urlToImage;
            col2.appendChild(newsimgZoom);

            const newsimg = document.createElement("img");
            newsimg.classList.add("projects-image", "img-fluid");
            newsimg.src = data.articles[i].urlToImage;
            newsimgZoom.appendChild(newsimg);

        }
    });


