/*
Make the last names bold and red using CSS (NOT inline styles).
*/



var customers = ["Sarah Smith","Mark Paul","Charles Marks","Sarah New","Michael Martin","Lori Lane"];

function init() {
	var sortNames = customers.sort((a,b) => {
		var aSplit = a.split(' ');
		var aLastName = aSplit[1];   				// looks at the second value of the a paramenter (the last name)
		var bSplit = b.split(' ');                  // splits the second parameter ('Nick Strumpf')
		var bLastName = bSplit[1];  				// looks at the second value of the parameter ('strumpf')
 		if(aLastName < bLastName) return -1;    	// if the first last name is less than the second last name puts it first.
 		if(aLastName > bLastName) return 1;  		// if the first last name is greater than it will put it after .
 		return 0;
 	})


	sortNames.map(function(cur, index) {
		var names = cur.split(" ")
		var text = `<li> ${names[0]} <strong> ${names[1]} </strong> </li>`
		return document.getElementById("member-list").insertAdjacentHTML("beforeend",text)
	})
}

window.onload = function() {
	if (window.location.href.indexOf('members.html') > -1) {
    init();
}
}


/*
// create a alphabetically-sorted list by last name.
function getNames(){
    var names = document.getElementById("myText").value; //points to the value of the textArea.
    var namesArr = names.split(',');   //Splits the names with a comma 
    var sortedNames = namesArr.sort(); //sorts the names in acending order
    var fullHTML = sortedNames.join(' ') // joins  the names with a space
    document.getElementById("list").innerHTML = fullHTML;   //replaces the content in the empty div with the new array of names.
}
*/