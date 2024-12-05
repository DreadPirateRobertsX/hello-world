<template>
  <div>
      <div class="logo">
        <img class="logoImg" src="../assets/logoWhite.png">   
        <p>Test</p>      
      </div>
  </div>
</template>

<script>
export default {
  name: 'MyFooter'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.logo {
  padding-top: 2%;
  padding-bottom: 2%;
  background-color: rgb(51, 51, 51);
width: 100vw;
margin: auto;
margin-top: 2%;
margin-bottom: 0px;
height: auto; /* Set a height for the container */
display: flex;
flex-direction: column; /* Stack children vertically */
justify-content: center; /* Center horizontally */
align-items: center; /* Center vertically */
}
.logoImg {
width: 25px;
height: 25px;
-o-object-fit: cover;
object-fit: cover;
filter: invert(0.5);
}
ul {
list-style-type: none;
width: 100%; /* Ensure the UL spans the full width if needed */
}
li {
display: inline-block;
margin: 0 40px;
}
a {
color: #42b983;
}
</style>
