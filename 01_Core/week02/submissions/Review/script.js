/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show"); //points to the dropdwon menu's class adds a toggle method to show the drop down menu.
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {                  // if the user is not clicking on the target element then removes the class value "show"
    var myDropdown = document.getElementById("myDropdown");
      if (myDropdown.classList.contains('show')) {
        myDropdown.classList.remove('show');
      }
    }
  }
  // create a alphabetically-sorted list by last name.
function getNames(){
    var names = document.getElementById("myText").value; //points to the value of the textArea.
    var namesArr = names.split(',');   //Splits the names with a comma 
    var sortedNames = namesArr.sort(); //sorts the names in acending order
    var fullHTML = sortedNames.join(' ') // joins  the names with a space
    document.getElementById("list").innerHTML = fullHTML;   //replaces the content in the empty div with the new array of names.
}

// string of full names

var names = ["Ziara Diaz", "Nick Strumpf", "Malcolm Taylor", "Chris Smith"];

var allNames = names.sort((a,b) => {  //Compare function that takes in the name and last name and compares them.
 var aSplit = a.split(' ');        // splits the first parameter with a space    
 var aLastName = aSplit[1].toLowerCase();   // looks at the second value of the a paramenter (the last name)
 var bSplit = b.split(' ');                  // splits the second parameter ('Nick Strumpf')
 var bLastName = bSplit[1].toLowerCase();  // looks at the second value of the parameter ('strumpf')
 if(aLastName < bLastName) return -1;    // if the first last name is less than the second last name puts it first.
 if(aLastName > bLastName) return 1;  // if the first last name is greater than it will put it after .
 return 0;
})


var id = document.getElementById("list");
allNames.forEach((i)=>{
  var newDiv = document.createElement('li');   // creater an new list that takes all the names
  id.appendChild(newDiv)  //adds the list to the empty names div
  newDiv.classList.add("addCSS");
  newDiv.innerHTML = i;  // prints the names by replacing the text in the empty div.
})

// I was not anle to figure out how to make just the last names red and bold. 
