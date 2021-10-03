function showForgotCred(val){

    if(val == 'forgot'){
        document.getElementById('forgot-credentials').style.display = "block";
        document.getElementById('login-credentials').style.display = "none";
    }else{
        document.getElementById('forgot-credentials').style.display = "none";
        document.getElementById('login-credentials').style.display = "block";
    }

}