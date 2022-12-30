// Get client's csrf_token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// function to increase likes when like button is clicked
async function increaseLikes()
{
    let count = 0;

     // Send a GET request to the API
    await fetch('/likes')
    // Put response into json form
    .then(response => response.json())
    .then(data => {
        // Update value in HTML page
        count = data+1;
        document.querySelector('#likes').innerHTML = count;
    });

     var csrf_token = getCookie('csrftoken');
    await fetch('/likes', { method: "POST", headers: {'X-CSRFToken': csrf_token}, body: JSON.stringify({
        likes: count
     })
    })
    .then(response => response.json())

    return false;

}

// function to increase dislikes when like button is clicked
async function increaseDislikes()
{
     let count = 0;

     // Send a GET request to the API
    await fetch('/dislikes')
    .then(response => response.json())
    .then(data => {
        // Update value in HTML page
        count = data+1;
        document.querySelector('#dislikes').innerHTML = count;
    });

    var csrf_token = getCookie('csrftoken');
    await fetch('/dislikes', { method: "POST", headers: {'X-CSRFToken': csrf_token}, body: JSON.stringify({
        dislikes: count
     })
    })
    .then(response => response.json())

    return false;
}

// Render JavaScript file only when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#like-btn').onclick = increaseLikes;
    document.querySelector('#dislike-btn').onclick = increaseDislikes;

});