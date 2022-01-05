//Selectors
var listaOp = [];

function removeItem(value, htmlItem) {
  htmlItem.parentNode.remove();
  listaOp = listaOp.filter((element) => element != value);
  console.log(listaOp);
}

function addOptiune() {
  if (document.querySelector("#addoptiune").value.length == 0) {
    alert("Te rog introdu o optiune");
  } else {
    document.querySelector(".lista").innerHTML += `
           <li>
              <span id="listaname">
                  ${document.querySelector("#addoptiune").value}
              </span>  
              <button class="delete" onclick="removeItem(${
                document.querySelector("#addoptiune").value
              }, this)">
                   <i>Sterge</i>
              </button>
            </li>
        `;
    listaOp.push(document.querySelector("#addoptiune").value);
    var curentopt = document.querySelectorAll(".delete");
    if (curentopt.length > 50) {
      alert("Ai adăugat numărul maxim de opțiuni!");
    }
  }
}

document.querySelector("#addBtn").onclick = function () {
  addOptiune();
};

const addVar = document.getElementById("addoptiune");

document.querySelector("#addoptiune").addEventListener("keyup", (e) => {
  if (e.keyCode === 13) {
    addOptiune();
  }
});
