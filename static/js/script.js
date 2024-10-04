function togglePasswordVisibility(element) {
   const icon = element.children[0];
   const isPasswordVisible = icon.getAttribute("data-password") === "visible";

   // toggle eye icon
   icon.setAttribute("data-password", isPasswordVisible ? "hidden" : "visible");

   // toggle password input type
   const passwordInput = element.parentElement.querySelector(".password-field");
   passwordInput.type = isPasswordVisible ? "password" : "text";
}
