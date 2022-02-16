function addFlight() {
    var date = document.getElementById("date").value;
    var time = document.getElementById("time").value;
    var number = document.getElementById("number").value;
    var from = document.getElementById("from").value;
    var to = document.getElementById("to").value;
    var airport = document.getElementById("airport").value;
    var price = document.getElementById("price").value;
    var container = document.getElementById("buttonContainer");
    var btn = document.createElement('button');
    btn.textContent = 'Rezervēt';
    var btnDelete = document.createElement('button');
    btnDelete.textContent = 'Dzēst';




    var table = document.getElementsByTagName("table")[0];

    var newRow = table.insertRow(1);

    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);
    var cell5 = newRow.insertCell(4);
    var cell6 = newRow.insertCell(5);
    var cell7 = newRow.insertCell(6);
    var cell8 = newRow.insertCell(7);
    var cell9 = newRow.insertCell(8);

    cell1.innerHTML = date;
    cell2.innerHTML = time;
    cell3.innerHTML = number;
    cell4.innerHTML = from;
    cell5.innerHTML = to;
    cell6.innerHTML = airport;
    cell7.innerHTML = price;
    cell8.appendChild(btn);
    cell9.appendChild(btnDelete);

    btn.addEventListener("click", function(){
        location = "/rezervacija"; 
      });

    btnDelete.addEventListener("click", function rowDelete(){
        var row = btnDelete.parentNode.parentNode;
        row.parentNode.removeChild(row);
    });
}



