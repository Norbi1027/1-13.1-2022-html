<?php
if (filter_input(INPUT_POST, "regisztraciosAdatok", FILTER_VALIDATE_BOOLEAN, FILTER_NULL_ON_FAILURE)) {
    $pass1= filter_input(INPUT_POST, "InputPassword");
    $pass2= filter_input(INPUT_POST, "InputPassword2");
    $name= htmlspecialchars(filter_input(INPUT_POST, "username"));
if ($pass1 != $pass2) {
    echo '<p>Nem egyeznek a jelszavak</p>';
}
 else {
     $db->register($name,$pass1);
}
}
?>
<div class="container">
    <form action="#" method="post">
        <div class="mb-3">
            <label for="username" class="form-label">Felhasználó név</label>
            <input type="text" class="form-control" id="username" name="username" aria-describedby="emailHelp">
            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
        </div>
        <div class="mb-3">
            <label for="InputPassword" class="form-label">Jelszó</label>
            <input type="password" class="form-control" id="InputPassword" name="InputPassword">
        </div>
        <div class="mb-3">
            <label for="InputPassword2" class="form-label">Jelszó</label>
            <input type="password" class="form-control" id="InputPassword2" name="InputPassword2">
        </div>

        <button type="submit" class="btn btn-primary" name="regisztraciosAdatok" value="true">Regisztáció</button>
    </form>
</div>