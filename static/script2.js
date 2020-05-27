function myFunction() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("selectField");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByClassName("filtering");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[3];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}