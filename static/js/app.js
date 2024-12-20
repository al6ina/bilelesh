function Nav() {
  var width = document.getElementById("mySidenav").style.width;
  if (width === "0px" || width == "") {
    document.getElementById("mySidenav").style.width = "100%";
    $('.animated-icon').toggleClass('open');
  }
  else {
    document.getElementById("mySidenav").style.width = "0px";
    $('.animated-icon').toggleClass('open');
  }
}

$('input[name="dates"]').daterangepicker();
