fetch("articles.json")
    .then((res) => res.json())
    .then((data) => {
        makePage(data);
});

var makePage = function(data) {
    console.log(document.URL);
    if ( document.URL.includes("feed.html") ) {
        makeFeed(data);
    } else if (document.URL.includes("latest.html")) {
        makeLatest(data);
    } else if (document.URL.includes("trending.html")) {
        makeTrending(data);
    }
}

function makeLatest(data) {
    let feed_div = document.getElementById("article-area");
    for (let i in data) {
        if (data[i].Latest == 0) {
            continue;
        }
        let new_card = document.createElement("div");
        new_card.classList.add("card", "flex-row", "flex-wrap");
        feed_div.appendChild(new_card);
        
        let new_header = document.createElement("div");
        new_header.classList.add("card-header", "border-0");
        new_card.appendChild(new_header);

        let new_img_ref = document.createElement("a");
        new_img_ref.href = "article.html";
        new_header.appendChild(new_img_ref);
        let new_img = document.createElement("img");
        new_img.classList.add("thumbnail");
        new_img.src = data[i].ThumbnailURL;
        new_img_ref.appendChild(new_img);

        let new_body = document.createElement("div");
        new_body.classList.add("card-body");
        new_card.appendChild(new_body);

        let new_title = document.createElement("h4");
        new_title.classList.add("card-title");
        new_title.innerHTML = data[i].Title;
        new_body.appendChild(new_title);

        let new_source = document.createElement("h5");
        new_source.classList.add("card-text");
        new_source.innerHTML = data[i].Source;
        new_body.appendChild(new_source);

        let new_text = document.createElement("h6");
        new_text.classList.add("card-text");
        new_text.innerHTML = "Author: " + data[i].Author + ", published on " + data[i].Date_Published;
        new_body.appendChild(new_text);

        let new_footer = document.createElement("div");
        new_footer.classList.add("card-footer", "w-100");
        new_card.appendChild(new_footer);

        let new_button = document.createElement("a");
        new_button.classList.add("btn", "btn-primary", "w-100");
        new_button.href = "article.html";
        new_button.innerHTML = "Go to article";
        new_footer.appendChild(new_button);
    }
}

function makeTrending(data) {
    let feed_div = document.getElementById("article-area");
    for (let i in data) {
        if (data[i].Trending == 0) {
            continue;
        }
        let new_card = document.createElement("div");
        new_card.classList.add("card", "flex-row", "flex-wrap");
        feed_div.appendChild(new_card);
        
        let new_header = document.createElement("div");
        new_header.classList.add("card-header", "border-0");
        new_card.appendChild(new_header);

        let new_img_ref = document.createElement("a");
        new_img_ref.href = "article.html";
        new_header.appendChild(new_img_ref);
        let new_img = document.createElement("img");
        new_img.classList.add("thumbnail");
        new_img.src = data[i].ThumbnailURL;
        new_img_ref.appendChild(new_img);

        let new_body = document.createElement("div");
        new_body.classList.add("card-body");
        new_card.appendChild(new_body);

        let new_title = document.createElement("h4");
        new_title.classList.add("card-title");
        new_title.innerHTML = data[i].Title;
        new_body.appendChild(new_title);

        let new_source = document.createElement("h5");
        new_source.classList.add("card-text");
        new_source.innerHTML = data[i].Source;
        new_body.appendChild(new_source);

        let new_text = document.createElement("h6");
        new_text.classList.add("card-text");
        new_text.innerHTML = "Author: " + data[i].Author + ", published on " + data[i].Date_Published;
        new_body.appendChild(new_text);

        let new_footer = document.createElement("div");
        new_footer.classList.add("card-footer", "w-100");
        new_card.appendChild(new_footer);

        let new_button = document.createElement("a");
        new_button.classList.add("btn", "btn-primary", "w-100");
        new_button.href = "article.html";
        new_button.innerHTML = "Go to article";
        new_footer.appendChild(new_button);
    }
}

function makeFeed(data) {
    let feed_div = document.getElementById("article-area");
    for (let i in data) {

        let new_card = document.createElement("div");
        new_card.classList.add("card", "flex-row", "flex-wrap");
        feed_div.appendChild(new_card);
        
        let new_header = document.createElement("div");
        new_header.classList.add("card-header", "border-0");
        new_card.appendChild(new_header);

        let new_img_ref = document.createElement("a");
        new_img_ref.href = "article.html";
        new_header.appendChild(new_img_ref);
        let new_img = document.createElement("img");
        new_img.classList.add("thumbnail");
        new_img.src = data[i].ThumbnailURL;
        new_img_ref.appendChild(new_img);

        let new_body = document.createElement("div");
        new_body.classList.add("card-body");
        new_card.appendChild(new_body);

        let new_title = document.createElement("h4");
        new_title.classList.add("card-title");
        new_title.innerHTML = data[i].Title;
        new_body.appendChild(new_title);

        let new_source = document.createElement("h5");
        new_source.classList.add("card-text");
        new_source.innerHTML = data[i].Source;
        new_body.appendChild(new_source);

        let new_text = document.createElement("h6");
        new_text.classList.add("card-text");
        new_text.innerHTML = "Author: " + data[i].Author + ", published on " + data[i].Date_Published;
        new_body.appendChild(new_text);

        // Adds content to the card for viewing the whole article
        // let new_content = document.createElement("p");
        // new_content.classList.add("card-text");
        // new_content.innerHTML = data[i].Content;
        // new_body.appendChild(new_content);

        let new_footer = document.createElement("div");
        new_footer.classList.add("card-footer", "w-100");
        new_card.appendChild(new_footer);

        let new_button = document.createElement("a");
        new_button.classList.add("btn", "btn-primary", "w-100");
        new_button.href = "article.html";
        new_button.innerHTML = "Go to article";
        new_footer.appendChild(new_button);
    }
}