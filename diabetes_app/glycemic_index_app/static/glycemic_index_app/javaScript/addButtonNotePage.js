function addFn() {
    const divEle = document.getElementById("note-GI-list");
    const wrapper = document.createElement("div");
    wrapper.classList.add("note-GI-item");
    const iFeild = document.createElement("input");
    const button = document.createElement("button");
    iFeild.setAttribute("type", "text");
    iFeild.setAttribute("placeholder", "Число от 1 до 100");
    iFeild.classList.add("note-GI-item-el");

    button.classList.add("minus-button");
    button.setAttribute("onclick", "delNode(this)");

    wrapper.appendChild(iFeild);
    wrapper.appendChild(button);
    divEle.appendChild(wrapper);
}

function delNode(el) { el.parentNode.remove() }