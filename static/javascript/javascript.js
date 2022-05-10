function myFunction(val) {
    if(val == "McDonald's"){
        let disable = document.getElementById('checkinputid')
        // disable.setAttribute('disabled', "")
        // disable.removeAttribute('required')
        disable.setAttribute('value', 'Not required')
        disable.style.backgroundColor='#d3d3d3'
        
        
        
    } else {
        let disable = document.getElementById('checkinputid')
        disable.removeAttribute('disabled')
        disable.style.backgroundColor='white'
    }
  }

 var specifiedElement4 = document.getElementById('companyinputid');

 document.addEventListener('click', function(event) {
  var isClickInside4= specifiedElement4.contains(event.target);
  if (isClickInside4) {
   document.getElementById("companylabelid").innerHTML = "e.g. McDonald's"
  } else {
    document.getElementById("companylabelid").innerHTML = "Company:"
  }
});

var specifiedElement1 = document.getElementById('surveyinputid');

//I'm using "click" but it works with any event
document.addEventListener('click', function(event) {
  var isClickInside1= specifiedElement1.contains(event.target);
  if (isClickInside1) {
   document.getElementById("surveylabelid").innerHTML = "e.g. 12-34"
  } else {
    document.getElementById("surveylabelid").innerHTML = "Survey Code:"
  }
});

var specifiedElement2 = document.getElementById('checkinputid');

//I'm using "click" but it works with any event
document.addEventListener('click', function(event) {
  var isClickInside2= specifiedElement2.contains(event.target);
  if (isClickInside2) {
   document.getElementById("checklabelid").innerHTML = "e.g. 5678"
  } else {
    document.getElementById("checklabelid").innerHTML = "Check Code:"
  }
});
var specifiedElement3 = document.getElementById('emailinputid');

//I'm using "click" but it works with any event
document.addEventListener('click', function(event) {
  var isClickInside3= specifiedElement3.contains(event.target);
  if (isClickInside3) {
   document.getElementById("emaillabelid").innerHTML = "e.g. john.doe@gmail.com"
  } else {
    document.getElementById("emaillabelid").innerHTML = "Email:"
  }
});


//I'm using "click" but it works with any event

// let getSubmit = document.getElementById('submitButton')
// getSubmit.addEventListener('click', changeSubmitButton())

function changeSubmitButton(){
  document.getElementById('submitButton').innerHTML = 'Loading ...'
}

var alert =document.getElementById('myalert')

var submit =document.getElementById('submitButton')

var span = document.getElementsByClassName("close")[0];


submit.onclick =function(){
  alert.style.display='block'
}

span.onclick = function() {
  alert.style.display = "none";
}