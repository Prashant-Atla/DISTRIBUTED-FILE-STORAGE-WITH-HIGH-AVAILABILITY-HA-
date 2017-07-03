<?php
// PHP code starts here ....................................................................................................         

                                                                           // Connect to the database
$con=mysql_connect("localhost","project","password");
$db=mysql_select_db("storage",$con);
   // Query for a list of all existing files
$q1 = "select  name, mime, size, created from hello";
$result = mysql_query($q1);
  // Check if it was successfull
if($result) {
   
     {
        
        echo '<table width="100%">
         <tr>
                    
                    <td><b>Name</b></td>
                    <td><b>Mime</b></td>
                    <td><b>Size (bytes)</b></td>
                    <td><b>Created</b></td>
                    <td><b>&nbsp;</b></td>
                </tr>';
                 // Print each file
        while($row = mysql_fetch_assoc($result)) {
            echo "
                <tr>
                 <td>{$row['name']}</td>
                    <td>{$row['mime']}</td>
                    <td>{$row['size']}</td>
                    <td>{$row['created']}</td>
                    <td><a href='http://localhost/storage/download.php?id={$row['id']}'>Download</a></td>
                </tr>";
        }
  // Close table
        echo '</table>';
    }
 // Free the result
    mysql_free();
}
// if there are errors in query
else
{
    echo 'Error! SQL query failed:';
    echo "<pre>{$mysql_error}</pre>";
}
 // Close the mysql connection
mysql_close();

// PHP code ends here ..............................................................................................................

?>