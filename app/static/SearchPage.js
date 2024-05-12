
//Sample Data
let threads = [
  { id: 1, title: 'Help with Math Homework', content: 'I need help with algebra problems.', date: '2024-04-14' },
  { id: 2, title: 'Programming Project Help', content: 'I am stuck on my programming project.', date: '2024-04-13' },
  { id: 3, title: 'Study Tips for Exams', content: 'Any tips for effective studying?', date: '2024-04-12' }
];

function searchBar() {

  let input = document.getElementById('searcher').value
  input = input.toLowerCase();

  document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
    searchBar(); // Call searchBar function
  });


  let matchedThreads = [];
  
  // Iterate through threads array
  threads.forEach(thread => {
    if (thread.title.toLowerCase().includes(input) || thread.content.toLowerCase().includes(input)) {
      matchedThreads.push(thread);
    }
  });
  
  var container = document.getElementById('searchResults');
  var populartopics = document.getElementById('popularTopics');
  populartopics.innerHTML = '';
  container.innerHTML = ''; // Clear previous results

  if (matchedThreads.length == 0) {
    var newParagraph = document.createElement('p');
    var newText = document.createTextNode('No results found');
    newParagraph.className = "errorNothingFound";
    newParagraph.appendChild(newText);
    container.appendChild(newParagraph);
  }

  else {

    matchedThreads.forEach(thread => {
      var newParagraph = document.createElement('p');
      var newLink = document.createElement('a');
      newLink.setAttribute('href', 'pathtothread.html');
      newLink.textContent = thread.title;
      newLink.className = "foundThreads";
      newParagraph.appendChild(newLink);
      container.appendChild(newParagraph);
    });
  }   
}