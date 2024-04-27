// Sample data for threads (you can replace this with data from a database)
let threads = [
    { id: 1, title: 'Help with Math Homework', content: 'I need help with algebra problems.', date: '2024-04-14'},
    { id: 2, title: 'Programming Project Help', content: 'I am stuck on my programming project.', date: '2024-04-13' },
    { id: 3, title: 'Study Tips for Exams', content: 'Any tips for effective studying?', date: '2024-04-12' }
];

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
                <button type="button" class="btn btn-primary btn-sm" onclick="replyToThread(${thread.id})">Reply</button>
            </div>
        `;
        threadsList.innerHTML += threadHTML;
    });
}

// Initial display of threads
displayThreads();