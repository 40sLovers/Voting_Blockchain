//import {SHA256} from sha256.js

const validateEmail = (email) => {
  return true; //de sters
  return String(email)
    .toLowerCase()
    .match(/[a-zA-Z]*.[a-zA-Z]*[0-9]*@e-uvt.ro/);
};

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

const butonInregistrare = document.getElementById("ButonInregistrare");

butonInregistrare.addEventListener("click", function () {
  if (
    window.location.href ==
    window.location.protocol + "//" + window.location.host + "/inregistrare"
  ) {
    if (validateEmail(document.getElementById("ad").value) == false) {
      alert("Adresa de email este invalidă!");
      document.getElementById("ad").value = "";
    } else {
      var adresa = document.getElementById("ad").value;
      var numarMatricol = document.getElementById("nrm").value;
      var cuvantCheie = document.getElementById("pass").value;
      const concatenare = adresa.concat(numarMatricol, cuvantCheie);
      console.log(concatenare);
      var criptare = SHA256(concatenare);
      console.log(criptare);
      postData(
        window.location.protocol +
          "//" +
          window.location.host +
          "/inregistrare",
        {
          adresa: adresa,
          numarMatricol: numarMatricol,
          cuvantCheie: cuvantCheie,
          criptare: criptare,
        }
      ).then((data) => {
        console.log(data);
        if (data == "ok") {
          window.location.href =
            window.location.protocol +
            "//" +
            window.location.host +
            "/confirmare";
        }
      });
    }
  } else window.location.href = window.location.protocol + "//" + window.location.host + "/inregistrare";
});
