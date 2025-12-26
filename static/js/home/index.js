let signup = document.getElementById('signup');
let login = document.getElementById('login');
signup.addEventListener('click', () => {
    let change = window.location.href = "signup";
})
login.addEventListener('click',() => {
    let change = window.location.href = "login"
})