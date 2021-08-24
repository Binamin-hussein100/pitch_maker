let dislike_btn = document.getElementById("dislike_vote")
dis_like = 7

function dislike(){
    dis_like += 1
    dislike_btn.textContent = dis_like
}