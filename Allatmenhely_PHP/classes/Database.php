<?php

class Database {

    private $db = null;

    public function __construct($host,  $username, $pass,$db) {
        $this->db = new mysqli($host,$username, $pass, $db);
    }

    public function login($name, $pass) {
         $stmt = $this->db->prepare('SELECT * FROM users WHERE name LIKE ?;');
         $stmt->bind_param("s",$name);
        if ($stmt->execute()) {
            $result = $stmt->get_result();
            $row = $result->fetch_assoc();
            if(password_verify($pass, $row['password'])){
                $_SESSION['username']=$row['name'];
                $_SESSION['login']=true;
            }
            else{
                $_SESSION['username']='';
                $_SESSION['login']=false;
            }
           
            // Free result set
            $result->free_result();
        }
        return false;
    }
    public function register($name, $pass) {
        $stmt=$this->db->prepare("INSERT INTO `users` (`name`, `password`) VALUES(?,?);");
        $stmt->bind_param("sb",$name,password_hash($pass,PASSWORD_BCRYPT));
        if ($stmt->execute()) {
           $_SESSION['login'] = true;
           header("Location:index.php");
        }
    }
}
