async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    mode: "cors", // no-cors, *cors, same-origin
    cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
    credentials: "same-origin", // include, *same-origin, omit
    headers: {
      "Content-Type": "application/json",
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: "follow", // manual, *follow, error
    referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

const vote = document.getElementById("Voteaza");
var URL = window.location.href;
let poz = URL.split("=");
const cod = poz[1];
console.log(cod);

vote.addEventListener("click", function () {
  var votOptions = document.getElementsByName("optiuneVot");
  var selectedOption;
  for (let option = 0; option < votOptions.length; option++) {
    if (votOptions[option].checked)
      selectedOption = document.getElementsByName("optiuneVot")[option].value;
  }
  postData(window.location.protocol + "//" + window.location.host + "/Votare", {
    selectedOption: selectedOption,
    cod: cod,
  }).then((data) => {
    console.log(data);
    if (data.succes == true) {
      window.location.href = "/rezultate?cod=" + data.cod;
      console.log("ai votat cu secces");
    } else {
      alert("Mai incerca o data!");
    }
  });
});

function getCod() {
  var URL = window.location.href;
  console.log(URL);
}
