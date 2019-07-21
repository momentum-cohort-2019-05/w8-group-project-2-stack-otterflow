favButton = document.querySelector('.favorite')
favButton.addEventListener('click', function () {
    // if (favorited === false)
    question = favButton.value
    // console.log(question)
    const favoritesList = document.createElement('div')
    favoritesList.classList.add('favorites-list')
    favoritesList.append(question)
    console.log(favoritesList)
    // else if (favorited === true)
    //     question = favButton.value
    //     // console.log(question)
    //     const favoritesList = document.createElement('div')
    //     favoritesList.classList.add('favorites-list')
    //     favoritesList.remove(question)
    //     console.log(favoritesList)

})

button = document.querySelector('#button-id')
button.addEventListener('click', function () {
    button.classList.toggle('class1');
    button.classList.toggle('class2');
})


// document.addEventListener('DOMContentLoaded', function () {

// })