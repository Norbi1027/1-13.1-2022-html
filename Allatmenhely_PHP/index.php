<?php
session_start();
echo 'ok';
require_once './classes/Database.php';
//-- Példányosítás
$db = new Database("localhost", "root", "", "menhely");

if (!isset($_SESSION['login'])) {
    $_SESSION['login'] = false;
}
$_SESSION['login'] = false;
if (filter_input(INPUT_POST,
                'belepesiAdatok',
                FILTER_VALIDATE_BOOLEAN,
                FILTER_NULL_ON_FAILURE)) {
    //-- A kapott adatok feldolgozása    
    $username = htmlspecialchars(filter_input(INPUT_POST, 'username'));
    $password = htmlspecialchars(filter_input(INPUT_POST, 'InputPassword'));
    $db->login($username, $password);

    if ($username == "Lajos" && $password == "Lajos") {
        $_SESSION['login'] = true;
        $_SESSION['username'] = 'Lajos';
        $_SESSION['password'] = 'Lajos';
    }
}
require_once './layout/head.php';
?>
<body>
    <?php
    require_once './layout/header.php';
    require_once './layout/menu.php';
    require_once './tartalom.php';
    require_once './layout/footer.php';
    ?>
    <script src="./bootstrap-5.2.3-dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
