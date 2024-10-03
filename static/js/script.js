function togglePasswordVisibility(element) {
   const isPasswordVisible = element.getAttribute("data-password") === "visible";

   // toggle eye icon
   element.setAttribute("data-password", isPasswordVisible ? "hidden" : "visible");

   // toggle password input type
   const passwordInput = element.parentElement.querySelector(".password-field");
   passwordInput.type = isPasswordVisible ? "password" : "text";
}
