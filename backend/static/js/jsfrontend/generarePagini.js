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

// //const butonGenerarePagina = document.getElementById("createVote");
var listaOp = [];

function stergeEl(value) {
  listaOp = listaOp.filter((element) => element != value);
  console.log(listaOp);
}

function getParameterByName(name, url = window.location.href) {
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
    results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return "";
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}

document.querySelector("#addBtn").onclick = function () {
  if (document.querySelector("#addoptiune").value.length == 0) {
    alert("Te rog introdu o optiune");
  } else {
    const ul = document.querySelector("ol");
    const item = document.querySelector("#addoptiune");
    if (listaOp.includes(item.value)) {
      alert("Optiunea a fost deja introdusa!");
    } else {
      listaOp.push(item.value);
      console.log(listaOp);
      const li = document.createElement("li");
      li.className = "item_lista";
      li.textContent = item.value;
      ul.appendChild(li);
      item.value = "";
      const items = document.querySelectorAll("li");
      for (let li of items) {
        li.addEventListener("click", () => {
          stergeEl(li.textContent);
          li.remove();
        });
      }
      if (items.length > 50) {
        alert("Ai ad??ugat num??rul maxim de op??iuni!");
      }
    }
    document.getElementById("addoptiune").value = "";
  }
};

document.querySelector("#createVote").addEventListener("click", function () {
  //let cod = crypto.randomUUID();
  const numeVot = document.getElementById("titluPoll").value;
  if (
    typeof numeVot != "string" ||
    !numeVot ||
    numeVot.trim().length == 0 ||
    listaOp.length <= 1
  ) {
    alert("Completeaza formularul!");
    return;
  }
  postData(
    window.location.protocol + "//" + window.location.host + "/newPoll",
    {
      numePoll: numeVot,
      listaOp: listaOp,
    }
  ).then((data) => {
    console.log(data);
    if (data.succes == true) {
      window.location.href = "/rezultate?cod=" + data.cod;
    } else {
      alert("Completeaza formularul!");
    }
    document.getElementById("titluPoll").value = "";
  });
});
