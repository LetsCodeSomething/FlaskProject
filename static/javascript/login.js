let loginTextBox, passwordTextBox, loginButton;

window.onload = function processPageLoad()
{
    loginTextBox = document.getElementById("loginTextBox");
    passwordTextBox = document.getElementById("passwordTextBox");
    loginButton = document.getElementById("loginButton");
}

function processTextChange()
{
    let login = loginTextBox.value;
    let password = passwordTextBox.value;
    
    loginButton.disabled = !login || !password;
}