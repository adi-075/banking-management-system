<?php
session_start();

// Ensure the user is logged in
if (!isset($_SESSION['loggedin']) || !$_SESSION['loggedin']) {
    header("Location: login.php");
    exit;
}

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

// Fetch the logged-in user's email
$email = $_SESSION['email'] ?? '';

// Prepare and execute a query to fetch account details
$query = "
    SELECT 
        a.AccountNumber, 
        a.AccountType, 
        ab.Balance 
    FROM 
        account a 
    JOIN 
        account_balance ab ON a.AccountID = ab.AccountID 
    JOIN 
        customer c ON a.CustomerID = c.CustomerID 
    WHERE 
        c.Email = ?
";
$stmt = $mysqli->prepare($query);
if ($stmt) {
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();

    // Fetch all account details into an array
    $accounts = $result->fetch_all(MYSQLI_ASSOC);
    $stmt->close();
} else {
    die("Error preparing database statement.");
}

// Close database connection
$mysqli->close();
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Account Information</title>
    <link rel="stylesheet" href="styles/styles.css">
  
</head>

<body>
    <nav class="navbar">
        <!-- Chase Brand -->
        <a href="index.php" class="navbar-brand" style="margin-left: 20px">
            <img src="assets/chase.svg" width="100" alt="Chase logo" />
        </a>
        <!-- Links -->
        <ul class="nav-links">
            <li class="nav-item">
                <a href="services.php" class="">Services</a>
            </li>
            <li class="nav-item">
                <a href="" class="">Transfer Funds</a>
            </li>
            <li class="nav-item">
                <a href="logout.php" class="">Logout</a>
            </li>
        </ul>
    </nav>
    <div class="content">
        <h2>Account Overview</h2>
        <div class="acc-info">
            <?php
            if (!empty($accounts)) {
                foreach ($accounts as $account) {
                    echo "<div class='account-item'>";
                    echo "<h2>Chase " . htmlspecialchars($account['AccountType']  . ' - ' . substr($account['AccountNumber'], -4)) . "</h2>";
                    
                    echo "<h3 class='balance'>$" . number_format($account['Balance'], 2) . "</h3>";
                    echo "<p class='balance'><strong>Available Balance</strong></p>";
                    echo "</div>";
                }
            } else {
                echo "<p>No accounts found for this user.</p>";
            }
            ?>
        </div>

        <!-- TODO: Recent Transactions  -->
         
         
    </div>
</body>

</html>
  <style>
        .content {
            margin-left: 36px;
            color: #111;
        }
        .account-item {
            border: 1px solid #ccc;
            padding: 10px;
            margin: 10px 35px;
            background: #f9f9f9;
            
        }
        .account-item h2 {
            color: #0846A8;
        }

        .balance {
            margin-left: 100px;
        }
        
        .account-item p {
            margin: 5px 0;
        }
    </style>