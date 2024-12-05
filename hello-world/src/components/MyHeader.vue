<template>
  <div>
    <div class="header">
      <div>
        <nav class="navbar" id="navbar">
          <ul class="navbar-nav">
            <li><a class="nav-item" href="#">Home</a></li>
            <li><a class="nav-item" href="#ideas">Projects</a></li>
            <li><a class="nav-item" href="#footer">About Us</a></li>
            <li><a class="nav-item" href="#footer">Contact Us</a></li>
          </ul>
            <button class="loginButton" id="loginButton">
              Log In
            </button>
        </nav>
        
      </div>
      
      <div class="container1">
        <div class="vertical-center">
          <p class="motivation"><span class="highlight">IdeasDatabase:</span> Building the Bridge from Imagination to Implementation.</p>
        </div>
      </div>
      <!-- <div class="container2">
        <div class="vertical-center-social">
          <ul class="test">
            <li class="liSocial"><a href="#Facebook"><img src="../assets/MediasLogos/icons8-facebook-50.png"></a></li>
            <li class="liSocial"><a href="#Instagram"><img src="../assets/MediasLogos/icons8-instagram-50.png"></a></li>
            <li class="liSocial"><a href="#LinkedIn"><img src="../assets/MediasLogos/icons8-linkedin-50.png"></a></li>
            <li class="liSocial"><a href="#X"><img src="../assets/MediasLogos/icons8-twitterx-50(1).png"></a></li>
          </ul>
        </div>
      </div> -->
    </div>
  </div>
</template>


<script>
export default {
  name: 'MyHeader'
}

var prevScrollpos = window.pageYOffset;
var threshold = 20; // Set the threshold to 100 pixels

window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  
  // Hide the navbar if scrolled down past the threshold, show if scrolled up
  if (prevScrollpos - currentScrollPos > threshold) {
    document.getElementById("navbar").style.top = "0";
  } else if (currentScrollPos - prevScrollpos > threshold) {
    document.getElementById("navbar").style.top = "-60px";
  }

  // Apply color change based on scroll position
  var navItems = document.getElementsByClassName("nav-item");
  if (currentScrollPos > window.innerHeight * 0.2) {
    document.getElementById("navbar").style.backgroundColor = "rgba(0, 0, 0, 0.9";
    document.getElementById("loginButton").style.color = "rgb(201, 201, 201)";
    for (var i = 0; i < navItems.length; i++) {
      navItems[i].style.color = "rgb(201, 201, 201)";
    }
  } else {
    document.getElementById("navbar").style.backgroundColor = "";
    document.getElementById("loginButton").style.color = "";
    for (var j = 0; j < navItems.length; j++) {
      navItems[j].style.color = "";
    }
  }

  prevScrollpos = currentScrollPos;
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.loginButton {
  padding: 8px 16px; /* Adjust padding to match design */
  font-size: 16px; /* Set font size */
  background-color: transparent; /* Example background color */
  color: rgb(82, 73, 43); /* Text color */
  border: none; /* Remove border */
  border-radius: 4px; /* Rounded corners */
  cursor: pointer; /* Pointer cursor on hover */
  font-size: 20px;
  margin-right: 30px;
  border-bottom: 1px solid;
}
#aNav{
  text-decoration: none;
  color: #434343;
}
.filter{
  width: 100%;
  height: 100px;
  background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.7), rgb(255, 255, 255,1));
  filter: blur(1px);
  -webkit-filter: blur(1px);
  border-top: 1px none;
  border-radius: 15px;
}
.header{
  height: 100vh;
  background-image: url(../assets/background1.jpg);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  /* margin-bottom: -50px; */
  /* padding-top: 15px; */
}
.navbar {
  position: fixed;
  z-index: 500;
  top: 0;
  width: 100%;
  display: flex; /* Apply Flexbox layout */
  justify-content: space-between; /* Space between navbar items and button */
  align-items: center; /* Center items vertically */
  padding: 0 20px; /* Add padding to ensure content doesn't touch the edges */
  transition: top 0.3s;
  height: 50px;
}

.navbar-nav {
  display: flex; /* Ensure the list displays inline */
  justify-content: center; /* Center navigation links horizontally */
  align-items: center; /* Center items vertically */
  /* list-style: none; Remove list styling */
  flex-grow: 1; 
  margin: 0 20px; /* Ensures it doesn't touch the buttonContainer */
}
.homeContent{
  background-color: #434343;
  position: relative;
}
.container1 { 
  height: 95vh;
  float: left;
  position: relative;
  width: 70%;
  /* border: 3px solid green;  */
  font-size: 11vh;
  /* color: rgb(45, 60, 89); */
  color: rgb(12, 0, 46);
}
.container2 { 
  height: 95vh;
  float: right;
  position: relative;
  width: 80px;
  /* border: 3px solid green;  */
}
.container2 img {
    width: 2.5vw;  /* sets the width of the images */
    height: 2.5vw; /* sets the height of the images */
    margin-top: 30px;
    object-fit: cover; /* ensures the images maintain their aspect ratio without distortion */
}
.motivation{
  text-align: left;
  background: -webkit-linear-gradient(#a8a8a8, #000000);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  padding-left: 1%;
}
.vertical-center {
  margin: 0;
  position: absolute;
  top: 40vh;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
  padding-left: 10px;
}
.vertical-center-social {
  margin: 0;
  position: absolute;
  top: 40vh;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}
.highlight {
  background: -webkit-linear-gradient(#a8a8a8, #995b04);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  color: #FF5733; /* Set your desired color */}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  color: #FFFFFF;
  font-size: larger;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 50px;  
}
.liSocial{
  margin: 0;  
}
a {
  text-decoration: none;
  color: #434343;
}
.home{
  color: #000000;
  border-bottom: 1.8px solid #000;
}
</style>

