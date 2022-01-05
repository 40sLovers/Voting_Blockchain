//Selectors
var listaOp = [];

function stergeEl(value) {
  listaOp = listaOp.filter((element) => element != value);
  console.log(listaOp);
}

document.querySelector("#addBtn").onclick = function () {
  if (document.querySelector("#addoptiune").value.length == 0) {
    alert("Te rog introdu o optiune");
  } else {
    const ul = document.querySelector("ol");
    const item = document.querySelector("#addoptiune");
    listaOp.push(item.value);
    console.log(listaOp);
    const li = document.createElement("li");
    li.className = "item";
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
      alert("Ai adăugat numărul maxim de opțiuni!");
    }
  }
};
// document.querySelector('#addoptiune').addEventListener('keyup', (e) => {
//     if (e.keyCode === 13 ) {
//         console.log(addoptiune.value);
//         document.querySelector('#addBtn').click();
//     }
// });
