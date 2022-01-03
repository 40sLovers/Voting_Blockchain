//Selectors
function addOptiune() {
  if (document.querySelector("#addoptiune").value.length == 0) {
    alert("Te rog introdu o optiune");
  } else {
    document.querySelector(".lista").innerHTML += `
           <li>
              <span id="listaname">
                  ${document.querySelector("#addoptiune").value}
              </span>  
              <button class="delete">
                   <i>Sterge</i>
              </button>
            </li>
        `;
    var curentopt = document.querySelectorAll(".delete");
    for (var i = 0; i < curentopt.length; i++) {
      curentopt[i].onclick = function () {
        this.parentNode.remove();
      };
    }
    if (curentopt.length > 50) {
      alert("Ai adăugat numărul maxim de opțiuni!");
    }
    document.querySelector("#addoptiune").value = "";
  }
}

document.querySelector("#addBtn").onclick = function () {
  addOptiune();
};

const addVar = document.getElementById("addoptiune");

addVar.addEventListener("keypress", (event) => {
  if (event.keyCode === 13) {
    addOptiune();
    console.log("aaa");
  }
});
