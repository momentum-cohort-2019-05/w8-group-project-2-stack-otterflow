
button = document.getElementById("bestAnswerButton").onclick = function (event) {
   
    button.addEventListener("mouseover", function (event) {   
    event.target.style.color = "orange";}
    setTimeout(function() {
    event.target.style.color = "";
    }, 500);
    }, false);

    button.addEventListener('click', function (event) {
        event.target.style.color = "green";
        if 'click' === true
            return.innerHTML("Best Answer!")
    })
}


// document.querySelector(all);  ?????
// Need:
// get request
// post request (url) (to change the database, and update the DOM)
// click fill-in first then send post update

