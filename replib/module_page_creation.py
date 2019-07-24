import os


def module_page_create(report_data,page_name,version, timetaken):

    html_file = open('../test_report/'+version+'/'+page_name.replace(' ', '') + '.html', 'w')
    # for module in test_modules:
    html_file.write("<div style='background-color: #ffffff; margin-top:10px;' class='mt-row-padding mt-padding-16' id='TestExecutionDetails'>")
    html_file.write("<div  id="+page_name.replace(' ', '')+" class='mt-col m12'><h1>")
    html_file.write(report_data['Module_Name'])
    html_file.write("""</h1> 
    <span style="padding: 0px 10px 0px 10px;border-radius: 13px;float: left;color: black;">Start at: """+timetaken[0]+"""</span>
    <span style="float:left">|</span>
    <span style="padding: 0px 10px 0px 10px;border-radius: 13px;float: left;color: black;">End at: """+timetaken[1]+"""</span>
    </div><div id='TestCase' class='mt-col m12'>""")

    for test_id in report_data['Test_cases'].keys():
        commment_with_status = report_data['Test_cases'][test_id]
        comment = commment_with_status[:-2]
        status = commment_with_status.replace(commment_with_status[:-2], '')
        if status == '_P':
            html_file.write("<p style='color:#707070; padding: 0.90em 16px; max-height:500px; height:100%; background-color: #F8F8F8; overflow:hidden;'>"
                            "<span style='background-color: #3366cc;padding: 3px 10px 3px 10px;color: white; border-radius: 3px;'>Pass</span>&nbsp<b>" + test_id + ". </b>" + comment + "")
        elif status == '_F':
            html_file.write("<p style='color:#707070; padding: 0.90em 16px; max-height:500px; height:100%; background-color: #F8F8F8; overflow:hidden;'>"
                            "<span style='background-color: #dc3912;padding: 3px 10px 3px 10px;color: white; border-radius: 3px;'>Fail</span>&nbsp<b>" + test_id + ". </b>" + comment + "")
        elif status == '_E':
            html_file.write("<p style='color:#707070; padding: 0.90em 16px; max-height:500px; height:100%; background-color: #F8F8F8; overflow:hidden;'>"
                            "<span style='background-color: #ff9900;padding: 3px 10px 3px 10px;color: white; border-radius: 3px;'>Error</span>&nbsp<b>" + test_id + ". </b>" + comment + "")
        elif status == '_S':
            html_file.write("<p style='color:#707070; padding: 0.90em 16px; max-height:500px; height:100%; background-color: #F8F8F8; overflow:hidden;'>"
                            "<span style='background-color: #109618;padding: 3px 10px 3px 10px;color: white; border-radius: 3px;'>Skip</span>&nbsp<b>" + test_id + ". </b>" + comment + "")
        elif status == '_I':
            html_file.write("<p style='color:#707070; padding: 0.90em 16px; max-height:500px; height:100%; background-color: #F8F8F8; overflow:hidden;'>"
                            "<span style='background-color: #990099;padding: 3px 10px 3px 10px;color: white; border-radius: 3px;'>Info</span>&nbsp<b>" + test_id + ". </b>" + comment + "")

        x = os.listdir('../test_report/'+version+'/'+report_data['Module_Name'].replace(' ', ''))

        for y in x:
            if '.png' in y:
                if y == test_id+".png":
                    html_file.write("""<img onclick="openModal('"""+test_id+"','"+report_data['Module_Name'].replace(' ','')+"""')" id='myImg' src = '""" + report_data['Module_Name'].replace(' ','') + """/""" + test_id + """.png""" + """' style = 'width:4%; float:right;' class ='mt-round' >""")

        html_file.write("""
                        <!-- The Modal -->
                        <div onclick="closeModal()" id="myModal" class="modal" style="z-index: 99;">
                          <span onclick="closeModal()" class="close">&times;</span>
                          <img class="modal-content" id="img01">
                        <!--  <div id="caption"></div> -->
                        </div>
                        """)


    html_file.write("""<script type="text/javascript">
                        var modal = document.getElementById('myModal');
                        
                        var captionText = document.getElementById("caption");
                        var span = document.getElementsByClassName("close")[0];
                        function openModal(tcid,module) {
                            var modalImg = document.getElementById("img01");
                            var src_l = module+"/"+tcid+".png"
                            modal.style.display = "block";
                            modalImg.src = src_l;
                            captionText.innerHTML = this.alt;
                        }
                        function closeModal() {
                            modal.style.display = "none";
                        }
                        
                        </script>
                        <!--</div>
                            <div>
                                <video width="400" controls>
                                    <source src = '""" + report_data['Module_Name'].replace(' ','') + """/""" + report_data['Module_Name'].replace(' ','') + """.mp4'""" + """type='video/mp4'>
                                    Your browser does not support HTML5 video.
                                </video>
                            </div>
                        </div> -->
                        """)

    html_file.close()