<template>
  <md-layout md-flex="33" md-align="center">
    <md-card md-with-hover md-align="center">
      <md-card-header>
        <div class="md-title">{{ news.title }}</div>
        <div class="md-subhead">{{ news.published }}</div>
      </md-card-header>

      <md-card-content>
        <span v-html="news.summary"></span>
      </md-card-content>

      <md-card-actions>
        <md-button @click="readMore">Ir para a notícia</md-button>
      </md-card-actions>
    </md-card>
  </md-layout>
</template>

<script type="text/javascript">
export default {
  name: "Card",
  props: ["news"],
  methods: {
    readMore: function () {
      window.open(this.news.link, "_blank");
    },
  },
};
</script>

<style>
.md-theme-default.md-card {
  left: 30%;
  top: 50%;
  background-color: #fff;
  width: 40%;
  height: 50%;
  margin-bottom: 20px;
  align-self: center;
}
</style>