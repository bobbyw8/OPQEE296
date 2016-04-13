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

    <!-- Le styles -->
%print check
</head>
<body>

    <div id="wrapper" class="menuDisplayed">
        <!-- Navbar -->
        <nav class="navbar navbar-default" role="navigation" style="margin-bottom: 0px; background-color:#FFFFFF;">
            <section class="container-fluid">
                <div class="navbar-header">

                    <button type="button" class="navbar-toggle" data-toggle="collapse" id="menu-toggle" style="display: inline">

                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>

                </div>
                <img src="/img/OPQ_LOGO.JPG" style="width:60px;height:60px">
            </section>
        </nav>




        <!-- Sidebar -->
        <div id="sidebar-wrapper">
            <ul class="sidebar-nav">
                <li><a href="/diagnostics">Diagnostics</a></li>
                <li><a href="/networks">Networks</a></li>
                <li><a href="/#">Link 3</a></li>
            </ul>
        </div>

        <!-- Page content -->
        <div id="page-content-wrapper">
            <div class="container-fluid">

                <div class ="row">
                    <div class ="col-lg-12">
                        %if check == "diagnostics":
                            %include diagnostics.tpl
                        %elif check == "networks":
                            %include networks.tpl
                        %else:
                            %include debug.tpl
                        %end
                    </div>
                </div>
            </div>
        </div>


        %include modals.tpl
    </div>




<!-- Javascript  -->

      <script src="/js/jquery.min.js"/>
      <script src="/js/bootstrap.min.js"/>

</body>
</html>