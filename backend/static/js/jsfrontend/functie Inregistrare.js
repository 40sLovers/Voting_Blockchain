const buton1 = document.getElementById("ButonInregistrare");
console.log(buton1);

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

buton1.addEventListener("click", function () {
  //add hash
  const adresa = document.getElementById("ad");
  const numarMatricol = document.getElementById("nrm");
  const cuvantCheie = document.getElementById("pass");
  const cryptare = concat(adresa, numarMatricol, cuvantCheie);
  console.log(cryptare);
  console.log(adresa, numarMatricol, cuvantCheie);
  postData("http://127.0.0.1:5000/login", {
    adresa: adresa,
    numarMatricol: numarMatricol,
    cuvantCheie: cuvantCheie,
  }).then((data) => {
    console.log(data);
  });
});
