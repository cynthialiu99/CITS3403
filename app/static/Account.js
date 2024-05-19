// Sample data for threads (you can replace this with data from a database)

// Function to display threads
function displayThreads(threads) {

    let threadsList = document.getElementById('threadsList');
    threadsList.innerHTML = '';

    threads.forEach(thread => {
        let threadHTML = `
            <div class="thread">
                <a href="/threads/${thread.thread_id}" class="thread-link">${thread.thread_name}</a>
            </div>
        `;
        threadsList.innerHTML += threadHTML;
    });
}

// Initial display of threads
if (typeof threads !== 'undefined') {
    displayThreads(threads);
} else {
    console.error('Threads data is not available');
}