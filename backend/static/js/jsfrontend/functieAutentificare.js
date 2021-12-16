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

const ButonAutentificare = document.getElementById("ButonAutentificare");

ButonAutentificare.addEventListener("click", function () {
  var adresa = document.getElementById("ad").value;
  var numarMatricol = document.getElementById("nrm").value;
  var cuvantCheie = document.getElementById("pass").value;
  const concatenare = adresa.concat(numarMatricol, cuvantCheie);
  var criptare = CryptoJS.SHA256(concatenare);
  criptare = criptare.toString();
  postData(window.location.protocol + "//" + window.location.host + "/", {
    criptare: criptare,
  }).then((data) => {
    console.log(data);
    if (data == "ok") {
      window.location.href =
        window.location.protocol + "//" + window.location.host + "/newPoll";
    }
    if (data == "notok") {
      alert("Datele introduse sunt gresite!");
      window.location.href =
        window.location.protocol + "//" + window.location.host + "/";
    }
  });
});
