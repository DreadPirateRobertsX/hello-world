<template>
  <div>
    <MyHeader/>
      test
    <AboutUs/>
  </div>
</template>

<script>
import MyHeader from './components/MyHeader.vue'
// import SingleProject from './components/Project.vue'
// import MyFooter from './components/Footer.vue'
import AboutUs from './components/AboutUs.vue'
// import CardScroller from './components/CardScroller/CardScroller.vue'


export default {
  name: 'ProjectDetail',
  components: {
    MyHeader,
    // SingleProject,
    // MyFooter,
    AboutUs
    // CardScroller
  }
}
</script>

<style>
html,body {
  
    margin:0;
    padding:0;
}
#app {
  font-family: SF Pro Display,SF Pro Icons,Helvetica Neue,Helvetica,Arial,sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  margin: 0px;
}
</style>
