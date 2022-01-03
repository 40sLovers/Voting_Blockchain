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

const butonGenerarePagina = document.getElementById("createVote");

butonGenerarePagina.addEventListener("click", function () {
  let cod = (Math.random() + 1).toString(36).substring(7);
  postData(
    window.location.protocol + "//" + window.location.host + "/newPoll",
    {
      cod: cod,
    }
  ).then((data) => {
    console.log(data);
    if (data == "ok") alert(cod);
  });
});
