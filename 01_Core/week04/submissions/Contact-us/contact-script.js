function contactUs() {
    var phone = document.forms["contact-form"]["phone"].value;
    var email = document.forms["contact-form"]["email"].value;
    var message = document.forms["contact-form"]["customer-message"].value;

    if (message == "" || email == "" || phone == "") {
        alert("Error: input field is empty")
    } else {
        alert("Form submitted successfully");
    }
}
