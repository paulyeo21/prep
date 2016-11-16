var numbers = [];

function getNumber() {
  $.ajax({
    method: "GET",
    dataType: "json",
    url: "http://my-sensor-api.herokuapp.com/meter",
    success: function(data) {
      var bar = document.createElement("div");
      bar.style.height = data.value;
      bar.style.width = "20px";
      bar.style.display = "inline-block";
      bar.style.backgroundColor = "black";
      numbers.push(bar);

      $("#numbers").append(bar);
      if (numbers.length > 20) {
        var deleted_bar = numbers.shift();
        deleted_bar.remove();
      }

      // console.log(numbers.length);
      setTimeout(getNumber, 1000);
    },
    error: function() {
      console.log("error");
    }
  })
}

setTimeout(getNumber, 1000);
