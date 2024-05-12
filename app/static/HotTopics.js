
function getHotTopics(){
    try{
        const xhttp = new XMLHttpRequest();
        xhttp.open('GET', 'SearchPage/PythonHomePage.html',true);
        xhttp.onreadystatechange = function(){
            if (xhttp.readyState === XMLHttpRequest.DONE){
                if (xhttp.status ===200){
                    const xhttpText = xhttp.responseText;
                    const xhttpTopics = extractTopics(xhttpText);

                //populate hot topics box with extracted topics
                const hotTopicsElement = document.getElementById('hotTopics');
                hotTopicsElement.innerHTML = '<h3>Hot Topics!</h3>';

                xhttpTopics.forEach(topic => {   //dynamically generate HMTL <a> tags for each topic in xhttp array
                    hotTopicsElement.innerHTML += `<a href="${topic.link}">${topic.title}</a><br>`;
                });
            }

            else{
                console.error("Error fetching page",xhttp.status);
            }
        }
    }
    xhttp.send();
    }
    catch (error){
        console.error("Error fetching topics:",error);
    }
}

function extractTopics(pageContent){
    //const topicRegex = /<a href="(.*?)">(.*?)<\/a>/g; // Regular expression to match links
    const topics = [];
    let match;
    while ((match = topicRegex.exec(pageContent)) !== null) {
        topics.push({ link: match[1], title: match[2] });
    }
    return topics;
}

//Call getHotTopics function when the page loads
window.onload = getHotTopics;