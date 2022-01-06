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

const conectareVotare = document.getElementById("connect");

conectareVotare.addEventListener("click", function () {
  var CodConectare = document.getElementById("conectare").value;
  postData(
    window.location.protocol +
      "//" +
      window.location.host +
      "/newPollVerificare",
    {
      CodConectare: CodConectare,
    }
  ).then((data) => {
    console.log(data);
    if (data == "ok") {
      window.location.href =
        window.location.protocol + "//" + window.location.host + "/Votare";
    } else {
      alert("Codul introdus este gresit!");
    }
    document.getElementById("conectare").value = "";
  });
});
