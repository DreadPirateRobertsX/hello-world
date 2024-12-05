<template>
  <div class="ideas" id="ideas">
    <h1>{{ categoryName }}</h1>
    <swiper
      :slidesPerView="3"
      :spaceBetween="50"
      :pagination="{
        clickable: true,
      }"
      :breakpoints="{
        '640': {
          slidesPerView: 1,
          spaceBetween: 1500,
        },
        '768': {
          slidesPerView: 3,
          spaceBetween: 0,
        },
        '1025': {
          slidesPerView: 3,
          spaceBetween: 13,
        },
        '1441': {
          slidesPerView: 4,
          spaceBetween: 45,
        },
        '2560': {
          slidesPerView: 5,
          spaceBetween: 60,
        },
      }"
      :modules="modules"
      class="mySwiper"
    >
      <!-- Dynamically generate swiper-slide with MyCard components -->
      <swiper-slide 
        v-for="(idea, index) in ideas" 
        :key="index"
      >
        <MyCard :ideaName="idea" />
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import MyCard from '../CardScroller/Card.vue'
import { Swiper, SwiperSlide } from 'swiper/vue'
import 'swiper/css'
import 'swiper/css/pagination'
import { Pagination } from 'swiper/modules'

export default {
  name: 'CardScroller',
  props: {
    categoryName: String,
    ideas: {
      type: Array,
      required: true,
    },
  },
  components: {
    MyCard,
    Swiper,
    SwiperSlide,
  },
  setup() {
    return {
      modules: [Pagination],
    }
  },
}
</script>

<style scoped>
.ideas {
  margin-top: 2%;
}
h1 {
  float: left;
  padding-left: 70px;
}
.mySwiper {
  width: 100%;
  height: 100%;
}
::v-deep .swiper-wrapper {
  /* Add your custom styles for the swiper wrapper here */
  height: 500px;
  padding-top: 15px;
  padding-left: 4%;
  display: flex;
  gap: 20px; /* Example: add a gap between the swiper slides */
  justify-content: left; /* Align items in the center */
}

::v-deep .swiper-slide {
  width: auto !important;}
</style>
