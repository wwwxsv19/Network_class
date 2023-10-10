var led = document.querySelector("#led");
var on = document.querySelector("#on");
var off = document.querySelector("#off");

on.addEventListener("click", function () {
  $.ajax({
    type: "GET",
    url: "/on",
  })
    .done(function (result) {
      led.src = "static/on.png"
    })
    .fail(function (result) {
      alert(result)
    })
})

off.addEventListener("click", function() {
  $.ajax({
    type: "GET",
    url: "/off",
  })
    .done(function (result) {
      led.src = "static/off.png";
    })
    .fail(function (result) {
      alert(result)
    })
});
