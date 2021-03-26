<?php
    $directory="documenti/";
    $extension=explode(".",$_FILES['file']['name']);
    $extension=$extension[1];
    $nome=$directory.str_replace(" ", "_", $_FILES['file']['name']);
    if(!move_uploaded_file($_FILES['file']['tmp_name'], $nome)){
        echo "NONE";
    }
    shell_exec('sudo libreoffice --headless --convert-to pdf --outdir documenti '.$nome);
    shell_exec('rm '.$nome);
    $nome=str_replace(".".$extension, ".pdf", str_replace("/", "%20", $nome));
    header("location: download.php?nome=$nome")
?>