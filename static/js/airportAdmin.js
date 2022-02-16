function addAirport() {
    var name = document.getElementById("name").value;
    var shorten = document.getElementById("shorten").value;
    var address = document.getElementById("address").value;
    var btnDelete = document.createElement('button');
    btnDelete.textContent = 'Dzēst';

    var table = document.getElementsByTagName("table")[0];

    var newRow = table.insertRow(1);

    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);
    

    cell1.innerHTML = name;
    cell2.innerHTML = shorten;
    cell3.innerHTML = address;
    cell4.appendChild(btnDelete);

    btnDelete.addEventListener("click", function rowDelete(){
        var row = btnDelete.parentNode.parentNode;
        row.parentNode.removeChild(row);
    });

}