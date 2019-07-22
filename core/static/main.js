function q (sel) {
    return document.querySelector(sel)
}

let favButton2 = q('.new_favorite')
let answerButton = q('#answer_form')
let newComment = q('#questionAnswerForm')

favButton2.addEventListener('click', function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url: 'favorite/',
        data:{
            // 'question': $('.question').val,
            // 'favorited_by': $('.user_class').val,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            alert('Added to favorites!')
        },
})
})

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

