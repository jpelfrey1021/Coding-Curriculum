var phone = document.forms["contact-form"]["phone"].value
var email = document.forms["contact-form"]["email"].value
var message = document.forms["contact-form"]["customer-message"].value

console.log(email)

function contactUs() {
    if (email== "") {
        alert("Must enter an email or phone number")
        console.log(phone)
        return false
    } else if (message == "") {
        alert("Must enter a message")
        return false
    } else {
        alert("Form Submitted Successfully")
        return true;
    }
}