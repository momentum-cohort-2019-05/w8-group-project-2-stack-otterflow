(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
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
},{}]},{},[1]);
