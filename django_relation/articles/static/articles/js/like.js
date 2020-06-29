const likeButton = document.querySelectorAll('.like-button');
likeButton.forEach(button => {
    button.addEventListener('click', function(event) {
        console.log(event.target)
        const articleId = event.target.dataset.id;
        const likecount = document.querySelector(`.like-count-${articleId}`);
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        axios.post(`/articles/${articleId}/like/`)
        .then(response => {
            likecount.innerText = response.data.count
            
            if(response.data.liked) {
                event.target.className = "fas fa-heart fa-md like-button";
                event.target.style.color = "crimson";
            } else {
                event.target.className = "far fa-heart fa-md like-button";
                event.target.style.color = "black";
            }
        })
    })
    // console.log(button);
})