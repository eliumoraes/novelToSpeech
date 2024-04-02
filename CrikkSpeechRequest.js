import fetch from 'node-fetch';

async function fetchData() {
    let headersList = {
        "Host": "crikk.com",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://crikk.com/text-to-speech/",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "304",
        "Origin": "https://crikk.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    };

    let bodyContent = "language=&charecter=en-GB-ThomasNeural&text=Meng+Qianqian's+eyes+lit+up+slightly+upon+seeing+this,+and+she+continued+to+stroke+the+surface+of+the+egg+with+the+feather+while+simultaneously+stroking+the+egg+with+her+other+hand.%0D%0A%0D%0AAll+of+a+sudden,+the+egg+stopped+swaying+and+fell+completely+still.";

    try {
        let response = await fetch("https://crikk.com/text-to-speech/", {
            method: "POST",
            body: bodyContent,
            headers: headersList
        });

        // Checking the response type
        console.log(`Response Content-Type: ${response.headers.get('Content-Type')}`);

        // To check if the response is binary, we look at the Content-Type header
        if(response.headers.get("Content-Type").includes("application/json")) {
            // It's JSON, handle it as a text
            let jsonData = await response.json();
            console.log(jsonData);
        } else if(response.headers.get("Content-Type").includes("text")) {
            // It's text, handle it as a text
            let textData = await response.text();
            console.log(textData);
        } else {
            // It's likely binary, handle it as an arrayBuffer or blob
            console.log('The response is likely binary.');
            let binaryData = await response.arrayBuffer();
            // For demonstration, logging the size of the binary data
            console.log(`Binary data size: ${binaryData.byteLength} bytes`);
        }
        
        console.log(data);
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call the async function
fetchData();
