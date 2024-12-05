<template>
  <div>
    <MyHeader />
    <!-- Dynamically generate CardScroller components for each category -->
    <CardScroller 
      v-for="(category, index) in categories" 
      :key="index" 
      :categoryName="category.title" 
      :ideas="category.ideas" 
    />
    <AboutUs />
  </div>
</template>

<script>
import MyHeader from './components/MyHeader.vue';
import AboutUs from './components/AboutUs.vue';
import CardScroller from './components/CardScroller/CardScroller.vue';

export default {
  name: 'App',
  components: {
    MyHeader,
    AboutUs,
    CardScroller,
  },
  data() {
    return {
      categories: [] // Initialize categories as an empty array
    };
  },
  async mounted() {
    try {
      // Fetch categories with their ideas from the custom API endpoint
      const response = await fetch("http://localhost:8000/api/categories/with_ideas/");
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      //test
      // Update the categories with API data
      this.categories = data;

    } catch (error) {
      console.error("Failed to fetch categories with ideas:", error);
    }
  }
};
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  scroll-behavior: smooth;
}

#app {
  font-family: SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
