const billDivideForm = document.getElementById('bill-divider-form');

billDivideForm.addEventListener('submit', billDividerHandler);

function billDividerHandler(event) {
    event.preventDefault();
    const inputs = getInputs();
    console.log(inputs);
}

function getInputs() {
    let subTotal = document.getElementById('subtotal').value;
    let tipPercent = document.getElementById('tip').value;
    let numPeople = document.getElementById('no-of-person').value;
    // console.log(subTotal, tipPercent, numPeople);
    return { subTotal, tipPercent, numPeople };


}


