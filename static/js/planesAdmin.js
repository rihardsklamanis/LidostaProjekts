function addPlane() {
    var name = document.getElementById("name").value;
    var places = document.getElementById("places").value;
    var year = document.getElementById("year").value;
    var airport = document.getElementById("airport").value;
    var btnDelete = document.createElement('button');
    btnDelete.textContent = 'Dzēst';

    var table = document.getElementsByTagName("table")[0];

    var newRow = table.insertRow(1);

    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);
    var cell5 = newRow.insertCell(4);

    cell1.innerHTML = name;
    cell2.innerHTML = places;
    cell3.innerHTML = year;
    cell4.innerHTML = airport;
    cell5.appendChild(btnDelete);

    btnDelete.addEventListener("click", function rowDelete(){
        var row = btnDelete.parentNode.parentNode;
        row.parentNode.removeChild(row);
    });


}