<?php
    $tipo=$_POST['tipo_filigrana'];
    $opacity=$_POST['opacita'];
    $directory="documenti/";
    $extension=".pdf";
    $nome=$directory.str_replace(" ", "_", $_FILES['file']['name']);
    if(!move_uploaded_file($_FILES['file']['tmp_name'], $nome)){
        echo "NONE";
    }
    echo exec("python3 fil.py $tipo $opacity '$nome'");
    $nome=str_replace(".pdf", "_f.pdf", str_replace("/", "%20", $nome));
    header("location: download.php?nome=$nome")
?>