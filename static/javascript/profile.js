let showPostsButton, showImagesButton, profileImages, profilePosts;

window.onload = function processPageLoad()
{
    showImagesButton = document.getElementById("showImagesButton");
    showImagesButton.addEventListener("click", processShowImagesButtonClick);
    showPostsButton = document.getElementById("showPostsButton");
    showPostsButton.addEventListener("click", processShowPostsButtonClick);
    profileImages = document.getElementById("profileImages");
    profilePosts = document.getElementById("profilePosts");
}

function processShowImagesButtonClick()
{
    profileImages.style.visibility = "visible";
    profilePosts.style.visibility = "hidden";
    profileImages.style.order = "1";
    profilePosts.style.order = "2";
}

function processShowPostsButtonClick()
{
    profileImages.style.visibility = "hidden";
    profilePosts.style.visibility = "visible";
    profileImages.style.order = "2";
    profilePosts.style.order = "1";
}