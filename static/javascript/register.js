let loginTextBox, passwordTextBox, registerButton;

window.onload = function processPageLoad()
{
    loginTextBox = document.getElementById("loginTextBox");
    passwordTextBox = document.getElementById("passwordTextBox");
    registerButton = document.getElementById("registerButton");
}

function processTextChange()
{
    let login = loginTextBox.value;
    let password = passwordTextBox.value;
    
    registerButton.disabled = !login || !password;
}