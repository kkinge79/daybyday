const cards = document.querySelectorAll('#card')


function ratingBackgroundColor() {
  for(i=0; i < cards.length; i++){
  let rating = cards[i].childNodes[3].childNodes[0].data
  console.log(rating)
  if (rating === "1" || rating === "2") {
    cards[i].style.backgroundColor = "#FB4B68";
  } else if (rating === "3" || rating === "4" || rating === "5"){
    cards[i].style.backgroundColor = "#FFE770";
  } else if (rating === "6" || rating === "7"){
    cards[i].style.backgroundColor= "#95D5B2";
  }
} return cards[i]
}
ratingBackgroundColor()