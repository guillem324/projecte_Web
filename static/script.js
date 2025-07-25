function login () {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let status = 400;
    fetch("/login?username="+username+"&password="+password,{method:"post"}).then(function(result){
        console.log(result.status);
        status = result.status;
        if (status == 400 ){
            let popup = document.getElementById("popup");
            popup.style.display = "flex";
        }
        else 
            {
                window.location.href="/contingut";
            }
    })
    console.log(status);


}
function closePopup( ){
    
            let popup = document.getElementById("popup");
        popup.style.display = "none";
}