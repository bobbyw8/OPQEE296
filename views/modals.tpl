  <div class="modal fade" id="CMD" role="dialog">
    <div class="modal-dialog">

      <!-- Modal content-->
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
          <h4 class="modal-title" >Are you sure?</h4>
        </div>
        <div class="modal-body">
            <p id="mbdialog"></p>
        </div>
        <div class="modal-footer">
          <form action ="/diagnostics" method="POST" >
          <input name="fCMD" id="idCMD" >
          <input type="submit" name="sub_CMD" value="OK" class="btn btn-default">
          <input type="button" class="btn btn-default" data-dismiss="modal" value ="Cancel">
          </form>
        </div>
      </div>
    </div>
  </div>

   <!--Send command to server and display what was submitted-->
  <script>

      function cmdmodal(){
      document.getElementById("idCMD").value = document.getElementById("fCmd").value;
      document.getElementById("mbdialog").innerHTML = "You entered your command as: \n\n"+"<br><br>"+ document.getElementById("fCmd").value +"<br><br>" +"\n\nSelect OK if correct or Cancel to edit.";
      }


  </script>