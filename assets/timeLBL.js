function clock() {
    var month = ["January","February","March","April","May","June","July","August","September","October","November","December"];
    var currentdate = new Date(); 
    var datetime = "" + currentdate.getDate() + " "
            + month[currentdate.getMonth()]  + " " 
            + currentdate.getFullYear() + "  "  
            + currentdate.getHours() + ":"  
            + currentdate.getMinutes() + ":" 
            + currentdate.getSeconds();
    document.getElementById("clock").innerHTML = datetime;
}

setInterval('clock()', 1000);