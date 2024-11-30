<?php
session_start();

// Load database configuration from myproperties.ini
$config = parse_ini_file("myproperties.ini", true)['DB'] ?? null;
if (!$config || !isset($config['DBHOST'], $config['DBUSER'], $config['DBPASS'], $config['DBNAME'])) {
    die("Error: Unable to load database configuration.");
}

// Establish database connection
$mysqli = new mysqli($config['DBHOST'], $config['DBUSER'], $config['DBPASS'], $config['DBNAME']);
if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

// Handle login form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve user input
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';

    // Prepare statement to fetch password securely
    $stmt = $mysqli->prepare("SELECT Password FROM CUSTOMER WHERE Email = ?");
    if ($stmt) {
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $stmt->store_result();

        // Check if the customer exists
        if ($stmt->num_rows === 1) {
            $stmt->bind_result($storedPassword);
            $stmt->fetch();

            // Compare passwords (use password_hash/password_verify in production)
            if ($password === $storedPassword) {
                // Authentication successful
                $_SESSION['loggedin'] = true;
                $_SESSION['email'] = $email;

                // Redirect to index.php
                header("Location: index.php");
                exit;
            } else {
                $_SESSION['error'] = "Invalid email or password.";
            }
        } else {
            $_SESSION['error'] = "Invalid email or password.";
        }
        $stmt->close();
    } else {
        die("Error preparing database statement.");
    }
}

// Close database connection
$mysqli->close();
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: #f0f8ff;
            font-family: Arial, sans-serif;
        }

        form {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            width: 100%;
            max-width: 400px;
            text-align: center;
        }

        form h2 {
            margin-bottom: 20px;
        }

        input[type="email"],
        input[type="password"] {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        input[type="submit"] {
            padding: 10px 20px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        input[type="submit"]:hover {
            background: #0056b3;
        }

        p {
            color: red;
        }
    </style>
</head>

<body>
    <form action="login.php" method="post">
        <img src="assets/chase.svg" width="100" alt="Chase logo" />
        <br>
        <br>
        <label for="email"><b>EMAIL:</b></label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="password"><b>PASSWORD:</b></label><br>
        <input type="password" id="password" name="password" required><br><br>

        <input type="submit" value="LOGIN">
    </form>

    <?php
    // Display error message if there is one
    if (isset($_SESSION['error'])) {
        echo "<p>" . htmlspecialchars($_SESSION['error']) . "</p>";
        unset($_SESSION['error']); // Clear the error message
    }
    ?>
</body>

</html>
