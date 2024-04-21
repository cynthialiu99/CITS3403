// Sample data for threads (you can replace this with data from a database)
let threads = [
    { id: 1, title: 'Help with Math Homework', content: 'I need help with algebra problems.', date: '2024-04-14' },
    { id: 2, title: 'Programming Project Help', content: 'I am stuck on my programming project.', date: '2024-04-13' },
    { id: 3, title: 'Study Tips for Exams', content: 'Any tips for effective studying?', date: '2024-04-12' }
];

// Function to add a new thread
function addThread() {
    let threadTitle = document.getElementById('threadTitle').value;
    let threadContent = document.getElementById('threadContent').value;

    // Validate form inputs
    if (!threadTitle.trim()) {
        alert('Please enter a thread title.');
        return;
    }

    if (!threadContent.trim()) {
        alert('Please enter thread content.');
        return;
    }

    // Create a new thread object
    let newThread = {
        id: threads.length + 1,
        title: threadTitle,
        content: threadContent,
        date: new Date().toISOString().split('T')[0]
    };

    // Add the new thread to the threads array
    threads.push(newThread);

    // Clear the form fields
    document.getElementById('threadTitle').value = '';
    document.getElementById('threadContent').value = '';

    // Display the updated list of threads
    displayThreads();
}


// Function to display threads
function displayThreads() {
    let threadsList = document.getElementById('threadsList');
    threadsList.innerHTML = '';

    threads.forEach(thread => {
        let threadHTML = `
            <div class="thread">
                <h5>${thread.title}</h5>
                <p>${thread.content}</p>
                <small>${thread.date}</small>
            </div>
        `;
        threadsList.innerHTML += threadHTML;
    });
}

// Function to search threads
function searchThreads() {
    let searchTerm = document.getElementById('searchInput').value.toLowerCase();
    let filteredThreads = threads.filter(thread => 
        thread.title.toLowerCase().includes(searchTerm) || 
        thread.content.toLowerCase().includes(searchTerm)
    );

    // Display the filtered list of threads
    let threadsList = document.getElementById('threadsList');
    threadsList.innerHTML = '';

    filteredThreads.forEach(thread => {
        let threadHTML = `
            <div class="thread">
                <h5>${thread.title}</h5>
                <p>${thread.content}</p>
                <small>${thread.date}</small>
            </div>
        `;
        threadsList.innerHTML += threadHTML;
    });
}

// Initial display of threads
displayThreads();
