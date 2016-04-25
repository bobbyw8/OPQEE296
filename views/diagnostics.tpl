<!--form to send input to modal-->
<form>
    <fieldset>
        Enter Command:<br>
        <input id="fCmd" type="text" name="fCommand" value=""/>
        <br><br>
        <p><input type="button" value="Submit" data-toggle="modal" data-target="#CMD" onclick="cmdmodal()"/> </p>

    </fieldset>
</form>

<!-- Table for log files -->
 <table class="table table-striped table-hover">
    <thead>
      <tr>
        <th>Log Files</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
%length_arrlog = len(arrlog)
%for i in range(length_arrlog):
      <tr id = tableRow>
        <td id= "tableCol_time{{i}}">{{arrlog[i][0]}}</td>
        <td id= "tableCol_cmd{{i}}">{{arrlog[i][1]}}</td>
      </tr>
%end
    </tbody>
  </table>