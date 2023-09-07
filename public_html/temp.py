import os

folder = '/public_html/assets/img/team'
path = os.getcwd() + folder

text="""
<div class="col-lg-3 col-md-6 d-flex align-items-stretch ">
    <div class="member " data-aos="fade-up " data-aos-delay="400 ">
        <div class="member-img ">
            <img src="assets/img/team/bhavika.png" class="img-fluid " alt=" ">
        </div>
        <div class="member-info ">
            <h4>Bhavika Ashwin</h4>
            <span>Receptionist</span>
        </div>
    </div>
</div>
"""

for name in os.listdir(path):
    t = text.replace('bhavika.png',name)
    t = t.replace('Bhavika Ashwin',name.replace('.jpg',''))
    print(t)