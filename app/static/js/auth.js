console.log("✅ auth.js loaded");

const API_BASE = "/api/v1";

/* ============================
   REGISTER
============================ */

async function register(event) {
    event.preventDefault();

    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    try {
        const response = await fetch(`${API_BASE}/auth/register`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                email,
                password
            })
        });

        const data = await response.json();

        if (response.ok) {
            alert("✅ Registration Successful!");
            window.location.href = "/login";
        } else {
            alert(data.detail || "Registration failed.");
        }

    } catch (error) {
        console.error(error);
        alert("Unable to connect to the server.");
    }
}


/* ============================
   LOGIN
============================ */

async function login(event) {
    event.preventDefault();

    console.log("🚀 Login button clicked");

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    const formData = new URLSearchParams();

    formData.append("username", email);
    formData.append("password", password);

    try {

        const response = await fetch(`${API_BASE}/auth/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: formData
        });

        const data = await response.json();

        console.log("Status:", response.status);
        console.log(data);

        if (response.ok) {

            // If you're using JWT in localStorage
          

            console.log("✅ Login Successful");
            console.log("➡ Redirecting to Dashboard");

            window.location.href = "/dashboard";

        } else {

            alert(data.detail || "Invalid email or password.");

        }

    } catch (error) {

        console.error(error);

        alert("Unable to connect to the server.");

    }
}


/* ============================
   LOGOUT
============================ */

async function logout() {

    alert("Logout button clicked!");

    console.log("Logout button clicked!");

    try {

        const response = await fetch(`${API_BASE}/auth/logout`, {
            method: "POST"
        });

        console.log("Response Status:", response.status);


        window.location.href = "/login";

    } catch (error) {

        console.error(error);

    }

}
/* ============================
   EVENT LISTENERS
============================ */

document.addEventListener("DOMContentLoaded", () => {

    console.log("DOM Loaded ✅");

    const registerForm = document.getElementById("register-form");

    if (registerForm) {
        console.log("Register form found");
        registerForm.addEventListener("submit", register);
    }

    const loginForm = document.getElementById("login-form");

    if (loginForm) {
        console.log("Login form found");
        loginForm.addEventListener("submit", login);
    }

    const logoutBtn = document.getElementById("logout-btn");

    console.log("Logout Button =", logoutBtn);

    if (logoutBtn) {
        console.log("Logout button event attached");

        logoutBtn.addEventListener("click", logout);
    }

});