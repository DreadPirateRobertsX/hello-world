<template>
    <div class="card">
        <div class="image-container">
            <img src="../../assets/background.jpg" alt="titleImage">
            <div class="text-container">
                <h1 class="card-title">{{ ideaName }}</h1>
                <p class="card-text">Your multi-line text goes here. This text can span multiple lines and will be styled to fit within the card design.</p>
            </div>
        </div>
    </div>
</template>

  
  <script>

  export default {
    name: 'MyCard',
    props: {
      ideaName: String,
      ideaAbstract: String
    },
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .text-container {
  position: absolute;
  color: rgb(201, 201, 201);
  font-family: SF Pro Display,SF Pro Icons,Helvetica Neue,Helvetica,Arial,sans-serif;
  font-size: 20px;
  font-weight: 200;
  text-align: justify;
  letter-spacing: -.022em;
  line-height: 1.2353641176;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end; /* Align text to the bottom */
  padding: 45px; /* Add some padding inside the text container */
  background-image: linear-gradient(to top, rgba(0,0,0,0.7) 10%, rgba(0,0,0,0) 100%); /* Gradient overlay for text readability */
}

.card {
  height: 90%; /* Matches the scroller’s height */
  max-height: 450px; /* Optional: Prevent cards from exceeding the scroller height */
  width: 450px;
  border-radius: 24px;
  box-shadow: 0.3em 0.3em 1em rgba(41, 41, 41, 0.6);
  transition: transform .3s;
  overflow: hidden;
}
.card:hover {
  transform: scale(1.02);
}

.image-container {
  position: relative;
  width: 100%;
  height: 100%;
}

img {
  width: 100%;
  height: 100%;
  border-radius: 24px;
  object-fit: cover; /* Ensures the image covers the area without stretching */
}

.card-title {
  position: absolute;
  text-align: left;
  top: 0;
  left: 0;
  margin-left: 5%;
  margin-top: 8%;
  margin-right: 25%;
  color: #995b04; /* Choose a color that stands out over your image */
  font-size: 1.5rem; /* Adjust size as needed */
  z-index: 0; /* Ensure it's above the image */
}

@media (max-width: 600px) {
  .card {
    width: 410px; /* Adjust width to a larger percentage of viewport width */
  }
}

/* Media query for medium screens (tablets) */
@media (min-width: 601px) and (max-width: 1024px) {
  .card {
    width: 300px; /* Adjust width for tablet */
  }
}

/* Media query for larger screens (desktop) */
@media (min-width: 1025px) and (max-width: 1440px) {
  .card {
    width: 380px; 
  }
}
@media (min-width: 1441px) and (max-width: 2560px) {
  .card {
    width: 400px; 
  }
}
@media (min-width: 2561px) {
  .card {
    width: 400px; 
  }
}
</style>

  