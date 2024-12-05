<template>
    <div>
        <span>
            <div class="AboutUs" id="footer">
                <div class="AboutUsContent">
                    <div class="container1">
                        <div class="logo" style="margin-top: 40px">
                            <img class="logoImg" src="../assets/logoWhite.png">   
                        </div>
                        <p class="footerMotto">Building the Bridge from Imagination to Implementation.</p>
                    </div>
                    <span class="container2">
                        <h1>About Us</h1>
                        <p class="AboutUsText">Lorem ipsum dolor sit amet, consectetur adipiscing elit. In consequat nec orci nec pharetra. Curabitur venenatis risus ac dolor commodo faucibus. Nunc commodo porttitor interdum. Praesent lacinia ligula odio, lacinia suscipit sapien condimentum consequat. Sed vel felis a neque consectetur dapibus nec sed dui. Maecenas convallis lectus vitae varius ullamcorper. Nullam hendrerit eget est in sollicitudin. Nam id vestibulum lacus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam commodo suscipit sapien, et porta tellus pretium a. Pellentesque accumsan ullamcorper dolor at pulvinar. Pellentesque ac eros purus. Pellentesque tempus sit amet dui nec tincidunt. Donec. </p>
                    </span>
                    <div class="container3">
                        <div class="contact">
                            <h1>Contact</h1>
                            <div style="margin-top: 40px">
                                <p>Address: Budatínska 20, Bratislava</p>
                                <p>Email: ideasdatabase@ideasdb.com</p>
                                <p>Mobile: +421 907 622 321</p>
                            </div>
                        </div>
                        <div class="socials" style="margin-top: 40px">
                            <h1>Social Media</h1>
                            <ul class="ulSocials" style="margin-top: 10px">
                                <li class="liSocial"><a href="#Facebook"><img src="../assets/MediasLogos/icons8-facebook-50.png"></a></li>
                                <li class="liSocial"><a href="#Instagram"><img src="../assets/MediasLogos/icons8-instagram-50.png"></a></li>
                                <li class="liSocial"><a href="#LinkedIn"><img src="../assets/MediasLogos/icons8-linkedin-50.png"></a></li>
                                <li class="liSocial"><a href="#X"><img src="../assets/MediasLogos/icons8-twitterx-50(1).png"></a></li>
                            </ul>  
                        </div> 
                    </div>
                </div>
            </div>
        </span>
        <div>
            <nav class="navbar">
                <ul class="navbar-nav">
                    <li class="liNav"><a class="aNav" href="#">Home</a></li>
                    <li class="liNav"><a class="aNav" href="#">Projects</a></li>
                    <li class="liNav"><a class="aNav" href="#">About Us</a></li>
                    <li class="liNav"><a class="aNav" href="#">Contact Us</a></li>
                </ul>
                </nav>
        </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AboutUs'
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
.footerMotto {
  font-size: 1.6rem;
  text-align: left; /* Center the text horizontally */
  margin: 0; /* Remove any default margin */
  margin-top: 40px;
}
.container1 {
  width: 350px;
  display: flex; /* Using flexbox */
  flex-direction: column; /* Stack children vertically */
  justify-content: center; /* Center children vertically */
  align-items: left; /* Center children horizontally */
  padding: 4% 0; /* Padding on top and bottom for spacing */
}
.logo {
  margin: 0; /* Removing margin at the top */
}
.logoImg {
  width: 100%;
  height: auto; /* Adjust height to maintain aspect ratio */
  -o-object-fit: cover;
  object-fit: cover;
  filter: invert(0.6);
}
  .socials{
    text-align: left;
  }
  .contact{
    text-align: left;
  }
  .AboutUsContent{
    display: inline-flex;
    justify-content: space-around;
    position: relative; z-index: 4000;
    margin-top: 0px;
    width: 100vw;
    padding-bottom: 1%;
  }
  .AboutUs{
    margin-top: 2%;
    width: 100vw;
    padding-bottom: 1%;
    background-color: rgb(51, 51, 51);
  }
  .AboutUsText{
    /* padding-left: 10%;
    padding-right: 10%; */
    text-align: justify;
    color: rgb(150, 149, 149);
    font-family: Arial, sans-serif; /* Clean and modern font */
    font-size: 16px; /* Adequate text size */
    line-height: 1.6; /* Spacious line height for readability */
    max-width: 600px; /* Maximum width for optimal reading */
    margin: 40px auto; /* Centered text with vertical spacing */
  }
  .footerNav{
    color: black;
    text-align: left;
  }
  .navbar{
  margin-top: 0px;
}
.navbar-nav{
  margin-top: 0px;
  padding-top: 15px;
}
p{
    color: rgb(150, 149, 149);
}
  h1{
    /* margin-top: 30%; */
  color: #504f4f; /* Set your desired color */
  }
  h3 {
    margin: 40px 0 0;
  }
  .ulNav {
  list-style-type: none;
  color: #FFFFFF;
  font-size: larger;
  padding: 0;
}
.liNav {
  display: inline-block;
  margin: 0 50px;  
}
.liSocial{
  margin: 0;  
}
.aNav {
  text-decoration: none;
  color: rgb(150, 149, 149);
}
  .ulSocials {
    list-style-type: none;
    width: 100%;
    padding: 0;
    display: inline-flex;
    justify-content: space-between;
  }
  ul {
    list-style-type: none;
    padding: 0;
    display: inline-flex;
    justify-content: space-between;
  }
  li {
    margin: 0 10px;
    display: inline-block;
  }
  a {
    color: #42b983;
  }
  img{
    filter: invert(0.5);
  }
  </style>