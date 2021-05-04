<template>
  <div>
    <h1>Feed - {{ site_name }}</h1>
    <md-layout md-gutter md-row md-align="start center">
      <card v-for="news in feed" :news="news" :key="news.id"></card>
    </md-layout>
  </div>
</template>


<script>
import axios from "axios";
import Card from "@/components/Card.vue";

const BASE_URL = "http://localhost:8000/api/";
const ACCESS_TOKEN = "access_token";

export const http = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    Authorization: `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`,
    "Content-Type": "application/json",
  },
});

export default {
  components: {
    Card,
  },
  data() {
    return {
      site_name: "",
      feed: [],
    };
  },
  methods: {
    initData: function (site_name) {
      http
        .get("feed/news", {
          params: {
            feed_name: site_name,
          },
        })
        .then((resposta) => {
          this.feed = resposta.data;
        });
    },
  },
  created: function () {
    this.site_name = this.$route.params.feed_name;
    this.initData(this.site_name);
  },
};
</script>