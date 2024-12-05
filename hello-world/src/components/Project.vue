<template>
    <button class="project">
        <span class="projectText">
            <h1>{{ name }}</h1>
            <p class="description">{{ description }} </p>
            <div class="textFooter">
                <span class="required">Potrebujem 10 000€</span>
            </div>
        </span>
        <span class="projectImg">
            <img src="../assets/logo.png" alt="Descriptive text for image">
        </span>
      </button>
  </template>
  
  <script>
  export default {
    name: 'SingleProject',
    props: {
    name: String,
    description: String
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .name{
    background-color: red;
  }
  .projectText{
    width: 60%;
    /* background-color: rgba(255, 0, 0, 0.5); */
    position: relative;
    z-index: 1; 
    border-top-left-radius: 2rem;
    border-bottom-left-radius: 2rem;
  }
  .projectImg{
    width: 40%;
    /* background-color: aqua; */
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center;    /* Center vertically */
    height: 42rem; /* Adjust the height as needed */
    border-top-right-radius: 2rem;
    border-bottom-right-radius: 2rem;
  }
  .project{
    display: flex;
    height: 42rem;
    background-color: blue;
    border-bottom: solid;
    margin: 2rem;
    padding: 0;
    border: none;
    box-shadow:
    0.3em 0.3em 1em rgba(41, 41, 41, 0.6);
    background-color: #eeececa2;
    transition: transform .5s; 
    border-top-right-radius: 2rem;
    border-bottom-right-radius: 2rem;
    border-top-left-radius: 2rem;
    border-bottom-left-radius: 2rem;
  }
  .project:hover{
    transform: scale(1.02); 
  }
  img {
    max-width: 80%; /* Ensure the image is responsive and fits inside the container */
    max-height: 80%; /* Prevent the image from exceeding the container's height */
    border-radius: 2rem;
  }
  
  .description{
    height: 20rem;
    /* background-color: yellow; */
    display: flex;
    font-size: 1.6vw;
    padding: 2rem;
    justify-content: center;
    text-align: justify;
    position: relative;
    z-index: 1; 
    align-items: center;
  }
  .required{
    text-align: left;
    border-bottom-left-radius: 2rem;
  }
  h1{
    text-align: left;
    margin: 0;
    font-size: 3vw;
    padding-left: 4rem;
    padding-top: 4rem;
    padding-bottom: 4rem;
  }
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  </style>
  