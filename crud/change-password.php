<?php
session_start();
$servername = "localhost"; // Az adatbázis szerver címe (általában localhost)
$username = "root"; // Az adatbázis felhasználóneve
$password = ""; // Az adatbázis jelszava
$dbname = "php-crud"; // Az adatbázis neve

// Adatbázis kapcsolat létrehozása
$conn = new mysqli($servername, $username, $password, $dbname);

// Kapcsolat ellenőrzése
if ($conn->connect_error) {
    die("Kapcsolódási hiba: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $bejelentkezve = true; // Példa: bejelentkezett felhasználó

    if ($bejelentkezve) {
        $regi_jelszo = $_POST["regi_jelszo"];
        $uj_jelszo = $_POST["uj_jelszo"];
        $uj_jelszo_megerosit = $_POST["uj_jelszo_megerosit"];

        // Ellenőrizzük, hogy a régi jelszó helyes-e
        $felhasznalonev = $_SESSION['user_name']; // Példa: bejelentkezett felhasználó neve

        $sql = "SELECT password FROM users WHERE user_name = '$felhasznalonev'";
        $result = $conn->query($sql);

        if ($result->num_rows == 1) {
            $row = $result->fetch_assoc();
            $helyes_regi_jelszo = $row["password"];

            if ($regi_jelszo == $helyes_regi_jelszo) {
                if ($uj_jelszo == $uj_jelszo_megerosit) {
                    // Új jelszó mentése a táblába
                  //$hashed_uj_jelszo = password_hash($uj_jelszo,PASSWORD_DEFAULT);
                    //$sql = "UPDATE users SET password = '$hashed_uj_jelszo' WHERE user_name = '$felhasznalonev'";
                    $sql = "UPDATE users SET password = '$uj_jelszo' WHERE user_name = '$felhasznalonev'";

                    if ($conn->query($sql) === TRUE) {
                        echo "Jelszóváltoztatás sikeres!";
                    } else {
                        echo "Hiba történt a jelszóváltoztatás során: " . $conn->error;
                    }
                } else {
                    echo "Az új jelszavak nem egyeznek meg.";
                }
            } else {
                echo "Helytelen régi jelszó.";
            }
        } else {
            echo "Nincs ilyen felhasználó.";
        }
    } else {
        echo "Nincs bejelentkezve. Kérjük, először jelentkezzen be.";
    }
}

// Adatbázis kapcsolat bezárása
$conn->close();
?>
<!DOCTYPE html>
<html>
<head>
    <title>Jelszóváltoztatás</title>
</head>
<body>
    <h2>Jelszóváltoztatás</h2>
    <form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
        Régi jelszó: <input type="password" name="regi_jelszo" required><br><br>
        Új jelszó: <input type="password" name="uj_jelszo" required><br><br>
        Új jelszó megerősítése: <input type="password" name="uj_jelszo_megerosit" required><br><br>
        <input type="submit" value="Jelszóváltoztatás">
    </form>
</body>
</html>
