<!DOCTYPE html>
<html lang="en">
<head>
      <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <link href="/css/bootstrap.min.css" rel="stylesheet">
    <script src="/js/jquery.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    <link  href="/css/sidebar.css" rel = "stylesheet">


    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
    </style>

    <!-- Le styles -->

</head>
<body>

    <div id="wrapper">

        <!-- Sidebar -->
        <div id="sidebar-wrapper">
            <ul class="sidebar-nav">
                <li><a href="#">BLEH1</a></li>
                <li><a href="#">BLEH2</a></li>
                <li><a href="#">BLEH3</a></li>
            </ul>
        </div>

        <!-- Page content -->
        <div id="page-content-wrapper">
            <div class="container-fluid">
                <div class ="row">
                    <div class ="col-lg-12">
                        <a href="#" class="btn btn-success" id="menu-toggle">Toggle Menu</a>
                        <h1>Sidebar Testing</h1>
                        <p> TEST TEST TEST TEST TEST TEST TEST TEST TEST
                        TEST TEST TEST TEST TEST TEST TEST TEST TEST
                        TEST TEST TEST TEST TEST TEST TEST TEST TEST
                        TEST TEST TEST TEST TEST TEST TEST TEST TEST</p>
                    </div>
                </div>
            </div>
        </div>


    </div>

    <!-- Menu toggle script -->
    <script>

        $("#menu-toggle").click( function (e){
           e.preventDefault();
           $("#wrapper").toggleClass("menuDisplayed");

        });
    </script>





<!-- Javascript  -->

</body>
</html>