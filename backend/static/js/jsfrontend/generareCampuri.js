const addInput = document.querySelector("x");
const addBtn = document.querySelector("y");
const divList = document.querySelector("listHolder");

addBtn.addEventListener("click", () => {
  if (addInput.value === "") {
    alert("Casuta este goala!");
  } else {
    const ul = divList.querySelector("ul");
    const li = document.createElement("li");
    li.innerHTML = addInput.value;
    addInput.value = " ";
    ul.appendChild(li);
  }
});
