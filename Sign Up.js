function validateEmail() {

    let valid = false;

    let input = document.getElementById('signup-email').value;

    if (input.toLowerCase().includes('uwa.edu.au') && input.toLowerCase().includes('@')) {
        valid = true;
    }

    return valid;
}

function confirmEmail() {
    let confirmed = false;

    let email = document.getElementById('signup-email').value;
    let confirm = document.getElementById('confirm-email').value;

    if (email.toLowerCase() == confirm.toLowerCase()) {
        confirmed = true;
    }

    return confirmed;
}

function confirmPassword() {

    let confirmed = false;

    let email = document.getElementById('signup-password').value;
    let confirm = document.getElementById('confirm-password').value;

    if (email.toLowerCase() == confirm.toLowerCase()) {
        confirmed = true;
    }

    return confirmed;
}

function validateInputs() {
    var container = document.getElementById('signup-error');
    container.innerHTML = ''; // Clear previous results
    if (validateEmail() == false) {
        var newParagraph = document.createElement('p');
        var newText = document.createTextNode('Invalid email');
        newParagraph.className = "errorSignUp";
        newParagraph.appendChild(newText);
        container.appendChild(newParagraph);
    }
    if (confirmEmail() == false) {
        var newParagraph = document.createElement('p');
        var newText = document.createTextNode('Emails do not match');
        newParagraph.className = "errorSignUp";
        newParagraph.appendChild(newText);
        container.appendChild(newParagraph);
    }
    if (confirmPassword() == false) {
        var newParagraph = document.createElement('p');
        var newText = document.createTextNode('Passwords do not match');
        newParagraph.className = "errorSignUp";
        newParagraph.appendChild(newText);
        container.appendChild(newParagraph);
    }
}