<?php
if ($_SESSION['login']) {
    echo $_SESSION['username'].' belépett ';
} else {
    if (filter_input(INPUT_GET, "menu")=="regisztracio") {
        require_once './pages/regisztracio.php';
    }else{
            require_once './pages/login.php';
    }
}
