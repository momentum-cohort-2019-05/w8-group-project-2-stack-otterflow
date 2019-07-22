
// newComment.addEventListener('submit',function(e){
//     e.preventDefault();
//     $.ajax({
//         type: 'POST',
//         url: 'answer/add/',
//         data: {
//             'answer': newComment.val(),
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
//         },
//         dataType: 'json',
//         success: function(data){
//             $('.commentStyle').append(data)  
//         }
//     });
//     });
    
    
    // answerButton.addEventListener('submit', function(event) {
    //     event.preventDefault();
    //     console.log("log this") 
    //     $.ajax({
    //         type: "POST",
    //         url: 'answer/add/',
    //         data:{
    //             answer_body:q('#answer_body'),
    //             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
    //         },
    //         datatype:'json',
    //         success: function(data) {
    //           if (data['success'])
    //              alert("successfully added to favorites")
    //         }
    //     }); 
    // });
    

    // favButton2.addEventListener('submit', function(event) {
    //     event.preventDefault(); 
    //     $.ajax({
    //         type: "POST",
    //         url: 'favorite/add/',
    //         data:{
    //             'question.pk':question.pk,
    //             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
    //         },
    //         datatype:'json',
    //         success: function(data) {
    //           if (data['success'])
    //              alert("successfully added to favorites")
    //         }
    //     }); 
    // });
    // favButton2.addEventListener('click', function(e){
    //     e.preventDefault();
    //     console.log('This tracks a click')
    //     $.ajax({
    //         type:'POST',
    //         url: 'favorite/add/',
    //         data:{
    //             'question': $('#question').val,
    //             'favorited_by': $('#user').val,
    //             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    //         },
    //         success:function(){
    //             alert('Added to favorites!')
    //         },
    // })
    // })
    
    
    
    
    // let favButton = document.querySelector('.favorite')
    // favButton.addEventListener('click', function () {
    //     // if (favorited === false)
    //     question = favButton.value
    //     // console.log(question)
    //     const favoritesList = document.createElement('div')
    //     favoritesList.classList.add('favorites-list')
    //     favoritesList.append(question)
    //     console.log(favoritesList)
    //     // else if (favorited === true)
    //     //     question = favButton.value
    //     //     // console.log(question)
    //     //     const favoritesList = document.createElement('div')
    //     //     favoritesList.classList.add('favorites-list')
    //     //     favoritesList.remove(question)
    //     //     console.log(favoritesList)
    
    // })
    
    // button = document.querySelector('#button-id')
    // button.addEventListener('click', function () {
    //     button.classList.toggle('class1');
    //     button.classList.toggle('class2');
    // })
    
    
    
    
    // document.addEventListener('DOMContentLoaded', function () {
    
    // })