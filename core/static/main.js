function q (sel) {
    return document.querySelector(sel)
}

function qs (sel) {
    return document.querySelectorAll(sel)
}

// Best Answer Button

let buttons = qs(".bestAnswerButton")

for (let button of buttons) {
    button.addEventListener('click', function() {
        console.log("tracking this?")
        const checkmarks = qs(".checkmark")  
        for (let checkmark of checkmarks) {
            checkmark.innerHTML = "✔"
        }
        console.log(checkmark)
    }
 )}