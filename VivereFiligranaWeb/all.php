<?php
    $tipo=$_POST['tipo_filigrana'];
    $opacity=$_POST['opacita'];
    $directory="documenti/";
    $extension=explode(".",$_FILES['file']['name']);
    $extension=$extension[1];
    $nome=$directory.str_replace(" ", "_", $_FILES['file']['name']);
    if(!move_uploaded_file($_FILES['file']['tmp_name'], $nome)){
        echo "NONE";
    }
    //Converto e Cancello Originale
    shell_exec('sudo libreoffice --headless --convert-to pdf --outdir documenti '.$nome);
    shell_exec('rm '.$nome);
    //Filigrano
    $nome=str_replace(".".$extension, ".pdf", $nome);
    shell_exec("python3 fil.py $tipo $opacity '$nome'");
    shell_exec('rm '.$nome);
    $nome=str_replace(".pdf", "_f.pdf", str_replace("/", "%20", $nome));
    header("location: download.php?nome=$nome")
?>