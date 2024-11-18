// script.js

// Función para registrar un nuevo usuario
function registerUser(event) {
    event.preventDefault();
  
    // Obtener valores del formulario de registro
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
  
    // Crear un objeto usuario
    const user = { username, email, password };
  
    // Guardar usuario en localStorage
    localStorage.setItem(email, JSON.stringify(user));
  
    // Mostrar mensaje de registro completo
    alert("Registro completo. Ahora puedes iniciar sesión.");
    window.location.href = "index.html"; // Redirige a la página de login
  }
  
  // Función para iniciar sesión
  function loginUser(event) {
    event.preventDefault();
  
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
  
    const storedUser = JSON.parse(localStorage.getItem(email));
  
    if (storedUser && storedUser.password === password) {
      alert("Inicio de sesión exitoso. ¡Bienvenido!");
      window.location.href = "feed.html"; // Redirige al feed
    } else {
      alert("Correo o contraseña incorrectos. Inténtalo de nuevo.");
    }
  }
  
  
  // Asignar funciones a los formularios al cargar el documento
  document.addEventListener("DOMContentLoaded", function () {
    const registerForm = document.querySelector("#registerForm");
    const loginForm = document.querySelector("#loginForm");
  
    if (registerForm) {
      registerForm.addEventListener("submit", registerUser);
    }
  
    if (loginForm) {
      loginForm.addEventListener("submit", loginUser);
    }
  });
  