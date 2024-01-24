import streamlit as st

def body_css():
    st.markdown(""" 
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Oswald">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open Sans">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
    h1,h2,h3,h4,h5,h6 {font-family: "Oswald"}
    </style>
    """, unsafe_allow_html=True,)

def kpi_box_css():
    st.markdown("""
    <style>
    .icon {  
    float: right;
    font-size:500%;
    position: absolute;
    top:0rem;
    right:-0.3rem;
    opacity: .16;
    }

  
    #container
    {
    display: flex;
    }



    .blue-gradient {
    background: linear-gradient(180deg, rgba(0, 4, 40,0.8) 0%, rgba(0, 78, 146,0.8) 80%);
    color: #fff;
    }
    
    .kpi-card
    {
    overflow: hidden;
    position: relative;
    box-shadow: 1px 1px 3px rgba(0,0,0,0.75);;
    display: inline-block;
    float: left;
    padding-top: 1em;
    padding-left: 1em;
    padding-right: 0.5em;
    padding-bottom: 0.5em;
    border-radius: 0.3em;
    font-family: sans-serif;  
    width: 180px;
    min-width: 180px;
    margin-right: 0em;
    margin-bottom: 30px;
    }

    .card-value {
    display: block;
    font-size: 200%;  
    font-weight: bolder;
    }

    .card-text {
    display:block;
    font-size: 70%;
    padding-left: 0.0em;
    }
    .lol {
    justify-content : space-around;
    }
    </style>
    """, unsafe_allow_html=True)


def kpi_box_granular(donors, unique_donors, regular_donors, percentage):
    st.markdown("""
    <div id="container"  class = "lol" >
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Flag_of_Malaysia.svg/383px-Flag_of_Malaysia.svg.png" alt="kedah" width = "35" height = "20">
            <span class="card-text">TOTAL DONORS</span>
            <span class="card-value">{:,}</span>    
        </div>
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Flag_of_Malaysia.svg/383px-Flag_of_Malaysia.svg.png" alt="kedah" width = "35" height = "20">
            <span class="card-text">UNIQUE DONORS</span>
            <span class="card-value">{:,}</span>    
        </div>
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Flag_of_Malaysia.svg/383px-Flag_of_Malaysia.svg.png" alt="kedah" width = "35" height = "20">
            <span class="card-text">REGULAR DONORS</span>
            <span class="card-value">{:,}</span>    
        </div>
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Flag_of_Malaysia.svg/383px-Flag_of_Malaysia.svg.png" alt="kedah" width = "35" height = "20">
            <span class="card-text">REGULAR DONORS (%)</span>
            <span class="card-value">{:.1%}</span>    
        </div>
                
                
    </div>
    """.format(donors, unique_donors, regular_donors, percentage), unsafe_allow_html=True)


def kpi_box_malaysia(malaysia):
    st.markdown("""
    <div id="container"  class = "lol" >
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Flag_of_Malaysia.svg/383px-Flag_of_Malaysia.svg.png" alt="kedah" width = "35" height = "20">
            <span class="card-text">MALAYSIA</span>
            <span class="card-value">{:,}</span>    
        </div>
                
    </div>
    """.format(malaysia), unsafe_allow_html=True)


def kpi_box_1(kedah, pulau_pinang, perak, selangor):
    st.markdown("""         
    <div id="container"  class = "lol" >
        <div class="kpi-card blue-gradient ">
            <img src="https://c4.wallpaperflare.com/wallpaper/71/359/733/2000px-flag-kuala-lumpur-malaysia-svg-wallpaper-preview.jpg" alt="kuala lumpur" width = "35" height = "20">
            <span class="card-text">KUALA LUMPUR</span>
            <span class="card-value">{:,}</span>
        </div> 
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Flag_of_Kedah.svg" alt="kedah" width = "35" height = "20">
            <span class="card-text">KEDAH</span>
            <span class="card-value">{:,}</span>
        </div>
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Flag_of_Perak.svg" alt="perak" width = "35" height = "20">
            <span class="card-text">PERAK</span>
            <span class="card-value">{:,}</span>
        </div>
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Flag_of_Johor.svg" alt="johor" width = "35" height = "20">
            <span class="card-text">JOHOR</span>
            <span class="card-value">{:,}</span>
        </div>
    </div>
    """.format(kedah, pulau_pinang, perak, selangor), unsafe_allow_html=True)

def kpi_box_2(putrajaya, n_sembilan, sabah, sarawak):
    st.markdown("""
    <div id="container"  class = "lol" >
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Flag_of_Sarawak.svg/383px-Flag_of_Sarawak.svg.png" alt="sarawak" width = "35" height = "20">
            <span class="card-text">SARAWAK</span>
            <span class="card-value">{:,}</span>
        </div>  
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a1/Flag_of_Penang_from_xrmap.svg" alt="pulau pinang" width = "35" height = "20">
            <span class="card-text">PULAU PINANG</span>
            <span class="card-value">{:,}</span>
        </div>
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Flag_of_Sabah.svg/255px-Flag_of_Sabah.svg.png" alt="sabah" width = "35" height = "20">
            <span class="card-text">SABAH</span>
            <span class="card-value">{:,}</span>
        </div>
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_Malacca.svg/1200px-Flag_of_Malacca.svg.png" alt="melaka" width = "35" height = "20">
            <span class="card-text">MELAKA</span>
            <span class="card-value">{:,}</span>
        </div>       
    </div>
    """.format(putrajaya, n_sembilan, sabah, sarawak), unsafe_allow_html=True)

def kpi_box_3(terengganu, pahang, melaka, johor):
    st.markdown("""
    <div id="container"  class = "lol" >
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/0c/Flag_of_Selangor.svg" alt="selangor" width = "35" height = "20">
            <span class="card-text">SELANGOR</span>
            <span class="card-value">{:,}</span>      
        </div>  
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/d/db/Flag_of_Negeri_Sembilan.svg" alt="negeri sembilan" width = "35" height = "20">
            <span class="card-text">NEGERI SEMBILAN</span>
            <span class="card-value">{:,}</span>
        </div> 
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/Flag_of_Terengganu.svg" alt="terengganu" width = "35" height = "20">
            <span class="card-text">TERENGGANU</span>
            <span class="card-value">{:,}</span>
        </div>
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Flag_of_Pahang.svg" alt="pahang" width = "35" height = "20">
            <span class="card-text">PAHANG</span>
            <span class="card-value">{:,}</span>
        </div>    
          
    </div>
    """.format(terengganu, pahang, melaka, johor), unsafe_allow_html=True)


def kpi_box_4(melaka, johor, perlis, labuan):
    st.markdown("""
    <div id="container"  class = "lol" >
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/61/Flag_of_Kelantan.svg" alt="kelantan" width = "35" height = "20">
            <span class="card-text">KELANTAN</span>
            <span class="card-value">{:,}</span>
        </div>        
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Flag_of_Perlis.svg" alt="perlis" width = "35" height = "20">
            <span class="card-text">PERLIS</span>
            <span class="card-value">{:,}</span>
        </div>
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Putrajaya.svg" alt="putrajaya" width = "35" height = "20">
            <span class="card-text">PUTRAJAYA</span>
            <span class="card-value">{:,}</span>
        </div>
        <div class="kpi-card blue-gradient ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/69/Flag_of_Labuan.svg" alt="labuan" width = "35" height = "20">
            <span class="card-text">LABUAN</span>
            <span class="card-value">{:,}</span>
        </div>          
    </div>
    """.format(melaka, johor, perlis, labuan), unsafe_allow_html=True)






































def kpi_box_new():
    st.markdown("""
    <div id="root">
        <div class="container pt-5">
            <div class="row align-items-stretch">
            <div class="c-dashboardInfo col-lg-3 col-md-6">
                <div class="wrap">
                <h4 class="heading heading5 hind-font medium-font-weight c-dashboardInfo__title">Portfolio Balance<svg
                    class="MuiSvgIcon-root-19" focusable="false" viewBox="0 0 24 24" aria-hidden="true" role="presentation">
                    <path fill="none" d="M0 0h24v24H0z"></path>
                    <path
                        d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z">
                    </path>
                    </svg></h4><span class="hind-font caption-12 c-dashboardInfo__count">€10,500</span>
                </div>
            </div>
            <div class="c-dashboardInfo col-lg-3 col-md-6">
                <div class="wrap">
                <h4 class="heading heading5 hind-font medium-font-weight c-dashboardInfo__title">Rental income<svg
                    class="MuiSvgIcon-root-19" focusable="false" viewBox="0 0 24 24" aria-hidden="true" role="presentation">
                    <path fill="none" d="M0 0h24v24H0z"></path>
                    <path
                        d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z">
                    </path>
                    </svg></h4><span class="hind-font caption-12 c-dashboardInfo__count">€500</span><span
                    class="hind-font caption-12 c-dashboardInfo__subInfo">Last month: €30</span>
                </div>
            </div>
            <div class="c-dashboardInfo col-lg-3 col-md-6">
                <div class="wrap">
                <h4 class="heading heading5 hind-font medium-font-weight c-dashboardInfo__title">Available funds<svg
                    class="MuiSvgIcon-root-19" focusable="false" viewBox="0 0 24 24" aria-hidden="true" role="presentation">
                    <path fill="none" d="M0 0h24v24H0z"></path>
                    <path
                        d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z">
                    </path>
                    </svg></h4><span class="hind-font caption-12 c-dashboardInfo__count">€5000</span>
                </div>
            </div>
            <div class="c-dashboardInfo col-lg-3 col-md-6">
                <div class="wrap">
                <h4 class="heading heading5 hind-font medium-font-weight c-dashboardInfo__title">Rental return<svg
                    class="MuiSvgIcon-root-19" focusable="false" viewBox="0 0 24 24" aria-hidden="true" role="presentation">
                    <path fill="none" d="M0 0h24v24H0z"></path>
                    <path
                        d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z">
                    </path>
                    </svg></h4><span class="hind-font caption-12 c-dashboardInfo__count">6,40%</span>
                </div>
            </div>
            </div>
        </div>
        </div>
                """.format(),  unsafe_allow_html=True)
    

def kpi_box_css_new():
    st.markdown("""
    <style>
    .c-dashboardInfo {
    margin-bottom: 15px;
    }
    .c-dashboardInfo .wrap {
    background: #ffffff;
    box-shadow: 2px 10px 20px rgba(0, 0, 0, 0.1);
    border-radius: 7px;
    text-align: center;
    position: relative;
    overflow: hidden;
    padding: 40px 25px 20px;
    height: 100%;
    }
    .c-dashboardInfo__title,
    .c-dashboardInfo__subInfo {
    color: #6c6c6c;
    font-size: 1.18em;
    }
    .c-dashboardInfo span {
    display: block;
    }
    .c-dashboardInfo__count {
    font-weight: 600;
    font-size: 2.5em;
    line-height: 64px;
    color: #323c43;
    }
    .c-dashboardInfo .wrap:after {
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 10px;
    content: "";
    }

    .c-dashboardInfo:nth-child(1) .wrap:after {
    background: linear-gradient(82.59deg, #00c48c 0%, #00a173 100%);
    }
    .c-dashboardInfo:nth-child(2) .wrap:after {
    background: linear-gradient(81.67deg, #0084f4 0%, #1a4da2 100%);
    }
    .c-dashboardInfo:nth-child(3) .wrap:after {
    background: linear-gradient(69.83deg, #0084f4 0%, #00c48c 100%);
    }
    .c-dashboardInfo:nth-child(4) .wrap:after {
    background: linear-gradient(81.67deg, #ff647c 0%, #1f5dc5 100%);
    }
    .c-dashboardInfo__title svg {
    color: #d7d7d7;
    margin-left: 5px;
    }
    .MuiSvgIcon-root-19 {
    fill: currentColor;
    width: 1em;
    height: 1em;
    display: inline-block;
    font-size: 24px;
    transition: fill 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
    user-select: none;
    flex-shrink: 0;
    }

    </style>
    """, unsafe_allow_html=True)