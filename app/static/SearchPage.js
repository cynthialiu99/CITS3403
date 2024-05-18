function searchThreads() {
  var input, filter, threads, thread, i, txtValue;
  input = document.getElementById('searchInput');
  filter = input.value.toUpperCase();
  threads = document.getElementById("threadsList").getElementsByTagName('a');

  for (i = 0; i < threads.length; i++) {
      thread = threads[i];
      txtValue = thread.textContent || thread.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
          thread.style.display = "";
      } else {
          thread.style.display = "none";
      }
  }
}
