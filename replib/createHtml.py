import os


def Prepare_report(final_result_list, time_stamp, all_pages):

    html_file = open('../test_report/'+final_result_list[5]+'/index.html', 'w')

    web_page_part_1 = """<!DOCTYPE html><html><title>Test Report</title><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1'>
                      <link rel='stylesheet' type='text/css' href='../mt.css' /><link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Raleway'>
                      <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'>
                      <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>
                      <style>
                      body,h1,h2,h3,h4,h5,h6 {font-family: 'Raleway', sans-serif}
                      .env {margin:10px 0px 10px 18px;}
                      .env1 {float:left; width:50%; color:#707070;}
                      .view{display:none !important;}
                      .active{color: #009688!important;}
                      """
    web_page_part_1a = """
                            #myImg {    border-radius: 5px;
                                cursor: pointer;
                                transition: 0.3s;
                            } #myImg:hover {opacity: 0.7;}
                            /* The Modal (background) */
                            .modal {
                                display: none;
                                position: fixed;
                                z-index: 1;
                                padding-top: 100px;
                                left: 0;
                                top: 0;
                                width: 100%;
                                height: 100%;
                                overflow: auto; background-color: rgb(0,0,0); background-color: rgba(0,0,0,0.9);
                            }
                            /* Modal Content (image) */
                            .modal-content {
                                margin: auto;
                                display: block;
                                width: 92%;
                            }
                            
                            /* Add Animation */
                            .modal-content, #caption {
                                -webkit-animation-name: zoom;
                                -webkit-animation-duration: 0.6s;
                                animation-name: zoom;
                                animation-duration: 0.6s;
                            }
                            @-webkit-keyframes zoom {
                                from {-webkit-transform:scale(0)}
                                to {-webkit-transform:scale(1)}
                            }
                            @keyframes zoom {
                                from {transform:scale(0)}
                                to {transform:scale(1)}
                            }
                            /* The Close Button */
                            .close {
                                position: absolute;
                                top: 15px;
                                right: 35px;
                                color: #f1f1f1;
                                font-size: 40px;
                                font-weight: bold;
                                transition: 0.3s;
                            }
                            /* 100% Image Width on Smaller Screens */
                            @media only screen and (max-width: 700px){
                                .modal-content {
                                    width: 100%;
                                }
                            }
                            .subOption{margin-left: 30px!important}
                        """
    
    web_page_part_1b = """</style><body class='mt-light-grey mt-content' style='max-width:2600px'>"""

    web_page_part_2 = """<!-- Sidebar/menu -->
                      <nav class='mt-sidebar mt-collapse mt-white mt-animate-left' style='z-index:3;width:300px;' id='mySidebar'><br>
                      </a><img src='"""+final_result_list[14]+"""' style='width:100%; padding:10px;' class='mt-round'><br><br>
                      </div><div class='mt-bar-block'>
                      <a id='pc' href='#portfolio' class='mt-bar-item mt-button mt-padding active'>
                      <i class='fa fa-th-large fa-fw mt-margin-right'></i>Pie Chart</a>
                      <a id='ted' href='#TestExecutionDetails' class='mt-bar-item mt-button mt-padding'>
                      <i class='fa fa-user fa-fw mt-margin-right'></i>Test Execution Details</a>
                      <div id="sub" class="view">"""
    web_page_part_2b ="""
                      <div id="sub" class="view">
                      <a href='#' class='mt-bar-item mt-button subOption'>
                      <i class='fa fa-file fa-fw mt-margin-right'></i>Test Execution Details</a>
                      """
    web_page_part_3 = """
                      </div>
                      </div>
                      </nav>
                      <div class='mt-overlay mt-hide-large mt-animate-opacity' onclick='mt_close()' style='cursor:pointer' title='close side menu' id='myOverlay'></div> 
                    <!-- !PAGE CONTENT! --> <div class='mt-main' style='margin-left:300px'>"""
    web_page_part_4b = "<!-- Header --><header id=\"portfolio\">" \
                      "<a href=\"#\"><img src='"+final_result_list[14]+"' style=\"width:100%;\" class=\"mt-circle mt-right mt-margin mt-hide-large mt-hover-opacity\"></a>" \
                      "<span class='mt-button mt-hide-large mt-xxlarge mt-hover-text-grey' onclick='mt_open()'><i class='fa fa-bars'></i></span>" \
                      "<div class='mt-container'>" \
                      "<div id='' style='height:100%; width:100%; text-align: center; background-color:white; margin-bottom: 10px; margin-top: 10px; max-height:900px;'>" \
                      "<h4 style='padding-top:10px; '><b>"+final_result_list[6]+"</b></h4></div>"
    web_page_part_4 = "<div style='height:100%; width:100%; background-color:white; margin-bottom: 10px; margin-top: 10px; max-height:900px; overflow: auto;'>" \
                      "<h5 style='margin: 10px 0px 3px 18px;'><b>Environment</b></h5>" \
                      "<div class='env1'>" \
                      "<p class='env'><b>Project Name:</b> "+final_result_list[7]+"</p>" \
                      "<p class='env'><b>UserName:</b> "+final_result_list[8]+"</p>" \
                      "<p class='env'><b>Script Team:</b> "+final_result_list[9]+"</p>" \
                      "<p class='env'><b>Date of Execution:</b> "+final_result_list[10]+"</p></div>" \
                      "<div class='env1'>" \
                      "<p class='env'><b>Script Version: </b> "+final_result_list[5]+"</p>" \
                      "<p class='env'><b>Testing Environment:</b> "+final_result_list[11]+"</p>" \
                      "<p class='env'><b>OS:</b> "+final_result_list[12]+"</p>" \
                      "<p class='env'><b>Java Version:</b> "+final_result_list[13]+"</p></div></div>"
    web_page_part_4a =  """<div id='pchart' style='height:100%; width:100%; background-color:white; margin-top: 10px; max-height:900px; padding-bottom:40px; '>
                            <div class="mt-container"><h5><b>General Stats</b></h5>
                                <p><b>Pass</b></p><div class="mt-grey">
                                  <div class="mt-container mt-center" style="background-color:#3366cc; color:#ffffff; width:"""+final_result_list[0]+"""%">"""+final_result_list[0]+"""%</div></div>
                                <p><b>Fail</b></p><div class="mt-grey">
                                  <div class="mt-container mt-center" style="background-color:#dc3912; color:#ffffff; width:"""+final_result_list[1]+"""%">"""+final_result_list[1]+"""%</div></div>
                                <p><b>Error</b></p><div class="mt-grey">
                                  <div class="mt-container mt-center" style="background-color:#ff9900; color:#ffffff; width:"""+final_result_list[2]+"""%">"""+final_result_list[2]+"""%</div></div>
                                <p><b>Skip</b></p><div class="mt-grey">
                                  <div class="mt-container mt-center" style="background-color:#109618; color:#ffffff; width:"""+final_result_list[3]+"""%">"""+final_result_list[3]+"""%</div></div>
                                <p><b>Info</b></p><div class="mt-grey">
                                  <div class="mt-container mt-center" style="background-color:#990099; color:#ffffff; width:"""+final_result_list[4]+"""%">"""+final_result_list[4]+"""%</div></div>
                             </div>
                        </div>
                        """

    web_page_part_6 = "</div>" \
                      "<!-- Footer -->" \
                      "          <footer style='position: fixed; left: 0; bottom: 0; width:100%; height:5px;'>" \
                      "          </div>" \
                      "          </footer>" \
                      "         <!-- End page content -->" \
                      "        </div>    "

    web_page_part_7 = "</body>" \
                      "<script>$(document).ready(function(){  " \
                      "$('#pc').click(function(){    " \
                      "$('#res').addClass('view'); " \
                      "$('#sub').addClass('view'); " \
                      "$('#pchart').removeClass('view'); " \
                      "$('#pc').addClass('active'); " \
                      "$('#ted').removeClass('active');  " \
                      "});" \
                      "$('#ted').click(function(){    " \
                      "$('#pchart').addClass('view'); " \
                      "$('#sub').removeClass('view'); " \
                      "$('#res').removeClass('view'); " \
                      "$('#ted').addClass('active'); " \
                      "$('#pc').removeClass('active');   });" \
                      "$('.view').on('click','a', function(){$(this).toggleClass('active').siblings().removeClass('active'); })" \
                      "});</script>" \
                      "</html>"

    html_file.write(web_page_part_1)
    html_file.write(web_page_part_1a)
    html_file.write(web_page_part_1b)
    html_file.write(web_page_part_2)
    for x in all_pages:
        html_file.write("""<a id='sub' href='#"""+x.replace(' ','')+"""' class='mt-bar-item mt-button subOption'>
                      <i class='fa fa-file fa-fw mt-margin-right'></i>"""+x+"""</a>
                      """)
    html_file.write(web_page_part_3)
    html_file.write(web_page_part_4b)
    html_file.write(web_page_part_4)
    html_file.write(web_page_part_4a)
    html_file.write("<div id = 'res' class='view'>")
    # print(final_result_list[5])

    # x = os.listdir('../test_report/'+final_result_list[5]+'/')
    # # print("x is ", x)
    # x.remove('index.html')
    # print("Now x is ", x)

    for ind in range(len(all_pages)):
        # print("ind is ", ind)
        # print('../test_report/' + final_result_list[5] + '/' + all_pages[ind]+".html")
        with open('../test_report/' + final_result_list[5] + '/' + all_pages[ind]+".html") as tag:
            for lines in tag:
                html_file.write(lines)

    # for y in x:
    #     if '.html' in y:
    #         with open('../test_report/'+final_result_list[5]+'/'+y) as tag:
    #             for lines in tag:
    #                 html_file.write(lines)
    html_file.write("</div>")
    html_file.write(web_page_part_6)
    html_file.write(web_page_part_7)
    html_file.close()